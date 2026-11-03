# Field guide: US entry-labeled software listings: screening file

## screening.csv (5,625 rows)

| Column | Meaning |
| --- | --- |
| `screen_row_id` | Opaque row ID for this file. Row order carries no meaning |
| `in_release` | `representative`: the listing is a record in the jobs dataset. `merged_repeat`: a repost the jobs dataset counts once under another record. `not_in_release`: not in the jobs dataset |
| `release_job_id` | The jobs dataset's `job_id` for the record this listing belongs to; blank when `not_in_release` |
| `text_group_id` | Opaque ID shared by listings with identical description text |
| `counts_in_unique_basis` | `yes` for the one listing per `text_group_id` used for unique-listing figures (the earliest in GSC's data) |
| `advertiser_key` | Opaque ID shared by listings from the same advertiser name; names are not included |
| `state` | Two-letter US state derived from the listed location; blank when not specified or not mapped |
| `location_specified` | `yes`, `no` (listing gives only "United States") or `unmapped` |
| `segment_group` | `ai_training_or_evaluation` (paid work training or evaluating AI models), `software` (plain software-engineering roles), `out_of_scope` (non-software, outside the US or unusable) or `other_software_role`; assigned in that order. A plain software role outside the US stays `software`; use `in_scope` for scope |
| `in_scope` | `yes` unless the listing is AI-training work or out of scope |
| `eligibility_tier` | First-screening outcome: `retained` (selected for the jobs dataset), `experience_review`, `other_secondary`, `exception` or `excluded` |
| `entry_level_basis` | Evidence of a junior role in the listing itself: `title_explicit`, `body_explicit`, `numbered_entry_level`, `academic_internship_route`, `metadata_only` (the LinkedIn label only; every screened listing carries it), `conflict` or `not_applicable` |
| `entry_evidence` | The grouping used in #1: `independently_supported`, `platform_label_only`, `conflict` or `not_applicable` |
| `junior_title_flag` | `yes` when the title contains junior, jr, entry, new grad, graduate or associate |
| `experience_status` | `quantified_required`, `preferred_only`, `ambiguous`, `not_stated` or `research_coded` |
| `minimum_professional_years` | Required minimum years of professional experience when quantified; blank otherwise |
| `minimum_operator` | `>=` or `>` when the wording settles it; blank when not recorded |
| `experience_band` | `zero` (explicitly none), `under_2`, `two` (2 to under 3), `three_four`, `five_plus`, `preferred_only`, `ambiguous` or `not_stated` |
| `review_depth` | Where the experience value comes from: `released_dataset` (the jobs dataset's corrected value), `rechecked` (re-coded under the final rules: every 2+ year and explicit-zero value outside the jobs dataset), or the first screening (`screen_cross_checked`, `screen_adjudicated`, `screen_single_reader`) |

"Required 2+ years" means `experience_band` is `two`, `three_four` or `five_plus`.

## aggregates.csv (231 rows)

| Column | Meaning |
| --- | --- |
| `claim_id` | GSC's ID for the figure (F1–F12 for #1; 5-1 to 5-5 for #5) |
| `article` | `#1` (experience requirements) or `#5` (AI-training listings) |
| `measure` | What is counted |
| `population` | `screened_listings` (the 5,625), a subset of them (suffix), or `all_collected_listings` (96,309, every listing in GSC's collection) |
| `basis` | `listings` or `unique_listings` |
| `group` | The category or subgroup |
| `statistic` | `share_pct`, `count`, `ratio`, `median_usd`, `q1_usd`, `q3_usd` or `margin_95_pts` |
| `numerator`, `denominator`, `value` | The figure; pay rows give the group size as `denominator` |
| `note` | Caveats, including suppressed small cells |
