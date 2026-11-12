# stashsmart.app website

`index.html` here is the live site at stashsmart.app (GoDaddy cPanel hosting).
GoDaddy pulls this repo every hour (cPanel Cron Job) and copies `website/index.html` and `website/waitlist.php` into `public_html/stashsmart.app/` (the domain's document root). Waitlist sign-ups are saved by waitlist.php to `~/waitlist-data/waitlist.csv` on the server (outside public_html, never in this repo).
Only change it after Austin approves the update. See WEBSITE.md for the update rules.
