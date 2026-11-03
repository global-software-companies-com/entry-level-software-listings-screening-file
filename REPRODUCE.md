# Reproducing the figures in GSC's articles #1 and #5

Article key: #1 experience requirements in entry-level listings; #5 AI-training listings.

Run `python3 reproduce.py` in this folder (Python 3, standard library only). It recomputes the figures below from `screening.csv` and compares each with `aggregates.csv`, printing `OK` or `MISMATCH`.

## Definitions

- **Required 2+ years:** `experience_band` is `two`, `three_four` or `five_plus`. **3+ years:** `three_four` or `five_plus`.
- **Explicitly accepted no experience:** `experience_band` is `zero`.
- **Listings:** count rows. **Unique listings:** count only rows with `counts_in_unique_basis = yes`.
- **AI-training listings:** `segment_group = ai_training_or_evaluation`.

## Figures you can recompute

| Article figure | How |
| --- | --- |
| #1 F1: required 2+ years | Share of all 5,625 rows (listings) and of the `counts_in_unique_basis = yes` rows (unique listings) |
| #1 F1: full experience distribution | Count rows by `experience_band` |
| #1 F2: without AI-training listings | Rows where `segment_group` isn't `ai_training_or_evaluation` |
| #1 F2: in-scope listings | Rows where `in_scope = yes` |
| #1 F2: plain software roles | Rows where `segment_group = software` |
| #1 F3: 3+, 5+, 8+ and 10+ years | `experience_band`, and `minimum_professional_years` for 8+ and 10+ |
| #1 F5: entry-level evidence | Count rows by `entry_evidence` |
| #1 F6: "Junior" titles | Rows with `junior_title_flag = yes` that require 2+ (or 3+) years; for unique, count distinct `text_group_id` among those rows |
| #1 F9: AI-training share of 3+ year listings | Among rows requiring 3+ years: listings, and the `counts_in_unique_basis = yes` rows |
| #1 F10: explicit zero | Rows with `experience_band = zero` |
| #1 F11: by state (listings) | In-scope rows, by `state`, for states with 100+ listings |
| #1 F12: 2+ years vs explicit zero | F1's count divided by F10's, on each basis |
| #5: AI-training listings | Rows with `segment_group = ai_training_or_evaluation`; for unique, count distinct `text_group_id` among them (out of all 3,811 unique listings). Also how many of them require 3+ years |

## Figures you can check only in aggregates.csv

Some figures need fields that aren't released per listing, so `aggregates.csv` gives their numerators and denominators:
- **Pay** (#1 F7) and **employment type** (#1 F8; #5).
- **LinkedIn label shares across all 96,309 listings in GSC's collection** (#1 F4).
- **Sensitivity ranges for the 2+ year figure** (#1 F2).
- **Titles with no AI wording** and **combined top-advertiser shares** (#5).
- **Unique-listing figures by state** (#1 F11). Each state uses the earliest listing of a text within that state, which this file doesn't order.

Figures about named employers appear only in the articles.
