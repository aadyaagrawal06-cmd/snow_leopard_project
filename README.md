# Snow Leopard Habitat Suitability in the Himalaya and Adjacent High-Mountain Asia

## Overall theme
What combined effects do climate and human pressure have on snow leopards in the Himalayas?

## Project question
Does including human pressure change predicted snow leopard habitat suitability in the Himalaya and adjacent high-mountain Asia, compared with climate and terrain alone?

## Scope note
GBIF records inside the Himalaya alone gave only 34 records after cleaning and thinning, too few for a stable model. The study area was therefore widened to adjacent high-mountain Asia (65-110°E, 25-50°N). Results will also be shown for the Himalaya separately.

## Status
In progress. Data cleaning is complete; climate and human pressure layers and modelling are next.

## Data
- Occurrence data: GBIF (*Panthera uncia*), downloaded 13 Oct 2026. Re-running the download may give slightly different counts as GBIF updates.
- Records: 421 raw, 196 after cleaning, 102 after thinning to one record per 10 arc-minute (about 18 km) cell.
- Cleaning: removed missing coordinates, duplicates, records before 1970, preserved specimens and records with coordinate uncertainty above 50 km.
- Over half of the raw records come from iNaturalist, which blurs locations of threatened species by about 20-30 km. This is why a coarse grid was used.
- Climate and terrain: WorldClim 2.1 (10 arc-minute), including elevation
- Human pressure: livestock density, population density

## Methods
- Present-day habitat suitability: Random Forest with spatial cross-validation (AUC and TSS)
- Model A: climate + terrain only
- Model B: climate + terrain + human pressure
- Outputs: suitability maps, a difference map (B minus A), and the percentage of suitable area that changes when human pressure is included
- Results shown for the whole study area and for the Himalaya separately

## Future work
- Project both models to future climate (e.g. 2041-2060, SSP2-4.5 and SSP5-8.5) to estimate shifts in suitable habitat, with human pressure held at present-day values
- Formally test interaction between climate and human pressure

## Limitations (to be expanded)
- Occurrence data are sparse and spatially biased (records cluster near roads, trekking routes and reserves)
- Many record locations are blurred by about 20-30 km
- The study area includes regions with different human pressure
- Pseudo-absences (background points) add uncertainty
- Models predict suitable habitat, not actual animal presence or movement

