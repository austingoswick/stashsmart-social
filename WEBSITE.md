# Website update rules (stashsmart.app)

The live site is `website/index.html`. GoDaddy copies it to public_html every hour, so anything pushed to main goes live within about an hour.

## Every update run
1. Check the page against PLAYBOOK.md and the brand rules (Brand Guidelines Edition 02): name StashSmart (one word), colors, Source Serif 4 only, no exclamation marks, cents on prices, pricing wording "1 month free, then $2.99/month. Family: $3.99/month for up to 4 people.", pre-launch wording (coming soon on iPhone, no launch date, no download links until launch). Fix anything out of date.
2. Add or refresh ONE small piece of fresh content, rotating:
   - a short "Kitchen tip" or food-waste fact (with a named reputable source) in the Why section,
   - a "Lately on Instagram" line or card linking to a recent well-performing post (use INSIGHTS.md and posts/*.json),
   - a seasonal note (holidays, back to school, summer grilling) in the hero sub-line.
   Keep the page's structure, layout and scripts. Change only the text or small blocks you need. Never remove the waitlist forms.
3. Never invent stats, reviews, testimonials, download counts or a launch date.
4. Keep the file self-contained (one HTML file, no new external scripts).

## Approval
Never push website changes without Austin's explicit approval. Send him a plain-language list of what changed plus the updated file to preview. After he approves, commit with a clear message and push to main.
