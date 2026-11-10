# StashSmart daily posting playbook

The daily scheduled task follows this file. Edit it to change how posts are written.

## Schedule
- Runs daily at 6:45am Pacific, Nov 10, 2026 through Feb 7, 2027 (90 days).
- Austin approves each morning (target 7:00am).
- Approved posts publish at **8:00am** and **3:00pm** Pacific, identical on Instagram and Facebook.
- Nothing is ever published without Austin's explicit approval in that day's conversation.

## Accounts (Windsor.ai for Social Media connector)
- Instagram: connector `instagram`, account `17841426931536218` (stashsmart.app), action `create_image_post` (params: `image_url`, `caption`).
- Facebook Page: connector `facebook_organic`, account `1343390778863435` (StashSmart), action `create_photo_post` (params: `image_url`, `caption`).
- Image URL format: `https://raw.githubusercontent.com/austingoswick/stashsmart-social/main/<image path>`

## About StashSmart
- All-in-one grocery app by StashSmart LLC: loyalty cards, coupons, receipt storage, pantry tracking with expiry alerts 48 hours before food goes bad, a smart shopping list with an in-store "do I have this?" check, and recipes you can save to a date to cook for your family.
- Family plan: shared with up to 3 other household members (pantry, lists, meal schedule, recipes, coupons, savings).
- Learns your buying habits over time, so recommendations get better the more you use it.
- Mission: take the stress out of remembering what you need, whether you have it at home, and whether it's still good, all while saving money.
- Pricing: 30-day free trial, then $2.99/month Individual or $3.99/month Family.
- Status: PRE-LAUNCH (iPhone first). Never say it's available now, never give a launch date, never invent download numbers, reviews, testimonials or user quotes. CTAs: follow, share, comment, tag a friend, "coming soon".

## Content
- Tone: positive, warm, upbeat, family-friendly. Never preachy or guilt-tripping.
- Rotate three pillars so each day has two different ones:
  1. **Food-waste facts**: compelling, true stats. Look each one up on a reputable source (U.S. EPA, USDA, ReFED, FAO, NRDC, WRAP, peer-reviewed research) and name the source on the image and in `source_note`. Never reuse a stat already in `posts/`.
  2. **What StashSmart helps you do**: one feature or benefit per post, framed as an outcome (save money, less stress, less waste, family on the same page).
  3. **Attention-grabbing hooks**: relatable questions, "be honest" moments, polls, myth vs. fact, quick tips, "tag someone who...".
- Captions: 40 to 120 words, a hook in the first line, 1 to 3 emoji, a soft CTA, then 6 to 10 hashtags (always include #stashsmart). The same caption goes to both platforms.
- Image headline under ~14 words; body under ~25 words.
- Before writing, read the last 14 days of `posts/*.json` and do not repeat an angle, stat, headline or opening line.

## Images
- Render with `python3 scripts/make_image.py spec.json images/<date>/<slot>.jpg`.
- Styles: `fact` (green), `feature` (cream), `hook` (orange). Fonts are in `fonts/`.
- Always look at each rendered image before sending it for approval, and fix any text that's cut off or overlapping.

## Files
- One file per day: `posts/YYYY-MM-DD.json` with `status` (`drafted` → `approved` → `posted`, or `skipped`) and each post's slot, pillar, image, image_spec, caption, source_note, plus post ids once published.
