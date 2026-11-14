# Local variable tests: what else went with Yes and No in MCPASD's Nov. 3, 2026 referendum, ward by ward

Analysis run Nov. 14, 2026. Ward-level numbers are in `new_variables_by_ward.csv` in this folder. Scripts are in `scripts/` (`acs_sf_fetch.py` and `gis_fetch.py` download, `build_units.py` builds each voting area's values, and `analyze.py` runs the tests and writes the CSV). Unless a line says otherwise, every correlation is weighted by 2026 referendum votes across the **19 reporting units with 100 or more referendum votes**, or the 12 with tax-bill history. "Same party lean" means the partial correlation holding the Democratic governor share constant, the same method as `property_tax_scripts/yes_drivers.py`. 2026 vote counts are the Dane County Clerk's unofficial results, as in the earlier notes.

## 1. Which new variables could be built from public data, and how?

### Takeaway
Twenty-six new measures were built for the 19 voting areas. They cover education, income, poverty, length of residence, new construction, private or home schooling, race and ethnicity, prior support, turnout change, roll-off, the three statewide amendments, ticket-splitting, distance to school, housing density and owner cost burden. Four requested items could only be approximated: move-in year (ACS has a 2020 cut, not 2018), year built outside Madison (a validated land-use proxy), private schooling (very large margins of error) and attendance areas (not determinable).

### Cited Findings
- **Geography.** Each 2020 Census block whose interior point lies inside MCPASD was assigned to its 2026 ward and reporting unit. The method is the same as `property_tax_scripts/hhkids.py`: the `unit()` function from `assign.py`, Dane County ward polygons, and the MCPASD polygon (SchoolID 3549). Block counts sum exactly to each unit's MCPASD part. — [Dane County ward boundaries, DaneCountyBase layer 18](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/DaneCountyBase/MapServer/18); [Dane County school districts, Districts layer 3](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Districts/MapServer/3); [2020 Census redistricting blocks, Esri Living Atlas](https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0)
- **ACS source and vintage.** ACS **2020–2024 5-year** estimates (files dated Jan. 29, 2026), at the block-group level. Tables: B15003 education, B19001 income distribution, B19013 median income, C17002 poverty ratio, B25038 year the householder moved in, B14002 public vs. private school, B25034 year built, B25091 owner costs as a share of income. They were read from the Census Bureau's public table-based summary files with small HTTP range requests, about two dozen requests of 6–200 KB per table, with no key needed. Column labels were checked against the 2024 table shells. — [ACS 2024 5-year summary files](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/); [ACS 2024 5-year table shells](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/documentation/ACS20245YR_Table_Shells.txt)
- **Why not Living Atlas or Census Reporter for ACS.** The Esri Living Atlas ACS layers for these topics have only state, county and tract layers, with no block groups. The Census Reporter API's robots.txt disallows all paths. One test request was made before checking; its data was deleted and not used. — [Living Atlas ACS Educational Attainment service](https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/ACS_Educational_Attainment_Boundaries/FeatureServer); [api.censusreporter.org/robots.txt](https://api.censusreporter.org/robots.txt)
- **Apportionment.** Each block group's ACS rate was applied to its blocks' 2020 counts:
  - adults 18+ for education (a proxy for 25+),
  - persons for poverty,
  - households for income, move-in year and cost burden,
  - children under 18 for school type,
  - housing units for year built.

  The results were then summed to units. Median income is interpolated from the pooled B19001 distribution. Approximate margins of error, apportioned by Census formulas, are in the CSV. — computed, `scripts/build_units.py`
- **Block-group fit.** Big units sit mostly inside their own block groups: on a household-weighted basis, **71–98%** of their block groups' households fall inside the unit (City ward groups, Village, Madison 118–119). The fit is middling in the Town of Middleton Wards 5–8 (62%) and Springfield (69%), and poor in the Town of Middleton Wards 1, 3–4 (30%) and Wards 2, 4A (16%), in the rural towns (20–28%), and in Madison Wards 100–117 (18–54%). In those places ACS values partly describe neighbors outside the unit. Units with under 50% fit carry about 16% of the 19-unit votes. — computed
- **District profile (MCPASD part of all units).**
  - Adults with a BA or more: **63.0%**.
  - Median household income: about **$108,000**.
  - Poverty: **6.0%**.
  - Householders who moved in 2020 or later: **31.7%**; owners who did: **15.7%**.
  - K–12 children in private or home school: **8.4%**.
  - Housing built 2010 or later: **21.5%**.
  - People of color in 2020: **21.8%** (Asian 8.3%, Hispanic 5.7%, Black 3.1%).

  — computed from the ACS and Census sources above
- **Length of residence.** The 2020–24 ACS splits move-in years as "2023 or later," "2020 to 2022" and "2010 to 2019," so a 2018 cut isn't possible. "2020 or later" was used for all householders and for owners. City of Madison parcel `OwnerChangeDate` and `OwnerOccupied` are blank for all 2,509 residential parcels in the district, so sale dates couldn't substitute. — [ACS 2024 table shells, B25038](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/documentation/ACS20245YR_Table_Shells.txt); [City of Madison parcels](https://maps.cityofmadison.com/arcgis/rest/services/Public/OPEN_DATA2/FeatureServer/0)
- **New construction, Madison.** City assessor `YearBuilt` exists for every Madison parcel. In the Madison part of the district, **1,455 of 4,171 dwelling units (35%)** are in buildings from 2015 or later, almost all in Wards 114 and 118. — [City of Madison parcels, TaxSchoolDist 3549](https://maps.cityofmadison.com/arcgis/rest/services/Public/OPEN_DATA2/FeatureServer/0)
- **New construction elsewhere.** Dane County's parcel, assessor and building layers have no year built. The proxy is the share of home parcels under 5 acres that were at least 90% undeveloped in Dane County's 2015 land use inventory:
  - "undeveloped" means farm fields, woods, open land, vacant subdivided lots or land under construction;
  - 2015 farm residences and farm buildings (codes 811x) don't count as undeveloped;
  - "home parcels" means improvements of at least $60,000 and value under $2.5M, the earlier notes' rule;
  - parcels of 5 acres or more are left out because their farmhouses aren't mapped separately.

  Tested on Madison homes with a known year built, it flags **541 of 610 homes built 2015 or later (89%)** and **8 of 1,551 older homes (0.5%)**. District-wide, **1,329 of 13,508 home parcels (9.8%)** are new by this measure. It counts parcels, so it leaves out large apartment buildings; the ACS "built 2010 or later" share is kept as a second measure that does count apartments. — [Dane County Land Use (2015), Landuse layer 14](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Landuse/MapServer/14); [Dane County parcels, TaxParcels layer 0](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/TaxParcels/MapServer/0); [Dane County Assessor service](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Assessor/MapServer)
- **Private or home school.** This is the share of enrolled K–12 children in private school from B14002. The ACS groups home school with private school, and IPUMS reports that home schooling was explicitly included starting with the 2008 ACS. Charter-school treatment isn't documented. Unit margins of error run about ±4 to ±35 points, and Madison wards are essentially unmeasured. — [ACS Data Community thread on B14002](https://acsdatacommunity.prb.org/discussion-forum/f/forum/488/where-are-definitions-of-private-and-public-schools-for-table-b14002-how-are-charter-schools-and-homeschooling-captured); [IPUMS USA, school type variable](https://usa.ipums.org/usa-action/variables/191126)
- **Race and ethnicity.** These come from 2020 Census block counts (P2), so they sum exactly to units. "People of color" means everyone except non-Hispanic white alone. — [2020 Census redistricting blocks](https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0)
- **Schools.** NCES lists **12 MCPASD school records (2023–24)**:
  - elementary: Elm Lawn, Northside, Park, Pope Farm, Sauk Trail, Sunset Ridge and West Middleton;
  - middle: Kromrey and Glacier Creek;
  - high: Middleton High and Clark Street Community School (same address);
  - the district 4K office.

  SchoolDigger's district list has the same 7 elementary, 2 middle and 2 high schools. Distance is the population-weighted straight-line distance from each block to the nearest school, and to the nearest elementary. — [NCES EDGE public school geocodes 2023–24](https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2324/MapServer/0); [SchoolDigger, MCPASD schools](https://www.schooldigger.com/go/WI/district/09510/search.aspx)
- **Election variables.** Sources:
  - `ward_results_2026.csv`, `ward_change.csv` and `partisan_by_ward_2026.csv`, from Dane County 2026 election 197;
  - 2022 Yes for each 2026 unit's comparison unit (the Town of Middleton's three 2026 units share the town-wide 2022 figure);
  - change in ballots cast and in referendum votes, 2022 to 2026;
  - 2026 roll-off;
  - 2026 ballots with the question per 2020 adult;
  - No on the three statewide amendments, sr1–sr3;
  - Democratic share minus No on the partial-veto amendment;
  - governor minus attorney general, and governor minus treasurer, Democratic two-party shares.

  sr1 is the partial-veto limit (race 0034), sr2 worship gatherings (0035) and sr3 anti-discrimination (0036), as identified in `partisan_correlation.md`. — [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197); amendment descriptions per [Wikipedia, 2026 Wisconsin elections](https://en.wikipedia.org/wiki/2026_Wisconsin_elections) as cited in `partisan_correlation.md`
- **Other variables added.** Households per square kilometer of land (log scale) from block land area; the share of owners paying 30% or more of income on housing (B25091); and Asian and Hispanic shares separately. — computed

### Inferences
- The new-construction proxy works well inside Madison, where it could be checked against year built. It is less certain in the rural towns: there, new homes on lots of 5 or more acres are missed, and some older rural homes on small lots carved out of 2015 farm fields may be miscounted as new.
- Because block groups don't fit the Town of Middleton's small reporting units, ACS values there (move-in year, built 2010+, poverty) partly reflect apartments and subdivisions just outside the town.

### Gaps
- **Attendance areas affected by the referendum: not determinable.** No public MCPASD attendance-boundary GIS was found. The City of Madison parcel layer's school fields are blank for 2,844 of 2,858 district parcels; the few filled ones name Madison Metropolitan schools. Earlier notes found only a generic "school consolidation" warning in 2026 coverage, with no named school (`tax_messaging.md`, citing [Channel 3000, Sept. 28, 2026](https://www.channel3000.com/news/middleton-cross-plains-area-school-district-voters-deciding-on-118m-school-referendum-in-november/article_21c34ed2-934f-4903-9354-3e66b2bfc210.html)). The Wisconsin Examiner's Sept. 21 article returned HTTP 403 and couldn't be checked. Distance to the nearest school stands in.
- A 2018 move-in cut isn't available without the Census API or microdata. Neither is a year-built-2015+ figure outside Madison from assessor data.
- Voter-file variables (registration date, age, vote history) would test length of residence and turnout at the person level. They weren't used.

## 2. Which variables go with Yes, raw and at the same party lean?

### Takeaway
Beyond party and bill growth, two variables stand out. **Prior support (2022 Yes, partial r +0.85)** and **education (share of adults with a BA, +0.71)** are strong, survive dropping any one unit, and hold up against other controls. Income, home value, turnout and new construction also look positive at the same party lean, but most of that is education or slow bill growth in disguise. On the No side, **private or home schooling (−0.42)** and **Hispanic share (−0.54)** are moderate and fragile. The statewide amendments and ticket-splitting don't behave like a coherent anti-tax signal.

### Cited Findings
- **Main table** (19 units unless n says 12). Columns:
  - "Same party lean" is the partial r with Yes, holding Democratic governor share.
  - "Drop-one range" is the range of that partial r when each unit is dropped in turn.
  - "Same lean and bill growth" also holds the 2022–25 bill increase, in the 12 non-Madison units.
  - "Margin per 1,000 voters, 1 SD" is the Yes-minus-No margin difference per 1,000 voters between areas one vote-weighted standard deviation apart, at the same party lean (20 × slope × SD).

  Sorted by the same-party-lean r. — computed, `scripts/analyze.py`; data in `new_variables_by_ward.csv`

| Variable | n | Raw r | Same party lean | Drop-one range | Same lean and bill growth (n = 12) | Yes, top vs bottom third | Margin per 1,000 voters, 1 SD |
|---|---|---|---|---|---|---|---|
| Democratic governor share (existing) | 19 | +0.80 | (held) | – | – | 65% vs 51% | – |
| 2022 referendum Yes, % | 19 | +0.95 | **+0.85** | +0.81 to +0.89 | +0.87 | 67% vs 49% | +166 (SD 7.5) |
| Adults 25+ with BA or more, % | 19 | +0.69 | **+0.71** | +0.64 to +0.75 | +0.62 | 64% vs 48% | +70 (SD 10) |
| Median household income ($000) | 19 | +0.09 | **+0.62** | +0.49 to +0.78 | +0.43 | 61% vs 62% | +59 (SD 31) |
| Dem share minus No on partial veto, pts | 19 | +0.88 | **+0.60** | +0.47 to +0.71 | +0.13 | 64% vs 51% | +129 (SD 3) |
| Referendum 4-yr cost, median home ($) (existing) | 19 | -0.06 | **+0.59** | +0.47 to +0.63 | +0.37 | 56% vs 59% | +61 (SD $1,830) |
| 2025 tax bill, median home ($) (existing) | 12 | -0.02 | **+0.59** | +0.45 to +0.76 | – | 55% vs 58% | +51 (SD $1,460) |
| Governor minus treasurer Dem share, pts | 19 | -0.11 | **+0.56** | +0.43 to +0.67 | -0.37 | 62% vs 64% | +60 (SD 0.68) |
| Housing built 2010 or later (ACS), % | 19 | +0.20 | **+0.55** | +0.43 to +0.61 | -0.03 | 62% vs 61% | +51 (SD 16) |
| Ballots cast, change 2022-26, % | 19 | +0.36 | **+0.51** | +0.40 to +0.57 | -0.11 | 62% vs 54% | +47 (SD 14) |
| 2026 ballots per 2020 adult | 19 | +0.02 | **+0.51** | +0.41 to +0.58 | +0.41 | 61% vs 62% | +49 (SD 0.16) |
| Ballots per household (turnout) (earlier) | 19 | -0.19 | **+0.49** | +0.38 to +0.56 | +0.29 | 59% vs 62% | +54 (SD 0.38) |
| Homes on land undeveloped in 2015, % | 19 | +0.26 | **+0.47** | +0.31 to +0.57 | -0.11 | 60% vs 64% | +43 (SD 17) |
| Asian (2020), % | 19 | +0.49 | **+0.42** | +0.25 to +0.48 | +0.62 | 63% vs 53% | +40 (SD 7.1) |
| Referendum votes, change 2022-26, % | 19 | +0.22 | **+0.37** | +0.09 to +0.43 | -0.33 | 60% vs 56% | +34 (SD 15) |
| Households with kids, % (existing) | 19 | -0.19 | **+0.29** | +0.12 to +0.44 | -0.49 | 60% vs 64% | +30 (SD 8.8) |
| No on worship amendment, % | 19 | +0.82 | **+0.27** | +0.19 to +0.34 | +0.28 | 63% vs 52% | +144 (SD 5.9) |
| Owners moved in 2020 or later, % of owners | 19 | +0.27 | **+0.26** | +0.02 to +0.42 | -0.72 | 63% vs 52% | +24 (SD 7.5) |
| Householders moved in 2020 or later, % | 19 | +0.54 | **+0.17** | +0.01 to +0.28 | -0.64 | 64% vs 57% | +19 (SD 7.6) |
| Roll-off (skipped the question), % | 19 | +0.41 | **+0.07** | -0.11 to +0.25 | +0.39 | 64% vs 55% | +7 (SD 2.4) |
| Households per km2 (log10) | 19 | +0.72 | **+0.06** | -0.06 to +0.17 | -0.19 | 64% vs 53% | +11 (SD 0.53) |
| People of color (2020), % | 19 | +0.50 | **+0.04** | -0.16 to +0.25 | -0.13 | 63% vs 48% | +5 (SD 9.7) |
| Owners paying 30%+ of income on housing, % | 19 | +0.02 | **+0.03** | -0.08 to +0.14 | -0.33 | 62% vs 63% | +3 (SD 4.6) |
| Poverty rate, % | 19 | +0.32 | **-0.07** | -0.33 to +0.30 | -0.42 | 62% vs 51% | -8 (SD 3.4) |
| Apartment share of housing, % (earlier) | 19 | +0.57 | **-0.10** | -0.19 to +0.10 | +0.38 | 66% vs 53% | -14 (SD 20) |
| Residents 65+, % (earlier) | 19 | 0.00 | **-0.17** | -0.25 to -0.09 | +0.47 | 63% vs 61% | -16 (SD 4.6) |
| Governor minus AG Dem share, pts | 19 | +0.54 | **-0.24** | -0.39 to -0.15 | -0.38 | 62% vs 51% | -36 (SD 0.56) |
| Distance to nearest MCPASD school, km | 19 | -0.51 | **-0.29** | -0.46 to -0.19 | +0.38 | 46% vs 62% | -30 (SD 1.1) |
| Distance to nearest elementary, km | 19 | -0.60 | **-0.40** | -0.50 to -0.30 | +0.34 | 46% vs 64% | -42 (SD 1) |
| K-12 kids in private or home school, % | 19 | -0.67 | **-0.42** | -0.47 to -0.33 | -0.26 | 52% vs 64% | -47 (SD 6.1) |
| 2026 assessment notice jump, % (earlier) | 19 | -0.02 | **-0.44** | -0.51 to -0.37 | -0.33 | 62% vs 54% | -42 (SD 24) |
| Tax bill growth 2022-25, $ (existing) | 12 | -0.73 | **-0.45** | -0.61 to +0.03 | – | 42% vs 61% | -48 (SD $340) |
| Hispanic (2020), % | 19 | +0.14 | **-0.54** | -0.63 to -0.44 | -0.34 | 63% vs 58% | -58 (SD 3) |
| No on partial-veto amendment, % | 19 | +0.71 | **-0.60** | -0.71 to -0.47 | -0.13 | 64% vs 52% | -266 (SD 6.2) |
| No on anti-discrimination amendment, % | 19 | +0.64 | **-0.62** | -0.74 to -0.54 | -0.11 | 65% vs 52% | -181 (SD 5.4) |
| Tax bill growth 2022-25, % (existing) | 12 | -0.87 | **-0.85** | -0.94 to -0.70 | (control) | 47% vs 64% | -88 (SD 5.9) |

- **Existing variables reproduce.** Bill growth comes out at −0.87 raw and −0.85 at the same lean; Dem share +0.80; households with kids −0.19 raw and +0.29 at the same lean; referendum cost +0.59 at the same lean. All match `yes_drivers_by_ward.csv`. — computed
- **Explained variation.**
  - Democratic share alone explains **64%** of the variation in Yes across 19 units. Adding education raises that to **82%**, at +0.33 Yes points per point of BA share. Adding 2022 Yes instead raises it to **90%**, and both together to 92%.
  - In the 12 bill-history units, Dem share explains 73%, Dem plus bill growth 92.5%, and Dem plus bill growth plus education 95.4%.

  — computed, weighted least squares
- **Education holds up against other controls.** Its partial r with Yes stays **+0.47 to +0.62** when income, home value (referendum cost), turnout or bill growth is held along with Dem share. It falls to +0.38 with 2022 Yes held. Built from tract-level ACS instead of block groups, it is +0.67. In the 9 units fully inside the district it is +0.89. — computed
- **Income and home value are mostly education.** Holding Dem share and education, income's partial r falls from +0.62 to **+0.16**, and referendum cost from +0.59 to **+0.13**. — computed
- **Turnout and new construction are mostly education or slow bill growth.** With education held:
  - ballots per 2020 adult falls from +0.51 to +0.17,
  - ballots-cast growth from +0.51 to +0.10,
  - homes on land undeveloped in 2015 from +0.47 to +0.13,
  - built 2010 or later from +0.55 to +0.17.

  With bill growth held (n = 12), the two new-construction measures go to −0.11 and −0.03. — computed
- **Private or home school.** Partial r −0.42 (drop-one −0.47 to −0.33). It holds −0.20 to −0.51 under the other controls, −0.61 in fully-inside units and −0.34 with tract data, but only −0.26 (drop-one −0.58 to +0.22) with bill growth held. The top third of units for private-school share are the Village core, the Town of Cross Plains, Berry and Madison Wards 101, 109 and 114; they voted **52% Yes**, against 64% in the bottom third. — computed
- **Hispanic share (2020).** Partial r −0.54, holding −0.31 to −0.41 under other controls. The range is narrow (1.2% to 18.8%), and the highest shares are Madison Ward 101 (18.8%), City Wards 5–8, 21 (10.5%), Madison 117 and 102, and City Wards 14–18 and 9–13. — computed
- **Recent movers flip sign depending on the control.**
  - Holding only Dem share, the share of householders who moved in 2020 or later is **+0.17**, and owners +0.26.
  - Holding Dem share and bill growth (n = 12), it is **−0.64** (drop-one −0.81 to −0.54), and owners **−0.72**.
  - Holding Dem share and 2022 Yes (n = 19), it is −0.51 for all householders and −0.49 for owners.

  The owner range across the 12 units is narrow, 6.5% to 17.5%. — computed
- **Distance to school.** Partial r −0.40 for the nearest elementary, but **+0.34** once bill growth is held. In fully-inside units it is +0.52. — computed
- **No clear relation at the same party lean:** roll-off (+0.07), poverty (−0.07), housing density (+0.06), people of color overall (+0.04) and owner cost burden (+0.03). — computed
- **Small-n significance bar.** Weighting by votes makes the effective number of units about **11.2** for the 19 units, **8.4** for the 12 and **9.4** for the 17 comparison units. At the 5% level, that puts the bar near |r| 0.60 (raw) and 0.63 (partial) for the 19-unit tests, and about 0.73 for the 12-unit partials. Only 2022 Yes, education and bill growth clear it comfortably. Income, the partial-veto and anti-discrimination amendments, and Hispanic share are near or below it. — computed (approximate t-test on effective n)

### Inferences
- Education is the one new demographic that adds real information beyond party: at the same Democratic share, highly educated areas voted more Yes. It overlaps with bill growth and home value but isn't explained by them. In the bill-history units, a model with education adds about 3 points of explained variation to Dem share plus bill growth.
- The "more expensive homes, more Yes" pattern in the earlier notes is mostly an education pattern. Areas with costlier homes have more college graduates, and the cost of the referendum itself didn't push them to No.
- The private-school and Hispanic-share links are real in this data but thin. The first is concentrated in Cross Plains-area and rural units that also had fast bill growth. The second likely marks lower-income, apartment-heavy parts of the City and Madison more than any choice by Hispanic voters, who are a small share of each unit's electorate.
- The mover result is unstable. It needs voter-level registration-date data before it can be used.

### Gaps
- With effective n of 8–11, the tests can't separate overlapping explanations (education vs. income vs. rural location vs. bill growth) with confidence.
- These are area-level correlations (ecological inference). They don't show how college graduates, private-school parents or newcomers voted as individuals.

## 3. Which variables go with roll-off and with the Democratic-ticket No vote? What went with the change in Yes from 2022 to 2026?

### Takeaway
The Democratic-ticket No vote (the minimum share of Democratic governor voters who voted No) was lowest where support was high in 2022, education and incomes are high, and bills grew slowly. It was highest where bills grew fast and private-school use is high. Yes fell most from 2022 in lower-turnout, lower-income, apartment-heavy and more diverse areas and in fast-bill-growth areas. 2022 support didn't predict the size of the drop. Roll-off follows seniors and poverty, not Yes.

### Cited Findings
- **Table: roll-off, Democratic-ticket No and change in Yes.**
  - "Dem-ticket No" is (Dem % − Yes %) / Dem %.
  - "Yes change" is 2026 minus 2022 Yes at the comparison-unit level: 17 units, with the Town of Middleton's three 2026 units merged, and 10 for the bill variables.
  - "Same lean" holds the 2026 Democratic governor share.

  — computed, `scripts/analyze.py`

| Variable | r with roll-off | r with Dem-ticket No | Dem-ticket No, same lean | r with Yes change 2022–26 | Yes change, same lean | n (change) |
|---|---|---|---|---|---|---|
| Democratic governor share (existing) | +0.46 | +0.10 | – | -0.18 | – | 17 |
| 2022 referendum Yes, % | +0.33 | -0.31 | -0.85 | -0.11 | +0.10 | 17 |
| Adults 25+ with BA or more, % | +0.16 | -0.60 | -0.69 | +0.26 | +0.36 | 17 |
| Median household income ($000) | -0.15 | -0.60 | -0.60 | +0.45 | +0.42 | 17 |
| Dem share minus No on partial veto, pts | +0.45 | -0.16 | -0.60 | +0.01 | +0.43 | 17 |
| Referendum 4-yr cost, median home ($) (existing) | -0.05 | -0.57 | -0.60 | +0.41 | +0.37 | 17 |
| 2025 tax bill, median home ($) (existing) | +0.29 | -0.54 | -0.54 | +0.74 | +0.74 | 10 |
| Governor minus treasurer Dem share, pts | -0.45 | -0.55 | -0.58 | +0.29 | +0.24 | 17 |
| Housing built 2010 or later (ACS), % | -0.23 | -0.52 | -0.52 | +0.24 | +0.22 | 17 |
| Ballots cast, change 2022-26, % | -0.23 | -0.47 | -0.48 | +0.20 | +0.22 | 17 |
| 2026 ballots per 2020 adult | -0.08 | -0.49 | -0.48 | +0.50 | +0.47 | 17 |
| Ballots per household (turnout) (earlier) | -0.13 | -0.47 | -0.49 | +0.49 | +0.47 | 17 |
| Homes on land undeveloped in 2015, % | -0.34 | -0.43 | -0.43 | +0.02 | +0.01 | 17 |
| Asian (2020), % | -0.22 | -0.34 | -0.39 | -0.28 | -0.24 | 17 |
| Referendum votes, change 2022-26, % | -0.38 | -0.35 | -0.35 | +0.03 | +0.03 | 17 |
| Households with kids, % (existing) | -0.42 | -0.35 | -0.35 | +0.17 | +0.10 | 17 |
| No on worship amendment, % | +0.46 | +0.06 | -0.26 | -0.17 | +0.06 | 17 |
| Owners moved in 2020 or later, % of owners | -0.51 | -0.21 | -0.23 | -0.31 | -0.30 | 17 |
| Householders moved in 2020 or later, % | -0.12 | -0.08 | -0.16 | -0.36 | -0.32 | 17 |
| Roll-off (skipped the question), % | – | -0.05 | -0.11 | +0.26 | +0.39 | 17 |
| Households per km2 (log10) | +0.31 | +0.04 | -0.10 | -0.25 | -0.22 | 17 |
| People of color (2020), % | +0.07 | +0.01 | -0.07 | -0.46 | -0.45 | 17 |
| Owners paying 30%+ of income on housing, % | -0.06 | -0.06 | -0.06 | -0.23 | -0.22 | 17 |
| Poverty rate, % | +0.44 | +0.06 | +0.01 | -0.20 | -0.13 | 17 |
| Apartment share of housing, % (earlier) | +0.25 | +0.17 | +0.14 | -0.44 | -0.48 | 17 |
| Residents 65+, % (earlier) | +0.62 | +0.18 | +0.17 | -0.08 | -0.06 | 17 |
| Governor minus AG Dem share, pts | +0.51 | +0.22 | +0.22 | -0.08 | +0.11 | 17 |
| Distance to nearest MCPASD school, km | 0.00 | +0.21 | +0.28 | -0.29 | -0.42 | 17 |
| Distance to nearest elementary, km | -0.07 | +0.30 | +0.40 | -0.34 | -0.50 | 17 |
| K-12 kids in private or home school, % | -0.37 | +0.27 | +0.40 | -0.35 | -0.56 | 17 |
| 2026 assessment notice jump, % (earlier) | -0.07 | +0.47 | +0.46 | -0.14 | -0.09 | 17 |
| Tax bill growth 2022-25, $ (existing) | -0.30 | +0.34 | +0.53 | -0.05 | -0.18 | 10 |
| Hispanic (2020), % | +0.37 | +0.45 | +0.46 | -0.41 | -0.38 | 17 |
| No on partial-veto amendment, % | +0.43 | +0.22 | +0.60 | -0.25 | -0.43 | 17 |
| No on anti-discrimination amendment, % | +0.47 | +0.30 | +0.63 | -0.25 | -0.29 | 17 |
| Tax bill growth 2022-25, % (existing) | -0.59 | +0.64 | +0.89 | -0.48 | -0.76 | 10 |

- **Where the Democratic-ticket No voters are.**
  - The bottom third of units by education is Berry, the Village core, Springfield, the Town of Cross Plains and Madison Wards 109 and 117. At least **26.8%** of their Democratic governor voters voted No, about **806** voters, against **21.3%** in the other 13 units.
  - In the top third by private-school share, the floor is **27.9%**, against 21.2% elsewhere.

  — computed
- **Persistence.** 2022 Yes is the strongest same-lean predictor of the 2026 Dem-ticket No share (−0.85). It doesn't predict the size of the change (r −0.11), so there was no regression toward the mean. — computed
- **Roll-off (raw r).**
  - Residents 65+: **+0.62**.
  - Governor-minus-AG split: +0.51.
  - Owners who moved in 2020 or later: **−0.51**.
  - Democratic share: +0.46.
  - Poverty: +0.44.
  - No on the statewide amendments: +0.43 to +0.47.
  - Households with kids: −0.42.
  - Education: only +0.16.

  — computed

### Inferences
- The Dem-ticket No lives in the same places the earlier notes found: fast bill growth, the Village and the rural towns. Lower education and more private schooling are additional markers of those places, not separate pools.
- The 2022-to-2026 slide was steepest in lower-turnout, lower-income, apartment-heavy and more diverse units (Madison 101, 102 and 109; City Wards 5–8). This matches the earlier finding that Madison and City Wards 5–8 lost the most ground. Those areas are better reached by persuasion and turnout work among Democratic-leaning renters and moderate-income households than by tax-bill messaging alone.

### Gaps
- Madison ward comparisons between 2022 and 2026 carry boundary and growth caveats (Ward 118 grew from 798 to 1,264 ballots; Wards 139–141 were renumbered), per `ward_results.md`.
- The change outcome has only 17 units (effective n about 9). Most change correlations fall below the rough significance bar; only bill growth at the same lean (−0.76, n = 10) is clearly strong.

## 4. Is there anti-tax or anti-government sentiment beyond party in the statewide amendments or ticket-splitting?

### Takeaway
No usable signal. No on the three Republican-sponsored amendments is almost a copy of the Democratic governor share (r 0.98 for the partial-veto limit). Once party is held, the three amendments point in different directions. Ticket-splitting gaps are tiny (SD about 0.6 points) and inconsistent in sign.

### Cited Findings
- **Overlap with party.** No on the partial-veto amendment correlates with the Democratic governor share at **r 0.98**. — computed
- **Same-lean partial r with Yes:**
  - partial-veto No: **−0.60**;
  - anti-discrimination No: **−0.62**;
  - worship No: **+0.27**.

  — computed
- **Rural units: amendment No votes track the Democratic vote one-for-one.** The Democratic share minus partial-veto No is 2–3 points in Springfield, the Town of Cross Plains and Berry, against about 10–15 points in the City and Madison. Yet the rural towns had the lowest Yes. — computed from `partisan_by_ward_2026.csv`
- **Ticket-splitting.**
  - Governor minus AG: partial **−0.24**, SD 0.56 points.
  - Governor minus treasurer: partial **+0.56**, SD 0.68 points.

  — computed
- **Context.** The partial-veto amendment limits the governor's ability to create or raise taxes by partial veto. It was a response to Evers' 2023 "400-year" school revenue veto. — [Wikipedia, 2026 Wisconsin elections](https://en.wikipedia.org/wiki/2026_Wisconsin_elections), as quoted in `partisan_correlation.md`

### Inferences
- The amendment votes measure party, not tax attitudes. Once party is held, what's left is mostly noise plus urban-vs.-rural differences in crossover. In the City and Madison more Democratic voters backed the GOP amendments, but those places still voted Yes at higher rates. The negative partials should not be read as "people who oppose the tax-limit amendment vote No on schools."
- Split units are a further problem. In the rural towns, Westport, City Wards 14–18 and most Madison wards, the amendment and partisan shares describe the whole unit, not just the MCPASD voters.

### Gaps
- A cleaner anti-tax measure would need a local tax question or a survey item. None was on the 2026 ballot in these units.

## 5. Ranking the levers for Yes and for No

### Takeaway
The best new levers are about **where to look**, not new persuasion targets.
- **Yes side:** 2022 Yes and education are the most reliable. Holding each unit at its 2022 rate is worth about **+1,290** votes of margin, which overlaps the earlier +1,636 "win back Democratic-ticket No voters" lever. Each 1,000 extra voters from the top-third education units nets about **+280**.
- **No side:** after bill growth, the markers are low education, private or home schooling and fast-growing rural or Cross Plains-area units. Closing their excess Democratic-ticket No is worth about **+330 to +380** of margin, overlapping with the earlier bill-growth levers.

### Cited Findings
- **Levers for Yes, ranked** by strength, robustness and size. All figures are computed in `scripts/analyze.py`; the 19-unit margin was +4,727 (all units: +4,806).
  1. **Prior support (2022 Yes).** Partial r **+0.85** (drop-one +0.81 to +0.89). Top third 67% Yes vs. bottom third 49%. If every unit had matched its 2022 Yes share on its 2026 turnout, the margin would have been **+6,018 instead of +4,727, i.e., +1,291**. This overlaps the existing "Democratic-ticket No back to 2022" lever (+1,636) and is not additive with it.
  2. **Education (share of adults with a BA).** Partial r **+0.71**, robust to the controls above. Each point of BA share is worth about +0.33 Yes points at the same party lean. One SD (10 points) equals about **+70 margin per 1,000 voters**.
     - **Turnout:** 1,000 extra voters from the top-third education units (Madison 101, 102, 114, 118 and 119; City Wards 9–13, 19, 22, 24), voting at those units' 64.2% Yes, net **+283**. From the bottom third (48.5% Yes) they net −30.
     - **Persuasion:** bringing the bottom-third education units' Democratic-ticket No rate (26.8%) down to the rest of the district's (21.3%) moves about 166 voters, or **+332** margin.
  3. **Income and home value.** Partial r +0.62 and +0.59, but **+0.16 and +0.13** with education held. They aren't separate levers. Higher-cost areas didn't vote No because of the referendum's higher cost to them.
  4. **Turnout level and growth.** Partial r about +0.51, but **+0.10 to +0.17** with education held. Higher-turnout units are more educated. As a pure turnout lever this is the same as row 2.
  5. **New construction.** Homes on land undeveloped in 2015: +0.47. Built 2010 or later: +0.55. These are near zero with bill growth or education held. New-home areas (Town of Middleton; City Wards 9–13, 19, 22, 24; Madison 114 and 118; and the Village core) lean Yes at the same party lean. Except in the Village, that's mainly because their bills grew slowly and their residents are highly educated.
  6. **Households with kids (existing).** Partial r +0.29, the weakest of the existing four.
- **Levers for No, ranked** (where No ran ahead of party):
  1. **Tax bill growth since 2022 (existing).** Partial r **−0.85** (n = 12), −0.76 for the change in Yes. Still the strongest No variable.
  2. **Low education**, the mirror of Yes lever 2. The bottom-third units voted **48.5% Yes** and hold about **806** Democratic-ticket No voters.
  3. **Private or home schooling.** Partial r **−0.42**, −0.56 for the change in Yes. Top third 52% Yes vs. 64%. Closing the excess Democratic-ticket No in the top-third private-school units (27.9% vs. 21.2%) is worth about **+376** margin. Those units overlap heavily with lever 2 and with bill growth: the Village core, Town of Cross Plains, Berry and Madison 101, 109 and 114. The margins of error are large.
  4. **Hispanic share (2020).** Partial r **−0.54**, −0.38 for the change in Yes. Likely a marker of moderate-income, apartment-heavy parts of the City and Madison (Madison 101 and 102; City Wards 5–8, 21) rather than a group to target. One SD (3 points) equals about −58 margin per 1,000 voters.
  5. **Newcomers (moved in 2020 or later).** Negative only with bill growth or 2022 Yes held (−0.51 to −0.72), and −0.32 for the change in Yes. Unstable sign: treat it as a hypothesis.
  6. **Distance from school / rural location.** Partial r −0.40, but it reverses with bill growth held. It isn't an independent lever.
  7. **No lever:** roll-off, poverty, density, owner cost burden, the statewide amendments and ticket-splitting.
- **For scale, the earlier levers** (from `property_tax_by_ward.md`): win back Democratic-ticket No voters to 2022 levels +1,636; 1,000 more voters from apartment-heavy wards +283; from family-heavy wards +232; cut skipping to 4% +208. — [property_tax_by_ward.md, Nov. 13 addenda](property_tax_by_ward.md)

### Inferences
- **For 2030 targeting:** 2022 and 2026 ward Yes rates plus education share are the best public map of where Yes voters are. Turnout drives in high-education units are worth about as much per 1,000 voters (+283) as apartment-ward drives (+283).
- **Persuasion priorities stay as before:** Democratic-leaning homeowners in the Village, City Wards 5–8 and Madison, with real-dollar bill messages. The new variables add two angles:
  - private and home-school families in the Cross Plains-area units, who may need a reason to support a district their children don't attend;
  - lower-education Democratic voters, who may respond to plainer cost and benefit framing.

  Both are hypotheses from ward patterns, not tested messages.
- **None of these levers add up.** Education, private schooling, bill growth and the 2022 base all pick out largely the same rural, Village and City Wards 5–8 areas. The plausible combined gain is the earlier +2,000 to +2,500, not that plus these.

### Gaps
- Per-1,000-voter and per-SD figures assume new or persuaded voters behave like their unit's average voter, which ecological data can't confirm.
- No estimate is causal. Education can't be "moved"; it tells a campaign where to look, not what to change.

## 6. How much weight can these results bear?

### Takeaway
Treat everything beyond party, bill growth, 2022 support and education as suggestive. The tests rest on 12–19 areas (effective n about 8–11). The data are 2020 counts and 2020–24 survey estimates applied to 2026 voters, the variables overlap heavily, and area patterns don't show individual behavior.

### Cited Findings
- **Effective sample size.** About 11 for the 19 units, 8 for the 12 bill-history units and 9 for the 17 comparison units, because a few large City and Town of Middleton units carry most votes. — computed
- **Overlap among predictors** (weighted r across the 19 units):
  - Education with bill growth: −0.69.
  - Education with Asian share: +0.76.
  - Education with 2022 Yes: +0.61.
  - Income with ballots per adult: +0.74.
  - New homes with ballots-cast growth: +0.83.
  - Private school with bill growth: +0.69.
  - Distance to elementary with bill growth: +0.75.
  - Partial-veto No with Dem share: +0.98.

  — computed, `scripts/analyze.py` diagnostics
- **Margins of error.** Unit margins of error across the 19 units: education ±0.5 to ±17 points, private or home school ±4 to ±35 points, moved in 2020 or later ±3 to ±19 points, poverty ±1 to ±9 points, built 2010 or later ±2 to ±18 points (see the `_moe` columns in the CSV). — computed by Census-style apportioned MOE formulas
- **Split units.** Partisan, amendment and turnout-change measures cover the whole reporting unit for split units: the four towns, Westport, City Wards 14–18 and most Madison wards. Demographic and referendum measures cover only the MCPASD part. — `partisan_by_ward_2026.csv` split flags
- **Excluded unit.** Village of Cross Plains Ward 7 (107 votes) is outside the 19 units because it has no 2020 Census households; it was built after 2020. — computed

### Inferences
- Before 2030, the most valuable next step is voter-file matching (registration date, age, household) and district enrollment by ward. That would turn the education, newcomer and private-school hypotheses into individual-level evidence.

### Gaps
- ACS block-group estimates for 2020–24 can't capture 2025–26 growth (for example, City Wards 9–13, 19, 22, 24 and Village Ward 7).
- 2026 results are unofficial until the canvass.
