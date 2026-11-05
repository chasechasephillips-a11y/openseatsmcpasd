# MCPASD operational referendum: ward/reporting-unit results, Nov. 8, 2022 vs Nov. 3, 2026

Data pulled 2026-11-05 from the Dane County Clerk's results site (elections.countyofdane.com) and its JSON API (api.danecounty.gov). The cleaned tables are saved next to this file:
- `ward_results_2022.csv`: 28 reporting units, official canvass.
- `ward_results_2026.csv`: 29 reporting units, unofficial. Includes under-votes and over-votes from the county's raw results file.
- `ward_change.csv`: change from 2022 to 2026 for each comparison unit and each municipality.
- `rolloff_by_contest.csv`: roll-off on the MCPASD question compared with the governor race and other ballot questions in the same reporting units.

Definitions:
- "Ref votes" means Yes + No.
- "Roll-off" means ballots that had the MCPASD question but recorded no valid Yes/No vote (under-votes + over-votes).
- "Ballots cast (whole unit)" is Dane County's BALLOTS CAST - TOTAL for the reporting unit. Many units include voters who live outside MCPASD (see Q5).

## Q1. What were the 2022 and 2026 questions, and what are the district-wide totals?

### Takeaway
Both questions were 4-year **non-recurring** operating referendums to exceed the revenue limit.
- **2022:** $7.345M, then $13.79M, $19.435M and $24.9M for 2023-24 through 2026-27, about $65.5M in all. It passed **14,596 to 8,608 (62.9%)**, official canvass.
- **2026:** $24.9M, then $27.9M, $31.1M and $34.6M for 2027-28 through 2030-31, $118.5M in all. Unofficial final returns are **14,263 to 9,457 (60.1%)**, with 29 of 29 units reporting.

The internal-notes figures are all correct. The "$65.5M" and "$24.9M" descriptions of 2022 are the same question: $24.9M is the final-year amount and about $65.5M is the four-year total.

### Cited Findings
- **2022 ballot text (from the district's Nov. 2022 referendum presentation):** "Shall the Middleton-Cross Plains Area School District, Dane County, Wisconsin be authorized to exceed the revenue limit specified in Section 121.91, Wisconsin Statutes, by $7,345,000 for the 2023-2024 school year, by $13,790,000 for the 2024-2025 school year, by $19,435,000 for the 2025-2026 school year and by $24,900,000 for the 2026-2027 school year, for non-recurring purposes consisting of expenses related to ongoing educational and extracurricular programming, and compensation, and other operational expenses?" — [MCPASD Nov 2022 Referendum presentation (PDF hosted on clubrunner)](https://clubrunner.blob.core.windows.net/00000006121/en-ca/files/homepage/m-cp-school-district-2022-referendum/Nov-2022-Referendum-M-CP-area-school-district-Presentation.pdf)
- The same presentation calls it "$24.9 million, non-recurring, 4-year period." Its tax impact per $100,000 of assessed value was $7, $53, $39 and $36 for years 1-4. — [same PDF](https://clubrunner.blob.core.windows.net/00000006121/en-ca/files/homepage/m-cp-school-district-2022-referendum/Nov-2022-Referendum-M-CP-area-school-district-Presentation.pdf)
- **2022 official result:** "Middleton Cross Plains SD Ref (Exceed revenue limit) - Official Canvass": Yes 14,596 (62.9%), No 8,608 (37.1%), 100% of precincts reporting (28 of 28). Finalized 11/15/2022 2:57 PM. — [Dane County 2022 General Election results](https://elections.countyofdane.com/Election-Result/145); [precinct table](https://elections.countyofdane.com/Precincts-Result/145/0042) ([Excel](https://elections.countyofdane.com/Precinct-ResultExcel/145/0042))
- **2026 ballot text (Dane County "What's on the Ballot"):** "Shall the Middleton-Cross Plains Area School District, Dane County, Wisconsin be authorized to exceed the revenue limit specified in Section 121.91, Wisconsin Statutes, by $24,900,000 for the 2027- 2028 school year, by $27,900,000 for the 2028-2029 school year, by $31,100,000 for the 2029-2030 school year and by $34,600,000 for the 2030-2031 school year, for non-recurring purposes consisting of expenses related to ongoing educational and extracurricular programming, and compensation, and other operational expenses?" — [Dane County What's on the Ballot, Nov 2026 (PDF)](https://elections.countyofdane.com/documents/pdf/What-s-on-the-Ballot-Nov-2026.pdf)
- **2026 unofficial result:** Yes 14,263 (60.1%), No 9,457 (39.9%), "100% of Precincts Reporting (29 of 29)". The Excel export reads "All Precincts Reported On: 11/3/2026 11:27 PM; Generated Report on: 11/4/2026 7:08 PM." — [Dane County 2026 General Election results](https://elections.countyofdane.com/Election-Result/197); [precinct table](https://elections.countyofdane.com/Precincts-Result/197/0040) ([Excel](https://elections.countyofdane.com/Precinct-ResultExcel/197/0040))
- The 2026 measure re-authorizes the $24.9M from the 2022 referendum, which expires at the end of 2026-27. The $118.5M total is the sum of the four annual amounts. Estimated tax impact reaches about $64 per $100,000 of value in year 4. All of this is secondhand, from search-result summaries of [WKOW](https://www.wkow.com/news/middleton-cross-plains-school-district-referendum-passes/article_a78a2ddc-8a60-40f1-a2e3-96bff2443aa3.html), [madison.com](https://madison.com/news/local/education/local_schools/article_ffce4d72-d972-44da-bb4f-11d43f6be0a8.html), [Channel 3000 ("poised to approve $118M")](https://www.channel3000.com/news/middleton-cross-plains-area-school-district-voters-poised-to-approve-118m-referendum/article_609b4a19-3042-41f0-a79b-71dcba49c850.html) and [Fox47](https://fox47.com/news/local/middleton-cross-plains-school-board-approves-346m-referendum-for-nov-3-election). The hosts could not be fetched directly.
- WMTV reported 14,263 Yes and 9,457 No, unofficial. This is secondhand via a search summary. — [WMTV, Nov. 4, 2026](https://www.wmtv15news.com/2026/11/04/voters-pass-middleton-cross-plains-school-district-referendum/)
- A WASB list reportedly describes an MCPASD measure as "$4,820,000 beginning with the 2023-2024 school year for recurring purposes". This conflicts with the ballot text above. It is secondhand via search summary and I could not open it. — [WASB](https://wasb.org/number-of-revenue-limit-referenda-in-2022-reaches-all-time-high)

### Inferences
- **2022 total:** $7.345M + $13.79M + $19.435M + $24.9M = $65.47M, which is the "$65.5 million" figure. "$24.9 million" is the year-4 amount. Both describe the same 2022 question, which passed with 62.9%.
- **2026 total:** $24.9M + $27.9M + $31.1M + $34.6M = $118.5M.
- **District-wide change, 2022 to 2026:**
  - Yes share: 62.90% to 60.13%, down 2.8 points.
  - Yes votes: down 333 (-2.3%).
  - No votes: up 849 (+9.9%).
  - Total ref votes: up 516 (+2.2%).
  - Yes margin: 5,988 to 4,806.
- **Channel 3's 14,248/9,445 count (28 of 29):** it is 15 Yes and 12 No short of the final unofficial total. That exactly equals Madison Ward 095 in 2026 (15 Yes, 12 No), so the Channel 3 figure was very likely captured before Ward 095 reported. It is not a conflicting count.
- **The WASB "$4.82M recurring" description:** it most likely refers to MCPASD's earlier (2018) operating referendum. The 2022 presentation cites a prior operating referendum of "a total of $4.8 million" with "more than 70% yes vote." I did not verify this.

### Gaps
- I could not reach the DPI referendum database. A guessed dpi.wi.gov path returned 404, and I did not find the right URL.
- mcpasd.k12.wi.us (district pages and the board resolution) failed with ENOTFOUND, so the 2026 tax-impact figures are secondhand.
- I found no official Dane County 2022 "What's on the Ballot" PDF. Three URL variants returned 404, so the 2022 ballot text comes from the district presentation rather than a county document.

## Q2. Which municipalities and wards are in MCPASD, and how many reporting units did each election have?

### Takeaway
MCPASD votes were reported from 8 municipalities in both years:
- City of Middleton
- part of the City of Madison
- Town of Middleton
- Village of Cross Plains
- Towns of Cross Plains, Springfield, Berry and Westport (parts)

There were 28 reporting units in 2022 and 29 in 2026. No other municipality shows MCPASD votes.

### Cited Findings
- **Reporting units by municipality (Dane County precinct tables):**

| Municipality | 2022 units | 2026 units | Notes |
|---|---|---|---|
| City of Madison | 15 (Wds 095, 100, 101, 102, 109, 113, 114, 115, 117, 118, 119, 137, 139, 140, 141) | 14 (Wds 095, 100, 101, 102, 109, 114, 115, 117, 118, 119, 120, 134, 135, 137) | Wd 137 had 0 votes both years. Wd 113 had 0 MCPASD votes in 2022 (2,239 ballots) and is absent from the 2026 list. |
| City of Middleton | 7 (Wds 1-4; 5-8; 9-13,19; 14-18; 20,23; 21; 22) | 5 (Wds 1-4; 5-8,21; 9-13,19,22,24; 14-18; 20,23) | Wds 20, 23 had 0 votes both years. |
| Town of Middleton | 1 (Wds 1-8) | 4 (Wds 1,3-4; 2,4A; 5-8; 8A) | Wd 8A had 0 ballots. |
| Village of Cross Plains | 1 (Wds 1-6) | 2 (Wds 1-6; Wd 7) | |
| Town of Berry | 1 (Wds 1-2) | 1 (Wds 1-2) | |
| Town of Cross Plains | 1 (Wds 1-2) | 1 (Wds 1-2) | |
| Town of Springfield | 1 (Wds 1-4) | 1 (Wds 1-4) | |
| Town of Westport | 1 (Wds 1-5) | 1 (Wds 1-5) | |

  Sources: [2022 MCPASD by precinct](https://elections.countyofdane.com/Precincts-Result/145/0042); [2026 MCPASD by precinct](https://elections.countyofdane.com/Precincts-Result/197/0040)
- **Ward-to-assembly assignments for 2026:** AD 79 includes "Town of Middleton ward 8A". AD 80 includes "Middleton wards 1, 3-8", "Village of Cross Plains wards 1-6" and "Middleton wards 20 and 23". AD 81 includes "Middleton wards 2 and 4A", "Cross Plains ward 7" and "Middleton wards 1-19, 21-22 and 24". — [Dane County What's on the Ballot, Nov 2026](https://elections.countyofdane.com/documents/pdf/What-s-on-the-Ballot-Nov-2026.pdf)

#### 2022 table (official canvass)
Roll-off is estimated as ballots cast minus Yes and No votes. It is shown only for units judged to lie fully inside MCPASD.

| Municipality | Ward(s) | Yes | No | Ref votes | Yes % | Ballots cast (whole unit) | Roll-off est. | Roll-off % |
|---|---|---|---|---|---|---|---|---|
| City of Madison | 095 | 28 | 12 | 40 | 70.0 | 549 |  |  |
| City of Madison | 100 | 44 | 11 | 55 | 80.0 | 335 |  |  |
| City of Madison | 101 | 197 | 112 | 309 | 63.8 | 1002 |  |  |
| City of Madison | 102 | 147 | 64 | 211 | 69.7 | 1037 |  |  |
| City of Madison | 109 | 227 | 99 | 326 | 69.6 | 881 |  |  |
| City of Madison | 113 | 0 | 0 | 0 |  | 2239 |  |  |
| City of Madison | 114 | 284 | 103 | 387 | 73.4 | 2202 |  |  |
| City of Madison | 115 | 33 | 7 | 40 | 82.5 | 1589 |  |  |
| City of Madison | 117 | 112 | 31 | 143 | 78.3 | 1445 |  |  |
| City of Madison | 118 | 533 | 210 | 743 | 71.7 | 798 | 55 | 6.9 |
| City of Madison | 119 | 993 | 510 | 1503 | 66.1 | 1563 | 60 | 3.8 |
| City of Madison | 137 | 0 | 0 | 0 |  | 0 |  |  |
| City of Madison | 139 | 54 | 8 | 62 | 87.1 | 66 | 4 | 6.1 |
| City of Madison | 140 | 136 | 67 | 203 | 67.0 | 204 | 1 | 0.5 |
| City of Madison | 141 | 1 | 0 | 1 | 100.0 | 1 | 0 | 0.0 |
| City of Middleton | 1-4 | 2154 | 966 | 3120 | 69.0 | 3261 | 141 | 4.3 |
| City of Middleton | 5-8 | 1625 | 810 | 2435 | 66.7 | 2605 | 170 | 6.5 |
| City of Middleton | 9-13, 19 | 1936 | 978 | 2914 | 66.4 | 3036 | 122 | 4.0 |
| City of Middleton | 14-18 | 1592 | 880 | 2472 | 64.4 | 3034 | (unit partly outside MCPASD) |  |
| City of Middleton | 20, 23 | 0 | 0 | 0 |  | 0 |  |  |
| City of Middleton | 21 | 96 | 32 | 128 | 75.0 | 141 | 13 | 9.2 |
| City of Middleton | 22 | 77 | 18 | 95 | 81.1 | 103 | 8 | 7.8 |
| Town of Berry | 1-2 | 126 | 240 | 366 | 34.4 | 742 |  |  |
| Town of Cross Plains | 1-2 | 218 | 213 | 431 | 50.6 | 1002 |  |  |
| Town of Middleton | 1-8 | 2134 | 1552 | 3686 | 57.9 | 3823 | 137 (upper bound) | 3.6 |
| Town of Springfield | 1-4 | 544 | 643 | 1187 | 45.8 | 1648 |  |  |
| Town of Westport | 1-5 | 128 | 113 | 241 | 53.1 | 2831 |  |  |
| Village of Cross Plains | 1-6 | 1177 | 929 | 2106 | 55.9 | 2252 | 146 | 6.5 |
| **Total** | 28 units | **14,596** | **8,608** | **23,204** | **62.9** | | | |

Sources: [MCPASD by precinct 2022](https://elections.countyofdane.com/Precincts-Result/145/0042); [Ballots cast by precinct 2022](https://elections.countyofdane.com/Precincts-Result/145/0002)

#### 2026 table (unofficial, 29/29)
Under-votes and over-votes come from the county raw file.

| Municipality | Ward(s) | Yes | No | Ref votes | Yes % | Under | Over | Ballots w/ question | Roll-off % | Ballots cast (whole unit) | Ballots w/o question |
|---|---|---|---|---|---|---|---|---|---|---|---|
| City of Madison | 095 | 15 | 12 | 27 | 55.6 | 7 | 0 | 34 | 20.6 | 590 | 556 |
| City of Madison | 100 | 45 | 26 | 71 | 63.4 | 12 | 0 | 83 | 14.5 | 354 | 271 |
| City of Madison | 101 | 184 | 141 | 325 | 56.6 | 26 | 0 | 351 | 7.4 | 1111 | 760 |
| City of Madison | 102 | 115 | 99 | 214 | 53.7 | 14 | 0 | 228 | 6.1 | 895 | 667 |
| City of Madison | 109 | 162 | 118 | 280 | 57.9 | 40 | 0 | 320 | 12.5 | 827 | 507 |
| City of Madison | 114 | 223 | 94 | 317 | 70.3 | 16 | 0 | 333 | 4.8 | 2777 | 2444 |
| City of Madison | 115 | 26 | 9 | 35 | 74.3 | 2 | 0 | 37 | 5.4 | 1672 | 1635 |
| City of Madison | 117 | 104 | 35 | 139 | 74.8 | 10 | 0 | 149 | 6.7 | 1393 | 1244 |
| City of Madison | 118 | 830 | 388 | 1218 | 68.1 | 46 | 0 | 1264 | 3.6 | 1264 | 0 |
| City of Madison | 119 | 889 | 558 | 1447 | 61.4 | 51 | 0 | 1498 | 3.4 | 1498 | 0 |
| City of Madison | 120 | 3 | 3 | 6 | 50.0 | 0 | 0 | 6 | 0.0 | 6 | 0 |
| City of Madison | 134 | 7 | 3 | 10 | 70.0 | 2 | 0 | 12 | 16.7 | 12 | 0 |
| City of Madison | 135 | 16 | 8 | 24 | 66.7 | 1 | 0 | 25 | 4.0 | 31 | 6 |
| City of Madison | 137 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 |
| City of Middleton | 1-4 | 2104 | 1003 | 3107 | 67.7 | 280 | 3 | 3390 | 8.3 | 3390 | 0 |
| City of Middleton | 5-8, 21 | 1622 | 974 | 2596 | 62.5 | 233 | 0 | 2829 | 8.2 | 2829 | 0 |
| City of Middleton | 9-13,19,22,24 | 2059 | 1121 | 3180 | 64.7 | 320 | 1 | 3501 | 9.2 | 3501 | 0 |
| City of Middleton | 14-18 | 1415 | 847 | 2262 | 62.6 | 253 | 0 | 2515 | 10.1 | 2954 | 439 |
| City of Middleton | 20, 23 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 |
| Town of Berry | 1-2 | 101 | 248 | 349 | 28.9 | 12 | 0 | 361 | 3.3 | 721 | 360 |
| Town of Cross Plains | 1-2 | 185 | 212 | 397 | 46.6 | 32 | 0 | 429 | 7.5 | 951 | 522 |
| Town of Middleton | 1, 3-4 | 829 | 657 | 1486 | 55.8 | 108 | 1 | 1595 | 6.8 | 1595 | 0 |
| Town of Middleton | 2, 4A | 222 | 169 | 391 | 56.8 | 23 | 0 | 414 | 5.6 | 414 | 0 |
| Town of Middleton | 5-8 | 1269 | 865 | 2134 | 59.5 | 177 | 0 | 2311 | 7.7 | 2354 | 43 |
| Town of Middleton | 8A | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 |
| Town of Springfield | 1-4 | 476 | 632 | 1108 | 43.0 | 58 | 0 | 1166 | 5.0 | 1552 | 386 |
| Town of Westport | 1-5 | 121 | 103 | 224 | 54.0 | 33 | 0 | 257 | 12.8 | 2931 | 2674 |
| Village of Cross Plains | 1-6 | 1173 | 1093 | 2266 | 51.8 | 74 | 0 | 2340 | 3.2 | 2340 | 0 |
| Village of Cross Plains | 7 | 68 | 39 | 107 | 63.6 | 4 | 0 | 111 | 3.6 | 111 | 0 |
| **Total** | 29 units | **14,263** | **9,457** | **23,720** | **60.1** | **1,834** | **5** | **25,559** | **7.2** | | |

Sources: [MCPASD by precinct 2026](https://elections.countyofdane.com/Precincts-Result/197/0040); [Ballots cast by precinct 2026](https://elections.countyofdane.com/Precincts-Result/197/0002); under/over votes from the [Dane County raw results file](https://elections.countyofdane.com/Election-RawResults) (fixed-width; [layout](https://elections.countyofdane.com/documents/pdf/ElectionResultsFileLayout.pdf)). The raw file's Yes/No counts match the Excel export exactly for every unit.

### Inferences
- The only municipalities in the district's footprint with MCPASD voters are the 8 above. Any Town of Verona, Dane or Vermont territory, if it exists in MCPASD, has no voters reported on this question.
- **Units that lie partly outside MCPASD:** in 2026, whole-unit ballots cast exceed ballots that had the question in 15 units. These are most Madison wards, Berry, Town of Cross Plains, Springfield, Westport, City of Middleton Wds 14-18 (439 ballots without the question) and Town of Middleton Wds 5-8 (43). Those units contain voters outside MCPASD, likely in Madison Metropolitan, Waunakee, Mount Horeb, Wisconsin Heights or Verona districts; I have not verified which. Whole-unit "turnout" in those units is therefore not MCPASD turnout.
- **Units fully inside MCPASD:** in 2026 these are City of Middleton 1-4, 5-8/21 and 9-13/19/22/24; Town of Middleton 1/3-4 and 2/4A; Village of Cross Plains 1-6 and 7; and Madison 118, 119, 120 and 134.

### Gaps
- No official list of MCPASD's ward composition was reachable, because the district site was blocked. The municipality list comes from the reporting units in the results.
- Which neighbouring school district holds the non-MCPASD voters in each split unit is not established.

## Q3. Which wards and municipalities swung toward or away from Yes, and where did the extra ~850 No votes come from?

### Takeaway
Yes share fell in 7 of 8 municipalities. Westport (+0.9 pts, tiny) was the exception, and the Town of Middleton was flat (-0.1).

The biggest drops in Yes share:
- City of Madison wards: -5.6 pts overall, with Wd 102 -16.0, Wd 109 -11.7 and Wd 101 -7.2
- Town of Berry: -5.5
- Town of Cross Plains: -4.0
- Village of Cross Plains: -3.6 (Wds 1-6 -4.1, to a near-even 51.8%)

The +849 net No votes came almost entirely from four places:
- City of Middleton: +261
- Madison wards: +260
- Village of Cross Plains: +203
- Town of Middleton: +139

The rural towns' No totals were flat.

### Cited Findings
All figures are computed from the Dane County precinct tables for [2022](https://elections.countyofdane.com/Precincts-Result/145/0042) and [2026](https://elections.countyofdane.com/Precincts-Result/197/0040). Full detail is in `ward_change.csv`.

#### Municipality change table

| Municipality | Yes 22 | No 22 | Yes% 22 | Yes 26 | No 26 | Yes% 26 | Chg pts | Chg Yes | Chg No | Chg ref votes |
|---|---|---|---|---|---|---|---|---|---|---|
| City of Madison (MCPASD wards) | 2789 | 1234 | 69.3 | 2619 | 1494 | 63.7 | -5.6 | -170 | +260 | +90 |
| City of Middleton | 7480 | 3684 | 67.0 | 7200 | 3945 | 64.6 | -2.4 | -280 | +261 | -19 |
| Town of Berry | 126 | 240 | 34.4 | 101 | 248 | 28.9 | -5.5 | -25 | +8 | -17 |
| Town of Cross Plains | 218 | 213 | 50.6 | 185 | 212 | 46.6 | -4.0 | -33 | -1 | -34 |
| Town of Middleton | 2134 | 1552 | 57.9 | 2320 | 1691 | 57.8 | -0.1 | +186 | +139 | +325 |
| Town of Springfield | 544 | 643 | 45.8 | 476 | 632 | 43.0 | -2.8 | -68 | -11 | -79 |
| Town of Westport | 128 | 113 | 53.1 | 121 | 103 | 54.0 | +0.9 | -7 | -10 | -17 |
| Village of Cross Plains | 1177 | 929 | 55.9 | 1241 | 1132 | 52.3 | -3.6 | +64 | +203 | +267 |
| **District** | 14596 | 8608 | 62.9 | 14263 | 9457 | 60.1 | -2.8 | -333 | +849 | +516 |

#### Comparison-unit change table
Units are grouped so the geography matches across years (see Q5).

| Comparison unit | Yes% 22 | Yes% 26 | Chg pts | Chg Yes | Chg No | Chg ref votes |
|---|---|---|---|---|---|---|
| C Madison Wd 095 | 70.0 | 55.6 | -14.4 | -13 | 0 | -13 |
| C Madison Wd 100 | 80.0 | 63.4 | -16.6 | +1 | +15 | +16 |
| C Madison Wd 101 | 63.8 | 56.6 | -7.2 | -13 | +29 | +16 |
| C Madison Wd 102 | 69.7 | 53.7 | -16.0 | -32 | +35 | +3 |
| C Madison Wd 109 | 69.6 | 57.9 | -11.7 | -65 | +19 | -46 |
| C Madison Wd 114 | 73.4 | 70.3 | -3.1 | -61 | -9 | -70 |
| C Madison Wd 115 | 82.5 | 74.3 | -8.2 | -7 | +2 | -5 |
| C Madison Wd 117 | 78.3 | 74.8 | -3.5 | -8 | +4 | -4 |
| C Madison Wd 118 (boundary/growth caveat) | 71.7 | 68.1 | -3.6 | +297 | +178 | +475 |
| C Madison Wd 119 | 66.1 | 61.4 | -4.7 | -104 | +48 | -56 |
| C Madison Wds 113/139/140/141 (2022) vs 120/134/135 (2026) | 71.8 | 65.0 | -6.8 | -165 | -61 | -226 |
| C Middleton Wds 1-4 | 69.0 | 67.7 | -1.3 | -50 | +37 | -13 |
| C Middleton Wds 5-8 (+21) | 67.1 | 62.5 | -4.6 | -99 | +132 | +33 |
| C Middleton Wds 9-13,19 (+22, +24) | 66.9 | 64.7 | -2.2 | +46 | +125 | +171 |
| C Middleton Wds 14-18 | 64.4 | 62.6 | -1.8 | -177 | -33 | -210 |
| T Berry Wds 1-2 | 34.4 | 28.9 | -5.5 | -25 | +8 | -17 |
| T Cross Plains Wds 1-2 | 50.6 | 46.6 | -4.0 | -33 | -1 | -34 |
| T Middleton (all wards) | 57.9 | 57.8 | -0.1 | +186 | +139 | +325 |
| T Springfield Wds 1-4 | 45.8 | 43.0 | -2.8 | -68 | -11 | -79 |
| T Westport Wds 1-5 | 53.1 | 54.0 | +0.9 | -7 | -10 | -17 |
| V Cross Plains Wds 1-6 | 55.9 | 51.8 | -4.1 | -4 | +164 | +160 |
| V Cross Plains Wd 7 (new in 2026) | n/a | 63.6 | n/a | +68 | +39 | +107 |

- **Madison's west-side wards combined** (118 + 139/140/141 in 2022; 118 + 120/134/135 in 2026), which removes the renumbering problem: 724 Yes / 285 No (71.8%) became 856 Yes / 402 No (68.0%), a change of -3.7 pts and +117 No.
- **Top-of-ticket partisanship in fully-in-district units was essentially unchanged.** Governor Democratic two-party share:
  - City of Middleton fully-in units: 84.0% (2022) to 84.9% (2026)
  - Village of Cross Plains 1-6: 71.1% to 70.9%
  - Town of Middleton: 68.3% to 68.8%
  - Madison 118-119: 77.2% to 77.4%

  Source: Dane County Governor precinct results, [2022](https://elections.countyofdane.com/Precincts-Result/145/0004) and [2026](https://elections.countyofdane.com/Precincts-Result/197/0004).
- **Countywide governor result, 2026:** David Crowley/Sarah Godlewski (DEM) 80.3%, Tom Tiffany/David Varnam (REP) 19.5%. — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197)

### Inferences
- **Where the +849 net No came from:**
  - City of Middleton: about 31% (+261), mostly Wds 5-8/21 (+132) and Wds 9-13/19/22/24 (+125, which includes the new Ward 24)
  - Madison wards: about 31% (+260)
  - Village of Cross Plains: about 24% (+203), of which Wds 1-6 gave +164 and new Ward 7 gave +39
  - Town of Middleton: about 16% (+139)

  The rural towns together netted -14 No.
- **Where the -333 net Yes loss came from:** City of Middleton (-280) and Madison (-170), partly offset by the growing Town of Middleton (+186) and the Village (+64).
- **Village of Cross Plains Wds 1-6 is the clearest "persuasion" swing.** Yes was flat (-4) while No rose by 164 on nearly the same ballots cast (2,252 to 2,340). The extra voters there broke almost entirely No.
- **City of Middleton Wds 14-18 is different:** Yes fell 177 while No fell 33, and total ref votes dropped 210 despite similar ballots cast. That pattern is consistent with roll-off (10.1% in 2026) rather than conversion to No.
- **The Town of Middleton held its share (57.8%) while growing.** Ref votes rose 8.8%, and new voters split roughly like existing ones.
- **Madison's big percentage drops come from small samples.** Wd 102 had 214 votes and Wd 109 had 280, both in wards that are mostly outside MCPASD. Madison as a whole (-5.6) is the more reliable signal.
- **Swing does not look like a partisan electorate shift.** Governor Democratic share was flat or slightly up in the same units, so the Yes decline looks referendum-specific: a larger ask, tax fatigue or a second-time request. These are hypotheses, not tested here.

### Gaps
- I don't have Madison ward boundary maps to show whether wards 118/139/140/141 were merged or renumbered. Treat individual Madison ward comparisons cautiously.
- I found no reliable data on the reasons behind the swing, such as polling or exit data.

## Q4. Did turnout differ, and did roll-off on the referendum rise in 2026 (back-of-ballot effect)?

### Takeaway
Turnout was modestly higher in 2026:
- Ref votes: +2.2%
- Ballots cast countywide: +3.5%
- Ballots cast in fully-in-district units: +7.7%, partly from growth

Roll-off on the MCPASD question was **7.2% district-wide in 2026** (1,839 of 25,559 ballots that had the question). On comparable fully-in-district geography it rose from about 5% in 2022 to about 7%, but the rise is concentrated in the City and Town of Middleton:
- City of Middleton: 5.0% to 8.6%
- Town of Middleton: about 3.6% to 7.2-8.1%

Roll-off actually fell in the Village of Cross Plains (6.5% to 3.2%) and in Madison Wds 118-119 (4.9% to 3.5%). So a uniform "back-of-ballot" effect is not supported. A layout difference specific to Middleton ballots is plausible but unverified.

### Cited Findings
Computed from the Dane County precinct tables and the raw file. Details are in `rolloff_by_contest.csv`.

- **2026 district-wide:** under-votes 1,834 and over-votes 5 on 25,559 ballots that had the question, a roll-off of 7.2%.
- **2026 roll-off by municipality:**

| Municipality | Roll-off | Share of ballots with the question | Notes |
|---|---|---|---|
| City of Middleton | 8.9% | 12,235 of 25,559 (48%) | 1,090 roll-offs, 59% of all MCPASD roll-off |
| Town of Middleton | 7.2% | | |
| Town of Cross Plains | 7.5% | | |
| Madison wards | 5.2% | | |
| Springfield | 5.0% | | |
| Berry | 3.3% | | |
| Village of Cross Plains | 3.2% | | |
| Westport | 12.8% | | only 257 ballots |

  Sources: [2026 precinct table](https://elections.countyofdane.com/Precincts-Result/197/0040); [raw file](https://elections.countyofdane.com/Election-RawResults)
- **Roll-off by contest in the same units:** the governor race, the other ballot questions and the MCPASD question.

| Units (fully or nearly fully in MCPASD) | Ballots 2022 | Ballots 2026 | Governor roll-off 22 / 26 | Other questions 2022 (county advisory #1, #3) | Statewide questions 2026 (#1, #2, #3) | MCPASD 2022 | MCPASD 2026 |
|---|---|---|---|---|---|---|---|
| City of Middleton Wds 1-4, 5-8/21, 9-13/19/22/24 | 9,146 | 9,720 | 0.6% / 0.7% | 1.6%, 1.9% (City levy ref 5.1%) | 3.7%, 3.1%, 3.4% | 5.0% | 8.6% |
| Town of Middleton (all) | 3,823 | 4,363 | 0.3% / 0.6% | 1.0%, 1.6% | 3.1%, 2.5%, 3.0% | 3.6%* | 8.1%* (7.2% direct) |
| Village of Cross Plains Wds 1-6 | 2,252 | 2,340 | 0.4% / 0.3% | 1.1%, 2.2% | 3.0%, 2.9%, 3.1% | 6.5% | 3.2% |
| Madison Wds 118-119 | 2,361 | 2,762 | 0.5% / 0.4% | 1.3%, 1.5% | 3.0%, 2.5%, 3.0% | 4.9% | 3.5% |

  \*Town of Middleton is computed as ballots cast minus Yes and No, which includes the roughly 43 ballots without the question in Wds 5-8.

  Sources: [2022 ballots cast](https://elections.countyofdane.com/Precincts-Result/145/0002), [2022 governor](https://elections.countyofdane.com/Precincts-Result/145/0004), [2022 Dane Co Ref #1](https://elections.countyofdane.com/Precincts-Result/145/0033), [2022 Dane Co Ref #3](https://elections.countyofdane.com/Precincts-Result/145/0035), [2022 C. Middleton levy ref](https://elections.countyofdane.com/Precincts-Result/145/0040), [2026 ballots cast](https://elections.countyofdane.com/Precincts-Result/197/0002), [2026 governor](https://elections.countyofdane.com/Precincts-Result/197/0004), [2026 State Ref 1](https://elections.countyofdane.com/Precincts-Result/197/0034), [2](https://elections.countyofdane.com/Precincts-Result/197/0035), [3](https://elections.countyofdane.com/Precincts-Result/197/0036)
- **Comparable fully-in-district geography combined** (City of Middleton full units + Village Wds 1-6 + Madison 118-119): roll-off 715 of 13,759 (5.2%) in 2022 and 1,008 of 14,822 (6.8%) in 2026. Adding the Town of Middleton on a ballots-minus-votes basis gives 4.8% (852/17,582) and 7.1% (1,360/19,185).
- **Other questions on the ballot:**
  - 2022: three Dane County advisory referendums (marijuana tax and regulation, expunge marijuana convictions, repeal abortion ban), plus a City of Middleton levy-limit referendum on City ballots. — [Dane County 2022 results](https://elections.countyofdane.com/Election-Result/145)
  - 2026: three statewide constitutional amendment questions (partial veto, freedom to gather, governmental discrimination). — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197)
- **Turnout:**
  - Dane County total ballots cast: 302,575 (2022) to 313,218 (2026), +3.5%. County-reported registered voters: 376,531 to 396,061.
  - MCPASD ref votes: 23,204 to 23,720 (+2.2%).
  - Ballots cast in the fully-in-district comparison units: 13,759 to 14,822 (+7.7%).
  - Town of Middleton ballots cast: 3,823 to 4,363 (+14.1%).

  Sources: [Dane County ballots cast 2022](https://elections.countyofdane.com/Precincts-Result/145/0002), [2026](https://elections.countyofdane.com/Precincts-Result/197/0002)

### Inferences
- **2022 turnout on the question is not directly measurable.** Applying the roughly 5% roll-off seen on comparable 2022 geography, 2022 ballots with the MCPASD question were about 24,400-24,500, so 2026 (25,559) was about 4-5% higher. This is an estimate, not a published figure.
- **2026 MCPASD roll-off is higher than the statewide questions printed just before it.** It is about 2.3-2.8 times higher in the City and Town of Middleton, but about equal in the Village of Cross Plains and Madison Wds 118-119. In 2022 the Village showed the opposite: high MCPASD roll-off of 6.5% against 1-2% on the county questions.
- **This looks like a ballot-layout effect that varies by ballot style and municipality,** such as which column or side the school question landed on, rather than a uniform back-of-ballot effect. It is consistent with the internal notes for the City and Town of Middleton, but I did not verify ballot layouts.
- **General roll-off on ballot questions roughly doubled in 2026** (1-2% on 2022's county advisory questions vs 2.5-3.7% on 2026's statewide questions), so some increase is ballot-wide.
- **Scale:** if the City and Town of Middleton had kept their 2022 roll-off rates, roughly 550 more Yes/No votes would have been cast. At those areas' 58-65% Yes rates, that would have added only about 100-150 to the Yes margin. Roll-off did not threaten passage, but it does account for part of the Yes decline in City of Middleton Wds 14-18.

### Gaps
- **2022 under-votes are not published.** Dane County's raw file, which carries the over/under counts, is available only for the current election; `/Election-RawResults/145` returns a web page, not data. 2022 roll-off can therefore only be estimated for units fully inside MCPASD.
- I could not obtain sample ballots or ballot layouts for either year, by municipality, to confirm where the school question was printed. Dane County's Ballot-Information page lists only the "What's on the Ballot" summary, and the municipal and district sites were not reachable or turned up nothing.
- I found no source for 2022 vs 2026 MCPASD-only registration or turnout.

## Q5. Were wards renumbered or changed between 2022 and 2026, and how were matching issues handled?

### Takeaway
Yes, reporting units changed in four of the eight municipalities:
- **City of Middleton:** Wds 21 and 22 were merged into neighbouring units, and Ward 24 is new.
- **Town of Middleton:** one unit (Wds 1-8) became four (1,3-4; 2,4A; 5-8; 8A).
- **Village of Cross Plains:** Ward 7 is new.
- **City of Madison:** Wds 113, 139, 140 and 141 dropped out of the list, and 120, 134 and 135 were added.

I compared at combined-unit or municipality level wherever the geography didn't match.

### Cited Findings
- **Reporting-unit lists by year:** see the Q2 tables. Sources: [2022 precinct table](https://elections.countyofdane.com/Precincts-Result/145/0042); [2026 precinct table](https://elections.countyofdane.com/Precincts-Result/197/0040)
- **2026 splits line up with assembly district lines:** Town of Middleton ward 8A is in AD 79; wards 1 and 3-8 are in AD 80; wards 2 and 4A are in AD 81. Village of Cross Plains wards 1-6 are in AD 80 and ward 7 in AD 81. City of Middleton wards 20 and 23 are in AD 80, and wards 1-19, 21-22 and 24 in AD 81. — [Dane County What's on the Ballot, Nov 2026](https://elections.countyofdane.com/documents/pdf/What-s-on-the-Ballot-Nov-2026.pdf)
- **2022 Madison wards 139/140/141** had 66, 204 and 1 ballots, with ref votes of 62, 203 and 1. **2026 Madison wards 120/134/135** had 6, 12 and 31 ballots, with ref votes of 6, 10 and 24. Madison Ward 118's ballots rose from 798 to 1,264. — [2022](https://elections.countyofdane.com/Precincts-Result/145/0002), [2026](https://elections.countyofdane.com/Precincts-Result/197/0002) ballots cast

### Inferences
- **"A" wards (4A, 8A) and the new Ward 7 / Ward 24** look like splits created to follow new district lines or annexations. Wisconsin's new legislative maps took effect for the 2024 elections; that is general background, not sourced here. The 2026 What's on the Ballot shows these wards split exactly at assembly lines. This is not confirmed by a municipal ward ordinance.
- **Madison Wd 118's jump of +466 ballots and the disappearance of 139/140 (about 270 ballots)** suggest these areas were re-warded or merged into 118 and nearby wards, possibly alongside new development. Individual Madison ward comparisons are therefore unreliable, and the Madison aggregate should be used.

How the comparisons were built (see `ward_change.csv`, column `comparison_unit`):
- **Exact matches:** City of Middleton 1-4, 14-18 and 20/23; Berry 1-2; Town of Cross Plains 1-2; Springfield 1-4; Westport 1-5; Village of Cross Plains 1-6; and same-numbered Madison wards, compared with caution.
- **City of Middleton:** 2022 "5-8" + "21" was compared to 2026 "5-8, 21". 2022 "9-13, 19" + "22" was compared to 2026 "9-13,19,22,24", so the 2026 total includes the new Ward 24.
- **Town of Middleton:** compared only at the town level.
- **Village of Cross Plains:** Ward 7 is reported as new. The village total includes it.
- **Madison:** 2022 wards 113/139/140/141 were grouped against 2026 wards 120/134/135, plus a check combining them with Ward 118. Madison is analysed mainly as an aggregate.
- **Roll-off:** compared only where a unit is fully inside MCPASD in both years. Full inclusion is judged from 2026, where ballots cast equal Yes + No + under + over, and assumed to hold in 2022 for units with the same definition.

### Gaps
- I did not get the actual ward ordinances or annexation records (City of Middleton, Town of Middleton, Village of Cross Plains, City of Madison) to confirm what changed. City and municipal sites were not tried after the district and news hosts failed with ENOTFOUND.
- I can't confirm whether boundaries of same-numbered units, such as City of Middleton 1-4 or Madison 119, changed slightly.

## Q6. Is the 2026 count still unofficial, and when is the canvass?

### Takeaway
Yes. As of Nov. 5, 2026, Dane County shows the MCPASD question as **unofficial**: there is no "Official Canvass" label and the API's FinalizedDate is null. Wisconsin county boards of canvassers must convene by 9 a.m. Tuesday, Nov. 10, 2026 and deliver certified results by Nov. 17, 2026, which is secondhand. In 2022 Dane County finalized the MCPASD canvass on Nov. 15, seven days after the election.

### Cited Findings
- Dane County's 2026 page is headed "2026 General Election Unofficial Results". It says the County Clerk "is responsible for tabulating and certifying the results of elections for county, state and federal offices and referenda. These results are labeled as Official Canvass. All other results appearing on this page, i.e. municipal and school district elections, are unofficial." — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197)
- The 2026 MCPASD precinct export shows "All Precincts Reported On: 11/3/2026 11:27 PM", with no canvass label. The API's election metadata has FinalizedDate null and PrecinctsReportedDate 2026-11-03T23:27. — [Excel](https://elections.countyofdane.com/Precinct-ResultExcel/197/0040); [API](https://api.danecounty.gov/api/v1/elections/precinctresults/197/0040)
- In 2022 the same contest is labeled "Official Canvass - Finalized On: 11/15/2022 2:57 PM". — [Dane County 2022 Excel](https://elections.countyofdane.com/Precinct-ResultExcel/145/0042)
- County boards of canvassers must convene by 9 a.m. on Tuesday, Nov. 10, 2026 (Wis. Stat. § 7.60(3)) and deliver certified statements to WEC by Nov. 17, 2026 (14 days after the election). This is secondhand via search summary. — [Campaign Legal Center 2026 Wisconsin Certification Guide](https://campaignlegal.org/sites/default/files/2026-08/2026%20Wisconsin%20Certification%20Guide_Final.pdf); [Brennan Center](https://brennancenter.org/our-work/research-reports/wisconsin-election-certification-processes-and-guardrails)
- WMTV reportedly said school referendum results "will be canvassed by districts this month before they are considered official." This is secondhand via search summary. — [WMTV, Nov. 4, 2026](https://www.wmtv15news.com/2026/11/04/voters-pass-middleton-cross-plains-school-district-referendum/)

### Inferences
- **Expected timing:** the official Dane County figures for the MCPASD question will likely post between about Nov. 10 and Nov. 17, 2026. In 2022 the county did label and finalize this contest as "Official Canvass".
- **Expected size of changes:** changes from provisional ballots or canvass corrections are usually a handful of votes. With a 4,806-vote margin, they will not change the outcome, but ward-level numbers could shift slightly.
- **Re-run when official:** re-download the ward tables from https://elections.countyofdane.com/Precinct-ResultExcel/197/0040 (or the API) after the canvass and re-run the CSVs.

### Gaps
- **Who certifies:** the 2026 disclaimer implies school district results are unofficial on the county site, while WMTV says districts canvass them. The 2022 result shows Dane County did label the MCPASD result "Official Canvass". I did not confirm under which statute, or by which body, the MCPASD question is certified in 2026.
- **Unreachable sources:**

| Host | Result |
|---|---|
| mcpasd.k12.wi.us | ENOTFOUND |
| wisconsinexaminer.com | ENOTFOUND |
| wkow.com | ENOTFOUND |
| dpi.wi.gov | reachable, but the guessed referenda URL returned 404 |
| Dane County past-election raw files | not offered |

  I did not retry hosts the coordinator already listed as blocked (wispolitics.com, channel3000.com, wmtv15news.com, elections.wi.gov and others). Information from those is secondhand via WebSearch summaries.
