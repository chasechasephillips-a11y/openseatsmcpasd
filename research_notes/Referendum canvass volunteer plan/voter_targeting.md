# Voter Targeting for the MCPASD Referendum GOTV: Who to Knock, Who Gets a Hanger, Who to Skip

*Source note (Oct 19, 2026): the fetch tool and direct HTTP were blocked in this session for every host except GitHub, so none of the papers' full text could be opened. Every figure below comes from a search engine's extract of a primary source, or of a secondary source where marked. Numbers labeled "secondhand" or "unverified" should be checked against the original paper or data before they go into anything public. Arithmetic I did myself is labeled "derived."*

---

## 1. Which turnout-propensity bands respond most to canvassing and to literature, in high- vs low-salience elections?

### Takeaway
The canvassing effect is largest for voters near their personal "tipping point." In a high-turnout election like the 2026 Wisconsin midterm, that tipping point moves down to low- and mid-propensity voters. High-propensity voters, who vote anyway, gain little. The headline studies (Enos/Fowler/Vavreck, Gerber-Green-Larimer) found the opposite pattern, but they come mostly from low-salience elections. Every tactic loses roughly one-third to three-quarters of its effect when salience rises.

### Cited Findings
**Arceneaux & Nickerson (2009), AJPS 53(1):1–16, "Who Is Mobilized to Vote? A Re-Analysis of 11 Field Experiments"**
- Model: canvassing mobilizes only citizens "whose propensity to vote is near the indifference threshold," and how interesting the election is sets where that threshold falls. Conclusion: "low-propensity voters can be effectively mobilized only in high-turnout elections." — [ISPS abstract](https://isps.yale.edu/research/publications/isps09-030); [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-5907.2008.00354.x); [author PDF](https://sites.temple.edu/nickerson/files/2017/07/Arceneaux_Nickerson.AJPS_.2009.pdf)
- The data are 11 randomized face-to-face canvassing experiments. Each study's control-group turnout serves as its measure of salience. — [author PDF via search extract](https://sites.temple.edu/nickerson/files/2017/07/Arceneaux_Nickerson.AJPS_.2009.pdf)
- A political-science teaching summary states the practical rule. In highly visible elections (e.g., presidential), target "those who rarely vote." In obscure elections (legislative primaries), target "those who regularly vote." In mid-level elections (congressional or mayoral), target "those who vote occasionally." — [Adam Brown (BYU) summary](https://adambrown.info/p/notes/arceneaux_and_nickerson_who_is_mobilized_to_vote_a_re_analysis_of_11_field_experiments)
- A contemporaneous summary says the effect "was greatest among those with a moderate propensity to vote," in experiments run 1998–2003. — [The Monkey Cage, 2009](https://themonkeycage.org/2009/10/the_hunt_for_campaign_effects_2/)
- **Effect sizes by band: NOT obtained.** A search extract mentions "G = .1" (low salience) and "G = .48" (high salience) as parameter values, with little canvassing effect on high-propensity voters in the high-salience case. I could not confirm what G denotes or find the band-level percentage-point estimates. — [search extract of author PDF; unverified](https://sites.temple.edu/nickerson/files/2017/07/Arceneaux_Nickerson.AJPS_.2009.pdf)

**Enos, Fowler & Vavreck (2014), JOP 76(1):273–288, "Increasing Inequality"**
- Pooled 24 field experiments (~1.2 million individuals). Propensity was estimated from age, race, gender, and geography. "Two-thirds of GOTV experiments mobilized high-propensity voters to a greater degree than low-propensity voters." — [paper PDF](https://scholar.harvard.edu/files/renos/files/enosfowlervavreck.pdf); [LSE USAPP summary](https://blogs.lse.ac.uk/usappblog/2014/03/27/get-out-the-vote-interventions-increase-inequality-in-voter-turnout/)
- In the Gerber-Green-Larimer "Neighbors" social-pressure mailing (Michigan, Aug. 2006 primary, a low-salience election):
  - The effect was about 4.8 points for the low-propensity group and "more than two times greater for the highest propensity group."
  - Modeled effect rises about 1.6 points per standard deviation of propensity.
  - The effect approaches about 12 points at the top of the propensity range.
  - Caveat: the PDF text extract was partly garbled, so verify against the paper's Figs. 2–3. — [paper PDF, search extract](https://scholar.harvard.edu/files/renos/files/enosfowlervavreck.pdf)
- Secondhand: a later paper cites Enos et al.'s own appendix as showing the propensity–effect relationship turns *negative* when control-group turnout exceeds 50%. That is consistent with Arceneaux & Nickerson. **Unverified.** — [ResearchGate listing / citing-paper extract](https://www.researchgate.net/publication/271664538_Increasing_Inequality_The_Effect_of_GOTV_Mobilization_on_the_Composition_of_the_Electorate)

**Salience meta-analysis: Mann & Haenschen, *Electoral Studies* vol. 87 (Feb. 2024), "A meta-analysis of voter mobilization tactics by electoral salience"**
- Effects of canvassing, phone, direct mail, and SMS fall by roughly **33% to 76%** from low- to high-salience elections. Most experiments ran in low-salience elections: only 40 of 240 were in presidential cycles. — [VoteAmerica copy](https://research.voteamerica.org/a-meta-analysis-of-voter-mobilization-tactics-by-electoral-salience/); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0261379423001518)
- Canvassing estimates (built on an adjusted Green & Gerber 2019 dataset; these appear to be per-contact effects):

  | Subset | Effect (points) | Studies (n) |
  |---|---|---|
  | Pooled | 3.96 | 56 |
  | Low salience | 4.58 | 32 |
  | High salience | 3.05 | 24 |
  | Attenuation | −33.4% | |

  A VoteAmerica-hosted table shows −23% for canvassing instead, which suggests version differences. Verify. — [ScienceDirect, search extract](https://www.sciencedirect.com/science/article/pii/S0261379423001518)

**Other pooled estimates**
- Green, McGrath & Aronow (2013, JEPOP 23(1):27–48) pooled 200+ GOTV experiments. Their average **intent-to-treat** effects (effect per voter assigned, whether or not contacted) are about 1.0 point for door-to-door, 0.7 for mail, and 0.4 for phone. These come secondhand, via private correspondence reported by Enos & Fowler (2015). — [Enos & Fowler 2015 PDF](https://www.ifs.org/wp-content/uploads/2015/05/Enos-Fowler-2015-Campaign-Spending-And-Turnout.pdf); [ISPS abstract](https://isps.yale.edu/research/publications/isps13-020)
- The same literature finds nonpartisan mail has a positive average effect, while advocacy mail has a "negative, but statistically insignificant" effect. — [Foos manuscript citing Green, Aronow & McGrath](https://discovery-pp.ucl.ac.uk/1531107/1/Manuscript_Foos_John.pdf)
- Secondhand: Florian Foos (LSE) analyzed 122 GOTV experiments and found campaigns do best targeting **40–60% propensity** voters. Source is a practitioner blog, not the paper itself. — [Campaign Lab](https://campaignlab.uk/project/blog-the-truth-about-voter-turnout-what-can-we-actually-learn-from-over-100-voter-turnout-experiments/)
- Green & Gerber, *Get Out the Vote* (4th ed., Brookings 2019), calls canvassing by friends and neighbors the "gold standard" tactic. I could not retrieve its per-contact numbers. — [Brookings front matter](https://www.brookings.edu/wp-content/uploads/2019/07/20190726-green-finan.pdf)

**Literature and door hangers**
- Nickerson (2005, *Annals* 601): in a randomized experiment in the **2002 Michigan gubernatorial election** (a midterm), partisan door hangers raised turnout **1.2 points** and volunteer phone calls 3.2 points. Both were judged cost-competitive with door knocking. — [IDEAS/RePEc](https://ideas.repec.org/a/sae/anname/v601y2005i1p10-27.html)
- Friedrichs, King & Nickerson (2004 WP): Michigan Democratic Party experiment across 14 state house districts comparing door hangers, volunteer calls, and face-to-face visits. All three had "similar cost-effectiveness." — [HKS WP via RePEc](https://ideas.repec.org/p/ecl/harjfk/rwp04-018.html)

**Analyst Institute**
- No public Analyst Institute document was retrievable. Practitioner vendors describe the common practice of pairing high partisanship/support scores with "low-to-mid turnout propensity scores" for GOTV. — [The Campaign Workshop](https://www.thecampaignworkshop.com/blog/political-direct-mail/democratic-direct-mail-targeting)

### Inferences
- **2026 is a high-salience election, likely more so than anything in the experimental base.** WI 2022 midterm turnout was 56.75% of voting-age population statewide and about 80% of registered voters in Dane County (Section 2). Control-group turnout among MCPASD registrants is therefore likely 75–85%, probably above any election in Arceneaux & Nickerson's sample. The threshold model then puts the persuadable-to-vote margin among **low- and mid-propensity** registrants. People who voted in 2018, 2022, 2024, and recent Aprils are near-certain voters: knocking them mainly spends volunteer time. This extrapolates beyond the sample, so treat it as directional.
- **Expected per-knock gains are small.** Take ~3 points per contacted voter (high-salience canvassing) times a typical contact rate (unknown here; often a minority of doors answer). Expect on the order of 1 extra voter per several dozen knocked doors. Door hangers (1.2 points per assigned voter, no contact needed) are competitive per minute. That is the case for "hang only" on lower-priority doors instead of skipping them, *if* those doors lean yes (see Section 4 on net-vote math).
- The Enos/Fowler/Vavreck high-propensity pattern comes largely from low-salience elections and mail. It should **not** be read as "knock the super-voters" in a November midterm.

### Gaps
- Band-level percentage-point effects from Arceneaux & Nickerson's tables could not be extracted; the paper is paywalled and fetch was blocked.
- Exact quartile estimates from Enos/Fowler/Vavreck, and the appendix result for >50% control turnout, are unverified.
- No Analyst Institute public memo on propensity targeting was found.
- Green & Gerber 4th-edition votes-per-contact figures were not retrieved.
- Rogers et al. (2017, *Electoral Studies*), "Social Pressure and Voting: A Field Experiment Conducted in a High-Salience Election," surfaced in search but its results were not retrieved. From background knowledge it may be the 2012 Wisconsin recall; unverified.
- No study isolates canvassing effects in an election with ~80% baseline turnout like MCPASD's.

---

## 2. Midterm drop-off voters as a GOTV target, and how big is the drop-off population?

### Takeaway
Drop-off voters (voted in the presidential general, skipped the midterm) are a large pool: statewide roughly 22–23% of 2024 presidential voters, and roughly 17% in Dane County, on a net basis. Theory suggests they are among the most mobilizable people in a high-salience midterm. They lean younger and Democratic, which likely correlates with referendum support here. Direct experimental evidence on canvassing them specifically is thin.

### Cited Findings
**Statewide turnout**
- **2022 midterm:** WEC unofficial turnout was **56.75%** of voting-age population. That is 2,653,820 governor votes (AP) over a VAP of 4,676,183, below the 2018 midterm record of **59.43%**. — [Channel 3000](https://www.channel3000.com/news/politics/elections/unofficial-turnout-in-2022-midterm-election-at-nearly-57-wisconsin-elections-commission-says/article_007c2063-a4a3-5dd5-ae77-d730e3305463.html); [WPR](https://wpr.org/wisconsins-voter-turnout-was-high-novembers-election-still-lower-2018)
- **2024 presidential:** about **72.6%** of VAP, unofficial (AP), vs. 72.9% in 2020; nearly 3.4 million ballots. — [WMTV/AP](https://www.wmtv15news.com/2024/11/06/wisconsin-turnout-presidential-race-nears-73/)
  - Unofficial presidential votes: **3,422,802**; total ballots run slightly higher. — [Marquette Law faculty blog](https://law.marquette.edu/facultyblog/page/35)
  - The highest rate since 1948 was 73.2% in 2004. — [WMTV/AP](https://www.wmtv15news.com/2024/11/06/wisconsin-turnout-presidential-race-nears-73/)
- **Derived:** 3,422,802 − 2,653,820 = **~769,000 fewer** top-of-ticket votes in 2022 than in 2024. 2022 was about 77.5% of the 2024 level, and about 22.5% of the 2024 presidential vote total is net "drop-off." The VAP turnout gap is 72.6 − 56.75 ≈ **15.9 points**. Individual-level drop-off is larger than this net figure because of churn (moves, new registrants, deaths). — derived from sources above

**Dane County**
- **2022:** **302,459 ballots** on 376,531 registered voters, **80.3%** (unofficial). 2018 midterm and 2020 presidential turnout were reported at 88% and 89.3%. — [Gigafact/Wisconsin Watch fact brief](https://gigafact.org/fact-briefs/did-dane-county-have-88-voter-turnout-in-2022-tied-with-the-2018-midterms)
- **2024:** Harris **273,954 (74.9%)**, Trump **85,449 (23.4%)**. — [Verona Press](https://www.veronapress.com/news/verona-dane-county-election-results/article_81c1b0bc-9dd9-11ef-8da8-7b6142df701a.html)
- **Derived:** the implied 2024 Dane presidential total is ≈273,954 / 0.749 ≈ **365,800**. 2022 ballots were therefore about **63,000 (~17%) fewer** than 2024 presidential votes. This counts presidential votes, not ballots, so it is approximate. — derived
- An NBC piece describes Dane's 2022 turnout as about 90% of its presidential turnout, a different denominator. It roughly agrees with the derived ~83%. — [NBC News](https://www.nbcnews.com/meet-the-press/rcna62095)

**MCPASD 2022**
- 2022 referendum: **14,592 yes / 8,606 no**, 23,198 total, **62.9% yes**, a 5,986-vote margin. — [Channel 3000](https://www.channel3000.com/news/politics/elections/middleton-cross-plains-area-school-district-referendum-passes/article_1d33d875-2226-504c-a797-f9ea84c6890a.html)

**Who drops off**
- Pew validated-voter study: 2018 voters who skipped 2022 had favored Democrats **64%–33%** in 2018. — [Pew Research Center, 2023](https://www.pewresearch.org/politics/2023/07/12/republican-gains-in-2022-midterms-driven-mostly-by-turnout-advantage/)

**Experimental evidence**
- Rise/BallotReady 2022 youth GOTV: people who voted in 2020 but not the 2018 midterm "seemed particularly responsive" to follow-up contact. The authors later corrected that the gain was **not statistically significant**. — [State of the Student Vote (Substack)](https://stateofthestudentvote.substack.com/p/in-gotv-conversations-follow-up-moves)
- Arceneaux & Nickerson imply low-propensity voters are mobilizable only in high-turnout elections, which a contested 2026 governor race should be. — [ISPS abstract](https://isps.yale.edu/research/publications/isps09-030)
- Caution: propensity scores built from vote history can mislead for newly registered voters and other groups with thin history. — [Sister District / States Win postcard white paper](https://stateswin.org/wp-content/uploads/2021/11/Postcard-Postmark-Whitepaper.pdf)

### Inferences
- **Priority order for a high-salience midterm:**
  1. Midterm drop-off voters (voted in the 2024 and/or 2020 November general, not the 2022 November general).
  2. "Occasional" voters (1–2 of the last 4 generals).
  3. Registrants new since 2022 with presidential-only history. New move-ins to a growing district skew toward young families, a likely-yes group.
  4. High-propensity voters (voted 2022 general *and* 2018 and/or recent spring elections) are last for a knock. They need at most a hanger or nothing.
- **Partisan lean of drop-off voters is probably favorable.** In MCPASD, presidential-only voters are disproportionately younger and lean Democratic. That correlates with yes on school funding in Dane County, but the correlation is unmeasured here.
- **Never-voters with no history in 4+ years** are low-yield, because contact rates are poor and they may have moved. Skip them unless the household also holds a priority voter.

### Gaps
- No randomized experiment was found that isolates presidential-only voters as the treatment group in a midterm canvass.
- MCPASD-specific 2022 vs. 2024 turnout (district boundary) was not found. Ward-level data would let the co-chair size the drop-off pool in her actual turf.
- Certified 2024 WEC totals were not retrieved; figures above are AP/unofficial.

---

## 3. Household spillover and multi-voter households

### Takeaway
A face-to-face GOTV contact spreads to housemates: about 60% of the effect on the person at the door carries over to the other voter in the home. Spillover across *different* households appears negligible. Knocking a door with two or more target voters is worth meaningfully more than a single-voter door. Neighbors do not get mobilized by proxy.

### Cited Findings
**Nickerson (2008), APSR 102(1):49–57, "Is Voting Contagious?"**
- Design: canvassers visited households with **exactly two registered voters** before the **September 2002 congressional primaries in Denver and Minneapolis**. Whoever answered got either a GOTV pitch or a recycling placebo. — [Cambridge abstract](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/is-voting-contagious-evidence-from-two-field-experiments/8C2E64552D946C87FD062DD2CCD9054E); [author PDF](https://sites.temple.edu/nickerson/files/2017/07/nickerson.contagion.pdf)
- Effect on the person who answered: **+9.8 points**. Effect on the housemate who did not answer: **+6.0 points**. The ratio is about **61%**; the abstract rounds to "60% of the propensity to vote is passed onto the other member of the household." — [summary by Adam Brown](https://adambrown.info/p/notes/nickerson_is_voting_contagious_evidence_from_two_field_experiments); [IDEAS/RePEc](https://ideas.repec.org/a/cup/apsrev/v102y2008i01p49-57_08.html)
- Context: this was a low-salience primary. Mann & Haenschen suggest effects shrink in high-salience elections (Section 1).

**Sinclair, McConnell & Green (2012), AJPS 56(4):1055–1069, "Detecting Spillover Effects"**
- Multilevel design: about 70,000 people in a **2009 Chicago special election**, social-pressure mailings. Neighborhoods were randomized to four saturation levels, then households within them. — [ISPS](https://isps.yale.edu/research/publications/isps12-025)
- Secondhand summary of results: positive total effects on turnout, "some evidence of within-household effects, but **no evidence of spillover across households**." The exact numbers were not retrieved. — [secondary review via search; ISPS listing](https://isps.yale.edu/research/publications/isps12-025)

**Foos & de Rooij (2017), AJPS 61(2):289–304, "All in the Family"**
- UK randomized spillover experiment. Within-household mobilization effects were **larger in politically heterogeneous households** (members backing rival parties) than in homogeneous ones, and grew with a more partisan message. The authors attribute this to discussion rather than mere contagion. — [AJPS author summary](https://ajps.org/2016/09/08/all-in-the-family/); [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/101419)

### Inferences
- **Value per door scales with the number of target voters inside.** One contact yields the direct effect on the person at the door plus about 0.6× that effect on each other voter in the home, using Nickerson's two-voter ratio; it is unknown whether it holds for 3+ voters.
  - A door with two drop-off/occasional voters ≈ **1.6×** the yield of a door with one.
  - A door whose only voters are high-propensity yields little regardless of household size.
- **Sort "knock first" by the count of priority voters per household.** In VAN, "household" views or a household-level count serve this purpose.
- **Mixed-support households are a real risk.** Foos & de Rooij found spillover strongest in politically divided homes. A GOTV knock at a home with one likely-yes and one likely-no voter could mobilize the no voter too. A referendum-specific GOTV message ("vote yes on the school question") makes this more likely than a generic "please vote" message. For mixed households, prefer a yes-message hanger, or skip if the no voter is clearly identified.
- **No neighborhood "halo."** Given the absent cross-household spillover in Sinclair et al., knocking non-list neighbors will not mobilize list voters indirectly. Non-list doors must justify themselves on their own net-vote math (Section 4).

### Gaps
- Sinclair et al. exact within-household estimates and CIs were not retrieved.
- No evidence was found on spillover magnitude in households with 3+ voters, or in high-salience November elections.
- No study of household spillover for ballot-measure *vote choice* (as opposed to turnout) was found.

---

## 4. Persuasion via canvassing, and whether to hit non-list neighbors (blanket vs. targeted)

### Takeaway
In candidate general elections, the best estimate of door-to-door persuasion is roughly zero, and there is documented backlash risk. Low-information ballot measures are more movable by information (Oregon voter-guide experiment), but tax framing reduces support. In a district that voted 63/37 in 2022, blanket GOTV yields only about a quarter of a net yes vote per extra voter. Targeted GOTV on 80%-likely-yes voters yields about 0.6. Non-list neighbors deserve at most a hanger, and only in clearly favorable areas.

### Cited Findings
**Persuasion in general elections**
- Kalla & Broockman (2018), APSR 112: in a meta-analysis of 40 prior field experiments plus 9 new ones, "the best estimate of the effects of campaign contact and advertising on Americans' candidate choices in general elections is **zero**." — [Cambridge](https://cambridge.org/core/journals/american-political-science-review/article/minimal-persuasive-effects-of-campaign-contact-in-general-elections-evidence-from-49-field-experiments/753665A313C4AB433DBF7110299B7433); [SSRN](https://papers.ssrn.com/abstract=3042867)
  - Exceptions in the abstract:
    - Candidates who take unusually unpopular positions, combined with campaigns that invest heavily in identifying persuadable voters. One summary puts that targeted effect at about 1.65 points.
    - Early contact measured immediately, which then decays. — [Cambridge](https://cambridge.org/core/journals/american-political-science-review/article/minimal-persuasive-effects-of-campaign-contact-in-general-elections-evidence-from-49-field-experiments/753665A313C4AB433DBF7110299B7433); [SSN key findings](https://scholars.org/sites/scholars/files/ssn-key-findings-kalla-and-broockman-on-what-campaigns-need-to-know-about-the-difficulty-of-persuading.pdf)
  - Secondhand: coverage says campaigning "significantly increases support for primary candidates and ballot measures," where there is no partisan cue. Not confirmed in the abstract; verify in the full text. — [Mother Jones coverage (search extract)](https://adops.motherjones.com/?p=519870)

**Backlash**
- Bailey, Hopkins & Rogers (2016), *Political Behavior* 38(3):713–746: field experiment on **56,000 Wisconsin voters** in the 2008 presidential race (canvass, phone, mail). Persuasive canvassing "possibly reduced candidate support and almost certainly did not increase it," and lowered survey response among infrequent voters. The authors conclude contact "may engender a backlash." — [HKS](https://www.hks.harvard.edu/publications/unresponsive-and-unpersuaded-unintended-consequences-voter-persuasion-efforts); [RePEc](https://ideas.repec.org/p/ecl/harjfk/rwp13-034.html)
- Panagopoulos et al. (2026, *Social Science Quarterly*): issue canvassing on campaign-finance reform in Broome County, NY; anti-reform canvassing "may have produced a backlash." — [EconPapers](https://econpapers.repec.org/RePEc:bla:socsci:v:107:y:2026:i:2:n:e70134)

**Ballot measures specifically**
- Rogers & Middleton (2015), *Political Behavior* 37(3):567–593: precinct-randomized experiment covering about 18% of Oregon households in 2008, testing a PAC's ballot-guide mail program.
  - The guides moved **how people voted, not whether they turned out**.
  - Treated precincts were more favorable to the campaign's position across 10–12 initiative races.
  - The campaign "may have even changed the final outcome in two of the contests." — [HKS WP](https://www.hks.harvard.edu/publications/are-ballot-initiative-outcomes-influenced-campaigns-independent-groups-precinct); [Harvard Crimson](https://thecrimson.com/article/2012/11/9/interest-groups-effect-ballot); [Todd Rogers page](https://toddrogers.scholars.harvard.edu/publications/are-ballot-initiative-outcomes-influenced-campaigns-independent-groups-0)
- Arceneaux (2005, *Annals* 601:169–179): precinct-randomized canvassing experiment in Kansas City, MO, framed as a methods paper. The ballot-measure vote-share results were not retrieved. — [ISPS](https://isps.yale.edu/research/publications/isps05-005)
- Brunner, Robbins & Simonsen (2021, *Public Administration Review*, survey experiment): adding property-tax information to school bond questions **lowered support 6–9 points**, depending on wording. Secondary summary. — [academic newsletter summary](https://academicnewsletter.sufe.edu.cn/info/421821)
- No field experiment canvassing specifically for a school levy, bond, or operating referendum was found. — (search null result)

### Inferences
**Net-vote arithmetic for GOTV.** If an extra voter has probability *s* of voting yes, the expected net yes votes from that voter = 2*s* − 1:

| Who the extra voter is | *s* | Net yes per extra voter |
|---|---|---|
| District average (2022 result) | 0.629 | **+0.26** |
| Likely supporter (support model ~0.8) | 0.8 | **+0.6** |
| Toss-up | 0.5 | 0 |
| Leans no | 0.4 | **−0.2** |

- Targeted GOTV on likely-yes voters is therefore about **2.3× as productive** per mobilized voter as blanket GOTV, before counting backlash.
- **The 2026 baseline may be closer than 62.9%.** The 2026 question is larger than a pure renewal (Section 6), so the effective *s* in mixed areas could be lower. That makes blanket mobilization of mixed precincts riskier.
- **Non-list neighbors:**
  - A neutral "vote on Nov 3" hanger in a 60/40 yes area nets ≈ 0.012 × 0.2 ≈ +0.002 votes per voter: positive but tiny.
  - An explicit "Vote YES" hanger to an unknown neighbor adds possible persuasion (Rogers & Middleton suggests information matters on low-salience measures) and possible backlash (Bailey/Hopkins/Rogers).
  - Rule: hang on non-list doors only in clearly favorable blocks, and only if time remains after list doors. Never knock non-list doors.
- **Message caution:** lead with "continues current funding" and outcomes, not with the tax number. This is consistent with Brunner et al.'s finding that tax information lowers support. It is a message point, not a targeting one.

### Gaps
- Kalla & Broockman's ballot-measure and primary sub-estimates were not verified.
- Effect sizes from Rogers & Middleton and from the Kansas City canvass were not retrieved.
- No school-referendum field experiment was found.
- Backlash magnitude for ballot-measure canvassing is unknown.

---

## 5. Dropping voters who already voted early: Wisconsin absentee data, VAN/MiniVAN refresh, Dane early-vote share

### Takeaway
Wisconsin publishes county-level absentee counts daily, and individual-level absentee status is available through Badger Voters and flows into VAN at a cadence the state party admin controls. In Dane County in 2022, about 37% of all ballots were cast before Election Day. During Oct 20–Nov 1, rebuild walk lists every 1–3 days to drop "voted" households, and confirm the DPW/VAN update schedule.

### Cited Findings
**WEC data**
- **Daily county report:** WEC releases a daily absentee report as an Excel file by county (requested, sent, returned). It is generated each morning (7:30 a.m. in 2024) from clerk data entry across about 1,850 municipalities, and posted on WEC's absentee statistics page. — [Civic Media, Sept. 2024](https://civicmedia.us/news/2024/09/25/the-wisconsin-elections-commission-has-started-releasing-its-daily-report-on-absentee-ballot-activity-for-the-november-5-general-election); [WEC absentee statistics page](https://elections.wi.gov/publications/statistics/absentee)
- **Individual-level data (Badger Voters):**
  - Fields include application date, application source, ballot type, and ballot status. — [WEC Absentee Data Request Data Elements (PDF)](https://BADGERVoters.wi.gov/img/Absentee%20Data%20Request%20Data%20Elements.pdf)
  - Pricing: **$25 base + $5 per 1,000 records, capped at $12,500**, with an absentee-data subscription option. — [Badger Voters FAQ](https://badgervoters.wi.gov/faq); [Wisconsin Watch, 2022](https://wisconsinwatch.org/2022/11/can-a-third-party-know-the-status-of-a-wisconsin-voters-absentee-ballot/)
  - "Any political party or individual" can buy ballot-status data. WEC told reporters it can be used to text or call voters about their ballot status. — [Gigafact](https://gigafact.org/fact-briefs/can-a-third-party-know-the-status-of-my-wisconsin-absentee-ballot/)
  - Wisconsin law places no restrictions on use of Badger Voters data, and confidential voters are excluded. — [Badger Voters FAQ](https://badgervoters.wi.gov/faq)

**2026 calendar and early counts**
- Absentee voting opened for Nov 3, 2026. As of Sept 18: **299,849 requested**, **4,309 returned** statewide. Early in-person absentee opens **Oct 20**; mail requests are due **Oct 29**; ballots must reach the clerk by poll close **Nov 3**. — [Wisconsin Examiner, Sept 18, 2026](https://wisconsinexaminer.com/2026/09/18/absentee-voting-opens-in-wisconsin/)
- The same search also returned an undated Examiner brief citing 1.7M requested and 1.4M returned. That appears to be from 2020; disregard for 2026. — [Wisconsin Examiner brief](https://wisconsinexaminer.com/brief/wisconsin-nears-absentee-request-deadline-ballots-shouldnt-be-mailed/)

**2022 early-vote share**
- **Dane County, Nov 7, 2022** (eve of the election): **110,836** absentee ballots returned, including **48,264** early in-person. City of Madison: 54,684 returned (23,222 in person) of 59,500 issued, against 184,250 registered. Dane in 2020: 254,335 absentee, of which 61,149 in person. — [Channel 3000](https://www.channel3000.com/more-than-110000-people-in-dane-co-have-already-voted-ahead-of-election-day)
- **Derived:** 110,836 / 302,459 = **36.6%** of Dane's 2022 ballots were cast before Election Day (in-person ≈ **16.0%**). Clerk entry lag means this is a slight undercount. — derived
- **Statewide 2022:** 719,429 absentee returned as of Nov 7, ≈ 27% of the 2,653,820 governor votes (derived). As of Oct 27: 545,483 requested and 353,929 returned, incl. 65,078 in person. — [Channel 3000](https://www.channel3000.com/more-than-110000-people-in-dane-co-have-already-voted-ahead-of-election-day); [WEC release via WisPolitics](https://www.wispolitics.com/2022/wisconsin-elections-commission-deadlines-fast-approaching-for-absentee-voters/)
- By mail specifically, 15.9% of WI 2022 ballots (EAC). — [Wisconsin Watch](https://wisconsinwatch.org/2024/01/election-voting-by-mail-us-wisconsin-turnout-fact-brief/)

**VAN / MiniVAN**
- NGP VAN's GOTV guide:
  - Absentee/early-vote data "is updated periodically by your admin," and update cadence varies by state; ask your admin.
  - Create-a-List and Virtual Phone Bank have checkboxes to **exclude anyone who has Early Voted or Absentee Voted**.
  - MiniVAN "automatically checks for people who have voted early or absentee and displays a 'Voted' icon" next to them. — [NGP VAN, "GOTV with MiniVAN" (Oct 2024)](https://ngpvan.com/wp-content/uploads/2024/10/GOTV-with-MiniVAN-OBP.pdf)
- In Virginia's VoteBuilder, list pulls exclude already-voted people by default unless unchecked. This is VA-specific; check WI behavior. — [VA Democrats VoteBuilder FAQ](https://votebuilder.vademocrats.org/votebuilder/absentee-voting-faq)
- Data availability varies by state. For example, NYC had no returned-ballot or early-voter data in VAN in 2021. — [NY Dems VAN support](https://support.nydems.org/support/solutions/articles/63000264482-6-12-2021-quick-van-gotev-gotv-updates)

### Inferences
- **Expect a large share of the list to vote early.** By GOTV weekend (Oct 31–Nov 2), likely **a third or more** of eventual MCPASD voters will already have voted, judging by Dane 2022's 36.6%. These skew high-propensity, the people already deprioritized. MCPASD's affluent suburbs may run higher; unverified.
- **Re-cut cadence:** re-pull lists with the Early Voted / Absentee Voted exclusions checked before each canvass block, at least every 2–3 days during Oct 20–Nov 1. Tell canvassers to skip any MiniVAN "Voted" icon. Expect a 1–3 day lag between someone voting in person and the flag appearing, given clerk entry and admin upload.
- **Ballot chase:** voters who *requested* a mail ballot but have not returned it are high-value. Give them a "return your ballot by 8 pm Nov 3; drop box or clerk, don't mail now" reminder instead of a standard GOTV pitch.
- **Data access:** if the co-chair's VAN is a party (DPW) or union instance, confirm its terms permit use for a nonpartisan referendum committee. Badger Voters is the legal, no-use-restriction fallback for absentee status at modest cost: ~$25 + $5/1,000 records, so about $36 for 2,102 records (derived).

### Gaps
- DPW/Dane Dems VoteBuilder absentee upload cadence for 2026 was not found; ask the VAN admin.
- Whether a MiniVAN list already downloaded to a phone drops voted people automatically, or only flags them, is not documented beyond the "Voted" icon.
- No MCPASD-specific early-vote share.
- WEC's final 2022 statewide in-person absentee total was not retrieved.

---

## 6. School-referendum-specific evidence on who supports referenda and whom to mobilize

### Takeaway
High-turnout November elections generally favor Wisconsin school referenda. Fall 2024 passage was 77.5% vs. 60.2% in the spring, and the Forum says passage "typically increase[s]" in high-turnout years. Low-turnout electorates skew older. Parents are a minority of school electorates. Older voters without children tend to be the least supportive. The 2026 MCPASD ask is bigger than the 2022 renewal, so the 62.9% baseline is not guaranteed.

### Cited Findings
**Election timing and electorate composition**
- Kogan, Lavertu & Peskowitz (2018), AJPS 62(3):637–651, "Election Timing, Electorate Composition, and Policy Outcomes": more than 10,000 school tax referenda matched to microtargeting data on actual participants.
  - Timing shifts electorate partisanship, ideology, and interest-group size, but effects on outcomes are "modest."
  - Timing matters most for **age**: "the elderly being the most overrepresented group in low-turnout special elections."
  - Effects vary by state. — [IDEAS/RePEc abstract](https://ideas.repec.org/a/wly/amposc/v62y2018i3p637-651.html)
- Kogan's related work (secondhand): voters with children are **20%–35%** of the electorate in the average school board election across 11 states. — [Ohio State News](https://news.osu.edu/why-parents-should-have-a-bigger-say-in-how-schools-are-run/)

**Wisconsin passage rates**
- 2024: a record **241** school referenda, **169** passed (70.1%), about 10 points below 2022. Fall **77.5%** vs. spring **60.2%**. Passage rates "typically increase amid the higher voter turnout of presidential and midterm election years." 2022 had 166 referenda and record operating-referendum approvals. — [Wisconsin Policy Forum](https://wispolicyforum.org/research/wisconsin-sets-more-referenda-records-to-fund-schools/)

**Age and household**
- Balsdon & Brunner (2003, UConn WP; California data): older voters without children mostly oppose higher *state* school spending, but are much more willing to back spending in their *own* district. Both housing-value capitalization and intergenerational altruism appear to matter. — [UConn working paper](https://media.economics.uconn.edu/working/2003-24.pdf)
- Anecdotal, from a WI district-survey consultant: "seniors will turn out at a much higher rate than younger folks on referendum votes." — [Waupaca Now (Clintonville survey)](https://waupacanow.com/?p=121037)

**The 2026 MCPASD question**
- **$118.5M over four years:** $24.9M in year 1, continuing the 2022 level, rising to $27.9M, $31.1M, and **$34.6M**. It is the second-largest November ask in the state, behind Green Bay. — [Wisconsin Examiner, Sept 21, 2026](https://wisconsinexaminer.com/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding/)
- WKOW: about **$237 over four years per $100,000** of property value. — [WKOW](https://www.wkow.com/news/middleton-cross-plains-school-district-asks-taxpayers-for-more-money-in-november-referendum/article_a1c6ba6d-441d-4075-bc4f-e46c4110d69e.html)
- 2022: the $24.9M non-recurring question passed 62.9% (14,592–8,606). — [Channel 3000](https://www.channel3000.com/news/politics/elections/middleton-cross-plains-area-school-district-referendum-passes/article_1d33d875-2226-504c-a797-f9ea84c6890a.html)

### Inferences
- **Mobilizing the "presidential-style" electorate helps the referendum.** In a November midterm, the extra voters GOTV can add are younger, more often parents or renters, and lean Democratic. In Dane County all three likely lean yes. The voters who show up anyway skew older, which is the group the literature finds least supportive. This aligns with Sections 1–2: knock drop-off and occasional voters, not super-voters.
- **Useful VAN proxy flags for "likely yes":**
  - Household with school-age children (if a modeled kids-in-household field exists).
  - Partisanship/support score.
  - Union/educator membership (WEAC lists).
  - Prior yes IDs from the 2022 campaign.
  - Age under ~55.
  - New registrant since 2022 in family-housing areas.
- **Likely-no flags:** older, long-tenure, no children, low partisanship score. These voters are best left alone for GOTV.
- Because the 2026 ask is a bigger increase, assume a tighter baseline than 63/37 when deciding whether mixed blocks get blanket coverage.

### Gaps
- Berkman & Plutzer (*Ten Thousand Democracies*, 2005; and work on long-tenured vs. newcomer elderly support) could not be retrieved. From background knowledge, long-time older residents are more supportive than newcomer retirees; **unverified, do not cite without checking**.
- The 2026 MCPASD community survey results (open through May 25, results to the board in June 2026) were not found. If available, they would give support by parent status and age.
- No MCPASD ward-level 2022 referendum results were retrieved; these would identify mixed vs. favorable blocks.
- No evidence was found on homeowner vs. renter referendum support specifically.

---

## 7. How support-score + turnout-score models are used to cut a "likely support, needs a nudge" universe, and how to sort the 2,102-door list

### Takeaway
Standard practice crosses a support (or partisanship) score with a turnout score. The **GOTV universe is high-support × low/mid-turnout**, high-support × high-turnout gets a light reminder, and low-support voters are excluded from GOTV. No public documentation of Catalist's or WEAC's specific cut points was found. For this list, combine that matrix with the high-salience finding (favor lower propensity), household counts, and early-vote exclusions.

### Cited Findings
- **Model basics:** scores are 0–1 probabilities; a group at 0.8 turnout should vote about 80% of the time. A partisan-elasticity score is used to build persuasion universes. — [Coefficient, "Voter Modeling"](https://coefficient.org/political/voter-modeling/)
- **The matrix:** campaigns cross high/low support with high/low turnout. Low-propensity supporters are where a GOTV universe "gets the most value per contact." High-propensity supporters need "little more than a reminder." — [CallHub GOTV canvassing guide](https://callhub.io/blog/canvassing/gotv-canvassing/); [DeckTools, "Deeper Look at Scores and Universes"](https://decktools.notion.site/Deeper-Look-at-Scores-and-Universes-69cf6731c74047b39ecec61c6f072bf7)
- **Vendor practice:** pair "high partisanship scores but low-to-mid turnout propensity scores" to find base voters who skip elections. — [The Campaign Workshop](https://www.thecampaignworkshop.com/blog/political-direct-mail/democratic-direct-mail-targeting)
- **Cut points by turnout band** (2014 Nunn campaign memo, Scribd upload; secondary): "if we are not winning among those who have an 80 percent plus chance of voting but are winning among those who have a 60-80 percent chance of voting... we can say how high the turnout needs to be to win." — [Scribd](https://www.scribd.com/doc/235287519/2014-Michelle-Nunn-Campaign-Memo)
- **Middle-propensity targeting** (40–60%) is supported by Foos's 122-experiment analysis (secondhand) and by the Arceneaux & Nickerson threshold model. — [Campaign Lab](https://campaignlab.uk/project/blog-the-truth-about-voter-turnout-what-can-we-actually-learn-from-over-100-voter-turnout-experiments/); [ISPS](https://isps.yale.edu/research/publications/isps09-030)
- **Turnout scores mislead for new registrants** and others with thin vote history. — [States Win white paper](https://stateswin.org/wp-content/uploads/2021/11/Postcard-Postmark-Whitepaper.pdf)

### Inferences
**Proposed sort for the 2,102-door list.** This is a synthesis of Sections 1–6. Thresholds are practitioner conventions, not empirically optimized.

**Step 0: daily exclusions.** Re-pull with "Early Voted" and "Absentee Voted" excluded. Skip any MiniVAN "Voted" icon. Move mail-ballot-requested-not-returned voters to a separate ballot-chase script.

**Step 1: tag each voter.**
- **Support:** use a support or partisanship score if available, or proxies: kids in household, prior yes ID, union/educator, age under ~55, Democratic partisanship.
  - Likely yes ≈ ≥65–70.
  - Unknown/mixed ≈ 40–65.
  - Likely no ≈ <40 (or ID'd no).
- **Propensity, using vote history** (more transparent than a modeled score for this audience):
  - **A, nudge:** voted Nov 2024 and/or Nov 2020, but NOT Nov 2022. Also: registered since 2022 with only presidential-general history.
  - **B, occasional:** voted in 1–2 of the last 4 November generals, including 2022.
  - **C, reliable:** voted Nov 2022 and Nov 2024, plus most of Nov 2018/2020 or recent April elections.
  - **D, dormant:** no vote in 4+ years.
- Turnout-score equivalents: A/B ≈ 25–75; C ≈ 80+; D ≈ <15.

**Step 2: household-level decision.** Count priority voters (likely-yes and A or B) per door.

| Bucket | Which doors | Why |
|---|---|---|
| **Knock first** | Doors with **≥2** likely-yes A/B voters, then doors with **1** likely-yes A/B voter | Highest net yield: 2*s* − 1 ≈ +0.4 to +0.6 per mobilized voter, plus ~60% housemate spillover |
| **Hang only** | Likely-yes **C-only** households; unknown-support A/B households in favorable blocks (block voted yes well above 63% in 2022 if ward data exist); non-list doors on the route in clearly favorable blocks, time permitting | Reliable voters gain little from a knock, but a hanger is cheap (≈1.2-pt hanger effect, 2002 MI). Unknown-support households and non-list doors are lower expected value |
| **Skip** | Already voted; likely-no voters; households whose priority voter shares the home with an ID'd/likely no voter (Foos & de Rooij spillover risk); D-only households (low contact, possibly moved); non-list doors in mixed blocks | Zero or negative expected net yes |

- **Mixed households (exception to Skip):** use a hanger with a "Yes for our schools" message aimed at the supporter if the race looks close.

**Step 3: timing.**
- Knock A/B doors early in the Oct 20–Nov 1 window to pull them into early voting.
- Re-cut so GOTV weekend (Oct 31–Nov 2) and Election Day focus only on not-yet-voted A/B likely-yes doors.
- Each re-cut drops a growing share; Dane 2022 had ~37% of ballots cast before Election Day.

**Rough expectations (derived).** Effect per contacted door = (effect on the person who answers) + 0.6 × (effect) × (other target voters in the home). Multiply by the contact rate, then by 2*s* − 1.

| Scenario | Effect per contact | Contact rate | Target voters per door | *s* | Extra voters per 1,000 doors | Net yes per 1,000 doors |
|---|---|---|---|---|---|---|
| Pessimistic | 3 pts | 25% | 1.3 | 0.7 | ~9 | ~3–4 |
| Optimistic | 4 pts | 40% | 2 | 0.8 | ~26 | ~15 |

So knocking 1,000 prioritized doors plausibly adds **~10–25 voters and ~4–15 net yes votes**. That decides only a very close race. The 2026 ask is bigger than 2022's, whose margin was 5,986 votes, which makes a close race more plausible than in 2022. This is an order-of-magnitude illustration: the actual contact rate and voters per door are unknown. The real value is efficiency: knocking likely-no or reliable-voter doors produces ~0 or negative net.

### Gaps
- No public documentation of **Catalist**, **WEAC/NEA**, or **union** support/turnout model names, scales, or recommended cut points was found. Ask the VAN admin which models exist in that instance (e.g., partisanship, turnout, kids-in-household, education-issue models) and their scales.
- Whether the co-chair's VAN has any issue-specific "education/school funding support" model is unknown.
- The support and turnout thresholds above are conventions, not empirically derived for school referenda.
- Contact rate, registered voters per door, and how many of the 2,102 doors hold A/B voters are unknown until the list is pulled.
