# Bill growth and education sorted Middleton's referendum

*A research paper for the MCPASD Yes Committee on the levers behind the Nov. 3, 2026 operating referendum. Prepared Nov. 14, 2026. All 2026 vote figures are unofficial until the Dane County canvass, due by Nov. 17, 2026.*

The Middleton-Cross Plains Area School District's operating referendum passed with **60.1% (14,263 Yes to 9,457 No), a margin of 4,806 votes**. Party set the ceiling, and real tax-bill growth decided how much of it Yes reached. The Democratic governor share explains **64%** of the variation in Yes across the district's 19 main voting areas, but no area voted Yes as heavily as it voted Democratic, and at least **22% of Crowley voters voted No**. Among areas equally Democratic, the strongest No lever was how fast a typical home's actual tax bill rose from December 2022 to December 2025 (partial correlation **−0.85**; party plus bill growth explains **93%** of the variation). The size of the bill did not drive No: costlier areas voted *more* Yes at the same party lean. Of 26 new variables tested beyond the original four, two stand out on the Yes side. The first is **prior support**: holding every area at its 2022 Yes rate would have been worth about **+1,290 votes of margin**. The second is **college education**, at about **+70 votes of margin per 1,000 voters** for each 10-point step in the share of adults with a degree. Education also accounts for most of what looked like income, home-value, turnout and new-construction effects. On the No side, low education, private or home schooling and Hispanic share all mark the same places. Those are the Village, the Cross Plains-area towns and moderate-income parts of the City and Madison, where bills grew fastest or Yes slid most. Having children in the household is the weakest of the original four. The research literature points to district-wide levers that ward data cannot see, and they are larger. November timing, the absence of a ballot tax disclaimer (worth **1,900 to 5,900 votes of margin** on Minnesota and Texas evidence), renewal framing and the lack of any organized No campaign all favored Yes. Statewide tax fatigue, a 39% higher final-year ceiling and a third straight renewal favored No. The levers overlap, so the realistic 2030 gain is about **+2,000 to +2,500 votes**, and the biggest single piece is winning back Democratic-leaning homeowners in those slipping areas.

## One point of Yes is worth 474 votes, and 19 voting areas carry the local evidence

The local evidence comes from the 19 Dane County reporting units that cast 100 or more votes on the question. Together they hold **23,440 of the 23,720 referendum votes** and **+4,727 of the +4,806 margin** ([Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197)). Tests that need real tax bills use the 12 non-Madison units, where the analysis read the 2022–2025 bills of 464 sampled homes on AccessDane ([AccessDane](https://accessdane.danecounty.gov/)). On top of the original four variables (party, tax paid, tax increase and children), the analysis built 26 new measures for each unit. It assigned 2020 Census blocks to 2026 wards and apportioned block-group estimates from the Census Bureau's 2020–24 American Community Survey (ACS) ([ACS 2024 5-year summary files](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/); [2020 Census blocks](https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0)). The new measures cover:

| Group | Measures |
|---|---|
| People and households | Education, income, poverty, length of residence, race and ethnicity, owner cost burden |
| Schools and place | Private or home schooling, distance to the nearest MCPASD school ([NCES school locations](https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2324/MapServer/0)), housing density |
| Housing growth | New construction, with a land-use proxy outside Madison ([Dane County 2015 land use](https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Landuse/MapServer/14)) |
| Voting | Prior support, turnout change, roll-off, the three statewide amendments, ticket-splitting |

Every correlation is weighted by referendum votes. The statistic that matters is the **same-party-lean correlation**, the partial correlation with Yes after holding the Democratic governor share constant. It asks whether a variable still separates high-Yes from low-Yes places among areas that are equally Democratic. In the tables, "drop-one range" means the range of that correlation when each unit is left out in turn.

Three limits apply to everything that follows.

1. **The sample is small.** A few large City and Town of Middleton units cast most of the votes, so the effective number of independent areas is about **11**, or about 8 for the 12 bill-history units. At the usual 5% significance level, a same-lean correlation must reach about **±0.63** to stand out from noise, or ±0.73 in the 12-unit tests. Only prior support, education and bill growth clear that bar comfortably.
2. **These are area patterns, not individual votes.** They show that more-educated wards voted more Yes, not that college graduates did.
3. **The data are imperfect.** In split towns and Madison wards, partisan and amendment shares cover the whole reporting unit, not just its MCPASD voters. Margins of error on the ACS estimates run from ±0.5 to ±17 points for education and up to ±35 points for private schooling.

To put the statistics in campaign terms, this paper sizes each lever in **votes of margin** (Yes minus No). On 23,720 votes, **each point of Yes share is worth 474 votes of margin**, the result of 237 voters moving from No to Yes. Where the notes allow, levers are sized in three ways:

- as a scenario applied to every unit;
- as the margin from 1,000 extra voters of a given kind;
- as the margin difference per 1,000 voters between two areas one standard deviation apart on the variable, at the same party lean.

None of these figures is causal, and the levers overlap heavily.

## Party sets the ceiling, and bill growth set how much of it Yes reached

The four variables studied first still form the backbone, but they rank very differently once party is held constant. The **Democratic governor share** explains **64%** of the variation in Yes across the 19 units, at about 0.69 Yes points per Democratic point ([Dane County governor 2026](https://elections.countyofdane.com/Precincts-Result/197/0004)). It is a ceiling, not a guarantee. In no unit with 20 or more votes did Yes reach the Democratic share, in either year. Assume every Tiffany voter voted No. Then at least **22.3% of Crowley voters voted No in 2026**, up from 17.9% of Evers voters in 2022. Computed unit by unit, this floor is what the rest of the paper calls the **Democratic-ticket No** rate ([Dane County referendum 2026](https://elections.countyofdane.com/Precincts-Result/197/0040); [Dane County referendum 2022](https://elections.countyofdane.com/Precincts-Result/145/0042)). Party composition is worth about 1,000 votes of margin. A modeled red-leaning midterm, four points less Democratic, cuts the margin to about **+3,600 to +3,850**. The 2026 Democratic wave, however, added voters without adding Yes. In units fully inside the district, 1,492 net new ballots produced 175 more Yes votes, 801 more No votes and 516 more blanks.

**Real tax-bill growth is the strongest No lever in the local data.** The median home's bill increase from December 2022 to December 2025 correlates with Yes at **−0.85** at the same party lean (drop-one range −0.94 to −0.70). In the 12 areas with bill history, adding it to party raises the explained share from 73% to **93%**. Each extra point of bill growth costs about **0.75 Yes points** ([AccessDane](https://accessdane.danecounty.gov/)). It is also the only variable that clearly predicts the slide from 2022 to 2026 (−0.76 at the same lean). Berry is the extreme case: bills up 43%, Yes at 28.9%, almost 18 points below its partisan expectation.

The slope can be turned into votes. Suppose bills in the Village core, Springfield, the Town of Cross Plains, Berry, Westport and two Town of Middleton units had grown no faster than the City's 12.5%. The slope implies **+730 to +770 votes of margin**, about 700 of them in the Village and the three Cross Plains-area towns. That figure is computed for this paper and overlaps the persuasion levers below.

The 2026 assessment notices jumped 34–37% in the City and 78% in the Village core. Their same-lean link to Yes is weaker (−0.44) and adds little once home value is in the model. They cannot explain the City's slide either, because every City ward saw almost the same jump.

**The size of the bill pushed the other way.** At the same party lean, a higher 2025 bill and a higher four-year referendum cost for the median home both went with *more* Yes (+0.59 each). Two examples:

- **Westport** paid the district's highest bills (about $15,660) and faced a four-year referendum cost near **$12,600**, yet voted 54% Yes, almost two points above its partisan expectation.
- **Town of Middleton Wards 5–8**, with about $8,900 in referendum cost, ran **6.5 points above** expectation. They had the district's lowest Democratic-ticket No rate (10.7%) and its slowest bill growth (9%).

The new data explain the pattern. Once education is also held constant, the link with referendum cost falls to **+0.13** and the link with income to +0.16. Expensive areas are educated areas, and the referendum's cost did not turn them against it.

**Households with children are the weakest of the four.** Their same-lean correlation is +0.29 (drop-one +0.12 to +0.44), and it turns negative (−0.49) once bill growth is held. Kid-heavy units had fewer Democratic-ticket No votes (r −0.35) and skipped the question less (r −0.42). A drive bringing 1,000 more voters from family-heavy wards would have netted about **+232**. Still, at the ward level children mark the Town of Middleton and Madison Wards 101 and 118 more than they drive the vote.

**Table 1. The four original variables, ranked**

| Rank | Variable | Same-party-lean r | Votes of margin, where sized | Verdict |
|---|---|---|---|---|
| 1 | Democratic governor share | Explains 64% on its own | A four-point less Democratic electorate: about −950 to −1,200 | Sets the ceiling |
| 2 | Real bill growth, Dec. 2022 to Dec. 2025 | **−0.85** (n = 12) | City-level growth everywhere: +730 to +770. Three points more Yes in the Village: +136; in the rural towns: +125 | Strongest No lever |
| 3 | Bill size and referendum cost, median home | +0.59, falling to +0.13 with education held | Not a lever | Higher cost did not mean No |
| 4 | Households with children | +0.29 | 1,000 more family-ward voters: +232 | Weak |

Sources: computed from [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197), [AccessDane](https://accessdane.danecounty.gov/) bills and 2020 Census blocks. The red-midterm scenario comes from a two-group ecological fit of the 2026 ward results.

## Earlier support and college degrees are the strongest new Yes markers

Of the 26 new measures, only two separate high-Yes from low-Yes areas at the same party lean strongly enough to survive the small sample.

**Prior support is the first.** A unit's 2022 Yes share correlates with its 2026 Yes share at +0.95 raw and **+0.85 at the same party lean** (drop-one +0.81 to +0.89). The top third of units voted 67% Yes and the bottom third 49%. Party plus 2022 Yes explains 90% of the variation ([Dane County 2022 referendum](https://elections.countyofdane.com/Precincts-Result/145/0042)). Support is sticky in a specific way. 2022 Yes strongly predicts the 2026 Democratic-ticket No share (−0.85 at the same lean), but it does not predict how much an area changed between the two votes (r −0.11). High-support areas did not drift back toward the middle, and low-support areas did not recover.

Had every unit matched its own 2022 Yes rate on its 2026 turnout, the margin would have been about **+6,018 instead of +4,727, a gain of +1,291**. That figure overlaps almost entirely with the earlier lever of winning Democratic-ticket No voters back to their 2022 level (+1,636). It is the same lost ground measured a second way. The value of prior support is that it works as a map: the 2022 and 2026 ward results are the best public guide to where Yes voters live and where they are slipping.

**College education is the second, and it is the only new demographic that adds real information beyond party.** The share of adults with a bachelor's degree correlates with Yes at **+0.71 at the same party lean**. Adding it to party raises the explained variation from 64% to **82%**, at about **+0.33 Yes points per point of degree share** ([ACS 2020–24, via the Census summary files](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/)). Unlike the other demographic links, it survives the obvious alternatives:

- It stays between **+0.47 and +0.62** when income, home value, turnout or bill growth is held alongside party.
- It reaches **+0.89** in the nine units fully inside the district.
- It holds at +0.67 when built from census tracts instead of block groups.

It falls to +0.38 when 2022 Yes is held, which says educated areas were already the high-support areas in 2022.

Areas one standard deviation apart, about 10 points of degree share, differ by roughly **+70 votes of margin per 1,000 voters**. Two levers can be sized from that:

- **Turnout.** 1,000 extra voters from the top-third education units would net about **+283**. Those units are Madison Wards 101, 102, 114, 118 and 119 and City of Middleton Wards 9–13, 19, 22 and 24, which voted 64.2% Yes. The same number of voters from the bottom third (48.5% Yes) would net −30.
- **Persuasion.** In the bottom-third units, 26.8% of Democratic voters voted No, against 21.3% in the rest of the district. Closing that gap moves about 166 voters, worth about **+332**.

**Several apparent Yes levers turn out to be education in disguise.**

- **Income** looks strong at the same party lean (+0.62) but falls to **+0.16** once education is held. That matches survey research finding that income has no independent effect when education is controlled.
- **Referendum cost and home value** fall to +0.13.
- **Turnout**, whether measured as ballots per 2020 adult or as growth in ballots cast, falls from about +0.51 to **+0.10–0.17**.
- **New construction** falls to about +0.13–0.17 with education held, and to roughly zero with bill growth held. This holds for both measures: homes on land that was undeveloped in 2015 (+0.47 before controls) and housing built since 2010 (+0.55). New-home areas lean Yes because their residents are educated and their bills grew slowly, not because new homes matter in themselves. Those areas include the Town of Middleton, City Wards 9–13/19/22/24 and Madison Wards 114 and 118.
- **Asian share** (+0.42) moves closely with education (r +0.76) and is best read the same way.

**Table 2. Yes levers in the local ward data, ranked**

| Rank | Lever | Same-lean r (drop-one range) | Survives other controls? | Votes of margin |
|---|---|---|---|---|
| 1 | Prior support (2022 Yes) | **+0.85** (+0.81 to +0.89) | Yes (+0.87 with bill growth held) | Hold 2022 rates: **+1,291**, overlapping the +1,636 win-back |
| 2 | Adults with a BA or more | **+0.71** (+0.64 to +0.75) | Yes (+0.47 to +0.62; +0.89 fully inside) | +70 per 1,000 voters per 10-point step. Turnout, top third: +283 per 1,000. Persuasion, bottom third: **+332** |
| 3 | Median household income | +0.62 (+0.49 to +0.78) | No (+0.16 with education held) | Mostly education |
| 4 | Referendum cost, median home (original) | +0.59 | No (+0.13) | Not a lever |
| 5 | Turnout level and growth | +0.49 to +0.51 | No (+0.10 to +0.17) | Same as row 2 when used as a turnout lever |
| 6 | New construction | +0.47 and +0.55 | No (about 0 with bill growth held) | Not a lever |
| 7 | Asian share | +0.42 | Moves with education | Not a lever |
| 8 | Households with children (original) | +0.29 (+0.12 to +0.44) | No (−0.49 with bill growth held) | 1,000 family-ward voters: +232 |

Sources: computed from [Dane County 2022](https://elections.countyofdane.com/Precincts-Result/145/0042) and [2026](https://elections.countyofdane.com/Election-Result/197) results and [ACS 2020–24 block-group tables](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/), weighted by referendum votes across 19 units.

## Low education, private schooling and rising rural bills mark the No vote

The No side has one strong driver, bill growth, and several markers that point to the same places. After bill growth, the clearest marker is **low education**, the mirror of the Yes lever. The bottom third of units by degree share are Berry, the Village core, Springfield, the Town of Cross Plains and Madison Wards 109 and 117. They voted **48.5% Yes** and hold about **806** Democratic-ticket No voters. At least **26.8%** of their Crowley voters voted No, against 21.3% in the other 13 units. Education is not simply standing in for bill growth. The two move together (r −0.69), yet education's same-lean link holds at +0.62 with bill growth held. In the 12 bill-history units, party, bill growth and education together explain **95.4%** of the variation in Yes.

**Private or home schooling is the second marker, and the newest finding.** The ACS share of K–12 children in private or home school correlates with Yes at **−0.42** at the same lean (drop-one −0.47 to −0.33). It correlates at −0.56 with the change from 2022 to 2026 ([ACS 2020–24 summary files, Table B14002](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/)). The top third of units on this measure voted **52% Yes**, against 64% in the bottom third. Those units are the Village core, the Town of Cross Plains, Berry and Madison Wards 101, 109 and 114. In them, at least **27.9%** of Democratic voters voted No, against 21.2% elsewhere. Closing that gap would be worth about **+376 votes of margin**.

The signal is fragile, for three reasons:

- With bill growth held, it drops to −0.26, and the drop-one range runs from −0.58 to +0.22.
- It moves closely with bill growth (r +0.69).
- Unit margins of error run from ±4 to ±35 points, and the Madison wards are essentially unmeasured.

The Town of Cross Plains fits both readings at once. **31.3%** of its school-age children are in private or home school, its bills rose 29%, and its MCPASD part flipped from 50.6% Yes in 2022 to 46.6% in 2026.

**Three more variables look like No levers but are better read as markers or hypotheses:**

- **Hispanic share** is real in the data: −0.54 at the same lean, and −0.31 to −0.41 under other controls. It is almost certainly a marker, not a group to target. Its range is narrow (1.2% to 18.8%). The highest shares sit in moderate-income, apartment-heavy parts of the City and Madison: Madison Ward 101 at 18.8% and City Wards 5–8/21 at 10.5%. Hispanic voters are a small share of any unit's electorate. One standard deviation (3 points) equals about −58 votes of margin per 1,000 voters.
- **Newcomers** flip sign depending on the control. The share of householders who moved in during 2020 or later is +0.17 with only party held. It is **−0.64** (owners alone: −0.72) with party and bill growth held, and −0.51 with 2022 Yes held. That makes it a hypothesis for voter-file registration dates to test, not a finding.
- **Distance from the nearest elementary school** shows −0.40 but reverses to +0.34 once bill growth is held. The far-flung units are the rural towns with fast bill growth, so this is location, not distance.

The slide from 2022 to 2026 followed a slightly different map from the 2026 level. Across 17 comparison units, Yes fell most:

- where bills grew fastest (−0.76 at the same lean, n = 10),
- where private schooling is common (−0.56),
- in apartment-heavy areas (−0.48),
- in more diverse areas (−0.45).

It fell least in higher-turnout (+0.47) and higher-income (+0.42) areas. Madison Wards 101, 102 and 109 and City Wards 5–8/21 lost the most ground. Most of these change correlations fall below the significance bar; only bill growth is clearly strong.

**Table 3. No levers in the local ward data, ranked**

| Rank | Lever | Same-lean r | Robustness | Votes of margin |
|---|---|---|---|---|
| 1 | Real bill growth since 2022 (original) | **−0.85** (n = 12) | Strong; also −0.76 for the change in Yes | City-level growth everywhere: **+730 to +770** |
| 2 | Low education | Mirror of +0.71 | Strong | Bottom third holds 806 Democratic-ticket No voters; persuasion **+332** |
| 3 | Private or home schooling | −0.42 | Fragile (−0.26 with bill growth held) | Closing the extra Democratic-ticket No: **+376** |
| 4 | 2026 assessment notice jump | −0.44 | Adds little once home value is held | Not separately sized |
| 5 | Hispanic share | −0.54 | Moderate; marks moderate-income City and Madison areas | −58 per 1,000 voters per 3-point step |
| 6 | Newcomers (moved in 2020 or later) | +0.17 to −0.72 | Sign flips with the control | Hypothesis only |
| 7 | Distance to the nearest school | −0.40 | Reverses with bill growth held | Not independent |

Sources: computed from [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197), [AccessDane](https://accessdane.danecounty.gov/) bills and [ACS 2020–24](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/) estimates. "Democratic-ticket No" is the minimum share of Crowley voters who must have voted No if every Tiffany voter did.

### Eleven plausible suspects showed no independent pull

Several variables that campaigns and opponents often point to show no link once party is held constant.

**Seniors** (share of residents 65 and over) come in at only −0.17. That fits research finding a much smaller "gray peril" for local measures than folklore suggests. Seniors are, however, the strongest predictor of *skipping* the question (r +0.62 with roll-off).

**Apartments and renters** come in at −0.10. Renters vote less, not differently. Apartment-heavy City wards and Madison cast about 1.1 ballots per household, against 1.7–2.0 in the Town of Middleton.

**Six more variables show essentially no link:**

| Variable | Same-lean r |
|---|---|
| Roll-off (skipping the question) | +0.07 |
| Housing density | +0.06 |
| People of color overall | +0.04 |
| Owners paying 30% or more of income on housing | +0.03 |
| Poverty | −0.07 |
| Ticket-splitting | Gaps of about 0.6 points, sign inconsistent |

**The three statewide constitutional amendments** looked like a ready-made measure of anti-tax sentiment, but they measure party. One of them, the partial-veto amendment, was written in response to the 2023 "400-year" school-revenue veto. No votes on it correlate with the Democratic governor share at **r 0.98**. With party held, the three amendments point in different directions (−0.60, −0.62 and +0.27) ([Dane County State Question 1](https://elections.countyofdane.com/Precincts-Result/197/0034); [Wikipedia, 2026 Wisconsin elections](https://en.wikipedia.org/wiki/2026_Wisconsin_elections)). In the rural towns, No on the amendments tracked the Democratic vote one-for-one, yet those towns had the lowest Yes. A clean anti-tax measure would need a local tax question or a survey item, and none was on these ballots.

## Research ranks election rules and campaigns above demographics

The ward data can test only what varies across 19 areas. Many levers were the same for every MCPASD voter: the date, the ballot wording, the structure of the ask, the campaign and the statewide mood. The research literature covers those, and it studies individuals rather than wards. Its central message is that **these district-wide levers outweigh any demographic effect**. In 2026, almost all of them leaned MCPASD's way.

### Election rules gave MCPASD a structural cushion

**Timing** is the best-documented lever. One study matched more than 10,000 school tax measures to voter files. In Wisconsin, the chance of passage was about **23 points lower in April statewide elections** and 18 points lower in special elections than in presidential Novembers. Midterms carried no significant penalty (−0.07) ([Kogan, Lavertu & Peskowitz 2018](https://joeornstein.github.io/pols-4641/readings/Kogan%20et%20al.%20-%202018%20-%20Election%20Timing,%20Electorate%20Composition,%20and%20Policy%20Outcomes.pdf)). The difference comes from who votes. Wisconsin's April electorate has about **10 points more voters aged 65 and over** and 4 points fewer voters with a child at home. A midterm November electorate looks almost like a presidential one.

The authors call their outcome models descriptive, because boards choose their dates strategically. Since 2017-18, Wisconsin law has tied referendums to regular election days, so the real choice is April or November ([DPI referendum procedures](https://dpi.wi.gov/sfs/reporting/safr/referendum/procedures)). MCPASD's November date captured the friendlier electorate. It also came with the cost the literature describes: extra November voters are less informed, skip more ballot items and react more to cost cues ([Kousser & Mullin 2007](https://www.eac.gov/sites/default/files/document_library/files/Political-Analysis-2007-Kousser-428-45.pdf); [Heller & Lyon 2026](https://edworkingpapers.com/sites/default/files/ai26-1500.pdf)). That fits the 2026 pattern, where new ballots broke toward No or left the question blank.

**Tax-salience wording is the largest lever measured anywhere, and Wisconsin ballots currently leave it out.** Two studies size it:

- **Texas.** Since 2019, school bond ballots there must say "THIS IS A PROPERTY TAX INCREASE." A difference-in-differences study finds the line cut Yes share by **7.5 points** overall and **12.5 points in November elections**, with no effect in off-cycle elections ([Heller & Lyon 2026](https://edworkingpapers.com/sites/default/files/ai26-1500.pdf)).
- **Minnesota versus Wisconsin.** Minnesota school bond ballots must state that a Yes vote raises property taxes; Wisconsin's need not. The Minnesota measures ran **4 to 7 points** lower in Yes share ([Brunner, Robbins & Simonsen 2018](https://ideas.repec.org/a/bla/pbudge/v38y2018i4p52-73.html)).

At MCPASD's 23,720 votes, the Minnesota estimate means **−1,900 to −3,300 votes of margin**. The Texas November estimate means **−5,900**, more than the entire 4,806-vote cushion. It would have turned 60.1% into about 47.6%.

The dose matters too. In Heller and Lyon's pre-registered experiments, a stated impact of $1.10 per $100,000 had no effect, while **$110 per $100,000 cut support by 18.4 points**. Wisconsin's 2025 SB 58 and AB 60 would print a "good faith estimate" of the annual property-tax difference on a median-valued home on every referendum ballot. Whether they were enacted is not confirmed ([SB 58](https://docs.legis.wisconsin.gov/2025/related/proposals/sb58); [WPR, May 2025](https://www.wpr.org/news/wisconsin-school-referendums-budget-limitations-proposals)). The number such a line would print for MCPASD decides where it lands on that curve. The district put the new money above current bills at $0 to $59 per $100,000 a year ([Civic Media, Sept. 21, 2026](https://civicmedia.us/news/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding)). The full $24.9M renewal comes to about **$212 per $100,000** a year ([DPI mill rates](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2026)).

**Renewal framing and a time-limited ask favor Yes.** In Ohio in November 2026, **80%** of renewals passed, against **55%** of new increases ([EdWeek, Nov. 2026](https://edweek.org/leadership/school-districts-asked-voters-for-more-funding-many-said-no/2026/11)). In Wisconsin from 1994 to 2013, time-limited (nonrecurring) questions passed more often than permanent (recurring) ones, 56% to 34%. This November, only 3 of 8 recurring operating questions passed statewide ([WPF 2014](https://wispolicyforum.org/wp-content/uploads/2018/08/1402_School-Referenda.pdf); [Civic Media, Nov. 4, 2026](https://civicmedia.us/news/2026/11/04/majority-of-school-referendums-pass-in-2026-general-election)). Next door, Waunakee's permanent operating increase won only 52.6% on the same ballot ([Cap Times, Nov. 4, 2026](https://captimes.com/news/elections/dane-county-voters-pass-three-school-funding-referendums/article_612b45b9-058a-4b7c-ae10-3712d49218ff.html)).

MCPASD's question was 84% a renewal of the existing $24.9M, which carried that advantage. It also raised the final-year ceiling by 39%, to $34.6M ([WMTV, Oct. 22, 2026](https://www.wmtv15news.com/2026/10/22/middleton-cross-plains-voters-weigh-school-referendum-district-faces-nearly-25m-potential-cuts/)). The district's own 2022 survey shows the cost of a bigger ask. Stated support fell from **64% at $20M to 58% at $24.9M and 52% at $30M**, about 1.2 points per $1M of annual ask. If that slope carried to the ballot, each $1M would cost roughly 570 votes of margin ([MCPASD 2022 presentation](https://clubrunner.blob.core.windows.net/00000006121/en-ca/files/homepage/m-cp-school-district-2022-referendum/Nov-2022-Referendum-M-CP-area-school-district-Presentation.pdf)). The survey understated the actual 2022 result by five points at $24.9M, so the slope is a better guide than the levels.

**Ballot fatigue and skipped questions are a smaller lever.** A California study estimates that without ballot fatigue, abstentions would fall 8% and 6% of failed propositions would have passed ([Augenblick & Nicholson 2016](https://ideas.repec.org/a/oup/restud/v83y2016i2p460-480..html)). A study of 242 California propositions, however, found no robust effect of ballot position on approval ([Public Choice 2016](https://ideas.repec.org/a/kap/pubcho/v167y2016i3d10.1007_s11127-016-0340-9.html)). MCPASD's question sat on the back of the ballot, behind three statewide amendments, and 7.2% of voters skipped it ([Dane County raw results](https://elections.countyofdane.com/Election-RawResults)). Bringing skipping in the City and Town of Middleton back to 2022 rates would have added about **+100 to +150** votes of margin. Cutting it to Waunakee's 4% would have added about **+208**.

**The statewide mood was the main structural headwind.** Marquette's February 2026 poll found **60%** of Wisconsin voters preferred lower property taxes over more school funding, the highest share since 2013. 57% said they were inclined to vote against a school tax referendum ([Marquette Law School Poll](https://law.marquette.edu/poll/2026/02/25/mlsp87-release/)). The November statewide pass rate fell to about **57% (45 of 79)**, from about 79% in 2022 ([WEAU, Nov. 4, 2026](https://www.weau.com/2026/11/04/voters-reject-34-wisconsin-school-referendums-approve-45/)). MCPASD lost 2.8 points while the state's pass rate fell about 22.

A concurrent anti-tax question does not have to sink a school measure. Florida voters passed a property-tax cut with 62% while approving 26 of 27 county school-tax measures ([WUSF, Nov. 12, 2026](https://wusf.org/education/2026-11-12/florida-voters-approve-school-taxes-amid-amendment-3)). That fits MCPASD's partial-veto amendment acting as a party marker rather than a tax signal.

### Campaign contact moves ballot measures by one to three points

Ballot measures are where persuasion works. A review of 49 field experiments found that contact persuades essentially no one in general-election candidate races. It found meaningful effects in ballot-measure campaigns that lack partisan cues ([Kalla & Broockman 2018](https://www.cambridge.org/core/product/753665A313C4AB433DBF7110299B7433)). In Oregon, a mail program randomized by precinct moved the margins on 10 of 12 initiatives by **2.5 to 6 points**, without changing turnout or skipping ([Rogers & Middleton](https://appext.hks.harvard.edu/publications/getFile.aspx?Id=943)). Pooled lawn-sign experiments show **+1.7 points** of vote share for candidates ([Green et al. 2016](https://acoppock.github.io/green_etal_2016.pdf)). For MCPASD, mail of that quality is worth about **590 to 1,420 votes of margin**. Signs are worth about **800** if the candidate-race result transfers to a referendum.

Two cautions apply. No randomized test of a school levy campaign exists. And Oregon's effects ran both ways, so an organized 2030 No campaign with similar reach could cost Yes the same amount.

The research identifies three No messages with the strongest evidence:

- **Current spending and pay.** Telling survey respondents their district's actual per-pupil spending cut support for increases by about **22 points** ([Education Next](https://www.educationnext.org/when-provided-with-accurate-information-public-support-for-increased-spending-on-schools-and-teacher-salaries-declines-researchers-find/)).
- **Explicit per-home tax dollars.** Tax disclaimers also pull voters' attention away from benefits and toward taxes ([Heller & Lyon 2026](https://edworkingpapers.com/sites/default/files/ai26-1500.pdf)).
- **The tax cut if the levy expires.** For MCPASD, that is about **$1,060 a year on a $500,000 home**.

The best-supported Yes counters keep concrete benefits in view and use Wisconsin's own evidence. Studies of close Wisconsin votes find that passing an operating referendum has "substantial positive effects on test scores, dropout rates, and postsecondary enrollment" ([Baron 2022](https://ideas.repec.org/a/aea/aejpol/v14y2022i1p1-39.html)). School spending also raises home prices at an elasticity of about **0.95** (a 1% spending increase lifts prices about 0.95%), driven mainly by teacher salaries ([Bayer, Blair & Whaley](https://www.nber.org/papers/w28255)). Neither has been tested as a persuasion message.

**Table 4. Levers the research says favored Yes in 2026, ranked by size**

| Rank | Lever | Best-evidence effect | MCPASD in 2026 | Votes of margin at MCPASD scale |
|---|---|---|---|---|
| 1 | No tax-increase disclaimer on the ballot | Disclaimer costs 4 to 7 points (MN vs. WI); 12.5 points in a Texas November | Absent | **+1,900 to +5,900** protected |
| 2 | November date instead of April | April: 23 points lower chance of passage (WI); 10 points more voters 65+ | November midterm | Not convertible; protected the friendlier electorate |
| 3 | Persuasion mail on a nonpartisan measure | Margin moved 2.5 to 6 points | Yes side only; no No campaign | +590 to +1,420 for whichever side mails |
| 4 | Lawn signs | +1.7 points (candidate races) | Yes signs, no No signs | About +800, if it transfers |
| 5 | Renewal, time-limited structure | Ohio renewals 80% vs. 55% for new asks; WI time-limited 56% vs. 34% permanent | 84% renewal | Not convertible |
| 6 | No organized opposition | Opposition mail works both ways | None formed | Avoided −590 to −1,420 |

Sources: [Brunner, Robbins & Simonsen 2018](https://ideas.repec.org/a/bla/pbudge/v38y2018i4p52-73.html); [Heller & Lyon 2026](https://edworkingpapers.com/sites/default/files/ai26-1500.pdf); [Kogan, Lavertu & Peskowitz 2018](https://joeornstein.github.io/pols-4641/readings/Kogan%20et%20al.%20-%202018%20-%20Election%20Timing,%20Electorate%20Composition,%20and%20Policy%20Outcomes.pdf); [Rogers & Middleton](https://appext.hks.harvard.edu/publications/getFile.aspx?Id=943); [Green et al. 2016](https://acoppock.github.io/green_etal_2016.pdf); [EdWeek](https://edweek.org/leadership/school-districts-asked-voters-for-more-funding-many-said-no/2026/11); [Civic Media, Sept. 21, 2026](https://civicmedia.us/news/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding). Vote conversions are computed at 474 votes per point.

**Table 5. Levers the research says favored No in 2026 or threaten 2030, ranked by size**

| Rank | Lever | Best-evidence effect | MCPASD exposure | Votes of margin at MCPASD scale |
|---|---|---|---|---|
| 1 | Per-home tax line on the ballot (if SB 58/AB 60 pass) | Small impact about 0; $110 per $100,000 costs 18 points | Full renewal ≈ $212 per $100,000 a year | Up to −1,900 to −5,900 |
| 2 | Statewide tax mood | WI pass rate 79% → 57%; 60% prefer tax cuts | Shared headwind | Cannot be separated from other causes |
| 3 | Bigger ask (dose-response) | MCPASD 2022 survey: −1.2 points per $1M of annual ask | 2030 starts at $34.6M | About −570 per $1M, if the slope holds |
| 4 | Spending and pay information (an opponent's message) | −22 points in stated support | Not used in 2026 | Not convertible (attitudes, not votes) |
| 5 | Ballot fatigue and skipping | Abstentions 8% higher (contested) | 7.2% skipped; back of the ballot | −100 to −208 |
| 6 | Negative quality label | Ohio districts labeled failing were 10% less likely to pass a levy | Five-star rating | None in 2026 |

Sources: [WPR, May 2025](https://www.wpr.org/news/wisconsin-school-referendums-budget-limitations-proposals); [Marquette Law School Poll](https://law.marquette.edu/poll/2026/02/25/mlsp87-release/); [WEAU](https://www.weau.com/2026/11/04/voters-reject-34-wisconsin-school-referendums-approve-45/); [MCPASD 2022 presentation](https://clubrunner.blob.core.windows.net/00000006121/en-ca/files/homepage/m-cp-school-district-2022-referendum/Nov-2022-Referendum-M-CP-area-school-district-Presentation.pdf); [Education Next](https://www.educationnext.org/when-provided-with-accurate-information-public-support-for-increased-spending-on-schools-and-teacher-salaries-declines-researchers-find/); [Augenblick & Nicholson 2016](https://ideas.repec.org/a/oup/restud/v83y2016i2p460-480..html); [AJPS summary of Kogan, Lavertu & Peskowitz](https://ajps.org/2015/05/15/federal-education-reforms-backfired-undermining-public-support-for-some-schools/).

### Demographic research predicted a small education effect, and Middleton found a large one

The research on individual voters mostly agrees with the ward data, with one large exception.

**Education** was expected to matter little. In a California survey with ideology controls, a college degree raised support for a local school bond by only 4 points, a result that was not statistically significant ([Brunner & Balsdon 2003](https://media.economics.uconn.edu/working/2003-24.pdf)). Wisconsin's ward-level education gap is also now tangled up with party ([Marquette Law blog](https://law.marquette.edu/facultyblog/2024/11/how-wisconsin-split-its-ticket-once-again/comment-page-1/)). In MCPASD, though, education is the strongest new variable at the same party lean.

The likeliest explanation is this. Inside a district that votes 77% Democratic, party no longer separates voters. Education instead separates Democratic professionals from Democratic homeowners who weigh cost information differently. That reading fits two findings: November's less-informed voters react most to tax cues ([Heller & Lyon 2026](https://edworkingpapers.com/sites/default/files/ai26-1500.pdf)), and complicated ballot choices invite a "defensive no" ([Burnett & Kogan 2015](https://doi.org/10.1080/10584609.2014.894160)). It remains an inference, not a tested mechanism.

**Age** matters less than folklore suggests, at least for local measures:

- In the same California survey, childless homeowners 65 and over were only 3.6 points less supportive of a local bond (not significant). Childless homeowners aged **45 to 54** had the largest local penalty, about **11 points** ([Brunner & Balsdon 2003](https://media.economics.uconn.edu/working/2003-24.pdf)).
- Analysis by generation finds every cohort becomes *more* supportive as it ages ([Plutzer & Berkman 2005](https://pure.psu.edu/en/publications/the-graying-of-america-and-support-for-funding-the-nations-school/)).
- The senior effect that does replicate is about **newcomers**. Long-time older residents support school spending, while older people who moved in recently lower it ([Berkman & Plutzer 2004](https://ideas.repec.org/a/bla/socsci/v85y2004i5p1178-1192.html); [Schlaffer 2018](https://ideas.repec.org/a/bla/socsci/v99y2018i1p118-135.html)).

MCPASD's −0.17 for seniors fits that picture. Its unstable newcomer result cannot test the prediction, because the ACS splits move-in year at 2020 and does not break it out by age.

**Renters** said they supported a local bond more than owners did (79% vs. 69%), but owners turn out more. Buying a home raises local-election turnout by about 5 points ([Hall & Yoder 2022](https://www.gsb.stanford.edu/index%2Ephp/insights/if-you-lived-here-you-might-be-voter-now)). MCPASD shows the turnout half of that story and no difference in how renters voted.

**Private-school households** are treated as likely No voters in theory, but the evidence is fragile. In New York, private-school share was a significant predictor only when enrollment growth was left out of the model ([Ehrenberg et al.](https://www.nber.org/system/files/working_papers/w9088/w9088.pdf)). The best modern evidence is about turnout. In Michigan, households using inter-district school choice voted **15% less** often in school bond elections, and charter households 12% less ([EdWeek on Mcilwain & Reckhow](https://www.edweek.org/policy-politics/how-school-choice-complicates-district-bond-elections/2025/05)). MCPASD's −0.42 sits in that fragile range.

**Race** shows its clearest effect before anything reaches the ballot. Boards propose fewer tax measures where white seniors and nonwhite students differ most. Once a measure is on the ballot, those same factors do not change whether voters approve it ([Nations & Martin 2020](https://ideas.repec.org/a/bla/socsci/v101y2020i6p2220-2237.html)).

**Children** are a weak or even negative ward-level predictor elsewhere too. Milwaukee's 2024 referendum drew **65.8%** Yes in wards where fewer than 20% of households had children, against about 46% in more child-dense wards ([WILL 2024](https://will-law.org/wp-content/uploads/2024/04/Referenda-2024-PB-with-Cover.pdf); [Marquette Law blog](https://law.marquette.edu/facultyblog/2024/04/highlights-from-the-2024-spring-election-in-milwaukee/)).

**Distance to school** has no rigorous study. The closest evidence is a half-point effect from voting in a polling place inside a school ([Berger, Meredith & Wheeler 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2449328)).

**Table 6. Research predictions versus MCPASD's ward results**

| Variable | What research predicts | MCPASD same-lean result | Verdict |
|---|---|---|---|
| College education | Small (+4 points locally, not significant) | **+0.71**, robust | **MCPASD diverges:** education is the main new lever |
| Income | About zero once education is controlled | +0.62, falling to +0.16 with education held | Agrees |
| Seniors 65+ | Small locally; newcomer seniors are the No group | −0.17; strongest predictor of skipping | Agrees; newcomer split untested |
| Childless homeowners 45–64 | Largest local penalty, about −11 points | Not measurable from ward data | Open |
| Renters | Slightly more Yes, lower turnout | −0.10; much lower turnout | Agrees on turnout |
| Private and school-choice households | Fragile negative; lower turnout | −0.42, fragile | Agrees |
| Newcomers in general | Not significant | Sign flips with the control | Agrees that it is unproven |
| Race and ethnicity | Acts on proposals more than on approval | Hispanic share −0.54, likely a marker | Partial |
| Children in the household | Weak, sometimes negative by ward | +0.29 | Agrees |
| Distance to school | No rigorous evidence | Reverses with bill growth held | Agrees |

Sources: [Brunner & Balsdon 2003](https://media.economics.uconn.edu/working/2003-24.pdf); [Berkman & Plutzer 2004](https://ideas.repec.org/a/bla/socsci/v85y2004i5p1178-1192.html); [Hall & Yoder 2022](https://www.gsb.stanford.edu/index%2Ephp/insights/if-you-lived-here-you-might-be-voter-now); [Ehrenberg et al.](https://www.nber.org/system/files/working_papers/w9088/w9088.pdf); [Nations & Martin 2020](https://ideas.repec.org/a/bla/socsci/v101y2020i6p2220-2237.html); [WILL 2024](https://will-law.org/wp-content/uploads/2024/04/Referenda-2024-PB-with-Cover.pdf); local results computed from [Dane County 2026 results](https://elections.countyofdane.com/Election-Result/197) and [ACS 2020–24](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/).

### Trust, quality and the size of the ask shape the No vote but resist measurement

Factors about the district itself are the hardest to measure and the ones No voters cite most. MCPASD's May 2026 Donovan Group survey of about 1,800 residents found 66% would probably or definitely vote Yes. After weighting to likely voters, that reportedly fell to about 47%. Non-supporters cited "property tax fatigue," a "preference for structural or state-level solutions," and a desire for "spending reductions, greater fiscal discipline, and greater transparency" ([Civic Media, Sept. 21, 2026](https://civicmedia.us/news/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding); [Citizen Portal summary, secondhand](https://citizenportal.ai/articles/8140470/wisconsin/school-districts/middleton-cross-plains-area-school-district/survey-finds-mixed-community-backing-for-november-operational-referendum-weighted-support-about-47)). Those are complaints about trust and efficiency, not about school quality. The research vice president of School Perceptions, a Wisconsin firm that runs district referendum surveys, says satisfaction with a district and willingness to fund it "used to be close to the same question," and the two are drifting apart as living costs rise ([School Perceptions](https://www.schoolperceptions.com/BlogPost.php?BlogId=173)).

**Quality ratings cut one way only.** Ohio districts labeled failing under No Child Left Behind were **10% less likely** to pass a levy, even where students were making gains ([AJPS summary](https://ajps.org/2015/05/15/federal-education-reforms-backfired-undermining-public-support-for-some-schools/)). No study finds that a good rating adds votes. MCPASD's support slid from 69% to 63% to 60% while it earned its first five-star state rating ([Madison365](https://madison365.com/middleton-cross-plains-area-school-district-reports-highest-ever-dpi-report-card-scores/)).

**No rigorous study shows that threatened cuts raise passage.** MCPASD warned of 20% cuts and a possible elementary closure if the question failed, and it pledged to cut $5M even if it passed. At a Sept. 17 information session, skeptical voters asked for side-by-side pass-and-fail budgets, not scarier warnings ([WMTV, Oct. 22, 2026](https://www.wmtv15news.com/2026/10/22/middleton-cross-plains-voters-weigh-school-referendum-district-faces-nearly-25m-potential-cuts/); [Civic Media](https://civicmedia.us/news/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding)).

**The one public trust shock faded.** In 2020, a recall drive targeted two board members over COVID-era virtual learning. It failed, and both won re-election in 2022 ([Ballotpedia News](https://news.ballotpedia.org/2020/10/16/two-wisconsin-school-board-members-named-in-recall-petition-after-voting-to-continue-virtual-learning/)).

**School staff are a small bloc.** Employees and their households vote more often in school elections but make up "a surprisingly modest share of the electorate" ([Hartney & Kogan 2026](https://www.hks.harvard.edu/sites/default/files/Taubman/PEPG/research/PEPG26_09.pdf)).

None of these factors can be sized in votes from current data. Together, though, they help explain two things: why MCPASD finished well above its reported weighted survey figure, and why a 40% No vote formed with no No campaign behind it.

## Overlapping levers cap the realistic 2030 gain at 2,000 to 2,500 votes

The levers cannot be added together. Education, private schooling, bill growth, distance and the 2022 base all point to largely the same places: the rural towns, the Village and City Wards 5–8. The turnout levers also overlap with education. The earlier estimate of a plausible combined gain, **+2,000 to +2,500 votes of margin**, holds after the new variables. They sharpen where to look; they do not add votes.

The 2030 question also starts from a weaker position on three counts:

- It will start at the $34.6M ceiling.
- It will be the third straight four-year renewal.
- The share of Democratic voters voting Yes, the number that decides the outcome, is already falling. It was an estimated 0.73–0.76 in 2026, down from 0.79–0.82 in 2022. With the electorate held fixed, the question fails if that share drops to about **0.60–0.63**. Two more cycles of the 2022-to-2026 decline would get there.

These rates come from an ecological fit of the [Dane County 2022 and 2026 ward results](https://elections.countyofdane.com/Election-Result/197).

**First, persuade Democratic-leaning homeowners in the places where bills rose fastest, degrees are fewest and private schooling is most common.** This is worth up to **+1,636** if Democratic-ticket No falls back to 2022 levels. The new variables name the target areas more precisely than before: the Village core, Springfield, the Town of Cross Plains, Berry, City Wards 5–8/21, and Madison Wards 101, 102 and 109. Three message ideas follow from the patterns. All are hypotheses drawn from ward data, not tested messages:

- Show real dollars on a real bill, and acknowledge the rural towns' 27–43% increases since 2022 rather than wave them away with mill rates.
- Use plain cost-and-benefit framing for Democratic voters without degrees.
- Give private- and home-school families a reason to back a district their children do not attend, such as home values and community.

**Second, defend the structural cushion.** That means:

- Hold the vote on **Nov. 5, 2030**, not in April.
- Keep the renewal framing, with a flat or modest first-year step.
- Keep athletics and amenities out of the ask.
- Track SB 58 and AB 60.

If a per-home tax line becomes law, the district needs a clear, accurate, single figure ready well before the ballot is printed. The research shows small stated impacts do no harm and large ones cost thousands of votes.

**Third, prepare for an organized No campaign.** There was none in 2026, and No still reached 40%. An opponent's mail program could take **590 to 1,420 votes of margin**. Its best-supported lines would be current per-pupil spending, per-home dollars, and "vote no and save about $1,060." The counters are:

- a public tracker of the promised $5M in cuts;
- the side-by-side pass-and-fail budgets voters asked for;
- Wisconsin's own evidence that operating money improves outcomes;
- a Waunakee-style pledge to levy less than the full authority if the new Democratic state government raises aid ([Waunakee 2026 referendum FAQ](https://www.waunakee.k12.wi.us/community/2026referendum/faq)).

**Fourth, drive turnout only where it pays.** General turnout did not help in 2026: the Democratic wave added No votes and blanks. Targeted turnout does, at about **+283 per 1,000 voters** from high-education units or apartment wards and **+232** from family wards. Cutting skipping to 4% is worth **+208**, so "flip the ballot" reminders belong in senior-heavy wards, where skipping concentrates.

**Fifth, collect the data the ward results cannot provide.** That includes:

- voter-file matching (registration date, age, household) to test the newcomer, senior-newcomer and empty-nester hypotheses;
- district enrollment and private- and home-school counts by ward;
- a post-election survey with ward identifiers;
- each municipality's revaluation calendar, so 2030 notices do not land mid-campaign the way the City, Village and Berry notices did in 2026.

**Table 7. The 2030 lever menu in votes of margin**

| Priority | Lever | Votes of margin | Overlaps with |
|---|---|---|---|
| 1 | Win back Democratic-ticket No to 2022 levels | **+1,636** | Prior support (+1,291), education (+332), private schooling (+376), bill growth (+730 to +770) |
| 2 | Keep a tax-increase disclaimer off the ballot, or answer it with one small, accurate number | Protects 1,900 to 5,900 | Ask size |
| 3 | Match or deter opposition mail | ±590 to 1,420 | Persuasion, priority 1 |
| 4 | Keep the ask from growing (survey slope) | About 570 per $1M of annual ask | Disclaimer exposure |
| 5 | Lawn signs | About +800, if the candidate-race effect transfers | Persuasion |
| 6 | 1,000 voters from high-education units or apartment wards | +283 each | Education |
| 7 | 1,000 voters from family-heavy wards | +232 | Children |
| 8 | Cut skipping to 4% | +208 | Senior-heavy wards |
| 9 | Three points more Yes in City Wards 5–8, the Village or the rural towns | +156, +136, +125 | Priority 1 |

Sources: computed from [Dane County 2022](https://elections.countyofdane.com/Precincts-Result/145/0042) and [2026](https://elections.countyofdane.com/Election-Result/197) results, with research conversions from Tables 4 and 5. The plausible combined gain is +2,000 to +2,500, not the sum of the rows.

## Conclusion

The 2026 vote changes the picture of who MCPASD's swing voter is. The ward data do not point to the childless senior, the renter or the Republican. They point to Democratic-voting homeowners in less-educated areas where the bill has risen fastest and more children attend private or home school. Two variables taken together locate those voters: the growth of the tax bill, not its size, and education. The original "who has kids" variable turned out to be the weakest of the four. Ward support is also sticky. 2022 Yes predicted 2026 Yes at 0.95, and the slipping places did not bounce back, so the 2026 ward map is a reliable map for 2030. The same stickiness means lost ground stays lost unless someone goes back for it.

The bigger insight is about scale. The demographic levers show *where* to work, but each is worth a few hundred votes. The district-wide levers decide *whether* the question passes, and each is worth thousands. A single line of ballot wording, of the kind Wisconsin lawmakers have proposed, could by the Texas evidence erase the entire 2026 margin. An opponent's mail program of ordinary quality could take a quarter of it. Neither existed in 2026, which means the 60.1% result measures a referendum that faced no opponent and no disclaimer. The Yes Committee's most valuable work before 2030 is to keep those protections in place, or to be ready if they fall. Field work in the Village, the Cross Plains towns and Middleton's slipping City wards matters too, but it comes second.
