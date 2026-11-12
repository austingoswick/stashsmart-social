<?php
// StashSmart waitlist sign-ups.
// Saves each email to a CSV file OUTSIDE public_html (so nobody can download it from the web)
// and emails a notice to info@stashsmart.app.
// File location on the server: <home folder>/waitlist-data/waitlist.csv

header('Content-Type: application/json');
header('X-Content-Type-Options: nosniff');

function reply($code, $status) {
    http_response_code($code);
    echo json_encode(['status' => $status]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') reply(405, 'error');

// Honeypot: real visitors never see or fill the "website" field; bots usually do.
if (!empty($_POST['website'])) reply(200, 'ok');

$email = strtolower(trim($_POST['email'] ?? ''));
$source = preg_replace('/[^a-z0-9_-]/i', '', $_POST['source'] ?? '');
if (strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL)) reply(400, 'invalid');

$dir = dirname($_SERVER['DOCUMENT_ROOT']) . '/waitlist-data';
if (!is_dir($dir) && !mkdir($dir, 0700, true)) reply(500, 'error');
$file = $dir . '/waitlist.csv';

$fh = fopen($file, 'c+');
if (!$fh || !flock($fh, LOCK_EX)) reply(500, 'error');

// Already on the list? Treat as success, don't add twice.
rewind($fh);
while (($row = fgetcsv($fh)) !== false) {
    if (isset($row[0]) && strtolower($row[0]) === $email) {
        flock($fh, LOCK_UN); fclose($fh);
        reply(200, 'ok');
    }
}

$isNew = (filesize($file) === 0);
fseek($fh, 0, SEEK_END);
if ($isNew) fputcsv($fh, ['email', 'joined_at', 'form']);
fputcsv($fh, [$email, gmdate('c'), $source]);
fflush($fh);
flock($fh, LOCK_UN);
fclose($fh);

// Email notice (best effort; the CSV is the real record).
@mail(
    'info@stashsmart.app',
    'New StashSmart waitlist sign-up',
    "New sign-up: $email\nForm: $source\nTime (UTC): " . gmdate('Y-m-d H:i'),
    "From: StashSmart Website <info@stashsmart.app>\r\nContent-Type: text/plain; charset=UTF-8"
);

reply(200, 'ok');
