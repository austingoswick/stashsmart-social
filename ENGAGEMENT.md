# Daily engagement list

Every morning, alongside the post drafts, send Austin a short engagement list. Austin posts every comment himself, from the stashsmart.app account. Never post comments on other accounts automatically, through any tool or browser.

## What to send
- Pick 6 accounts from the target list below. Rotate them: check `engagement/log.md` and don't repeat an account used in the last 5 days.
- For each account give:
  - the handle as a tap-able link: https://www.instagram.com/<handle>/
  - one line on what they usually post
  - 2 comment options that fit their usual content (e.g. one for a recipe or meal post, one for a grocery haul or savings tip). Austin opens their newest post and pastes the one that fits, or edits it.
- Add a line to `engagement/log.md`: date and the 6 handles. Commit and push.

## How the comments should sound
- Like a real person who loves this stuff, not a brand. 8 to 30 words.
- React to something specific they'd plausibly post about (a tip, a meal, a price, their kids, a haul), or ask a genuine question.
- Follow the brand voice: no exclamation marks, at most one emoji, sentence case, cents on any price.
- NEVER promote: no "check out our app", no links, no "DM us", no hashtags, no mention of StashSmart. The profile does the selling. Generic praise like "Great post" or "Love this" on its own is not allowed.
- Vary openings and wording every day so comments never look copy-pasted.

## Target accounts
Family meals, budget groceries and meal planning on Instagram. Austin can add or remove handles here any time. If he says an account is inactive, wrong, or not a fit, remove it.

| Handle | Focus |
|---|---|
| budgetbytes | low-cost recipes and meal prep |
| 5dollardinners | budget family dinners, meal planning, freezer cooking |
| morgantaylerathome | mom saving families money on groceries, meal plans |
| kidseatincolor | feeding kids, picky eaters, simple family food |
| weelicious | family recipes and kid-friendly food |
| damndelicious | easy weeknight dinners |
| lalalunchbox | school lunch ideas |
| lunchboxdad | fun lunches from a dad |
| plantbasedonabudget | cheap plant-based meals |
| victoriasmealprep | grocery app deals and meal prep for a family |
| singlemombudgeting | single-mom budgeting and grocery savings |
| alicetayloreats | real-life family cooking, stretching meals |
| couponangel29 | grocery coupon hauls |

## Replies to comments on our own Instagram posts
Every morning, after the engagement list:
- Read comments on our Instagram posts from the last 14 days with Windsor get_data: connector `instagram`, account `17841426931536218`, fields `comment_id, comment_text, comment_username, comment_timestamp, comment_parent_id, media_id, media_permalink`, `date_preset` `last_14d`.
- Skip comments we already handled (listed in `engagement/replied.md`), our own comments, replies to replies, and spam. Hide nothing and delete nothing without Austin asking.
- Draft one reply per new comment: warm, short (5 to 30 words), human, in the brand voice (no exclamation marks, at most one emoji, cents on prices). Answer real questions honestly using PLAYBOOK.md facts. Never promise a launch date. Thank people by name when the username is available.
- Send them to Austin in the same morning message flow, numbered, under "Comment replies". He approves with "approve" (posts and replies) or edits individual ones ("reply 2: ...", "skip reply 3").
- On approval, post each with execute_action: connector `instagram`, account `17841426931536218`, action `reply_to_comment`, params `{comment_id, message}`. Add each handled comment_id (posted or skipped) to `engagement/replied.md`, commit and push.
- Facebook comments can't be replied to through this connector yet; if Austin asks, say so.
