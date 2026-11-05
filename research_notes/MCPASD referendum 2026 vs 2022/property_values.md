# Property values, assessments and school taxes by MCPASD municipality, 2022 to 2026, and whether they line up with the 2026 No vote

Labels used below:
- **[primary]**: a document or data file I downloaded and read (DOR PDF or Excel, Zillow CSV, news page text, municipal PDF).
- **[secondhand]**: known only from a search-engine summary or from an earlier research note whose page I could not reopen.
- All arithmetic was done in Python on the cited figures (scripts kept outside the download folders). The comparison table is saved as `property_values_comparison.csv` in this folder.

Access notes (for the report writer): revenue.wi.gov, files.zillowstatic.com, treasurer.danecounty.gov, accessdane.danecounty.gov, cityofmiddleton.us (most pages), wkow.com, channel3000.com, wmtv15news.com, captimes.com, civicmedia.us and badgerhomeowner.com all worked through curl. **Blocked or failed:** web.archive.org (connection reset, so no archived copies of old DOR reports or of the district's referendum page); perry-wi.gov (connection reset); cityofmiddleton.us/m/faq (connection reset); cityofmiddleton.us CivicSend messages 274491 and 297551 (404); api.census.gov (now redirects to a "missing key" page, so no ACS pull); mcpasd.k12.wi.us not tried, per instructions (JS challenge). DOR keeps only the last three years of its municipal equalized-value reports online, so **no 2022 municipal-level DOR file could be retrieved** (2022 and 2023 versions of the school certification, the Statement of Changes, the county apportionment and the Town, Village and City Taxes bulletin all returned 404).

## Q1. How much did equalized value rise, 2022 to 2026, in each municipality and in its MCPASD portion?

### Takeaway
District-wide, MCPASD's TID-out equalized value rose **42.4%**, from $9.17B (2022) to **$13.06B (2026)**. For the municipal MCPASD portions, the earliest DOR file still online is 2024. From 2024 to 2026, growth ranged from **+4.0% in the Town of Berry to +24.4% in the City of Middleton**. About half of the district's 2025-to-2026 jump (+11.3%) came from a **City of Middleton tax-increment district (TID) closing**, which returned about $654M of value to the tax base. It did not come from homes appreciating. DOR *cut* the 2026 values of the Towns of Springfield (−4.3%) and Berry (−5.1%).

### Cited Findings
- **MCPASD portion of each municipality, TID-out equalized value [primary]** (DOR, *Fall School District Certification of Values*, report dated Sept. 21, 2026 for 2026; 2024 and 2025 editions):

  | Municipality (MCPASD part) | 2024 | 2025 | 2026 | 2024→2026 | 2025→2026 | Share of district 2025 → 2026 |
  |---|---|---|---|---|---|---|
  | City of Middleton | $4,477.5M | $4,617.0M | $5,568.7M | **+24.4%** | +20.6% | 39.36% → **42.64%** |
  | City of Madison | $2,532.3M | $2,772.4M | $2,871.3M | +13.4% | +3.6% | 23.64% → 21.98% |
  | Town of Middleton | $2,149.4M | $2,293.9M | $2,521.8M | +17.3% | +9.9% | 19.56% → 19.31% |
  | Village of Cross Plains | $563.7M | $639.3M | $685.7M | +21.6% | +7.3% | 5.45% → 5.25% |
  | Town of Springfield | $558.7M | $665.7M | $637.0M | +14.0% | **−4.3%** | 5.68% → 4.88% |
  | Town of Westport | $326.8M | $350.5M | $384.5M | +17.7% | +9.7% | 2.99% → 2.94% |
  | Town of Cross Plains | $189.4M | $213.0M | $222.9M | +17.7% | +4.7% | 1.82% → 1.71% |
  | Town of Berry | $162.3M | $177.9M | $168.8M | +4.0% | **−5.1%** | 1.52% → 1.29% |
  | **District total** | **$10,960.1M** | **$11,729.7M** | **$13,060.6M** | **+19.2%** | **+11.3%** | 100% |

  Sources: [DOR 2026 certification](https://www.revenue.wi.gov/SLFReportsschoolspec/2026sche.pdf); [2025](https://www.revenue.wi.gov/SLFReportsschoolspec/2025sche.pdf); [2024](https://www.revenue.wi.gov/SLFReportsschoolspec/2024sche.pdf); [DOR landing page](https://www.revenue.wi.gov/Pages/Report/fall-school-district-certification.aspx). The 2024 and 2025 district totals match DPI's 2024-25 and 2025-26 equalized values exactly — [DPI 2025-26](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2026).
- **2022 district baseline [primary]:** MCPASD TID-out equalized value was $9,174,128,987 for the 2022 tax year (2022-23 school year) — [DPI FY2022-23](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2023). Growth to 2026 is **+42.4%** (my arithmetic).
- **The City of Middleton TID closure [primary]:**
  - In 2025 the City's MCPASD portion was $5,575.3M with TIDs counted (TID-in) and $4,617.0M without them (TID-out), a $958.3M gap. In 2026 the gap was $304.1M — [DOR 2025](https://www.revenue.wi.gov/SLFReportsschoolspec/2025sche.pdf); [DOR 2026](https://www.revenue.wi.gov/SLFReportsschoolspec/2026sche.pdf).
  - DOR's 2026 county apportionment lists only one City of Middleton TID, No. 005 (created 2009), with a $304,082,400 increment — [DOR 2026 county apportionment](https://www.revenue.wi.gov/SLFReportsassessor/2026coapprt.PDF). DOR's Town, Village and City Taxes data showed two City TIDs in 2024 and 2025 — [TVC 2024](https://www.revenue.wi.gov/SLFReportscotvc/tvc24.xlsx); [TVC 2025](https://www.revenue.wi.gov/SLFReportscotvc/tvc25.xlsx).
  - The Town of Springfield's one TID (an $11.9M increment in 2025) also no longer appears in 2026 — [DOR 2025](https://www.revenue.wi.gov/SLFReportsschoolspec/2025sche.pdf); [DOR 2026](https://www.revenue.wi.gov/SLFReportsschoolspec/2026sche.pdf).
- **Whole-municipality real-estate equalized value, 2023 → 2026 [primary]** (DOR *Statement of Changes in Equalized Values by Class and Item*; 2023 is the prior-year column of the 2024 edition):

  | Municipality (whole) | Residential 2023 | Residential 2026 | Change | All real estate, 2023→2026 |
  |---|---|---|---|---|
  | City of Middleton | $2,879.2M | $3,532.4M | +22.7% | +23.1% |
  | City of Madison | $26,032.0M | $31,926.4M | +22.6% | +26.4% |
  | Town of Middleton | $1,881.2M | $2,420.0M | +28.6% | +27.6% |
  | Village of Cross Plains | $450.5M | $624.1M | **+38.5%** | +39.1% |
  | Town of Springfield | $559.7M | $711.1M | +27.0% | +21.7% |
  | Town of Westport | $1,307.4M | $1,624.2M | +24.2% | +24.3% |
  | Town of Cross Plains | $321.8M | $421.0M | +30.8% | +30.4% |
  | Town of Berry | $226.9M | $304.9M | +34.4% | +34.3% |

  Sources: [DOR SOC Dane 2024](https://www.revenue.wi.gov/SLFReportsassessor/2024socdane.PDF); [2025](https://www.revenue.wi.gov/SLFReportsassessor/2025socdane.PDF); [2026, dated Aug. 11, 2026](https://www.revenue.wi.gov/SLFReportsassessor/2026socdane.PDF). These figures include new construction and "all other changes." Berry's 2024 residential line, for example, carries a +16% "all other changes" entry on top of a +13% economic change.
- **2026 whole-municipality TID-out values used to apportion the county levy [primary]:**
  - City of Middleton $5,810.4M (all school districts)
  - Town of Middleton $2,548.0M
  - Town of Westport $1,787.4M
  - Town of Springfield $856.3M
  - Village of Cross Plains $685.7M
  - Town of Cross Plains $501.4M
  - Town of Berry $372.7M
  - City of Madison $49,866.6M

  Source: [DOR 2026 county apportionment](https://www.revenue.wi.gov/SLFReportsassessor/2026coapprt.PDF)

### Inferences
- Excluding the two TID closures (about $654M in the City and $12M in Springfield), district equalized value grew about **5.7%** from 2025 to 2026, not 11.3% (my arithmetic). A closed TID's value joins the base of every taxing body, so it **lowers the school mill rate for every MCPASD taxpayer**, not only in the City. The City's larger share of the levy (39.4% → 42.6%) falls mostly on the formerly TIF-captured, largely commercial parcels, not on existing City homes.
- Springfield's and Berry's 2026 declines mean that, for a given 2026-27 levy, those towns' aggregate MCPASD school tax on the December 2026 bills will fall relative to the rest of the district. Their shares drop 14% and 15% (my arithmetic). DOR's figures came out in August and September 2026, before the vote, but voters would not see them on a bill until after it.
- The split towns' MCPASD portions moved differently from the towns as a whole. Berry's MCPASD part grew only 4.0% from 2024 to 2026, while the whole town's residential value grew faster. Whole-town DOR measures are therefore only a proxy for the slices that vote on MCPASD questions.

### Gaps
- **2022 municipal and MCPASD-portion equalized values were not retrievable.** DOR has removed the 2022 and 2023 editions of every municipal report, and the Wayback Machine was unreachable. Municipal-level comparisons therefore start in 2023 (whole municipality) or 2024 (MCPASD portion). The MCPASD budget book, which normally lists each municipality's equalized value and levy share, is on the blocked district site.
- I could not confirm the number or name of the closed City of Middleton TID, or its closure date, from a City document. The ~$654M figure is inferred from DOR's TID-in/TID-out gaps.

## Q2. Assessed values, assessment ratios, and when each municipality revalued

### Takeaway
Through 2025, three municipalities had drifted well below market. The City of Middleton (**0.78**), the Village of Cross Plains (**0.65**) and the Town of Berry (**0.67**) were all outside DOR's 0.90–1.10 band. The Towns of Springfield, Westport and Middleton revalued for 2025, the Town of Cross Plains for 2024, and the City of Middleton for 2026. Madison assesses at market every year. The City's 2026 revaluation alone raised the *number* on a typical notice by about 28% (1 ÷ 0.7827), before any market change. That is consistent with the City's reported ~32% rise in total assessed value.

### Cited Findings
- **DOR assessment levels (assessed ÷ equalized, whole municipality) [primary]:**

  | Municipality | 2023 | 2024 | 2025 | Revaluation evidence |
  |---|---|---|---|---|
  | City of Middleton | 0.89 | 0.80 | 0.78 (0.7827) | Citywide revaluation to 100% for 2026 |
  | City of Madison | 0.99 | 0.99 | 0.97 | Annual market-level assessment |
  | Town of Middleton | 0.78 | 0.73 | 0.97 (0.9659) | Jump implies a 2025 revaluation; another revaluation for 2026 (notices April 2026) |
  | Village of Cross Plains | 0.81 | 0.72 | **0.65 (0.6528)** | No revaluation through 2025; 2026 roll valued July 22, 2026, Open Book Aug. 3, 2026 |
  | Town of Springfield | 0.63 | 0.58 | 0.94 (0.9449) | Jump implies a 2025 revaluation |
  | Town of Westport | 0.72 | 0.71 | 0.98 (0.9795) | Jump implies a 2025 revaluation |
  | Town of Cross Plains | 0.66 | 1.01 | 0.93 (0.9336) | Jump implies a 2024 revaluation |
  | Town of Berry | 0.91 | 0.73 | **0.67 (0.6662)** | No revaluation 2024–2025 |

  Sources: [DOR TVC 2023 data](https://www.revenue.wi.gov/SLFReportscotvc/tvc23.xlsx), [2024](https://www.revenue.wi.gov/SLFReportscotvc/tvc24.xlsx), [2025](https://www.revenue.wi.gov/SLFReportscotvc/tvc25.xlsx) (column "Assm't Level"); four-decimal 2025 ratios from [Dane County Treasurer, Mill Rates for the 2025 Tax Year](https://treasurer.danecounty.gov/documents/pdf/CurrentYear-DaneCountyMillRatesByDistrict-NOT-C-Madison.pdf).
- **City of Middleton revaluation [primary]:** the City "contracted with Associated Appraisal Consultants (AAC) to perform a revaluation of all property for the 2026 assessment cycle. The purpose of the revaluation is to bring all assessed values to 100% market value." It adds: "Wisconsin laws require periodic market updates to keep assessment levels at or very near actual market values." The PDF was created Oct. 29, 2025 — [City of Middleton Revaluation Overview](https://www.cityofmiddleton.us/DocumentCenter/View/20472/Middleton-Revaluation-Overview). The City's Assessor page now lists AAC office hours for revaluation questions — [City of Middleton Assessor](https://cityofmiddleton.us/94/Assessor).
- **City notice and Board of Review [secondhand]:** total assessed value rose about 32%. The notice says revaluation "redistributes how the tax levy is shared among properties; it does not, by itself, generate additional tax revenue." Board of Review was Sept. 22, 2026 — [City of Middleton message (now 404)](https://cityofmiddleton.us/CivicSend/ViewMessage/message/297551), as recorded in `tax_messaging.md`. A City commercial parcel on AccessDane shows a 2026 valuation date of **09/21/2026** and a 2025 ratio of 0.7827 [primary] — [AccessDane parcel 255/0708-034-5420-2](https://accessdane.danecounty.gov/070803454202).
- **Town of Middleton [secondhand, from earlier note]:** "The Town Assessor has completed a revaluation of the Town … new assessment notices will be mailed out the week of April 14th." Open Book was April 23 and Board of Review May 12, 2026 — [Town of Middleton Spring 2026 newsletter](https://middletonwi.govoffice3.com/vertical/Sites/%7B97A50AAB-3824-4833-ACEA-EF2B9A14C856%7D/uploads/Spring_2026_website.pdf).
- **Village of Cross Plains 2026 roll [primary]:** a Village parcel on AccessDane shows a 2026 valuation date of 07/22/2026 and Open Book starting **08/03/2026** — [AccessDane parcel 113/0707-021-9001-1](https://accessdane.danecounty.gov/070702190011). A search summary also mentions a Sept. 16, 2026 Board of Review on another Village parcel [secondhand].
- **Town of Cross Plains [secondhand]:** a 2026 Open Book notice lists an in-person session on June 1, 2026 — [Town of Cross Plains notice](https://townofcrossplains.org/images/uploads/docs/event_1925_28561.pdf) (search summary only).
- **DOR's compliance rule [primary]:** "State law requires average assessment ratios to be within 10% of market value, that is, between 90% and 110% once every five years." — [DOR, 2026 Guide for Property Owners (PB-060)](https://www.revenue.wi.gov/pubs/slf/pb060.pdf)
- **Ratios change what the school line on the bill looks like [primary]:** In 2025, the MCPASD mill rate per $1,000 of *assessed* value ranged from **8.88 (Westport) and 8.93 (Town of Middleton) to 11.06 (City of Middleton), 12.94 (Berry) and 13.25 (Village of Cross Plains)**. Multiplied by each assessment ratio, every one converts to **8.58–8.70 per $1,000 of market value** (my arithmetic). That matches DPI's 8.62 district equalized rate — [Dane County Treasurer 2025](https://treasurer.danecounty.gov/documents/pdf/CurrentYear-DaneCountyMillRatesByDistrict-NOT-C-Madison.pdf); [DPI 2025-26](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2026).

### Inferences
- For a City of Middleton home, moving from a 0.7827 ratio to 1.00 multiplies the assessed number by 1.278 with no change in market value. DOR's 2026 City residential economic change of +4% (Q3) brings that to about **1.33**. That is consistent with the reported ~32% total assessed increase (my arithmetic).
- The Village of Cross Plains (0.65) and Berry (0.67) entered 2026 with the lowest ratios in the district. Any 2026 revaluation there would produce notice jumps of 50% or more for unchanged market values. The Village's late (July/August) 2026 roll fits a revaluation but does not prove one.
- Assessment ratios do **not** change any municipality's share of the MCPASD levy, which DOR apportions on equalized value (Q7). They change only the assessed number and the per-assessed-dollar rate printed on the bill.

### Gaps
- 2022 assessment ratios, and 2026 ratios for every municipality, were not found. Dane County posts only the current year's mill-rate sheet, and the 2026 sheet will not exist until December 2026. A Town of Perry copy of the 2022 sheet exists, but perry-wi.gov reset the connection.
- I did not confirm from a Village or Town document whether the Village of Cross Plains, the Town of Berry or the Town of Cross Plains revalued for 2026, or the exact years of the earlier Town revaluations. Those years are inferred from DOR ratio jumps.
- The City's 2026 assessment notice text is known only secondhand. The page now returns 404.

## Q3. Typical/median home value change

### Takeaway
Typical home values rose about **23–26% from January 2022 to January 2026** across the district's ZIPs and places, by Zillow's mid-tier index. The City of Middleton went from about $485K to $610K (+25.8%) and the Village of Cross Plains from $410K to $504K (+23.0%). Growth has been slow since January 2025 (+2–3%). DOR's municipal residential "economic change" estimates (2023 to 2026) separate the towns more sharply. They range from +14.5% (Westport) and +15.5% (Berry) to +28.1% in the **Village of Cross Plains, the fastest-appreciating unit**. The City of Middleton, at +17.8%, was the slowest of the four large units.

### Cited Findings
- **Zillow Home Value Index (mid-tier single-family and condo, smoothed, seasonally adjusted), January values [primary]:**

  | Geography | Jan 2022 | Jan 2023 | Jan 2024 | Jan 2025 | Jan 2026 | Sept 2026 | Jan 2022→Jan 2026 |
  |---|---|---|---|---|---|---|---|
  | Middleton (city) | $485,044 | $528,597 | $564,057 | $596,971 | $610,366 | $614,311 | **+25.8%** |
  | Cross Plains (village) | $409,626 | $440,415 | $461,532 | $489,768 | $504,024 | $510,868 | **+23.0%** |
  | Madison (city) | $335,606 | $364,276 | $387,381 | $410,837 | $420,158 | $424,543 | +25.2% |
  | ZIP 53562 (Middleton city and town) | $489,226 | $534,865 | $569,504 | $603,079 | $616,377 | $620,703 | +26.0% |
  | ZIP 53528 (Cross Plains; parts of Town of Cross Plains and Berry) | $423,391 | $456,823 | $478,938 | $509,587 | $528,408 | $536,986 | +24.8% |
  | ZIP 53717 (west Madison) | $398,140 | $435,900 | $463,790 | $488,616 | $499,591 | $511,481 | +25.5% |
  | ZIP 53719 (southwest Madison) | $343,797 | $371,746 | $392,862 | $417,107 | $426,010 | $428,179 | +23.9% |
  | ZIP 53597 (Waunakee; parts of Springfield and Westport) | $473,467 | $515,311 | $538,977 | $574,911 | $591,168 | $596,803 | +24.9% |
  | ZIP 53515 (Black Earth; part of Berry) | $350,360 | $380,967 | $394,808 | $422,141 | $431,625 | $441,303 | +23.2% |
  | ZIP 53529 (Dane; parts of Springfield and Berry) | $384,339 | $424,158 | $453,128 | $484,807 | $500,645 | $506,474 | +30.3% |

  Sources: [Zillow ZHVI by ZIP](https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv); [Zillow ZHVI by city](https://files.zillowstatic.com/research/public_csvs/zhvi/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv) (files last modified Oct. 16, 2026; data through Sept. 30, 2026). Zillow publishes no town-level series.
- **DOR residential "economic change" (market appreciation, excluding new construction), by municipality and year [primary]:**

  | Municipality (whole) | 2024 | 2025 | 2026 | Cumulative 2023→2026 |
  |---|---|---|---|---|
  | Village of Cross Plains | +13.0% | +10.0% | +3.0% | **+28.1%** |
  | Town of Cross Plains | +12.0% | +8.0% | +4.0% | +25.8% |
  | Town of Springfield | +8.0% | **+17.9%** | −2.0% | +24.7% |
  | Town of Middleton | +7.0% | +5.0% | +8.0% | +21.3% |
  | City of Madison | +8.0% | +7.0% | +4.0% | +20.2% |
  | City of Middleton | +10.0% | +3.0% | +4.0% | +17.8% |
  | Town of Berry | +12.7% | +9.0% | **−6.0%** | +15.5% |
  | Town of Westport | 0.0% | +5.0% | +9.0% | +14.5% |

  Sources: [DOR SOC Dane 2024](https://www.revenue.wi.gov/SLFReportsassessor/2024socdane.PDF), [2025](https://www.revenue.wi.gov/SLFReportsassessor/2025socdane.PDF), [2026](https://www.revenue.wi.gov/SLFReportsassessor/2026socdane.PDF) (residential "Economic Change" ÷ prior-year residential value; cumulative is my compounding).
- A home-assessment marketing site shows a "sample" Middleton alert: "Up 31% in 2026 from $467,900. The median Middleton home rose 32%." It is an illustration, not reporting — [BadgerHomeowner](https://www.badgerhomeowner.com/school-referendums-dane-county/).

### Inferences
- Zillow and DOR agree on the broad pattern of 20–28% gains since 2022–23 that flattened in 2025–26. They disagree on small towns, where DOR's year-to-year estimates swing on few sales: Springfield went +17.9% then −2.0%, Berry +12.7% then −6.0%, and Westport 0% then +9%. Treat single-year town figures with caution.
- On DOR's measure, the City of Middleton's homes appreciated *less* than the district's other large units in 2023–26. The 2026 revaluation notices nonetheless showed City owners roughly +33% (Q2), several times their real appreciation over the prior year.

### Gaps
- ACS median values (B25077) by town were not pulled: the Census API now requires a key. Redfin data were not tried, for time.
- No assessor-published median or average home assessment was found for any municipality for 2022 or 2026.
- ZIP-to-town matching is coarse. ZIP 53562 mixes the City and Town of Middleton, and the MCPASD slices of Springfield, Berry and Westport sit in shared ZIPs.

## Q4. School-tax change on a typical home, 2022 to 2025 (and what 2026 can show)

### Takeaway
At the uniform district equalized rate, a typical home's gross MCPASD school tax rose about **$580–$860 (16–20%)** from the 2022 bill to the 2025 bill, using Zillow values. The 2025 bill, paid in 2026, was the last one voters saw before Nov. 3. Measured with DOR's municipal appreciation instead (2023 to 2025 bills), the increase ranged from **+7.7% in Westport and +15–16% in the City and Town of Middleton to +24–31% in the Town of Cross Plains, Berry, the Village of Cross Plains and Springfield**. Each municipality's aggregate MCPASD school tax rose between **+6.9% (City of Middleton) and +23.5% (Springfield)** from the 2024 to the 2025 bills. 2026 bills will not exist until December 2026. The 2026-27 levy was not found.

### Cited Findings
- **District equalized school rates (levy ÷ TID-out value) [primary]:**
  - 2022 tax year: 8.886 per $1,000
  - 2023: 8.411
  - 2024: 8.317
  - 2025: 8.624

  Sources: [DPI FY2022-23](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2023); [FY2023-24](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2024); [FY2024-25](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2025); [FY2025-26](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2026)
- **Each municipality's MCPASD school tax (levy apportioned to it), 2024 → 2025 tax year [primary]:**
  - Springfield: $4.65M → $5.74M (**+23.5%**)
  - Village of Cross Plains: $4.69M → $5.51M (+17.6%)
  - Town of Cross Plains: $1.58M → $1.84M (+16.6%)
  - Berry: $1.35M → $1.53M (+13.6%)
  - Madison portion: $21.06M → $23.91M (+13.5%)
  - Westport: $2.72M → $3.02M (+11.2%)
  - Town of Middleton: $17.88M → $19.78M (+10.7%)
  - City of Middleton: $37.24M → $39.81M (**+6.9%**)
  - District levy: +11.0%

  Source: [DOR TVC 2024, "School District Data"](https://www.revenue.wi.gov/SLFReportscotvc/tvc24.xlsx); [TVC 2025](https://www.revenue.wi.gov/SLFReportscotvc/tvc25.xlsx)
- **2025 MCPASD rates as printed per assessed dollar** (City of Middleton 0.011059306 at ratio 0.7827, and others) are in Q2 — [Dane County Treasurer 2025](https://treasurer.danecounty.gov/documents/pdf/CurrentYear-DaneCountyMillRatesByDistrict-NOT-C-Madison.pdf)
- The 2026-27 MCPASD levy and rate were not on DPI's FY2026-27 page when last checked, Nov. 5, 2026 (per `tax_messaging.md`) — [DPI FY2026-27](https://sfs.dpi.wi.gov/safr_ro/all_mill_rate.asp?year=2027). A search for October 2026 levy coverage found nothing.

### Inferences
- **Typical-home gross school tax (Zillow January value × district rate; before state credits; assumes the home is assessed at its municipality's average ratio):**

  | Geography (proxy) | 2022 bill | 2025 bill | Change |
  |---|---|---|---|
  | City of Middleton (Zillow city) | $4,310 | $5,148 | +$838 (+19.4%) |
  | ZIP 53562 (Town of Middleton; Westport and Springfield proxy) | $4,347 | $5,201 | +$854 (+19.6%) |
  | ZIP 53717 (Madison wards) | $3,538 | $4,214 | +$676 (+19.1%) |
  | ZIP 53528 (Town of Cross Plains and Berry proxy) | $3,762 | $4,394 | +$632 (+16.8%) |
  | Village of Cross Plains (Zillow) | $3,640 | $4,224 | +$584 (+16.0%) |

- **Typical-home school tax, 2023 → 2025 bills, using DOR residential appreciation in each municipality:**
  - Springfield +30.5%
  - Village of Cross Plains +27.5%
  - Berry +26.0%
  - Town of Cross Plains +24.0%
  - Madison +18.5%
  - City of Middleton +16.2%
  - Town of Middleton +15.2%
  - Westport +7.7%

  This uses the rate ratio 8.624/8.411 times the 2024 and 2025 economic changes (my arithmetic).
- **2026 (Dec. 2026 bills), illustration only:** if the 2026-27 levy stayed at $101.15M, the equalized rate would fall to about **7.75** on the $13.06B base, and to about 8.36 with an 8% levy increase (my arithmetic). Because of the TID closure, a levy increase of up to about 11% would not raise the rate.

### Gaps
- No actual 2022–2025 tax bills for a named typical home were retrieved. AccessDane has parcel-level bills, but I found no defensible "typical" parcel.
- The 2026-27 levy, rate and bills are not yet public. The state school levy tax credit and lottery credit were left out (gross figures only).

## Q5. Comparison table: did the areas that voted No, or added the most No votes, see bigger value or tax increases?

### Takeaway
**Not consistently.** Faster school-tax growth lines up loosely with *Yes-share erosion* in the small rural units: Springfield, Berry, the Town of Cross Plains and the Village. Those places saw the fastest 2023–25 home school-tax growth and some of the largest Yes drops. But **most of the 849 new No votes came from the City of Middleton and the Madison wards, where school taxes on a typical home grew at or below the district rate.** The City of Middleton had the *slowest* aggregate school-tax growth (+6.9%) and the slowest appreciation of the large units. The one place where everything lines up is the **Village of Cross Plains**. Fast appreciation, a 0.65 assessment ratio (the highest printed school rate in the district), the second-fastest tax growth and a 22% jump in No votes all coincide there. In the City, the likely tax trigger was the **revaluation notice** (about +33% on paper), not the bill.

### Cited Findings
- **Comparison table** (vote figures are from `ward_change.csv` and the final report; all other columns are from Q1–Q4 sources):

  | Municipality (MCPASD part) | 2026 Yes % | Δ Yes pts | Δ No votes (%) | MCPASD-portion EQ value 2024→26 | Residential EQ value (whole muni) 2023→26 | DOR home appreciation 2023→26 | Zillow typical home Jan 2022→Jan 2026 (proxy) | Muni's MCPASD school tax, 2024→25 bills | Typical-home school tax 2023→25 (DOR index) | Ratio 2025 / revaluation |
  |---|---|---|---|---|---|---|---|---|---|---|
  | City of Middleton | 64.6 | −2.4 | **+261 (+7.1%)** | +24.4% (TID closure) | +22.7% | +17.8% | +25.8% (city) | **+6.9%** | +16.2% | 0.78 → revalued to 100% for 2026 |
  | City of Madison wards | 63.7 | −5.6 | **+260 (+21.1%)** | +13.4% | +22.6% (city) | +20.2% (city) | +25.5% (53717) | +13.5% | +18.5% | 0.97, annual |
  | Town of Middleton | 57.8 | −0.1 | +139 (+9.0%) | +17.3% | +28.6% | +21.3% | +26.0% (53562) | +10.7% | +15.2% | 0.97, revalued 2025 and 2026 |
  | Village of Cross Plains | 52.3 | −3.6 | **+203 (+21.9%)** | +21.6% | **+38.5%** | **+28.1%** | +23.0% (village) | +17.6% | +27.5% | **0.65**, no revaluation through 2025 |
  | Town of Springfield | **43.0** | −2.8 | −11 (−1.7%) | +14.0% (−4.3% in 2026) | +27.0% | +24.7% | ~+25–30% (shared ZIPs) | **+23.5%** | **+30.5%** | 0.94, revalued 2025 |
  | Town of Cross Plains | **46.6** | −4.0 | −1 (−0.5%) | +17.7% | +30.8% | +25.8% | +24.8% (53528) | +16.6% | +24.0% | 0.93, revalued 2024 |
  | Town of Berry | **28.9** | −5.5 | +8 (+3.3%) | +4.0% (−5.1% in 2026) | +34.4% | +15.5% | ~+23–25% (shared ZIPs) | +13.6% | +26.0% | 0.67, no revaluation |
  | Town of Westport | 54.0 | +0.9 | −10 (−8.8%) | +17.7% | +24.2% | +14.5% | ~+25–26% (shared ZIPs) | +11.2% | +7.7% | 0.98, revalued 2025 |
  | **District** | **60.1** | **−2.8** | **+849 (+9.9%)** | **+19.2%** (+42.4% 2022→26) | | | | **+11.0%** (levy) | | |

  Vote sources: [Dane County 2022](https://elections.countyofdane.com/Precincts-Result/145/0042); [Dane County 2026](https://elections.countyofdane.com/Precincts-Result/197/0040). The CSV version, with more columns, is `property_values_comparison.csv`.
- **Correlations across the 8 units (unweighted; Pearson r, with Spearman ρ in parentheses):**

  | Measure | vs. Δ Yes pts | vs. % Δ No votes | vs. 2026 Yes % |
  |---|---|---|---|
  | Typical-home school tax 2023→25 (DOR index) | −0.66 (−0.55) | +0.23 (+0.12) | −0.58 (−0.67) |
  | Muni's MCPASD school tax 2024→25 | −0.31 (−0.43) | −0.04 (−0.10) | −0.50 (−0.76) |
  | DOR home appreciation 2023→26 | −0.23 (−0.24) | +0.40 (+0.40) | +0.02 (−0.19) |
  | Residential EQ value 2023→26 | −0.30 (−0.14) | +0.25 (+0.14) | −0.60 (−0.69) |
  | MCPASD-portion EQ value 2024→26 | +0.46 (+0.51) | +0.16 (+0.10) | +0.74 (+0.46) |
  | Zillow Jan 2022→Jan 2026 (proxy) | +0.46 (+0.70) | −0.53 (−0.50) | +0.25 (+0.27) |

  The "Δ No votes" column measures each unit's No count change as a percentage of its 2022 No count. All coefficients are my calculations. A negative value in the "Δ Yes pts" column means faster growth went with bigger Yes losses.

### Inferences
- **Tax growth tracks *where Yes slipped*, weakly, but not *where No votes came from*.** The strongest relationship is between a typical home's 2023–25 school-tax growth and the change in Yes points (r ≈ −0.66). It rests on the small towns and the Village, which together cast about 19% of 2026 referendum votes. On the share of new No votes, the relationship is near zero.
- **The City of Middleton cuts against the "bigger bills → more No" story.** Its aggregate MCPASD school tax rose only 6.9% from 2024 to 2025 and its homes appreciated least among the large units, yet it added the most No votes (+261). What the City had that others did not was a revaluation notice in summer 2026 showing about +33%, with Board of Review on Sept. 22, six weeks before the vote. The data cannot distinguish a notice-shock effect from other causes such as partisanship or turnout (see `partisan_correlation.md`). It is the most plausible tax-related mechanism for the City.
- **The Madison wards** added nearly as many No votes (+260, +21%) on middling value and tax growth (city-wide +20% appreciation; MCPASD-portion school tax +13.5%). Madison assesses at market every year, so there was no notice shock. Value or tax growth does not explain Madison well. Ward renumbering also complicates the comparison there (final report).
- **The Village of Cross Plains fits the hypothesis on every measure.** It had the fastest residential appreciation (+28% DOR; +38.5% residential value with new construction), +17.6% aggregate school tax in one year and a +27.5% typical-home school tax since 2023. At a 0.65 ratio, the school line printed **13.25 per $1,000 assessed**, the highest in the district, against 8.9–9.2 in the revalued towns. Its No votes rose 22% and its core fell to 51.8% Yes.
- **The No-voting towns** (Springfield 43.0%, Town of Cross Plains 46.6%, Berry 28.9%) did see above-average 2023–25 school-tax growth. Springfield's +23.5% one-year jump followed DOR's +17.9% residential estimate and a 2025 revaluation. But those towns added almost no No votes (−11, −1, +8); their Yes share fell because Yes voters dropped out. DOR then *cut* Springfield's and Berry's 2026 values, so their December 2026 school-tax shares will fall.
- **Caveats:** there are only 8 units. Small towns' DOR figures are noisy. Town measures cover the whole town, not the MCPASD slice. Zillow geographies are shared ZIPs, which is why Zillow correlates in the "wrong" direction. Value growth is confounded with rurality and partisanship: the fastest-growing units are also the most Republican. School tax per market dollar is identical across the district, so differences come only from relative appreciation and, within a municipality, assessment uniformity.

### Gaps
- No survey or reporting links tax bills or revaluation notices to individual vote choice. This is ecological inference only.
- A ward-level version of this test, such as City of Middleton wards with the largest notice increases versus No growth, would need parcel-level assessment changes by ward from the assessor. Those were not available.

## Q6. The two 2026 tax-impact sets: exact wording, dates, and what the district's own page showed

### Takeaway
The **August set** came from the district's Aug. 12 board-approval release: about **$64 a year by year four** per $100,000 of *fair market value*. As tabulated by BadgerHomeowner, that was **$44, $65, $64, $64**, which WKOW summed to **"$237 over four years."** By **Sept. 17–21**, a district "explanatory page" showed **$0, $21, $40, $59** per $100,000. Channel 3000 restated those as "$600 over four years" on a $500,000 home, and the Cap Times as "$120 per $100,000 … over the next four years." NBC15 printed the same district table under an "Increase from previous year" header and then said "**$600 more annually by the fourth year**." That reading conflicts with the others and is almost certainly wrong. BadgerHomeowner still showed the August set on Oct. 24, ten days before the vote. I could not view the district's page to date the switch.

### Cited Findings
- **Channel 3000, Aug. 12, 2026 (published 8:22 a.m., page modified Sept. 3), relaying the district release [primary]:** "Based on current projections, the estimated tax impact on a property with a fair market value of $100,000 would increase gradually over the four-year period, reaching about $64 a year in the fourth year." — [Channel 3000, Aug. 12, 2026](https://www.channel3000.com/news/middleton-cross-plains-school-board-approves-34-6m-referendum-for-nov-3-election/article_1db2aab8-7a6b-4944-aab3-394bc0a8ac26.html); the same text is in [Fox 47](https://fox47.com/news/local/middleton-cross-plains-school-board-approves-346m-referendum-for-nov-3-election) per `tax_messaging.md`.
- **WKOW, Aug. 12, 2026 [primary]:** "The raise would be about $237 — over the course of four years — per every $100,000 worth of property." — [WKOW](https://www.wkow.com/news/middleton-cross-plains-school-district-asks-taxpayers-for-more-money-in-november-referendum/article_a1c6ba6d-441d-4075-bc4f-e46c4110d69e.html)
- **BadgerHomeowner (third-party tracker; page dated Oct. 24, 2026, "Last checked October 24, 2026") [primary]:**
  - The tracker lists "$44 in 2027-2028, $65 in 2028-2029, $64 in 2029-2030, $64 in 2030-2031 per $100,000 of property value (district)."
  - It notes: "Middleton-Cross Plains says its first year, $24.9 million, is no increase over this school year … The district calls each yearly figure in the table an estimated tax bill increase but doesn't say compared to what."

  Source: [BadgerHomeowner](https://www.badgerhomeowner.com/school-referendums-dane-county/). 44 + 65 + 64 + 64 = 237 (my arithmetic). The site sells assessment checks, so it is a commercial source.
- **Wisconsin Examiner via Civic Media, Sept. 21, 2026 (10:04 a.m. CT), on a Sept. 17 information session [primary]:**
  - "An explanatory page provided by the district shows that property taxpayers could expect to pay no additional money in the first year, $21 in the second, $40 in the third and $59 in the fourth. However, the numbers are pegged to $100,000 of property. The district said it provided the information in the form it did so individuals could do the math easily depending on the cost of the house."
  - It adds: "The average cost of a house is $500,000 in Middleton, meaning in the second year … an average homeowner could expect to pay an additional $105."

  Source: [Civic Media](https://civicmedia.us/news/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding). The original is at [wisconsinexaminer.com](https://wisconsinexaminer.com/2026/09/21/middleton-referendum-discussion-highlights-tension-between-property-taxes-and-school-funding/), which is blocked here.
- **Channel 3000, Sept. 28, 2026 (5:08 p.m.; modified Sept. 30) [primary]:** "For an average $500,000 Middleton home, the district estimates the referendum would increase property taxes by about $600 over four years. The estimated taxpayer impact for a $100,000 home is $120 over four years: Year 1: $0 increase; Year 2: $21 increase; Year 3: $40 increase; Year 4: $59 increase" — [Channel 3000](https://www.channel3000.com/news/middleton-cross-plains-area-school-district-voters-deciding-on-118m-school-referendum-in-november/article_21c34ed2-934f-4903-9354-3e66b2bfc210.html)
- **Cap Times, Oct. 20, 2026 (6:00 a.m.) [primary]:** "It would raise tax bills by $120 per $100,000 of property value over the next four years." It appears next to "Waunakee's referendums combined would raise property taxes on the average home … by approximately $210 per year." — [Cap Times](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)
- **NBC15/WMTV (page stamp "Published: Oct. 21, 2026 at 9:40 PM CDT; Updated 10:52 PM"; the URL is dated 2026/10/22) [primary]:**
  - "For a home with a fair market value of $500,000, the district estimates the following additional annual increases: School year / Increase from previous year — 2027–28 $0; 2028–29 $105; 2029–30 $200; 2030–31 $295. Combined, those increases would mean an estimated $600 more annually by the fourth year compared with the first year."
  - It also says: "Those figures are district projections and account only for the referendum. They do not include … property valuation changes or … $325 per student."
  - It notes that more information "is available on the Middleton-Cross Plains Area School District's referendum website."

  Source: [WMTV](https://www.wmtv15news.com/2026/10/22/middleton-cross-plains-voters-weigh-school-referendum-district-faces-nearly-25m-potential-cuts/)
- **District's own page:** not viewable. mcpasd.k12.wi.us sits behind a JS challenge, and the Wayback Machine reset the connection. A "Myths Versus Facts" article title is known only from a search listing — [MCPASD](https://www.mcpasd.k12.wi.us/article/3148218/) (per `tax_messaging.md`).

### Inferences
- **When the numbers changed:** between the Aug. 12 release, still unchanged when Channel 3000 edited its story on Sept. 3, and the Sept. 17 session the Examiner covered. The district's page cannot confirm this.
- **What each set means:**
  - $0/$21/$40/$59 are *levels above today's bill*, adding to $120 per $100K (**$600 over four years**, $295 a year by year four, on a $500K home). They match new referendum dollars of $0, $3.0M, $6.2M and $9.7M divided by a growing equalized base (`tax_messaging.md`, Q2).
  - The August $44/$65/$64/$64 cannot be referendum-only, because year one is $44 while the referendum is flat. It likely folded in other levy growth, such as the $325-per-pupil revenue-limit increase, but this is unconfirmed.
  - NBC15's "$600 more annually by the fourth year" doubles the year-four figure.
- **Lesson for the campaign:**
  - Voters could find four different "costs" in the press: $64 a year (year 4), $237 over four years, $120 per $100K over four years, and $600 a year.
  - A commercial tracker kept publishing the superseded set into late October.
  - Publish one dated table with an explicit baseline ("compared with your 2026-27 bill"). Show both per-$100K and $500K-home figures, plus the fail scenario. Ask outlets to correct superseded numbers.

### Gaps
- I could not see the district's referendum page or FAQ, so I cannot confirm what it showed in August, when it changed, or the baseline the August set used.
- No district statement explains the change, and none of the outlets noted it.

## Q7. "Per $100K" of what? And how a 78%-to-100% revaluation changes the notice and the bill

### Takeaway
**Correction to the assignment's premise:** the district's *2026* figures were stated per $100,000 of **fair market value**, not assessed value. The Aug. 12 release said "a property with a fair market value of $100,000," and NBC15 quoted "a home with a fair market value of $500,000." The *2022* deck did use "$100,000 assessed value." Before 2026, a City of Middleton owner who applied the per-$100K figure to the assessed value on the bill (78% of market) would have understated the cost by about 22%. The correct base was the bill's "estimated fair market value" line. After the 2026 revaluation, assessed value is roughly equal to market in the City, so the two coincide. **School taxes are apportioned to municipalities by DOR equalized value, so a revaluation cannot raise the City's school taxes. It enlarges the assessed number and shrinks the rate.**

### Cited Findings
- **2026 district basis is fair market value [primary]:**
  - "estimated tax impact on a property with a fair market value of $100,000" — [Channel 3000, Aug. 12, 2026](https://www.channel3000.com/news/middleton-cross-plains-school-board-approves-34-6m-referendum-for-nov-3-election/article_1db2aab8-7a6b-4944-aab3-394bc0a8ac26.html)
  - "For a home with a fair market value of $500,000, the district estimates …" — [WMTV, Oct. 21/22, 2026](https://www.wmtv15news.com/2026/10/22/middleton-cross-plains-voters-weigh-school-referendum-district-faces-nearly-25m-potential-cuts/)
  - Other outlets were vaguer: "$100,000 worth of property" ([WKOW](https://www.wkow.com/news/middleton-cross-plains-school-district-asks-taxpayers-for-more-money-in-november-referendum/article_a1c6ba6d-441d-4075-bc4f-e46c4110d69e.html)), "$100,000 of property value" ([Cap Times](https://captimes.com/news/education/two-dane-county-school-districts-ask-voters-to-raise-property-taxes/article_56b581ca-9603-48fd-ad2e-566c6748b5bc.html)), "a $100,000 home" ([Channel 3000, Sept. 28](https://www.channel3000.com/news/middleton-cross-plains-area-school-district-voters-deciding-on-118m-school-referendum-in-november/article_21c34ed2-934f-4903-9354-3e66b2bfc210.html)).
- **2022 basis was assessed value [primary, per earlier note]:** the 2022 deck's slide was titled "Tax Impact: $24.9 million … $100,000 assessed value" — [2022 MCPASD presentation](https://clubrunner.blob.core.windows.net/00000006121/en-ca/files/homepage/m-cp-school-district-2022-referendum/Nov-2022-Referendum-M-CP-area-school-district-Presentation.pdf)
- **DOR on revaluations and taxes [primary]:**
  - "Property owners fear that taxes will go up if a revaluation is done. This may or may not be the case. Taxes are directly tied to the amount of money that the municipality needs to collect. This is called the levy. If the total levy remains the same, only those properties that are not presently paying their fair share of the tax burden will pay more taxes after a revaluation. Properties presently paying more than their fair share will pay less."
  - "If the assessed values established by a revaluation are greater than they were before and the tax levy is the same, then the tax rate will be less. For example, if the tax levy remains unchanged and the total assessed value of the taxation district is doubled, the tax rate will be cut in half." The guide's before/after example: $200,000 ÷ $4,000,000 = 5%, then $200,000 ÷ $8,000,000 = 2.5%.

  Source: [DOR 2026 Guide for Property Owners, PB-060 (R. 1-26)](https://www.revenue.wi.gov/pubs/slf/pb060.pdf)
- **DOR on why school levies use equalized value [primary]:** "Equalized values are used for apportioning county property taxes, public school taxes … a school levy among the municipalities in the school district … The values determined by local assessors cannot be used to apportion levies among different municipalities … since the assessed values are not comparable among municipalities, whereas the equalized values are all at market value." — [DOR PB-060](https://www.revenue.wi.gov/pubs/slf/pb060.pdf)
- **DOR on the bill's fair-market line [primary]:** "The total estimated fair market value is calculated by dividing the total assessed value by the average assessment ratio. Property taxes are levied on the total assessed value, not the total estimated fair market value." — [DOR PB-060](https://www.revenue.wi.gov/pubs/slf/pb060.pdf)
- **City of Middleton framing [secondhand]:** revaluation "redistributes how the tax levy is shared among properties; it does not, by itself, generate additional tax revenue" — [City message, now 404](https://cityofmiddleton.us/CivicSend/ViewMessage/message/297551). Purpose: "to bring all assessed values to 100% market value" [primary] — [City Revaluation Overview](https://www.cityofmiddleton.us/DocumentCenter/View/20472/Middleton-Revaluation-Overview)

### Inferences
- **Worked example for a $500K-market City of Middleton home (my arithmetic, gross school line only):**
  - **2025 bill:** assessed about **$391,350** (0.7827 × $500K) × 0.011059306 = **$4,328**. That equals $500K × 8.66 per $1,000 of market value.
  - **2026 notice:** about **$520,000** assessed (100% of market, after DOR's +4% City residential economic change). That is **33% higher on paper**, with only 4% real appreciation.
  - **Dec. 2026 bill:** the rate per assessed dollar drops to the district equalized rate. That is about 7.75 per $1,000 if the 2026-27 levy is flat (school line about **$4,027**), or about 8.36 with an 8% levy increase (about **$4,349**). The bill moves with the levy and the home's value relative to the district, not with the 33% jump on the notice.
- **Same per-$100K figure, different bill math by municipality:** in 2025, the same $59 per $100K-of-market figure would show up against school mill rates per assessed dollar of 13.25 in the Village, 12.94 in Berry and 11.06 in the City, but 8.9 in the revalued towns. A homeowner multiplying the district figure by assessed value in the Village (ratio 0.65) would have understated the cost by about 35%.
- **Campaign implication:** where notices jumped from a revaluation (the City in 2026; possibly the Village), say plainly: "Your new assessment is close to market value, so use the new number with our per-$100K figures. Your school tax depends on the levy, not the notice." That is accurate only because the district's 2026 figures were per market value.

### Gaps
- The City's own 2026 revaluation FAQ (cityofmiddleton.us/m/faq) reset the connection, so I could not quote City wording beyond the overview PDF and the secondhand notice text.
- I did not find a district statement saying explicitly how 2026 revaluations should be used with its per-$100K figures.
