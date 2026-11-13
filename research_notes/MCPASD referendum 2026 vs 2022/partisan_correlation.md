# MCPASD operating referendum support vs. partisan voting, Nov. 8, 2022 vs. Nov. 3, 2026

Status: 2022 figures are the Dane County **official canvass**. 2026 figures are **unofficial** election-night results from the Dane County Clerk (282 of 282 precincts reporting; the Clerk marks them "Unofficial Results"). School results get canvassed by districts later in November 2026. All MCPASD ward-level numbers below come from the same Dane County results files that hold the partisan contests, so the correlation is self-contained.

Data files saved alongside these notes (same folder):
- `partisan_by_ward_2022.csv`, `partisan_by_ward_2026.csv`: one row per reporting unit that carried the MCPASD question. Columns: Yes/No, ballots cast in the unit, governor/AG/treasurer two-party Democratic %, 2022 U.S. Senate, 2022 Dane abortion advisory, 2026 state constitutional questions, Yes minus Dem gap, and a `split_unit` flag.
- `partisan_by_area_2022_vs_2026.csv`: municipality-level aggregates and changes.
- Cross-check: the other researcher's `ward_results_2022.csv` / `ward_results_2026.csv` in this folder have the same district totals (2022: 14,596 Yes / 8,608 No; 2026: 14,263 / 9,457).

## 1. By ward/municipality, how does Yes % track governor (and other top-of-ticket) Democratic share each year, and did the slope steepen or flatten?

### Takeaway
Referendum Yes tracks Democratic vote share strongly in both years: weighted r ≈ 0.88 in 2022 and ≈ 0.79 in 2026 across 24 reporting units. In 2026 the relationship got **weaker and flatter**, not more polarized: the slope fell from 0.81 to 0.69 Yes points per Dem point (0.68 to 0.51 in units fully inside the district). Partisanship explained less of the variation in 2026 because Yes fell even in heavily Democratic areas. With only 10–24 units, the slope change is directional, not statistically conclusive.

### Cited Findings

#### Data and method
- **Source.** Dane County Clerk results by reporting unit, read from the county's precinct-results API, which feeds the "Votes by Precinct" pages. 2026 General = election 197: MCPASD question = race 0040, Governor = 0004, AG = 0005, Treasurer = 0007, ballots cast = 0002, state questions = 0034–0036. 2022 General = election 145: MCPASD = 0042, Governor = 0004, AG = 0005, Treasurer = 0007, U.S. Senate = 0008, ballots = 0002, Dane abortion advisory = 0035. — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197); [2026 MCPASD by precinct](https://elections.countyofdane.com/Precincts-Result/197/0040); [Dane County 2022 results](https://elections.countyofdane.com/Election-Result/145); [2022 MCPASD by precinct](https://elections.countyofdane.com/Precincts-Result/145/0042); API pattern `https://api.danecounty.gov/api/v1/elections/precinctresults/{election}/{race}`
- **Units that carried the question.** The Dane file lists these as carrying the MCPASD question: Towns of Berry, Cross Plains, Middleton, Springfield and Westport; Village of Cross Plains; City of Middleton; and City of Madison wards 95, 100, 101, 102, 109, 113 (0 votes), 114, 115, 117, 118, 119, 137 (0), 139, 140 and 141 in 2022. In 2026 the Madison wards are 95, 100, 101, 102, 109, 114, 115, 117, 118, 119, 120, 134, 135 and 137 (0). Madison ward numbers above 119 were renumbered between the elections. There are 28 units in 2022 and 29 in 2026. — [Dane County 2022](https://elections.countyofdane.com/Precincts-Result/145/0042); [2026](https://elections.countyofdane.com/Precincts-Result/197/0040)
- **District totals.** 2022 official canvass: Yes 14,596, No 8,608 (62.9%). 2026 unofficial: Yes 14,263, No 9,457 (60.1%). — [Dane 2022](https://elections.countyofdane.com/Election-Result/145); [Dane 2026](https://elections.countyofdane.com/Election-Result/197)
- **Critical limitation: split reporting units.** Many reporting units straddle MCPASD's boundary. The governor count covers the whole unit, but the referendum count covers only the MCPASD part. Shares of unit ballots that carried the MCPASD question:
  - Town of Berry: ~48–49%
  - Town of Cross Plains: ~42–43%
  - Town of Springfield: ~71–72%
  - Town of Westport: ~8%
  - Several Madison wards: 2–37%
  - City of Middleton Wds 14–18: 2,515 of 2,954 ballots in 2026 (per the other researcher's ballot-style count)

  For these units the partisan share is for the whole unit, not the MCPASD voters. I flag a unit "split" when its referendum votes are under 85% of its ballots cast. Non-split units carry 73% (2022) and 76% (2026) of all MCPASD referendum votes. — derived from [Dane County files](https://elections.countyofdane.com/Election-Result/197)
- **Candidates verified.**
  - 2026 governor: Democrat David Crowley / Sarah Godlewski vs. Republican Tom Tiffany / David Varnam. Dane County: Crowley 80.3% (250,376), Tiffany 19.5% (60,840), unofficial. — [Dane County 2026](https://elections.countyofdane.com/Election-Result/197)
  - 2022 governor: Tony Evers 78.6% (236,577) vs. Tim Michels 20.7% (62,300) in Dane. — [Dane County 2022](https://elections.countyofdane.com/Election-Result/145)
  - 2026 AG is a Kaul vs. Toney **rematch** of 2022, which makes it the cleanest apples-to-apples partisan measure across years. — [Dane County 2026](https://elections.countyofdane.com/Election-Result/197); [Dane County 2022](https://elections.countyofdane.com/Election-Result/145)
- **Statewide context.**
  - Crowley won statewide by "just over eight percentage points," as part of "a national Democratic wave." Wisconsin Democrats won both legislative chambers. — [Wikipedia, 2026 Wisconsin gubernatorial election](https://en.wikipedia.org/wiki/2026_Wisconsin_gubernatorial_election) (secondary; unofficial results)
  - Democrats were "projected by news outlets to win a majority" of the U.S. House (as of Nov. 4, 2026; 88.3% of districts called). — [Wikipedia, 2026 U.S. House elections](https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections)
  - Wisconsin Watch headlines: "Democrats flip two Wisconsin battleground congressional districts" and "Democrats take control of Wisconsin government." — [Wisconsin Watch](https://wisconsinwatch.org/2026/04/wisconsin-voters-school-district-referendum-funding-support-property-tax-election-2026/) (related-stories links)
  - 2022 statewide: Evers 1,358,774 (51.15%) vs. Michels 1,268,535. — [Wikipedia, 2022 WI gubernatorial](https://en.wikipedia.org/wiki/2022_Wisconsin_gubernatorial_election), citing WEC

#### Unit-level table, 2026 (unofficial; units with ≥20 referendum votes)
| Reporting unit | Ref votes | Yes % | Crowley 2-party % | Yes − Dem | Split? |
|---|---|---|---|---|---|
| T Berry Wds 1-2 | 349 | 28.9 | 57.6 | −28.7 | yes |
| T Cross Plains Wds 1-2 | 397 | 46.6 | 59.6 | −13.0 | yes |
| T Springfield Wds 1-4 | 1,108 | 43.0 | 56.7 | −13.7 | yes |
| T Westport Wds 1-5 | 224 | 54.0 | 65.4 | −11.4 | yes |
| T Middleton Wds 1, 3-4 | 1,486 | 55.8 | 71.0 | −15.2 | no |
| T Middleton Wd 2, 4A | 391 | 56.8 | 73.1 | −16.3 | no |
| T Middleton Wds 5-8 | 2,134 | 59.5 | 66.6 | −7.1 | no |
| V Cross Plains Wds 1-6 | 2,266 | 51.8 | 70.9 | −19.1 | no |
| V Cross Plains Wd 7 | 107 | 63.6 | 66.7 | −3.1 | no |
| C Middleton Wds 1-4 | 3,107 | 67.7 | 83.7 | −16.0 | no |
| C Middleton Wds 5-8, 21 | 2,596 | 62.5 | 86.7 | −24.2 | no |
| C Middleton Wds 9-13,19,22,24 | 3,180 | 64.7 | 84.5 | −19.8 | no |
| C Middleton Wds 14-18 | 2,262 | 62.6 | 82.2 | −19.6 | yes |
| C Madison Wd 095 | 27 | 55.6 | 90.9 | −35.3 | yes |
| C Madison Wd 100 | 71 | 63.4 | 87.4 | −24.0 | yes |
| C Madison Wd 101 | 325 | 56.6 | 86.4 | −29.8 | yes |
| C Madison Wd 102 | 214 | 53.7 | 85.2 | −31.5 | yes |
| C Madison Wd 109 | 280 | 57.9 | 79.0 | −21.1 | yes |
| C Madison Wd 114 | 317 | 70.3 | 83.6 | −13.3 | yes |
| C Madison Wd 115 | 35 | 74.3 | 90.0 | −15.7 | yes |
| C Madison Wd 117 | 139 | 74.8 | 81.9 | −7.1 | yes |
| C Madison Wd 118 | 1,218 | 68.1 | 78.4 | −10.3 | no |
| C Madison Wd 119 | 1,447 | 61.4 | 76.6 | −15.2 | no |
| C Madison Wd 135 | 24 | 66.7 | 90.3 | −23.6 | yes |

— computed from [Dane County 2026 MCPASD](https://elections.countyofdane.com/Precincts-Result/197/0040) and [2026 Governor by precinct](https://elections.countyofdane.com/Precincts-Result/197/0004)

#### Unit-level table, 2022 (official canvass; units with ≥20 referendum votes)
| Reporting unit | Ref votes | Yes % | Evers 2-party % | Yes − Dem | Split? |
|---|---|---|---|---|---|
| T Berry Wds 1-2 | 366 | 34.4 | 59.6 | −25.2 | yes |
| T Cross Plains Wds 1-2 | 431 | 50.6 | 59.3 | −8.7 | yes |
| T Springfield Wds 1-4 | 1,187 | 45.8 | 56.5 | −10.7 | yes |
| T Westport Wds 1-5 | 241 | 53.1 | 65.6 | −12.5 | yes |
| T Middleton Wds 1-8 | 3,686 | 57.9 | 68.3 | −10.4 | no |
| V Cross Plains Wds 1-6 | 2,106 | 55.9 | 71.1 | −15.2 | no |
| C Middleton Wds 1-4 | 3,120 | 69.0 | 82.7 | −13.7 | no |
| C Middleton Wds 5-8 | 2,435 | 66.7 | 85.8 | −19.1 | no |
| C Middleton Wds 9-13, 19 | 2,914 | 66.4 | 83.8 | −17.4 | no |
| C Middleton Wds 14-18 | 2,472 | 64.4 | 80.0 | −15.6 | yes |
| C Middleton Wd 21 | 128 | 75.0 | 86.9 | −11.9 | no |
| C Middleton Wd 22 | 95 | 81.1 | 85.4 | −4.3 | no |
| C Madison Wd 095 | 40 | 70.0 | 86.9 | −16.9 | yes |
| C Madison Wd 100 | 55 | 80.0 | 90.5 | −10.5 | yes |
| C Madison Wd 101 | 309 | 63.8 | 84.7 | −20.9 | yes |
| C Madison Wd 102 | 211 | 69.7 | 83.8 | −14.1 | yes |
| C Madison Wd 109 | 326 | 69.6 | 75.1 | −5.5 | yes |
| C Madison Wd 114 | 387 | 73.4 | 81.9 | −8.5 | yes |
| C Madison Wd 115 | 40 | 82.5 | 88.5 | −6.0 | yes |
| C Madison Wd 117 | 143 | 78.3 | 80.7 | −2.4 | yes |
| C Madison Wd 118 | 743 | 71.7 | 78.9 | −7.2 | no |
| C Madison Wd 119 | 1,503 | 66.1 | 76.3 | −10.2 | no |
| C Madison Wd 139 | 62 | 87.1 | 90.9 | −3.8 | no |
| C Madison Wd 140 | 203 | 67.0 | 72.4 | −5.4 | no |

— computed from [Dane County 2022 MCPASD](https://elections.countyofdane.com/Precincts-Result/145/0042) and [2022 Governor by precinct](https://elections.countyofdane.com/Precincts-Result/145/0004)

#### Correlations and regressions (Yes % on Dem two-party %, weighted by referendum votes)
| Sample | Partisan measure | 2022 r / slope | 2026 r / slope |
|---|---|---|---|
| All units, ref ≥ 20 (n=24 both years) | Governor | 0.879 / 0.81 | 0.793 / 0.69 |
| All units | Attorney General (Kaul–Toney both years) | 0.875 / 0.80 | 0.796 / 0.72 |
| All units | Treasurer | 0.863 / 0.74 | 0.771 / 0.64 |
| All units | 2022 U.S. Senate (Barnes) | 0.882 / 0.77 | n/a |
| Non-split units only (n=11 / 10) | Governor | 0.842 / 0.68 | 0.705 / 0.51 |
| Non-split units only | Attorney General | 0.825 / 0.65 | 0.705 / 0.53 |
| Unweighted, all units | Governor | 0.884 / 1.08 | 0.699 / 0.67 |
| Unweighted, non-split | Governor | 0.819 / 1.02 | 0.551 / 0.39 |

- Intercepts (weighted, governor): 2022 all units 0.9, 2026 7.0; non-split 2022 11.5, 2026 21.6. — computed from Dane County files
- **Bootstrap (4,000 resamples of units), all units:** slope 0.81 [90% interval 0.66–1.03] in 2022 vs. 0.69 [0.44–0.92] in 2026. Change −0.12, 90% interval −0.46 to +0.16. 77% of resamples show a flatter 2026 slope.
- **Bootstrap, non-split units:** change −0.16, 90% interval −0.63 to +0.51; 70% of resamples flatter. — computed
- **Ideological ballot questions.**
  - 2022 Dane advisory "repeal abortion ban" Yes % correlates with school Yes at r = 0.87 (all units) and 0.90 (non-split).
  - 2026: the share voting No on the three Republican-sponsored constitutional amendments correlates at r = 0.70 (partial-veto limit), 0.80 (worship gatherings) and 0.63 (anti-discrimination/DEI). All are weaker than or similar to the governor race. — computed; amendment descriptions from [Wikipedia, 2026 Wisconsin elections](https://en.wikipedia.org/wiki/2026_Wisconsin_elections)
- **Partial-veto amendment.** It limits the governor's partial veto from creating or raising taxes, "largely in response to Governor Tony Evers' partial veto in the 2023 state budget, which authorized ... education funding through referendums for '400 years'." In MCPASD non-split units it got 32.5% Yes. Wikipedia reports it was ratified statewide. — [Wikipedia, 2026 Wisconsin elections](https://en.wikipedia.org/wiki/2026_Wisconsin_elections); MCPASD figure computed from [Dane County race 0034](https://elections.countyofdane.com/Precincts-Result/197/0034)

#### Comparison: other Dane County school questions
Dane-County portion only. Gap = Yes % minus referendum-vote-weighted governor Dem two-party %.

| Year | District question | Yes % | Est. Dem % | Gap |
|---|---|---|---|---|
| 2022 | MCPASD (revenue limit) | 62.9 | 76.6 | −13.7 |
| 2022 | Waunakee #1 (bonds $175M) | 52.6 | 65.9 | −13.2 |
| 2022 | Oregon (revenue limit) | 60.6 | 73.4 | −12.8 |
| 2022 | Sun Prairie (revenue limit) | 60.5 | 71.7 | −11.2 |
| 2022 | Verona (revenue limit) | 69.9 | 77.2 | −7.3 |
| 2022 | Belleville (revenue limit) | 62.4 | 69.5 | −7.0 |
| 2022 | Stoughton #2 / #1 (bonds) | 62.6 / 65.7 | 69.2 | −6.6 / −3.4 |
| 2022 | Waunakee #2 (revenue limit) | 60.3 | 65.9 | −5.6 |
| 2022 | Mount Horeb (revenue limit) | 65.1 | 68.6 | −3.4 |
| 2022 | Waterloo (revenue limit) | 51.7 | 50.5 | +1.2 |
| 2026 | MCPASD (revenue limit) | 60.1 | 77.3 | −17.1 |
| 2026 | Waunakee 1 (revenue limit) / 2 (bonds $97.5M) | 52.6 / 51.7 | 66.5 | −13.9 / −14.9 |
| 2026 | Lodi 1 (revenue limit) / 2 (bonds) | 51.7 / 46.8 | 48.9 | +2.8 / −2.1 |

In 2022, MCPASD had the largest negative gap of any Dane school question. In 2026 the gap grew further. — computed from [Dane County 2022](https://elections.countyofdane.com/Election-Result/145) and [2026](https://elections.countyofdane.com/Election-Result/197) files

### Inferences
- Partisanship is the dominant predictor of where MCPASD Yes is high or low. But the Yes line sits well below the Dem line everywhere. In both years the intercept/slope pattern means Yes rises about 0.5–0.8 points per Dem point, not one-for-one.
- **2026 was less polarized on this question, not more.** The correlation fell and the slope flattened under every partisan measure tried (governor, AG, treasurer). Yes fell most in some of the most Democratic geography (City of Middleton, Madison split wards) and held in the less-Democratic Town of Middleton. Dropping split units still shows the same pattern.
- **Ecological inference (Goodman) is illustrative only and assumes constant party-specific rates across wards.**
  - Non-split fit: about 11% of Republican-voting participants voted Yes in 2022 vs. about 22% in 2026. About 79% of Democratic-voting participants voted Yes in 2022 vs. about 73% in 2026.
  - All-unit fit: Republicans ~1% → 7%, Democrats ~82% → 76%.
  - The direction is consistent: Democratic support softened by roughly 5–6 points, and Republican support may have ticked up. The magnitudes are not reliable with 10–24 units.
- The AG rematch is a cleaner year-over-year partisan baseline than the governor race. Evers was a strong incumbent in 2022, and Crowley was a first-time statewide nominee. On AG, MCPASD's Democratic share rose more (+3.2 points) than on governor (+0.7).

### Gaps
- No finer-than-reporting-unit partisan data exists for split units. WEC and the Dane Clerk report by reporting unit. LTSB's ward-level disaggregation would allocate votes proportionally, so it cannot recover the partisan lean of the MCPASD portion of a split ward or town. The Town of Berry/Cross Plains/Springfield/Westport and split Madison figures therefore use whole-unit partisanship.
- I did not verify, against DPI or district maps, whether any MCPASD territory lies outside Dane County. The Dane file lists only the municipalities above.
- 2026 numbers are unofficial. District canvass changes could shift unit figures slightly.
- LTSB open data and WEC ward-by-ward reports were not fetched (elections.wi.gov previously returned 403). The Dane County API gave complete reporting-unit data for both elections, so they were not needed for MCPASD.

## 2. Yes % minus Democratic %: did the gap grow or shrink, and where (city vs. town; Middleton vs. Cross Plains vs. towns vs. Madison wards)?

### Takeaway
The gap grew. District-wide, Yes ran 13.7 points behind the estimated Evers share in 2022 and 17.1 points behind Crowley in 2026. On the AG rematch it ran 11.4 points behind in 2022 and 17.4 in 2026. The widening came mainly from the City of Madison MCPASD wards (−6.5 points), the Town of Cross Plains (−4.3), the City of Middleton (−3.6), the Village of Cross Plains (−3.2) and the Towns of Berry and Springfield (about −3). The Town of Middleton (−0.6) and the Westport portion (+1.1) "stayed true."

### Cited Findings
#### Municipality-level comparison
Partisan % is the referendum-vote-weighted governor two-party Dem %.

| Area | Yes 2022 | Yes 2026 | Δ Yes | Dem 2022 | Dem 2026 | Gap 2022 | Gap 2026 | Δ Gap | Ref votes 22 / 26 | % of ref votes from split units (22/26) |
|---|---|---|---|---|---|---|---|---|---|---|
| City of Middleton | 67.0 | 64.6 | −2.4 | 83.1 | 84.3 | −16.1 | −19.7 | −3.6 | 11,164 / 11,145 | 22 / 20 |
| City of Madison (MCPASD part) | 69.3 | 63.7 | −5.6 | 78.9 | 79.7 | −9.5 | −16.0 | −6.5 | 4,023 / 4,113 | 38 / 35 |
| Town of Middleton | 57.9 | 57.8 | −0.1 | 68.3 | 68.9 | −10.4 | −11.0 | −0.6 | 3,686 / 4,011 | 0 / 0 |
| Village of Cross Plains | 55.9 | 52.3 | −3.6 | 71.1 | 70.7 | −15.2 | −18.4 | −3.2 | 2,106 / 2,373 | 0 / 0 |
| Town of Springfield (part) | 45.8 | 43.0 | −2.8 | 56.5 | 56.7 | −10.7 | −13.7 | −3.0 | 1,187 / 1,108 | 100 / 100 |
| Town of Cross Plains (part) | 50.6 | 46.6 | −4.0 | 59.3 | 59.6 | −8.7 | −13.0 | −4.3 | 431 / 397 | 100 / 100 |
| Town of Berry (part) | 34.4 | 28.9 | −5.5 | 59.6 | 57.6 | −25.2 | −28.7 | −3.5 | 366 / 349 | 100 / 100 |
| Town of Westport (part) | 53.1 | 54.0 | +0.9 | 65.6 | 65.4 | −12.5 | −11.4 | +1.1 | 241 / 224 | 100 / 100 |
| **District** | **62.9** | **60.1** | **−2.8** | **76.6** | **77.3** | **−13.7** | **−17.1** | **−3.4** | 23,204 / 23,720 | 27 / 24 |

— computed from Dane County files ([2022](https://elections.countyofdane.com/Precincts-Result/145/0042), [2026](https://elections.countyofdane.com/Precincts-Result/197/0040)); saved as `partisan_by_area_2022_vs_2026.csv`

- **AG-based district figures.** Est. Kaul two-party share 74.3% (2022) and 77.5% (2026), so the gap went from −11.4 to −17.4. Non-split units: Kaul 75.7% → 78.5%. — computed from [Dane County AG 2022](https://elections.countyofdane.com/Precincts-Result/145/0005) and [2026](https://elections.countyofdane.com/Precincts-Result/197/0005)
- **Madison sub-groups.**
  - Split wards (MCPASD is a minority of the ward): Yes 70.9% → 62.2%; gap −10.8 → −21.9. Individual wards: 102 69.7 → 53.7; 95 70.0 → 55.6; 100 80.0 → 63.4; 101 63.8 → 56.6; 109 69.6 → 57.9.
  - Whole wards (118, 119 plus small ones): Yes 68.4% → 64.5%; gap −8.8 → −12.9. — computed
- **City of Middleton by unit.** Wds 1–4: 69.0 → 67.7. Wds 5–8 (+21 in 2026): 66.7 → 62.5, gap −19.1 → −24.2, the largest gap among large non-split units. Wds 9–13/19 (+22, 24): 66.4 → 64.7. Wds 14–18: 64.4 → 62.6. — computed

#### Outliers relative to the partisan fit
Residual = actual Yes minus Yes predicted by that year's weighted all-unit governor regression.

- **Yes ran ahead of partisanship in 2026:**
  - Madison Wd 117: +11.5 (split; 139 votes)
  - V Cross Plains Wd 7: +10.7 (new ward; 107 votes)
  - Madison Wd 118: +7.2
  - T Middleton Wds 5–8: +6.7 (59.5% Yes at 66.6% Dem, the smallest gap of any large unit)
  - Madison Wds 114: +5.8 and 115: +5.4 (split)
  - C Middleton Wds 1–4: +3.1
- **Yes ran ahead in 2022:**
  - Madison Wd 139: +12.6 (62 votes)
  - Madison Wd 117: +12.1
  - C Middleton Wd 22: +11.1 (95 votes)
  - Madison Wds 115: +10.0, 109: +7.9, 140: +7.5 and 118: +6.9
- **Yes lagged partisanship in 2026:**
  - T Berry: −17.7 (28.9% Yes in a unit that went 57.6% Crowley)
  - Madison Wds 95: −13.9, 102: −11.9 and 101: −9.8 (all split)
  - C Middleton Wds 5–8/21: −4.1
  - V Cross Plains Wds 1–6: −3.9
- **Yes lagged in 2022:** T Berry: −14.7; Madison Wd 101: −5.7; C Middleton Wds 5–8: −3.6; V Cross Plains: −2.5.

— computed

### Inferences
- **Who "stayed true":** the Town of Middleton. Yes was flat at ~58% while Dem share edged up, and Wds 5–8 beat the partisan prediction by ~7 points. Madison Wd 118 and City of Middleton Wds 1–4 also stayed near their 2022 levels relative to partisanship. The Westport sliver held, but on a small n.
- **Where the gap grew most:** the far-west Madison wards in MCPASD, especially the split ones, where Yes dropped 8–16 points despite steady 85–90% Democratic wards. Also City of Middleton Wds 5–8/21 and the Village of Cross Plains. The Madison split-ward partisan shares describe whole wards, but the MCPASD slices are the same geography both years. So the Yes decline there is real even if the true partisan baseline of the slice is unknown.
- **City vs. town:** the gap is largest in absolute terms in the most Democratic places (City of Middleton ~ −20; Madison split wards ~ −22). It is smaller in the Town of Middleton (~ −11). The rural towns (Berry, Springfield, Cross Plains) have low Yes and middling gaps, except Berry, which is an extreme negative outlier both years. Berry and the other rural towns are split units, so their partisan baseline is uncertain.
- Yes ran behind Democratic share in every unit with 20+ votes in both years. Any outlier language should be "Yes ran ahead of/behind what partisanship predicts," not "Yes exceeded the Democratic vote."

### Gaps
- Neighborhood identities of the Madison split wards (95, 100–102, 109, 114–117) were not mapped. A ward-to-neighborhood lookup (City of Madison ward maps) would explain the large drops there.
- For split units, which wards inside the unit are in MCPASD was not determined, so their partisan baseline is approximate.

## 3. Did the 2026 "blue wave" raise Democratic turnout without lifting Yes proportionally? How much Yes must have come from non-Democrats (minimum crossover)?

### Takeaway
Yes. In the geography fully inside MCPASD, Crowley got 1,265 more votes than Evers (+9.2%) and total ballots rose 1,492 (+8.4%). But Yes rose only 175 votes (+1.6%), while No rose 801 (+13.2%) and ballots skipping the question rose 516. Yes never exceeded Democratic share in any unit, so no Republican crossover is required anywhere. Instead, at least 22% of Democratic-voting referendum participants district-wide must have voted No in 2026, up from at least 18% in 2022. More realistic assumptions push that above a quarter.

### Cited Findings
#### Clean geographies (units fully in MCPASD: Town of Middleton, Village of Cross Plains, City of Middleton excl. Wds 14–18, Madison Wds 118/119 + small whole wards)
| | Ballots | Gov Dem | Gov Rep | Yes | No | Yes % | Dem 2-party % | Ballots not voting on question |
|---|---|---|---|---|---|---|---|---|
| 2022 (Evers/Michels) | 17,853 | 13,780 | 3,884 | 10,916 | 6,080 | 64.2 | 78.0 | 857 (4.8%) |
| 2026 (Crowley/Tiffany) | 19,345 | 15,045 | 4,150 | 11,091 | 6,881 | 61.7 | 78.4 | 1,373 (7.1%) |
| Change | +1,492 (+8.4%) | +1,265 (+9.2%) | +266 (+6.8%) | +175 (+1.6%) | +801 (+13.2%) | −2.5 | +0.4 | +516 |

— computed from Dane County files ([2022 gov](https://elections.countyofdane.com/Precincts-Result/145/0004), [2026 gov](https://elections.countyofdane.com/Precincts-Result/197/0004), referendum races above)

- By area (clean units):
  - Town of Middleton: ballots 3,823 → 4,363; Yes 2,134 → 2,320; No 1,552 → 1,691.
  - Village of Cross Plains: ballots 2,252 → 2,451; Yes 1,177 → 1,241; No 929 → 1,132.
  - City of Middleton non-split: ballots 9,146 → 9,720; Yes 5,888 → **5,785** (down); No 2,804 → 3,098.
  - Madison whole wards: ballots 2,632 → 2,811; Yes 1,717 → 1,745; No 795 → 960. — computed
- District-wide, Yes votes fell from 14,596 to 14,263 (−333) while No rose from 8,608 to 9,457 (+849). — [Dane 2022](https://elections.countyofdane.com/Election-Result/145); [Dane 2026](https://elections.countyofdane.com/Election-Result/197)
- **Minimum crossover / defection arithmetic.** Shares are of referendum participants, using the ref-vote-weighted governor share.
  - Yes was below Dem two-party share in every unit with ≥20 votes in both years. The closest were V Cross Plains Wd 7 2026 (−3.1) and Madison Wd 117 2022 (−2.4). So the minimum Republican crossover the data require is zero everywhere. — computed
  - Lower bound on Democratic No votes, assuming every Republican voted No so all Yes came from Democrats: 2022 (76.6 − 62.9)/76.6 = **17.9%**; 2026 (77.3 − 60.1)/77.3 = **22.3%**. Clean geographies: 17.7% → 21.3%. City of Middleton Wds 5–8/21 (2026): at least 27.9%. — computed
  - Illustrative scenario: if 15% of Republican-voting participants voted Yes in 2026, the Democratic Yes rate would be (60.1 − 0.227 × 15)/77.3 ≈ 73%, so ~27% of Democrats voted No. The Goodman non-split fit gives a similar ~73% Democratic Yes rate. — computed

### Inferences
- The 2026 wave raised MCPASD turnout and Democratic votes about as much as overall ballots. The extra voters did not translate into Yes: in clean geography roughly 54% of net new ballots became No votes (801 of 1,492) and about a third skipped the question. This fits two possibilities, which ecological data cannot separate:
  - wave-motivated voters (including Democrats) who were cooler on a larger, 4-year, $118.5M property-tax ask;
  - more of 2022's Yes voters switching to No or skipping.
- MCPASD's problem in 2026 was **Democratic softness, not Republican opposition**. Even if every Tiffany voter voted No, more than one in five Crowley voters had to vote No for the result to come out as it did.
- "Yes as % of Democratic governor votes" in clean geography fell from 79.2% (10,916/13,780) to 73.7% (11,091/15,045). This is a crude, roll-off-inclusive measure of how much of the Democratic vote turned into Yes.

### Gaps
- Individual-level data (exit polls, voter-file surveys) would be needed to split the change into switchers, new voters and skippers. None was found for MCPASD.
- Turnout by registration or party is not published in Wisconsin (no party registration), so "Democratic turnout" here means votes cast for the Democratic candidate.

## 4. What do statewide research and reporting say about partisanship and Wisconsin school referendums, and did the partisan gap in outcomes widen statewide in 2026 vs. 2022?

### Takeaway
Statewide, referendum support has historically crossed party lines. In 2022, Yes beat Evers' county share in about three-quarters of districts, and Dane/Milwaukee were the exceptions where Yes lagged. Polling shows the climate turned sharply against school tax referendums between 2022 and 2026, and pass rates fell from 79% (Nov 2022) to about 57% (Nov 2026, unofficial). Opinions on school funding are strongly partisan in polls. I found no source that measured whether the pass-rate gap between Republican- and Democratic-leaning districts widened in 2026.

### Cited Findings
- **Nov 2022 statewide.** 64 of 81 school referendums passed (79%), and 133 of 166 for the year. Cap Times compared each referendum's Yes % with Evers' share in its county: local support outpaced Evers in 61 of 81 measures. Of the 20 where Evers ran higher, 12 were in Dane or Milwaukee counties (both >70% Evers), and all 12 still passed. — [Cap Times, Nov. 24, 2022](https://captimes.com/news/education/wisconsin-school-referendum-results-dont-follow-partisanship/article_a5bd39dc-7265-5b77-af03-5703777a7123.html)
- **School Perceptions' Rob DeMeuse (via Cap Times).** Voters' "party affiliation was not 'activated'" in referendums. In his predictive model, moving a district's Republican presidential share from 0% to 100% moved predicted approval from more than 90% to about 52%: still above 50%, but a large partisan effect. — [Cap Times, 2022](https://captimes.com/news/education/wisconsin-school-referendum-results-dont-follow-partisanship/article_a5bd39dc-7265-5b77-af03-5703777a7123.html)
- **Wisconsin Policy Forum (secondhand: search summary only; wispolicyforum.org unreachable).** In an earlier analysis using 2020 municipal presidential results, Biden's share ran behind referendum approval in 43 of 51 races. Referendums "performed well in communities carried by both presidential candidates." The Forum notes Wisconsin counties don't publish precinct-level data and many districts cross municipal lines. — [Wisconsin Policy Forum](https://wispolicyforum.org/research/wisconsin-school-referenda-rise-above-economy-politics/) (not directly verified)
- **Nov 2026 statewide (unofficial).**
  - 45 of 79 school measures passed (~57%), just over $1.3B; 34 failed.
  - Of the 45 passes, 16 were by less than 5 points.
  - Only 3 of 8 recurring (permanent) operating referendums passed (Waunakee, Fox Point J2, Seneca). 14 of 17 capital questions passed.
  - Limited-term operating referendums did better in "larger cities and suburbs." Middleton-Cross Plains is listed among passing operating referendums over $20M.
  - 2026 full year: 91 passed, 63 failed. Spring 2026: 46 of 75. 2025: 51 of 89. — [Civic Media, Nov. 4, 2026](https://civicmedia.us/news/2026/11/04/majority-of-school-referendums-pass-in-2026-general-election)
  - WEAU gives the same 45/34 split. Spectrum News counted 83 referendums (secondhand via search). — [WEAU](https://www.weau.com/2026/11/04/voters-reject-34-wisconsin-school-referendums-approve-45/); [Spectrum News](https://spectrumnews1.com/wi/milwaukee/news/2026/11/04/school-referendums-wisconsin-election-results-2026)
- **Spring 2026.** 61% passage, "below the 70% average from 2020 to 2025 but slightly above last year's 56%." — [Wisconsin Watch, April 2026](https://wisconsinwatch.org/2026/04/wisconsin-voters-school-district-referendum-funding-support-property-tax-election-2026/)
- **Marquette Law School Poll, Feb. 11–19, 2026** (818 registered voters, ±4.3) — all from [Marquette Law School Poll release](https://law.marquette.edu/poll/2026/02/25/mlsp87-release/):
  - "If your local school board proposed a referendum to increase taxes for schools...": 43% for, 57% against (same as Oct 2025). Earlier: 52/46 (June 2025), 57/34 (Feb 2020), 55/35 (Jan 2016).
  - "Reduce property taxes or increase spending on public schools?": 60% taxes / 40% schools, the highest property-tax share in 26 polls since 2013. In fall 2022 it was 42/52 (Oct 3–9), 46/48 (Oct 24–Nov 1). Property taxes have led since June 2023.
  - Evers' 400-year partial veto: Republicans 15% "necessary to support schools" / 82% "tax increases for centuries"; independents 50/47; Democrats 79/21.
  - "Legislature failed to provide enough funding" vs. "schools must live within budgets": Republicans 18/81, independents 61/39, Democrats 79/21.
- Marquette's June 2026 summary: a trend "toward opposing local school referendum proposals," which together with the tax-vs-spending item indicates "headwinds facing advocates of increased school spending." — [Marquette Today, June 2026](https://today.marquette.edu/2026/06/insight-from-the-marquette-law-school-poll-goes-beyond-election-contests/)
- **MCPASD 2026 ask.** $118.5M over four years, the second-largest November ask in the state after Green Bay. Opposition cited property-tax fatigue. — [Wisconsin Examiner, Sept. 21, 2026](https://wisconsinexaminer.com/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding/)

### Inferences
- The statewide pattern (Yes outrunning Democrats in Republican-leaning rural districts, lagging them in Dane/Milwaukee) fits MCPASD. A school question compresses partisan differences: Republicans vote Yes more than their party's issue positions imply, and highly Democratic suburbs vote Yes less than their Democratic share. MCPASD's flattening slope in 2026 is that compression getting stronger at the Democratic end.
- In polls, attitudes on school funding are now sharply partisan (roughly 80/20 splits by party). Yet the MCPASD ward data show the question became less partisan in 2026. The likeliest reconciliation: the statewide anti-referendum turn (57% against in Feb 2026) reached Democratic suburban voters too, for example through property-tax concern and ask size, rather than deepening the party split.
- The statewide pass rate fell about 22 points from Nov 2022 (79%) to Nov 2026 (~57%) despite a Democratic wave year. That supports the view that the referendum climate moved independently of partisan tides.

### Gaps
- **No source found that computes 2026 pass rates by district partisan lean** (e.g., Trump- vs. Harris-won districts) or compares that gap to 2022. Searches of Civic Media, WEAU, WBAY, Spectrum and Wisconsin Watch found none. This would require merging DPI's 2026 referendum list with district-level presidential or governor results, which was not attempted here.
- The Wisconsin Policy Forum site (wispolicyforum.org) was unreachable from this session (DNS failure via WebFetch; HTTP 511 via curl). Its findings are cited from search summaries only, and any Nov 2026 WPF analysis was not retrieved.
- No Marquette crosstab splitting the referendum-vote question itself by party was retrieved. The release shows party splits only for the veto and funding questions.
- No academic peer-reviewed study of Wisconsin referendum partisanship was found in this search.

## 5. Ticket-splitting and roll-off: do Republican-leaning wards skip the back-of-ballot question more?

### Takeaway
No. If anything the reverse: in 2026 the most Democratic areas skipped the MCPASD question most. Undervotes ran 8–10% in City of Middleton units, against about 3–4% in the Village of Cross Plains, Madison Wds 118/119 and the Town of Berry. The weighted correlation between undervote rate and Republican share was −0.47. School-question roll-off in non-split units rose from 4.8% (2022) to 7.1% (2026), far above roll-off on the 2026 statewide constitutional questions on the same ballots (about 2–3%).

### Cited Findings
- **2026 undervotes on the MCPASD question** (ballots with the question minus votes, from the other researcher's ballot-style counts in `ward_results_2026.csv`, same Dane source):
  - C Middleton: Wds 1–4 8.3%, Wds 5–8/21 8.2%, Wds 9–13/19/22/24 9.2%, Wds 14–18 10.1%
  - T Middleton: 5.6–7.7%
  - V Cross Plains: Wds 1–6 3.2%, Wd 7 3.6%
  - Madison Wd 118 3.6%, Wd 119 3.4%
  - T Berry 3.3%, T Springfield 5.0%, T Cross Plains 7.5%, T Westport 12.8% (257 ballots)
  - Small Madison split wards: 4.8–14.5%
  - Weighted r (undervote %, Tiffany two-party %) = **−0.47** (n = 21 units with ≥50 ballots); district-weighted undervote ≈ 7.2%. — computed from [Dane County 2026](https://elections.countyofdane.com/Precincts-Result/197/0040) via `ward_results_2026.csv`
- **Same-ballot comparison, 2026 non-split units.** School-question roll-off vs. governor votes was 7.7–8.8% in City/Town of Middleton units. The three state constitutional questions had 1.8–3.4% roll-off in the same units (e.g., C Middleton Wds 1–4: school 7.7%, partial veto 2.9%, worship 2.3%, anti-discrimination 2.7%). In V Cross Plains and Madison 118/119, school roll-off (2.9–3.6%) matched the state questions. — computed from [Dane County races 0034–0036, 0040](https://elections.countyofdane.com/Election-Result/197)
- **2022 non-split units.** School roll-off 0.5–7.9% (most 3–6%). Dane County's advisory abortion question on the same ballots had 0–4.9% (mostly about 1–2%). Roll-off vs. Republican share: r = −0.21 (2022) and −0.35 (2026). Both are weak, and both point the "wrong" way for a Republican-skipping story. — computed
- **Ticket-splitting signals.**
  - Kaul (AG) and Crowley ran almost identically in MCPASD in 2026 (77.5% vs. 77.3% two-party). In 2022 Evers ran ~2 points ahead of Kaul (76.6% vs. 74.3%).
  - The Republican-sponsored 2026 amendments drew 28–39% Yes in MCPASD non-split units (worship 27.9%, partial veto 32.5%, anti-discrimination 38.8%), above Tiffany's ~21.6%. Some Democratic voters backed GOP-sponsored amendments, including the one aimed at Evers' school-revenue veto. — computed from [Dane County 2026](https://elections.countyofdane.com/Election-Result/197)

### Inferences
- There is no evidence that Republican-leaning MCPASD wards skip the school question more. Skipping is highest in the very Democratic City of Middleton. That fits "Democrats skipping" (conflicted voters abstaining rather than voting No), but ecological data can't prove which voters skipped.
- City and Town of Middleton roll-off rose from about 3–6% to 6–9%, while the Village of Cross Plains and Madison wards did not. That is a geographic pattern worth checking against ballot layout. Did the school question sit on a different ballot side or column in those municipalities' ballot styles? Or is it a reporting artifact that the canvass will correct? If it is a genuine choice, ~500 extra non-votes in clean geography is meaningful but small next to the 4,806-vote 2026 margin.
- Yes ran below Democratic share everywhere, and the GOP amendments ran above Republican share. Together this shows sizable cross-pressure among MCPASD Democrats on tax and veto questions. That is consistent with Marquette's finding that property-tax concern now outweighs school spending statewide.

### Gaps
- 2022 under/over-vote counts for split units were not available in the files used, so 2022 roll-off is measured only for non-split units (ballots cast minus referendum votes).
- Ballot design per municipality (question placement, ballot length, front/back) was not checked. It could explain the City/Town of Middleton roll-off pattern.
- 2026 counts are unofficial. Undervote figures in particular can change at canvass.
- **General caveat (ecological inference):** every relationship here is between ward aggregates. None of it shows how any individual Democrat or Republican voted. "Democratic defection" and "Republican crossover" figures are bounds or model estimates under stated assumptions, not observed behavior.
