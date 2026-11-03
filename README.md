# US entry-labeled software listings: screening file

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23917043.svg)](https://doi.org/10.5281/zenodo.23917043)

Research by **Global Software Companies**. Version **2026-10-11c**.

Documentation, downloads and citation: [www.globalsoftwarecompanies.com/research-data/#entry-level-screening-file](https://www.globalsoftwarecompanies.com/research-data/#entry-level-screening-file). Used in: [We Analyzed 5,625 “Entry-Level” Software Jobs. Only 9% Explicitly Accepted Beginners.](https://www.globalsoftwarecompanies.com/entry-level-software-jobs-experience/).

This package lets you check the figures in two GSC articles: how many "entry-level" software jobs require experience (#1), and AI-training listings (#5). Both draw on **5,625 US software listings labeled "Entry level" on LinkedIn** (January–August 2026), more than the 2,517 in GSC's published jobs dataset, *US entry-labeled software job listings*.

- `screening.csv`: one row per screened listing with GSC's coding (experience required, entry-level evidence, role group, AI-training flag, state, review depth). It has no listing text and no LinkedIn identifiers, titles, advertiser names, locations, posting dates or pay for listings outside the jobs dataset. Rows that are in the jobs dataset link to it through `release_job_id`.
- `aggregates.csv`: every published figure in #1 and #5, with numerator, denominator and population. This includes figures computed over all 96,309 listings in GSC's collection, pay medians and employment types, which aren't released per listing. Pay medians appear only for groups of 10 or more listings, and quartiles for 30 or more.
- `REPRODUCE.md` and `reproduce.py`: how to recompute the headline figures from `screening.csv`. Run `python3 reproduce.py` in this folder.
- `FIELD-GUIDE.md`: column definitions.

## Method in brief

GSC's source data hold 96,309 US LinkedIn software listings posted January–August 2026; GSC did all classification. GSC selected the 5,625 labeled "Entry level" whose titles contain "software" plus developer, engineer or programmer, leaving out titles with senior, manager, director, instructor, tutor, sales or recruiter. Each listing's required professional experience was classified with AI assistance under written rules. Listings in the jobs dataset carry its values. The other listings that first screening put at 2+ years, or at an explicit zero, were re-coded under the same rules; the rest keep their first-screening values (`review_depth` says which). Which listings count as AI-training work was checked listing text by listing text: two AI coders worked independently, and a third review decided disagreements and close calls. A duration tied to one area of software work or to particular languages or tools counts as a professional minimum only when it is stated as professional or work experience.

## Interpretation

These are selected listings, not a representative sample of the US jobs market or of unique vacancies. "Listings" counts what job-seekers see, including reposts; "unique listings" counts each identical description once (rows with `counts_in_unique_basis = yes`). Most listings were posted in July and August 2026, so the data don't support trends over time. The classification is AI-assisted. A GSC researcher checked about 1 in 5 of the AI classifications by hand and reviewed the edge cases those checks identified; this is a spot check, not a measured accuracy rate.

## License and citation

The GSC contribution is licensed under CC BY 4.0 (see LICENSE.md). Suggested citation:

> Global Software Companies (2026). *US entry-labeled software listings: screening file*. Version 2026-10-11c. https://doi.org/10.5281/zenodo.23917043. Documentation: https://www.globalsoftwarecompanies.com/research-data/#entry-level-screening-file. CC BY 4.0.
