# Waunakee Community School District referendums (Nov. 3, 2026) compared with MCPASD

Status: All Nov. 3, 2026 figures are **unofficial** Dane County Clerk election-night results (9 of 9 Waunakee reporting units; the feed shows `FinalizedDate: null`, last published 2026-11-03 23:27). The canvass is due by Nov. 17, 2026. The 2020, 2022 and 2024 figures are Dane County **official canvass** results.

Data files saved in this folder:
- `waunakee_ward_results_2020_2026.csv`: one row per reporting unit, per Waunakee question, per year (2020, 2022, 2024, 2026). Columns: Yes/No, whole-unit ballots, valid-vote share of unit ballots, Democratic two-party % (Biden 2020, Evers 2022, Harris 2024, Crowley 2026), Kaul AG two-party % (2022, 2026), Yes − Dem, and a split-unit flag.
- `waunakee_rolloff_2026.csv`: 2026 under- and over-votes by unit for both Waunakee questions, the three statewide constitutional questions and governor, from the Dane County raw results file.
- `waunakee_mcpasd_dpi_mill_rates.csv`: DPI levy, TIF-out equalized value and mill rate, 2020-21 to 2025-26, for Waunakee (6181), MCPASD (3549), DeForest (1316) and Sun Prairie (5656).

Method: the same Dane County precinct API used in `partisan_correlation.md`, `https://api.danecounty.gov/api/v1/elections/precinctresults/{election}/{race}`.

| Election | ID | Waunakee race(s) |
|---|---|---|
| Nov 2020 | 124 | 0045 |
| Nov 2022 | 145 | 0050 bonds, 0051 operating |
| Nov 2024 | 172 | 0051 |
| Nov 2026 | 197 | 0041 operating, 0042 bonds |

Partisan races: governor 0004 and AG 0005 (2022, 2026); president 0004 (2020, 2024). Ballots cast are race 0002. Statewide questions in 2026 are races 0034–0036. Under- and over-votes come from the [Dane County raw results file](https://elections.countyofdane.com/Election-RawResults) (current election only).

My 2026 and 2022 district totals and gaps match the cross-check in `partisan_correlation.md`: 2026 −13.9 / −14.9; 2022 −13.2 / −5.6.

## 1. What was on Waunakee's ballot: wording, amount, recurring vs. nonrecurring, purpose and tax claim, next to MCPASD

### Takeaway
Waunakee put two questions on the ballot.
- **Q1** was a **recurring (permanent)** revenue-limit increase. It is phased in to **$10.5M a year**: $4.2M in 2027-28, of which $2.1M replaces an expiring 2024 temporary amount, then +$2.1M a year through 2030-31. It is for staff compensation only.
- **Q2** was **$97.5M in general obligation bonds**, mainly for Waunakee Community High School (WCHS).

The district claimed **$17 (Q1) + $25 (Q2) = $42 per $100,000 of value per year, or about $210 a year on a $500,000 home**.

MCPASD's question was **nonrecurring** (four years, $118.5M total). Its claimed impact was "$120 per $100K over four years" cumulative, which is $59 per $100K a year by year 4.

**Correction to the brief.** The Cap Times did not print "$210 per year per $100K" for Waunakee. It printed about $210 a year on "the average home, valued at about $500,000." Per $100K, the Waunakee claim was $42 a year.

### Cited Findings
- **Q1 ballot wording:** "Shall the Waunakee Community School District, Dane County, Wisconsin be authorized to exceed the revenue limit specified in Section 121.91, Wisconsin Statutes, by $4,200,000 for the 2027-2028 school year; by an additional $2,100,000 for the 2028-2029 school year; by an additional $2,100,000 for the 2029-2030 school year; and by an additional $2,100,000 for the 2030-2031 school year (for a total of $10,500,000 and to remain at that amount thereafter), for recurring purposes consisting of ongoing operational expenses and employee compensation expenses?" — [WCSD 2026 Referendum Newsletter](https://www.waunakee.k12.wi.us/fs/resource-manager/view/1da25b04-b199-4671-b104-b2d50023302b); resolution text at [WCSD referendum page](https://www.waunakee.k12.wi.us/community/2026referendum)
- **Q1 district description:** "recurring funding for the district's annual operating budget ... to provide competitive salaries and benefits." The district "would maintain its current annual operational funding of $2.1 million (approved in 2024) and increase this amount by up to $2.1 million per year ... phased in over four years, beginning in the 2027-2028 school year. After the four-year phase-in, our new revenue limit would remain at this level." — [WCSD referendum page](https://www.waunakee.k12.wi.us/community/2026referendum)
- **Q1 is permanent.** The Tribune: "It is a recurring referendum, so that amount would be permanent and continue after 2030-31." — [Waunakee Tribune / Tribune Enterprise, Aug. 2026](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-district-to-hold-fall-referendum-on-97-5-million-high-school-project-operational/article_c8ffecd3-9bf2-4f6a-b01f-84d42f2fe55d.html). The Cap Times: it "would permanently increase taxes by up to $10.5 million." — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **Channel 3000 got the structure wrong.** It described Q1 as "$10.5 million ... through the 2030-31 school year." That reads as time-limited, but the ballot says "to remain at that amount thereafter." — [Channel 3000, Aug. 2026](https://www.channel3000.com/news/waunakee-school-district-adds-2-referendums-to-november-ballot/article_5f6f981a-e92a-4707-9e98-ee964c7c3972.html)
- **Q1 sole purpose:** "provide competitive compensation to all employee groups." The board directed a policy "to lower annual amounts if the state budget provides resources to match annual budgetary expenditures." — [WCSD 2026 Referendum Presentation](https://www.waunakee.k12.wi.us/fs/resource-manager/view/ed84ad2b-2a12-45b9-a894-107102763cc2)
  - Summers: the board can choose "in October to not levy the full amount that's been approved by the public." — [Tribune, Aug. 2026](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-district-to-hold-fall-referendum-on-97-5-million-high-school-project-operational/article_c8ffecd3-9bf2-4f6a-b01f-84d42f2fe55d.html)
  - Board VP Chris Sonne: "If we don't need the (referendum) money, we're not going to use the money." — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **Q2 ballot wording:** general obligation bonds "in an amount not to exceed $97,500,000 for the public purpose of paying the cost of a school facility improvement project consisting of: removal of an older portion of the High School and construction of additions and renovations at the High School; renovations at the old middle school (known as the High School South Campus); outdoor athletic field renovations and improvements at the High School Campus; district-wide renovations, capital maintenance and site improvements; and acquisition of furnishings, fixtures and equipment." — [WCSD Newsletter](https://www.waunakee.k12.wi.us/fs/resource-manager/view/1da25b04-b199-4671-b104-b2d50023302b)
- **Q2 breakdown:**
  - About $88.7M for WCHS renovation and new construction
  - About $4.4M for South Campus (former middle school)
  - About $4.4M for outdoor athletic fields

  The district called it the "final phase" of a long-range facilities plan begun after a failed 2010 referendum. — [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq)
- **How the price came down:** from $105M (surveyed) to $97.5M. The board voted 5-1 (Ted Frey dissenting). Applying energy rebates cut the chosen option from $99.5M. — [Tribune, summer 2026](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-picks-97-5-million-referendum-option-for-high-school-improvements/article_90cac93d-23e2-4c4b-aa11-491f4174f1a9.html). Both final resolutions passed 7-0 on Aug. 10, 2026. — [WCSD referendum page](https://www.waunakee.k12.wi.us/community/2026referendum)
- **District tax-impact claim:**
  - "Q1: Operational (Increase of $0.17 per $1,000)" = $17.00 per $100,000
  - "Q2: Capital (Increase of $0.25 per $1,000)" = $25.00
  - "Annual Combined Tax Impact" = $42.00 per $100K; $126 at $300K; $210 at $500K; $315 at $750K
  - "Example: For a home with an estimated fair market value of $500,000, the combined estimated property tax impact would be approximately $210 per year (or about $17.50 per month)."
  - "Tax impacts shown are estimates based on interest rates, borrowing terms and timing, and may change."

  — [WCSD 2026 Referendum Fact Sheet](https://www.waunakee.k12.wi.us/fs/resource-manager/view/54156bdc-8bac-43e4-8464-c6c34af2a164); [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq)
- **What the Cap Times printed, both times.** Oct. 20: "Waunakee's referendums combined would raise property taxes on the average home, valued at about $500,000, by approximately $210 per year." The same story said MCPASD "would raise tax bills by $120 per $100,000 of property value over the next four years." The Nov. 4 story repeated both. — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html); [Cap Times, Nov. 4, 2026](https://captimes.com/news/elections/dane-county-voters-pass-three-school-funding-referendums/article_612b45b9-058a-4b7c-ae10-3712d49218ff.html)
- **The district's own financing plan shows a larger debt-rate rise than the fact sheet.** The PMA Securities plan linked from the FAQ ("most recent ... presented at the Budget Committee on October 6," dated 09/29/26) shows the debt-service (Fund 39) mill rate:
  - $1.55 in the 2025-26 base year
  - $1.31 in the 2026 levy year
  - $1.76 in 2027, $1.99 in 2028, $2.27 in 2029
  - $2.20–$2.35 through 2048
  - Printed summary: "Base Year (2025-26): $1.55 ... Max Year: $2.35 ... Impact: $0.80."
  - Assumptions: borrowing of $44M (2027), $19.5M (2028) and $34M (2029); "2025 Equalized Valuation (TID-OUT) of $5,520,979,855 with annual growth of 4.20%"; existing debt follows "2022 referendum financing plan."

  — [PMA example financing plan via WCSD FAQ](https://drive.google.com/file/d/1a6wr9TiG0BIGDVOu5zMEQY7pncvRA5O_/view)
- **Earlier estimates, same as the final Q1 figure.** At the spring survey stage, the district said the operating extension alone would raise the mill rate by $0.17 ($17 per $100K). Both questions together would add $0.43 ($43 per $100K), with the then-$105M capital plan. — [Tribune, May 2026](https://www.hngnews.com/tribune_enterprise/news/local/waunakee-school-district-survey-results-show-support-for-operational-capital-building-referendums/article_a023290f-ea63-426c-9fea-d71f6ffaab56.html); [Tribune, April 2026](https://www.hngnews.com/tribune_enterprise/news/community-gets-deeper-look-at-waunakee-schools-referendum-survey/article_9ea62010-4d13-4743-a81a-5722a27b0c8e.html)
- **MCPASD side, for comparison** (already established in `tax_messaging.md`): four-year nonrecurring authority of $24.9M, $27.9M, $31.1M and $34.6M ($118.5M). The district's per-$100K impact is $0, $21, $40 and $59 (year 4). The Cap Times called it "seventh largest proposed in state history" (Wisconsin Policy Forum). — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)

### Inferences
- **The Cap Times put mismatched numbers side by side.** Waunakee's figure is annual and per $500K home. MCPASD's is a four-year cumulative per $100K. Expressed the same way, the districts' own claims are:
  - Per $100K per year: Waunakee $42 (both questions); MCPASD $59 by year 4.
  - On a $500K home per year: Waunakee $210; MCPASD $295 by year 4.

  So on the districts' own claims, MCPASD's year-4 annual cost was higher. MCPASD's ends after four years. Waunakee's Q1 is permanent and Q2 is roughly 20-year debt.
- **Waunakee's Q1 claim of $0.17 per $1,000 looks low against the ballot amounts.** This is my arithmetic, using the same referendum-only method used for MCPASD in `tax_messaging.md`.
  - New operating levy above 2026-27 would be $2.1M (2027-28), $4.2M, $6.3M and $8.4M (2030-31). The $2.1M temporary amount carries over.
  - On PMA's equalized-value path ($5.52B growing 4.2% a year), that is about $0.35, $0.67, $0.97 and $1.24 per $1,000 if levied in full with nothing else changing.
  - Even with the 10.2% value jump DOR estimated for 2026 (Q7), year 4 is still above $1 per $1,000.
  - $0.17 per $1,000 equals only about $1.0M of levy, about half of the first year's new money.
  - The district may plan not to levy the full amount early. Business director Allie Newton said "in the first two years, the full $2.1 million may not be needed" ([Tribune](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-picks-97-5-million-referendum-option-for-high-school-improvements/article_90cac93d-23e2-4c4b-aa11-491f4174f1a9.html)).
  - The derivation of $0.17 was not published. Treat this as a flagged discrepancy, not a proven error.
- **Q2's $0.25 per $1,000 matches only the first year of PMA's plan.**
  - Taking total levy minus existing debt and dividing by equalized value, new-debt-only levy is about $0.28 per $1,000 in levy year 2027. It rises to about $0.70–0.75 in 2029–2031, and about $1.5–1.6 in 2044–2048 after the 2022 debt drops off (my arithmetic from the plan's columns).
  - PMA's own printed "Impact: $0.80" is the maximum total debt rate versus 2025-26, and includes the rising 2022-referendum debt levy.
  - The district's flat "$25 per $100K per year" therefore understates the sustained effect under its own adviser's plan.

### Gaps
- I did not find how WCSD derived $0.17 and $0.25. Its year-by-year tax-impact slides are images in the presentation.
- No year-by-year Q1 tax table was published, unlike MCPASD's $0/$21/$40/$59.

## 2. Results: Yes/No totals and Yes %, by municipality and reporting unit

### Takeaway
Both questions passed narrowly (unofficial):
- **Q1 (operating):** Yes 6,787 to No 6,114, **52.6%** (margin 673)
- **Q2 ($97.5M bonds):** Yes 6,647 to No 6,219, **51.7%** (margin 428)

The Village of Waunakee (67% of votes) carried both: Q1 54.5%, Q2 52.3%. The Town of Westport, the second-largest bloc, **rejected Q1 (49.6%)** but passed Q2 (52.3%). The rural towns of Dane, Springfield and Vienna voted No on both.

For comparison, MCPASD passed 60.1% (14,263–9,457), a 4,806-vote margin.

### Cited Findings
- **District totals (Dane County, unofficial):**
  - Ref 1 "(Exceed revenue limit)": Yes 6,787 (52.6%), No 6,114 (47.4%)
  - Ref 2 "(Bonds $97,500,000)": Yes 6,647 (51.7%), No 6,219 (48.3%)
  - 9 of 9 precincts reporting

  — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197); [Waunakee Ref 1 by precinct](https://elections.countyofdane.com/Precincts-Result/197/0041); [Ref 2 by precinct](https://elections.countyofdane.com/Precincts-Result/197/0042)
- **Media totals agree with Dane County.**
  - WMTV gave Q1 as 6,787–6,114 "according to unofficial results." It then repeated the same numbers for Q2, which is an error: Dane shows 6,647–6,219. — [WMTV, Nov. 4, 2026](https://www.wmtv15news.com/2026/11/04/referendum-questions-pass-waunakee-school-district/)
  - Cap Times: Q2 "Nearly 52%"; Q1 "nearly 53%." — [Cap Times, Nov. 4, 2026](https://captimes.com/news/elections/dane-county-voters-pass-three-school-funding-referendums/article_612b45b9-058a-4b7c-ae10-3712d49218ff.html)
- **2026 by reporting unit.** "Ballots w/ Q" is Yes + No + under + over on Q1, from the raw file. "Share" is ballots with the Waunakee question ÷ whole-unit ballots.

| Reporting unit | Q1 Yes | Q1 No | Q1 Yes % | Q2 Yes | Q2 No | Q2 Yes % | Ballots w/ Q | Unit ballots | Share |
|---|---|---|---|---|---|---|---|---|---|
| V Waunakee Wds 1-5 | 2,449 | 2,077 | 54.1 | 2,268 | 2,252 | 50.2 | 4,674 | 4,674 | 100% |
| V Waunakee Wds 6-16 | 2,280 | 1,866 | 55.0 | 2,262 | 1,877 | 54.7 | 4,275 | 4,275 | 100% |
| V Waunakee Wd 17 | 0 | 0 | – | 0 | 0 | – | 0 | 0 | – |
| T Westport Wds 1-5 | 1,236 | 1,256 | 49.6 | 1,300 | 1,188 | 52.3 | 2,674 | 2,931 | 91.2% |
| T Vienna Wds 1-2 | 236 | 267 | 46.9 | 223 | 275 | 44.8 | 512 | 847 | 60.4% |
| T Springfield Wds 1-4 | 132 | 226 | 36.9 | 117 | 238 | 33.0 | 372 | 1,552 | 24.0% |
| T Dane Wd 1 | 20 | 55 | 26.7 | 23 | 51 | 31.1 | 78 | 520 | 15.0% |
| C Madison Wd 035 | 167 | 224 | 42.7 | 181 | 207 | 46.6 | 415 | 1,239 | 33.5% |
| C Middleton Wds 14-18 | 267 | 143 | 65.1 | 273 | 131 | 67.6 | 439 | 2,954 | 14.9% |
| **Total** | **6,787** | **6,114** | **52.6** | **6,647** | **6,219** | **51.7** | **13,439** | | |

  — computed from [Dane race 0041](https://elections.countyofdane.com/Precincts-Result/197/0041), [0042](https://elections.countyofdane.com/Precincts-Result/197/0042), [ballots cast 0002](https://elections.countyofdane.com/Precincts-Result/197/0002) and the [raw results file](https://elections.countyofdane.com/Election-RawResults)

- **By municipality, 2026:**
  - Village of Waunakee: Q1 4,729–3,943 (54.5%); Q2 4,530–4,129 (52.3%)
  - Town of Westport: Q1 49.6%; Q2 52.3%
  - Town of Vienna: Q1 46.9%; Q2 44.8%
  - City of Middleton portion: Q1 65.1%; Q2 67.6%
  - City of Madison portion: Q1 42.7%; Q2 46.6%
  - Town of Springfield: Q1 36.9%; Q2 33.0%
  - Town of Dane: Q1 26.7%; Q2 31.1%

  — computed from Dane County 2026 files above
- **Which municipalities are in the footprint.** Dane County lists only the nine units above as carrying the Waunakee questions in 2026: Village of Waunakee; Towns of Westport, Vienna, Springfield and Dane; City of Madison Wd 35; City of Middleton Wds 14-18.
  - **No Town or Village of Windsor, Town of Berry or Town of Middleton unit** carried a Waunakee question in 2020, 2022, 2024 or 2026.
  - The Town of Westport is split between Waunakee (2,674 ballots) and MCPASD (257 ballots). These sum exactly to the town's 2,931 ballots. — computed from [Dane races 0040/0041](https://elections.countyofdane.com/Election-Result/197) and the raw file

### Inferences
- **The Q2 margin rested on the newer part of the Village.** In Village Wds 1-5, Q2 passed by 16 votes (2,268–2,252). Village Wds 6-16 and Westport supplied the margin.
- **Westport split its votes.** It favored the building (52.3%) over the permanent operating increase (49.6%). The Village did the reverse (54.5% operating, 52.3% building).
- **Small swings would have flipped the results.** About 215 voters switching would have defeated Q2, and about 337 would have defeated Q1. That is roughly 1.7% and 2.6% of the votes cast.

### Gaps
- I did not map which Village wards are in units 1-5 versus 6-16 (for example, near the high school or downtown). The Dane file reports only combined units.
- Waunakee CSD appears to have voters only in Dane County: all media totals equal the Dane totals. I did not verify this against DPI's district county list.

## 3. Democratic baseline and Yes-minus-Dem gap, and how it compares with MCPASD

### Takeaway
Waunakee's Dane-portion Democratic baseline is much lower than MCPASD's: Crowley at **66.5%** two-party (referendum-vote-weighted) vs. **77.3%** in MCPASD. Waunakee's Yes ran **13.9 points** (Q1) and **14.9 points** (Q2) behind Crowley. MCPASD's Yes ran **17.1 points** behind.

So relative to partisanship, Waunakee did slightly better than MCPASD. The 7.5-point difference in Yes share is more than explained by the 10.8-point difference in Democratic baseline.

The trend is the problem. Waunakee's operating-question gap widened from −5.6 (2022) to −13.9 (2026), an 8.3-point erosion. MCPASD's widened 3.4 points (−13.7 to −17.1).

### Cited Findings
- **District level, 2026** (Dem % = governor two-party, weighted by referendum votes; AG = Kaul two-party):

| Question | Yes % | Crowley 2p | Gap | Kaul AG 2p | Gap (AG) |
|---|---|---|---|---|---|
| Waunakee Q1 operating (recurring) | 52.6 | 66.5 | −13.9 | 67.2 | −14.6 |
| Waunakee Q2 bonds $97.5M | 51.7 | 66.5 | −14.9 | 67.2 | −15.5 |
| MCPASD operating (nonrecurring) | 60.1 | 77.3 | −17.1 | 77.5 | −17.4 |

  — computed from [Dane 2026 governor by precinct](https://elections.countyofdane.com/Precincts-Result/197/0004), [AG](https://elections.countyofdane.com/Precincts-Result/197/0005), [Waunakee 0041](https://elections.countyofdane.com/Precincts-Result/197/0041), [0042](https://elections.countyofdane.com/Precincts-Result/197/0042). MCPASD figures from `partisan_correlation.md`.

- **By municipality, 2026.** Whole-unit Crowley share; split units use whole-unit partisanship.

| Area | Ref votes Q1 | Q1 Yes % | Crowley 2p | Q1 gap | Q2 Yes % | Q2 gap |
|---|---|---|---|---|---|---|
| Village of Waunakee | 8,672 | 54.5 | 66.8 | −12.2 | 52.3 | −14.4 |
| Town of Westport (91% Waunakee) | 2,492 | 49.6 | 65.4 | −15.8 | 52.3 | −13.2 |
| Town of Vienna (60%) | 503 | 46.9 | 54.3 | −7.4 | 44.8 | −9.6 |
| City of Middleton Wds 14-18 (15%) | 410 | 65.1 | 82.2 | −17.1 | 67.6 | −14.6 |
| City of Madison Wd 35 (34%) | 391 | 42.7 | 80.7 | −38.0 | 46.6 | −34.1 |
| Town of Springfield (24%) | 358 | 36.9 | 56.7 | −19.8 | 33.0 | −23.7 |
| Town of Dane (15%) | 75 | 26.7 | 42.7 | −16.1 | 31.1 | −11.7 |
| **District** | **12,901** | **52.6** | **66.5** | **−13.9** | **51.7** | **−14.9** |

  — computed; see `waunakee_ward_results_2020_2026.csv`

- **The same reporting units carried both districts' questions in 2026.** Each unit's whole-unit partisan baseline is therefore the same for both districts, though the sub-unit populations differ:
  - Town of Westport: Waunakee Q1 49.6% (2,492 votes) vs. MCPASD 54.0% (224 votes)
  - City of Middleton Wds 14-18: Waunakee Q1 65.1% (410) vs. MCPASD 62.6% (2,262)
  - Town of Springfield: Waunakee Q1 36.9% (358) vs. MCPASD 43.0% (1,108)

  — computed from [Dane 0040](https://elections.countyofdane.com/Precincts-Result/197/0040) and [0041](https://elections.countyofdane.com/Precincts-Result/197/0041)
- **2026 statewide constitutional questions in Waunakee territory** (whole-unit Yes, where Yes is the Republican-sponsored side):
  - Village of Waunakee: partial-veto limit 41.1%, worship 36.5%, anti-discrimination 48.4%
  - Westport: 41.4%, 36.6%, 47.5%

  For comparison, MCPASD non-split units gave the partial-veto limit 32.5% Yes (`partisan_correlation.md`). — computed from [Dane races 0034–0036](https://elections.countyofdane.com/Election-Result/197) via the raw file

### Inferences
- **Decomposing the difference from MCPASD.** Yes difference −7.5 = Democratic baseline difference −10.8 + gap difference +3.2.
  - Waunakee is a less Democratic electorate. It is about 11 points less Democratic and about 9 points more supportive of the partial-veto amendment.
  - That alone would predict a much narrower margin than MCPASD's.
  - Given that electorate, Waunakee ran closer to its partisan ceiling than MCPASD did.
- **Madison Wd 35 is an outlier: 42.7% Yes in an 81% Crowley ward.** The Waunakee part is only 34% of the ward's ballots, so the Waunakee-side electorate is probably much less Democratic than the ward as a whole. Whole-unit partisanship is a poor proxy here. The ward fell from 65.9% Yes (2022) to 46.6% (2024) and 42.7% (2026). Ward geography may also have changed between 2022 and 2024: the unit had 2,341 ballots in 2022 and 1,340 in 2024.
- **Split-unit caveat.** As in MCPASD, gaps for split units (everything except the Village and, nearly, Westport) use whole-unit partisanship. The Village plus Westport carry 87% of Waunakee votes, so the district-level gap is more reliable than MCPASD's, where 24% of votes come from split units.

### Gaps
- There is no sub-ward partisan data for the Waunakee portions of Madison Wd 35, Middleton Wds 14-18, Springfield, Vienna or Dane.
- With only 2–3 non-split units, a meaningful within-district regression slope is not possible for Waunakee.

## 4. Turnout and roll-off on the Waunakee questions vs. the statewide questions

### Takeaway
Roll-off on Waunakee's questions was low: **4.0% (Q1) and 4.3% (Q2)** of the 13,439 ballots that carried them, against MCPASD's **7.2%**.
- In the fully-in-district Village, school-question roll-off (3.1–3.2%) was the same as the three statewide questions printed on the same ballots (3.0–3.6%).
- Westport was higher: 6.8–7.0% vs. about 3% on the statewide questions.

Where both districts' questions appeared in the same reporting unit, Waunakee's roll-off was lower than MCPASD's every time. District materials told voters to "Flip the Ballot."

Turnout on the operating question rose 4.1% over 2022 (12,394 to 12,901 valid votes), against MCPASD's 2.2%. But No votes rose 24% (4,923 to 6,114) while Yes fell 9% (7,471 to 6,787).

### Cited Findings
- **2026 roll-off by unit** (under + over ÷ ballots carrying the question; statewide questions ÷ whole-unit ballots):

| Unit | Waunakee Q1 | Waunakee Q2 | State Q1 partial veto | State Q2 worship | State Q3 anti-discrimination | Governor |
|---|---|---|---|---|---|---|
| V Waunakee Wds 1-5 | 3.2% | 3.3% | 3.4% | 2.7% | 3.2% | 0.6% |
| V Waunakee Wds 6-16 | 3.0% | 3.2% | 3.9% | 3.3% | 3.7% | 0.4% |
| **Village combined** | **3.1%** (277/8,949) | **3.2%** (290) | 3.6% | 3.0% | 3.4% | 0.5% |
| T Westport (91% in) | 6.8% (182/2,674) | 7.0% | 3.6% | 2.8% | 3.4% | 0.6% |
| T Vienna (part) | 1.8% | 2.7% | 4.0% | 3.2% | 4.1% | 0.6% |
| T Springfield (part) | 3.8% | 4.6% | 3.2% | 3.6% | 3.9% | 0.5% |
| C Madison Wd 35 (part) | 5.8% | 6.5% | 2.1% | 1.9% | 2.3% | 0.6% |
| C Middleton Wds 14-18 (part) | 6.6% | 8.0% | 3.0% | 3.0% | 3.4% | 0.4% |
| **District** | **4.0%** (538/13,439) | **4.3%** (573) | 3.5% (whole units) | 3.0% | 3.5% | 0.5% |

  — computed from the [Dane County raw results file](https://elections.countyofdane.com/Election-RawResults) (races 0002, 0004, 0034–0036, 0041, 0042); saved as `waunakee_rolloff_2026.csv`

- **Same units, other district's question, roll-off:**
  - Westport: Waunakee 6.8% vs. MCPASD 12.8%
  - City of Middleton Wds 14-18: Waunakee 6.6% vs. MCPASD 10.1%
  - Springfield: Waunakee 3.8% vs. MCPASD 5.0%

  MCPASD district-wide was 7.2%, and 8.9% in the City of Middleton. — MCPASD figures from `ward_results.md`; Waunakee computed as above
- **"Make Sure to Flip the Ballot!"** appears in the district's mailed newsletter and in its Oct. 16 Waunakee Tribune information piece. — [WCSD Newsletter](https://www.waunakee.k12.wi.us/fs/resource-manager/view/1da25b04-b199-4671-b104-b2d50023302b); [WCSD Tribune piece](https://www.waunakee.k12.wi.us/fs/resource-manager/view/43d6a3c8-59ec-45ae-91c3-c0fb65f303d5)
- **Turnout across cycles** (valid votes on the operating question; Village whole-unit ballots):
  - 2020: 13,568; Village ballots 9,462
  - 2022: 12,394; Village 8,507
  - 2024: 14,873; Village 10,356
  - 2026: 12,901; Village 8,949 (+5.2% vs. 2022)
  - 2026 ballots carrying the questions: 13,439

  — computed from Dane elections [124](https://elections.countyofdane.com/Election-Result/124), [145](https://elections.countyofdane.com/Election-Result/145), [172](https://elections.countyofdane.com/Election-Result/172), [197](https://elections.countyofdane.com/Election-Result/197)
- **2022 to 2026 operating-question vote change:**
  - District: Yes −684, No +1,191
  - Village: Yes −383 (5,112 to 4,729), No +750 (3,193 to 3,943)
  - Westport: Yes −114, No +293
  - MCPASD for comparison: Yes −333, No +849 (14,596/8,608 to 14,263/9,457)

  — computed

### Inferences
- **Roll-off did not drive Waunakee's narrow margin.** Village roll-off equaled the statewide questions. If anything, the Waunakee question was completed at least as fully as MCPASD's.
- **The "Flip the Ballot" reminder plausibly helped.** Layout is unverified, but in all three shared units the Waunakee question had lower roll-off than the MCPASD question printed on the same unit's other ballot style.
- **The narrowing came from new and converted No voters, not from Yes voters staying home.** Turnout rose, but the No column grew far faster in Waunakee (+24%) than in MCPASD (+10%).

### Gaps
- I did not verify ballot layout (column, or back of ballot) for either district.
- 2022 and 2024 under-votes are not published in the Dane feed (raw file is current election only), so roll-off trends cannot be computed.
- Registered-voter counts by unit were zero in the 2026 raw file, so turnout as a share of registered voters was not computed.

## 5. Waunakee's referendum history (2020–2026) and the support trend

### Takeaway
Waunakee has put an operating question on **every November ballot since 2020**, and all passed:
- 2020: 62.6%
- 2022: 60.3%
- 2024: 54.7%
- 2026: 52.6%

It added large capital questions in 2022 ($175M, 52.6%) and 2026 ($97.5M, 51.7%). There were no Waunakee school questions in spring 2023–2026 or in the August 2024/2026 primaries.

Measured against the Democratic baseline, operating support fell steadily: gap −1.3 (2020), −5.6 (2022), −8.9 (2024), −13.9 (2026). Capital questions sat at about −13 to −15 both times. Before 2020: a $44.8M facilities referendum passed in 2014, and two facilities referendums failed in 2010.

### Cited Findings
| Election | Question | Structure | Yes | No | Yes % | Dem baseline (2p) | Gap |
|---|---|---|---|---|---|---|---|
| Nov 2020 | Exceed revenue limit | nonrecurring (per Tribune) | 8,491 | 5,077 | 62.6 | Biden 63.9 | −1.3 |
| Nov 2022 | #1 Bonds $175M (new Heritage Elem., new Middle School) | debt | 6,520 | 5,866 | 52.6 | Evers 65.9 | −13.2 |
| Nov 2022 | #2 Exceed revenue limit | nonrecurring, 3 years | 7,471 | 4,923 | 60.3 | Evers 65.9 | −5.6 |
| Nov 2024 | Exceed revenue limit | mixed recurring + nonrecurring | 8,141 | 6,732 | 54.7 | Harris 63.6 | −8.9 |
| Nov 2026 | Q1 Exceed revenue limit | recurring, to $10.5M | 6,787 | 6,114 | 52.6 | Crowley 66.5 | −13.9 |
| Nov 2026 | Q2 Bonds $97.5M | debt | 6,647 | 6,219 | 51.7 | Crowley 66.5 | −14.9 |

  — Dane County: [2020 race 0045](https://elections.countyofdane.com/Precincts-Result/124/0045) and [president 0004](https://elections.countyofdane.com/Precincts-Result/124/0004); [2022 races 0050/0051](https://elections.countyofdane.com/Precincts-Result/145/0050); [2024 race 0051](https://elections.countyofdane.com/Precincts-Result/172/0051) and [president](https://elections.countyofdane.com/Precincts-Result/172/0004); [2026](https://elections.countyofdane.com/Election-Result/197). Gaps are computed. The 2020 and 2024 baselines are presidential, so they are not strictly comparable with the governor years.

- **No other Waunakee school questions.** Dane County's spring 2023, 2024, 2025 and 2026 ballots (elections 153, 164, 179, 190) list school questions for other districts only. The August 2024 and 2026 primaries (168, 194) list none. — [2023](https://elections.countyofdane.com/Election-Result/153); [2024](https://elections.countyofdane.com/Election-Result/164); [2025](https://elections.countyofdane.com/Election-Result/179); [2026 spring](https://elections.countyofdane.com/Election-Result/190)
- **Village of Waunakee operating Yes:** 64.5% (2020), 61.6% (2022), 56.6% (2024), 54.5% (2026). Gap: +0.3, −4.6, −6.9, −12.2.
- **Westport operating Yes:** 59.5%, 58.4%, 52.1%, 49.6%. Gap: −3.9, −7.2, −12.1, −15.8. — computed; see CSV
- **2022 operating question details.** It was "a three-year, non-recurring referendum ... by $1 million in the 2022-23 school year, by $3 million in the 2023-24 year and by $6 million in the 2024-25 year," to "attract and retain staff, operate additional facilities, and maintain current programs and services." — [Tribune, Aug. 2022](https://www.hngnews.com/waunakee_tribune/news/local/waunakee-school-referendum-questions-ready-for-the-nov-8-ballot/article_b4a6765e-22f0-11ed-86b4-f3e9e1707a3d.html)
  - Media called it "$10 million." — [Tribune, Nov. 2022](https://www.hngnews.com/waunakee_tribune/news/government/waunakee-school-referendums-pass-pool-fails/article_bc13e5e8-5fe5-11ed-a05e-43abeb6bd1d8.html); [Channel 3000, Nov. 2022](https://www.channel3000.com/news/education/voters-approve-pair-of-waunakee-school-referendum-questions/article_56055a08-a08d-526e-80bf-049f9c5f3098.html)
  - The 2024 Tribune instead described it as "$1 million the first year and then $3 million for the next two." This conflicts with the 2022 description. — [Tribune, Sept. 2024](https://www.hngnews.com/waunakee_tribune/news/school/waunakee-school-officials-face-referendum-related-questions/article_0ada0572-8005-11ef-87cf-53da258f0603.html)
- **2022 capital margin.** It passed "52.6 in favor and 47.4 against, a difference of 652 votes." "Some objected to plans to build a new Heritage Elementary School near the Intermediate School ... relocating the elementary school from the historic downtown." On the same ballot, a Village advisory question on an outdoor pool failed 60–40. — [Tribune, Nov. 2022](https://www.hngnews.com/waunakee_tribune/news/government/waunakee-school-referendums-pass-pool-fails/article_bc13e5e8-5fe5-11ed-a05e-43abeb6bd1d8.html)
- **2024 question.** Recurring: "$8.6 million for 2025-26 and an additional $500,000 for 2026-27 and thereafter," which converted two expiring nonrecurring referendums to permanent. Nonrecurring: "$1.050 million for 2025-26 and $2.1 million for 2026-27 strictly for employee compensation." The Tribune reported "8,139 to 6,732, or 54.7% to 45.3%." The Dane official canvass shows 8,141 Yes. — [Tribune, Nov. 2024](https://www.hngnews.com/waunakee_tribune/news/local/waunakee-approves-school-district-operational-referendum/article_51589df0-9c49-11ef-94bd-ab670e873d28.html); [Dane 2024](https://elections.countyofdane.com/Precincts-Result/172/0051)
  - Total authority was $9.65M (2025-26) and $11.2M (2026-27). — [Tribune, Sept. 2024](https://www.hngnews.com/waunakee_tribune/news/school/waunakee-school-officials-face-referendum-related-questions/article_0ada0572-8005-11ef-87cf-53da258f0603.html)
- **The cycle of temporary renewals was raised by voters.** At a 2024 information session, an attendee asked whether it was "possible to break a cycle of asking the public for more money to replace funding from temporary referendums." Summers blamed the state's $0 revenue-limit increases in 2021-22 and 2022-23 and the loss of ESSER funds. — [Tribune, Sept. 2024](https://www.hngnews.com/waunakee_tribune/news/school/waunakee-school-officials-face-referendum-related-questions/article_0ada0572-8005-11ef-87cf-53da258f0603.html)
  - "Waunakee voters have been faced with three operational referendums this decade (2020, 2022 and 2024)." — [Tribune, summer 2026](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-picks-97-5-million-referendum-option-for-high-school-improvements/article_90cac93d-23e2-4c4b-aa11-491f4174f1a9.html)
  - The board wanted "a pattern for operational referendums that would reduce the number of them." — [Tribune, 2025](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-considers-strategies-for-tax-levy-reduction/article_37cc13aa-1b19-4eee-827c-507b74803ed5.html)
- **Earlier facilities history.** "Voters greenlit a $44.8 million referendum in 2014 to add to Prairie Elementary, renovate Heritage Elementary and build Waunakee Intermediate School." — [Channel 3000, Aug. 2026](https://www.channel3000.com/news/waunakee-school-district-adds-2-referendums-to-november-ballot/article_5f6f981a-e92a-4707-9e98-ee964c7c3972.html). The plan followed "two failed facilities referendums in 2010." — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)

### Inferences
- **Support for successive operating asks has eroded steadily**: about −10 points of Yes and about −12.6 points of partisan gap over four cycles. MCPASD's one renewal cycle cost −2.8 Yes and −3.4 gap.
- **Waunakee's 2026 operating result (52.6%) equals its 2022 capital result (52.6%).** Operating questions, once its "easy" asks, now poll like its building asks.
- **The 2026 recurring structure answered the "break the cycle" complaint.** But it is also the most expensive permanent operating ask Waunakee has made, and it passed by the smallest operating margin.

### Gaps
- The amount and wording of the Nov. 2020 question were not retrieved. Only its result and its nonrecurring status (per the Tribune) are known.
- I did not retrieve the 2010 and 2014 vote totals.

## 6. Campaign context: committees, opposition, coverage and district messaging

### Takeaway
I found **no organized Yes committee for Waunakee 2026** in the Cap Times, Tribune, Channel 3000 or WMTV coverage, or on district pages. By contrast, MCPASD had a parent-led "Yes" group (co-chair Kris Tawil).

I found **no organized 2026 No committee** in news coverage. In 2022, a "coalition of residents" mailed Vote No fliers calling the $175M plan "excessive." The Nextdoor post urging No on the high school could not be retrieved or verified.

The district ran an information-only campaign ("Investing in People / Investing in Places") built on:
- the long-range plan and low spending per pupil
- state underfunding
- levy-reduction credentials
- board discretion to levy less

It also explicitly declined to name cuts: "no budget reduction list," and a failed question would likely be retried in April 2027. MCPASD, by contrast, warned of "catastrophic" 20% cuts and a possible school closure.

### Cited Findings
- **District messaging, by theme:**
  - *Low spending:* "Among peer districts in Dane County, WCSD has the second-lowest spending amount per student." It cited $16,106 vs. a "regional average of $16,839." — [WCSD Fact Sheet](https://www.waunakee.k12.wi.us/fs/resource-manager/view/54156bdc-8bac-43e4-8464-c6c34af2a164); [Newsletter](https://www.waunakee.k12.wi.us/fs/resource-manager/view/1da25b04-b199-4671-b104-b2d50023302b)
  - *State underfunding:* state funding has "created an estimated shortfall of $3,379 per student ... an estimated total funding shortfall of $14,853,650." — [Newsletter](https://www.waunakee.k12.wi.us/fs/resource-manager/view/1da25b04-b199-4671-b104-b2d50023302b)
  - *Levy credentials:* the board "approved refinancing existing debt, which lowered the district's tax levy by approximately $2.39 million" (fall 2025). — [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq). Also: the "2025-26 tax levy included a $2.3 million reduction under what was allowed." — [WCSD Presentation](https://www.waunakee.k12.wi.us/fs/resource-manager/view/ed84ad2b-2a12-45b9-a894-107102763cc2)
  - *No cuts named:* "At this time, the Board of Education and Administrative team has not created a budget reduction list. If the operational referendum is not approved, the School Board will seek feedback ... and likely consider another operational referendum for April 2027." — [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq). The Cap Times: Waunakee officials said "cuts could be needed but haven't specified what could be cut." — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
  - *Recurring vs. temporary:* the FAQ explains the recurring choice: nonrecurring referendums require "frequent return of operational referendum support and disruptions to budget planning." — [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq)
  - *Specific capital needs:* about 22 students a year shut out of culinary courses; more than 50 CNA students who must "travel off site ... at a cost of $800 per student"; a high school with portions "more than 55 years old." — [WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq); [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **Outreach:**
  - Seven community drop-ins (coffee shops, library, Village Center, district office)
  - Two days of high school tours with information sessions (Sept. 29, Oct. 13)
  - Two virtual sessions (Oct. 6)
  - A mailed postcard and newsletter to all households, a Spanish version, Instagram reels and a student podcast

  — [WCSD referendum page](https://www.waunakee.k12.wi.us/community/2026referendum); [WCSD Presentation](https://www.waunakee.k12.wi.us/fs/resource-manager/view/ed84ad2b-2a12-45b9-a894-107102763cc2)
  - The district lists a "Waunakee Tribune Article" from Oct. 16. The linked PDF is a district-branded information piece ("LEARN MORE. GET THE FACTS."), apparently paid placement rather than news. — [WCSD Tribune piece](https://www.waunakee.k12.wi.us/fs/resource-manager/view/43d6a3c8-59ec-45ae-91c3-c0fb65f303d5)
- **Advocacy limits.** In 2022 the superintendent said "he and Summers cannot be advocates, but can provide information." — [Tribune, Aug. 2022](https://www.hngnews.com/waunakee_tribune/news/local/waunakee-school-referendum-questions-ready-for-the-nov-8-ballot/article_b4a6765e-22f0-11ed-86b4-f3e9e1707a3d.html)
- **Board and officials' framing in the press:**
  - Board VP Sonne: "The tax funding formula for public schools is just broken." Also: "Do we want to continue to invest in older, outdated learning environments ... or do we want to continue on that long-range plan?"
  - Summers: the operating money "would solely pay for keeping staff salaries at current levels, which are based on the average salaries of similar-size school districts in Dane County."

  — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **MCPASD contrast in the same story.** Hesselbein: "Twenty percent (cuts) would be catastrophic." Failure "could lead to the closure of an elementary school." Kris Tawil "co-chairs a 'Yes' group supporting the referendum." — [Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **Spring 2026 survey (School Perceptions):**
  - Capital ($105M plan): weighted support 51.1% "definitely/probably yes." Non-staff/non-parents were 43% for and 45% against. School Perceptions' president: "you're within the margin of error."
  - Operating (then framed as extending $2.1M "for four more years"): weighted support 61.5%. Non-staff/non-parents were 54% yes, 34% no.
  - Response: 1,809 respondents, a 19% response rate.

  — [Tribune, May 2026](https://www.hngnews.com/tribune_enterprise/news/local/waunakee-school-district-survey-results-show-support-for-operational-capital-building-referendums/article_a023290f-ea63-426c-9fea-d71f6ffaab56.html). The district page gives 1,822 responses. — [WCSD referendum page](https://www.waunakee.k12.wi.us/community/2026referendum) (small conflict)
- **The operating question changed after the survey.** The board adopted an "alternative approach": "continuing the $2.1 million that's expiring with an additional $2.1 million in new funding annually," as "a recurring referendum." — [Tribune, summer 2026](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-picks-97-5-million-referendum-option-for-high-school-improvements/article_90cac93d-23e2-4c4b-aa11-491f4174f1a9.html)
- **2022 opposition was organized.** "As households in Waunakee receive information from a coalition of residents opposing the school district's referendums ... The flier sent to residents calls the $175 million capital referendum 'excessive.'" — [Tribune, Oct. 2022](https://www.hngnews.com/waunakee_tribune/news/government/school-district-responds-to-vote-no-information/article_595a0172-4e5f-11ed-9cd7-2f213b9f8a0f.html). Also: "Some Waunakee residents opposed to massive $175 million school referendum" (headline and description only). — [WKOW, Nov. 2022](https://www.wkow.com/townnews/school/some-waunakee-residents-opposed-to-massive-175-million-school-referendum/article_3605922c-5efe-11ed-ae5f-374a61ca66b5.html)
- **2022 tax message.** The district stressed "tax-rate consistency" and said the mill rate would hold steady even with a $150M-plus referendum. — [Tribune, Feb. 2022](https://www.hngnews.com/waunakee_tribune/news/local/waunakee-school-districts-financial-strategies-keep-tax-rate-consistent-even-with-a-150-million-referendum/article_365eaad2-94c0-11ec-a781-d749ff61e35f.html). DPI shows the rate fell from 10.89 (2021-22) to 9.69 (2022-23). The Tribune had reported the plan to drop it to $9.68. — [Tribune, Oct. 2022](https://www.hngnews.com/waunakee_tribune/news/government/school-district-responds-to-vote-no-information/article_595a0172-4e5f-11ed-9cd7-2f213b9f8a0f.html); [DPI](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2023)
- **Statewide context (secondhand, from other notes).** Only 3 of 8 recurring operating questions passed in Nov. 2026, Waunakee among them. — [Civic Media, Nov. 4, 2026](https://civicmedia.us/news/2026/11/04/majority-of-school-referendums-pass-in-2026-general-election) (cited in `tax_messaging.md`; not re-fetched here)

### Inferences
- **Waunakee's low-stakes framing probably cost urgency.** "No cut list; we'd come back in April" gave persuadable voters a free option to vote No. MCPASD's cut warning had no counterpart. Waunakee's operating result fell about 9 points short of its weighted survey; its capital result matched its survey (51.7% vs. 51.1%).
- **The operating survey was for a smaller, temporary ask.** The 61.5% measured support for renewing $2.1M for four years. Voters were shown a permanent increase up to $10.5M. That change is a plausible cause of the shortfall.
- **No organized Yes group was visible, unlike MCPASD.** That may matter more in a district whose Democratic baseline gives only a few points of cushion.

### Gaps
- **Nextdoor post:** not retrieved (login-gated; not attempted, per the no-bypass rule). Its author, content and reach are unknown.
- I found no news coverage of a 2026 organized No campaign, ads or mailers. Waunakee Tribune letters for Oct. 2026 were not found in search.
- No campaign-finance filings (school referendum committees register locally) were checked.
- **Unreachable host:** the Citizen Portal mirror (cpo.soar.com) returned CONNECT 502. Its board-meeting summaries (survey debate over a "4K note and facility framing"; levy-cut options) were not read.

## 7. Property values, levy and mill rate, 2021-22 to 2025-26 (and 2026-27), vs. MCPASD

### Takeaway
Waunakee's levy grew almost exactly as fast as MCPASD's (+26.9% vs. +27.1%, 2021-22 to 2025-26). But its TIF-out equalized value grew faster (+60.6% vs. +46.6%), so its mill rate fell further: **10.89 to 8.60 (−21%)** vs. MCPASD's 9.95 to 8.62 (−13%). By 2025-26 the two districts' rates were essentially equal (8.60 vs. 8.62).

Waunakee's 2026-27 draft levy is about $51M at about $8.80 (+6.5% levy). The district estimated about +$200 on a $500K home before any referendum effect.

### Cited Findings
- **DPI equalized levy rates (TIF-out), Waunakee Community (6181):**

| School year | Levy | Equalized value | Mill rate | Levy Δ | Value Δ |
|---|---|---|---|---|---|
| 2020-21 | $34,648,262 | $3,181,517,136 | 10.89 | | |
| 2021-22 | $37,434,390 | $3,437,359,073 | 10.89 | +8.0% | +8.0% |
| 2022-23 | $38,555,555 | $3,980,468,177 | 9.69 | +3.0% | +15.8% |
| 2023-24 | $41,692,918 | $4,649,771,435 | 8.97 | +8.1% | +16.8% |
| 2024-25 | $44,823,271 | $5,036,421,267 | 8.90 | +7.5% | +8.3% |
| 2025-26 | $47,501,003 | $5,520,979,855 | 8.60 | +6.0% | +9.6% |

  — [DPI FY2021](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2021), [FY2022](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2022), [FY2023](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2023), [FY2024](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2024), [FY2025](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2025), [FY2026](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2026)

- **MCPASD (3549), same source, matches `tax_messaging.md`:** levy $79,590,285 to $101,150,743; value $8.00B to $11.73B; rate 9.95 to 8.62 (2021-22 to 2025-26).
- **Year by year, Waunakee vs. MCPASD.** Waunakee's levy rose every year (+3.0% to +8.1%). MCPASD's levy was nearly flat through 2023-24, then jumped +8.4% and +11.0%. Waunakee's rate fell every year. MCPASD's rose in 2025-26 (8.32 to 8.62). — DPI as above
- **Neighbors for context, 2025-26 rates:** DeForest 9.00; Sun Prairie 10.21. — DPI FY2026; saved in `waunakee_mcpasd_dpi_mill_rates.csv`
- **2026-27 draft (July 2026 annual meeting):**
  - A "$51 million 2026-27 tax levy" with "the current tax rate we have in there is $8.80" vs. $8.60 for 2025-26
  - "The average estimated tax increase for a $500,000 home ... is $200, if the final tax levy for 2026-27 stays at $8.80"
  - Equalized value projected at "$5.852 billion" (+6%), but DOR's Aug. 15 estimate was "+10.22%," with "at least 2.9%" from new construction
  - State aid down $491,805; "local taxes figure to go up by 9%, or $3,385,734"
  - The photo caption calls the 2026-27 levy "6.49% higher than last year's"
  - The final levy was due Oct. 26.

  — [Tribune, July 2026](https://www.hngnews.com/tribune_enterprise/news/51-million-26-27-tax-levy-approved-at-waunakee-school-districts-annual-meeting/article_791dd8e9-ed47-4637-9b8d-97de24353522.html)
- **The 2025 levy-cut history.** Without action, the state budget's $0 equalization-aid increase would have meant a 10.47% levy rise for 2025-26. Debt restructuring and project savings "could save in the range of $2 million." — [Tribune, 2025](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-considers-strategies-for-tax-levy-reduction/article_37cc13aa-1b19-4eee-827c-507b74803ed5.html). The final DPI 2025-26 levy was +6.0%.
- **DPI's FY2026-27 page had no district rows** when fetched Nov. 5, 2026. — [DPI FY2027](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2027)

### Inferences
- **Both districts' "rate is falling" stories rest on value growth.** Waunakee's 61% value growth includes rapid new construction. Its rate fell 2.3 mills while the levy rose 27%.
- **Illustrative bill.** My arithmetic, assuming a home tracked district-wide value growth (an overstatement for existing homes, since growth includes new construction): a $400K home in 2021-22 paid about $4,356 gross school tax. At about $642K in 2025-26 it paid about $5,525 (+27%). MCPASD's equivalent was about +27% (`tax_messaging.md`).
- **On rates alone, the districts were tied entering 2026.** So differences in referendum support are unlikely to come from different current tax burdens per dollar of value.
- **Waunakee's planned 2026-27 rate rise (to about 8.80) came just before the vote,** on top of the referendum asks. MCPASD's 2025-26 rate also rose.

### Gaps
- The final Waunakee and MCPASD 2026-27 levies and mill rates were not found. The boards certified in late October 2026; DPI has not posted them.
- I did not separately fetch DOR's municipal and school-district equalized value reports. DPI's TIF-out values are DOR-derived, and the 10.22% figure is DOR's as reported by the Tribune.

## 8. What explains Waunakee's narrower margin vs. MCPASD, and lessons for MCPASD

### Takeaway
Most of the 7.5-point difference (52.6% vs. 60.1%) is **electorate**. Waunakee's district is about 11 points less Democratic, and it actually ran about 3 points closer to its partisan baseline than MCPASD did.

The **trend** is what MCPASD should watch. Waunakee's repeated operating asks lost support every cycle (62.6, 60.3, 54.7, 52.6; gap −1.3 to −13.9). The No vote surged by about a quarter in 2022–2026. And its 2026 package combined:
- a permanent, larger-than-surveyed operating increase
- a $97.5M building ask four years after a $175M one
- low-urgency messaging, with no cut list and a promise of an April retry

### Cited Findings
- Yes difference −7.5 = Democratic baseline difference (66.5 vs. 77.3, −10.8) + gap difference (−13.9 vs. −17.1, +3.2) — computed (Q3)
- Waunakee operating gap: −5.6 (2022) to −13.9 (2026), an 8.3-point change. MCPASD: −13.7 to −17.1, a 3.4-point change. — computed (Q3, Q5)
- No votes 2022 to 2026: Waunakee +24% (4,923 to 6,114); MCPASD +10% (8,608 to 9,457). — computed (Q4)
- The operating question was surveyed at 61.5% weighted support as a four-year $2.1M renewal. It was put on the ballot as a recurring increase to $10.5M and got 52.6%. The capital question, surveyed at 51.1%, got 51.7%. — [Tribune survey story](https://www.hngnews.com/tribune_enterprise/news/local/waunakee-school-district-survey-results-show-support-for-operational-capital-building-referendums/article_a023290f-ea63-426c-9fea-d71f6ffaab56.html); [Tribune board option story](https://www.hngnews.com/tribune_enterprise/news/waunakee-school-board-picks-97-5-million-referendum-option-for-high-school-improvements/article_90cac93d-23e2-4c4b-aa11-491f4174f1a9.html); Dane County results
- Waunakee lost the operating question in Westport (49.6%) and all rural towns. It won it in the Village (54.5%) and the City of Middleton portion (65.1%). — computed (Q2)
- Messaging contrast: Waunakee said there was no cut list and it would likely retry in April 2027 ([WCSD FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq)). MCPASD warned of "catastrophic" 20% cuts and a possible school closure, with a parent Yes group ([Cap Times, Oct. 20, 2026](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)).

### Inferences
**What explains Waunakee's narrower margin:**
1. **Partisan baseline.** This explains more than the whole gap. Waunakee's electorate is about 66.5% Crowley vs. about 77% in MCPASD, and more conservative on the 2026 constitutional questions.
2. **Ask fatigue and stacking.** This is the fourth operating question in four Novembers since 2020, plus the second big capital question in four years. The steady widening of the operating gap fits cumulative fatigue. Voters raised the "cycle" complaint publicly in 2024.
3. **Permanence and size.** The recurring $10.5M structure differs from what was surveyed. Statewide, recurring questions fared poorly in Nov. 2026 (secondhand). The district's $17 per $100K claim looks low against the ballot amounts (Q1 inferences), which could have fed skeptics.
4. **Low stakes.** With no cuts named and a promise of an April 2027 retry, a No vote cost persuadable voters little.
5. **What did *not* explain it: roll-off.** The Village's school-question roll-off equaled the statewide questions'.

**Lessons for MCPASD** (all inferences):
- **MCPASD's cushion comes mostly from partisanship, and it is underused.** At −17.1, MCPASD's Yes-minus-Dem gap is the largest of the 2026 Dane questions. MCPASD is leaving more partisan support on the table than Waunakee is. Closing even a few points in the City of Middleton and the Madison wards (Q2 of `partisan_correlation.md`) is the cheapest margin available.
- **Serial renewals erode support.** Waunakee lost about 10 Yes points over four consecutive operating asks. MCPASD's 2030 renewal would be its third straight four-year nonrecurring ask. Two paths are worth weighing for that cycle: a recurring conversion, which Waunakee passed narrowly, or a smaller renewal. Expect a lower baseline than 60% either way.
- **Keep the ballot question close to what was surveyed.** Waunakee's operating question underperformed its survey by about 9 points after its structure changed. MCPASD's weighted survey (about 47%, secondhand) instead underestimated its 60.1% result. Survey weighting is firm-specific, so the useful signal is the change in a district's own numbers over time.
- **Publish comparable tax numbers.** Give per-$100K and per-median-home figures, annual and cumulative, year by year. Otherwise the press will mismatch them, as the Cap Times did with $120 cumulative per $100K vs. $210 per year per home. Both districts' numbers were hard to compare.
- **Fix roll-off with "flip the ballot" reminders.** In the units both districts shared, Waunakee's question had lower roll-off than MCPASD's on every ballot style. MCPASD's 7.2% (8.9% in the City of Middleton) was roughly 1,800 lost votes. A Waunakee-style "Flip the Ballot!" reminder in mailers and the Yes campaign is low-cost.
- **Concrete stakes still matter.** The district with clear consequences and an organized Yes group (MCPASD) ran stronger in absolute terms. It also had the more Democratic electorate, so the two effects cannot be separated with this data.

### Gaps
- Causal attribution among fatigue, structure, stakes framing and the Nextdoor or other opposition activity cannot be isolated with ward-level data from one election.
- Ecological partisan estimates for the split units are weak (Q3).
- All 2026 figures are unofficial until the Nov. 17 canvass.
