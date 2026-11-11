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

## Brand (StashSmart Brand Guidelines, Edition 02, Nov 2026)
- Brand line: "Smart shopping made easy." App tagline: "Know what you have. Buy what you need." Promise: "StashSmart gets smarter every time you shop."
- Personality: practical, thrifty, quietly smart. Like a helpful note on the fridge.
- Name: always "StashSmart", one word (never "Stash Smart", "Stashsmart", "STASHSMART" in running text). App areas: Pantry, List, Meals, Wallet. Plans: Individual and Family. Say "members", not "users". Phrases: "Stock your kitchen", "Do I have this?", "What's for dinner?".
- Colors: Paper #F3F2F2 and Receipt Ink #201E1D for most of every post; Aisle Cyan #0088B0 (Cyan 700 #006786 for text, Cyan 900 #0A303E for dark grounds). Deal Marigold #F2B705 (text #8A6400) ONLY for money saved/wasted or something running out, at most one marigold accent per post. Never white text on marigold.
- Type: Source Serif 4 only. Headlines Semibold, body Regular, tips and "Smart" in Italic. No second typeface.
- Logo: icon tile + wordmark, "Stash" Semibold roman + "Smart" Regular italic in cyan (Cyan 200 on dark). Never stretch, outline or add effects. The icon is brand/app-icon-512.png, unchanged.
- Social backgrounds: Paper (`paper` style) or Cyan 900 to 500 feature gradient (`cyan` style). Mostly Paper.

## Voice rules (apply to captions AND image text)
- Short, specific, done. Lead with the number. Second person, present tense.
- NO exclamation marks, anywhere.
- Sentence case. Always show cents: $1.00, $2.99/month, $2,913.00.
- Emoji: at most one per line, only as a signpost, from this set: 🔥 🙌 💰 🍗 🥛 🧊 🥫. Never inside prices.
- Pricing wording: "1 month free, then $2.99/month. Family: $3.99/month for up to 4 people."
- Not hype ("Amazing savings!!", "You're a superstar"). Not guilt ("Oops, did you waste food?").

## Content
- Tone: positive and encouraging, within the voice rules above.
- Rotate three pillars so each day has two different ones:
  1. **Food-waste facts**: compelling, true stats. Look each one up on a reputable source (U.S. EPA, USDA, ReFED, FAO, NRDC, WRAP, peer-reviewed research) and name the source on the image and in `source_note`. Never reuse a stat already in `posts/`.
  2. **What StashSmart helps you do**: one feature or benefit per post, framed as an outcome (save money, less stress, less waste, family on the same page).
  3. **Attention-grabbing hooks**: relatable questions, "be honest" moments, polls, myth vs. fact, quick tips, "tag someone who...".
- Captions: 40 to 120 words, at most one emoji per line, a soft CTA, then the hashtags. The same caption goes to both platforms.
- HUMANIZE every caption (Austin's request, Nov 10): write it the way a real person who's building this app would talk to a friend, not like an ad or an AI. Use contractions, everyday words and a real moment people recognize (the 9pm fridge stare, the second jar of cinnamon, the receipt at the bottom of the bag). Vary sentence length; a short fragment is fine. A little warmth or light humor is good. "We" is the StashSmart team. Avoid marketing filler and AI tells: no "Say goodbye to", "Introducing", "game-changer", "seamless", "unlock", "elevate", "Imagine a world", "Whether you're... or...", no lists of three adjectives, no em dashes, no rhetorical question followed by its own answer. Still follow the voice rules above (no exclamation marks, cents on prices, numbers with sources). Read it aloud before sending: if it sounds like a brand, rewrite it.
- HASHTAGS (Austin's request, Nov 10): every post ends with these five, always, in this order: #smartshopping #groceryshopping #familymeals #stashsmart #mobilepantry. Use ONLY these five, never add any others (Austin: more hashtags reduce Instagram reach). Put them on their own line after a blank line.
- Image headline under ~14 words; body under ~25 words.
- Before writing, read INSIGHTS.md (lean into what's working) and IDEAS.md (use the newest unused ideas first and mark each one used with today's date).
- Before writing, read the last 14 days of `posts/*.json` and do not repeat an angle, stat, headline or opening line.

## Images
- Render with `python3 scripts/make_image.py spec.json images/<date>/<slot>.jpg`.
- Styles: `paper` (default; facts and hooks) and `cyan` (feature posts). Use `highlight` (marigold) only for a money or running-out figure. Fonts are in `fonts/`, icon in `brand/`.
- Always look at each rendered image before sending it for approval, and fix any text that's cut off or overlapping.

## Files
- One file per day: `posts/YYYY-MM-DD.json` with `status` (`drafted` → `approved` → `posted`, or `skipped`) and each post's slot, pillar, image, image_spec, caption, source_note, plus post ids once published.
