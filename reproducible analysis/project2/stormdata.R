#data processing
#read data
storm <- read.csv(bzfile("repdata-data-StormData.csv.bz2"), header = TRUE)
storm <- subset(storm, select = c(EVTYPE, FATALITIES : CROPDMGEXP))
#Change all letters into lower case
storm$EVTYPE <- tolower(storm$EVTYPE)
storm$CROPDMGEXP <- tolower(storm$CROPDMGEXP)
storm$PROPDMGEXP <- tolower(storm$PROPDMGEXP)
#unify the expression of each event type
storm$EVTYPE <- gsub("^flash flood.*", "flash flood", storm$EVTYPE)
storm$EVTYPE <- gsub("*.flash flood.*", "flash flood", storm$EVTYPE)

storm$EVTYPE <- gsub("^flood.*", "flood", storm$EVTYPE)

storm$EVTYPE <- gsub("^winter storm.*", "winter weather", storm$EVTYPE)
storm$EVTYPE <- gsub("winter mix", "winter weather", storm$EVTYPE)
storm$EVTYPE <- gsub("wintery mix", "winter weather", storm$EVTYPE)
storm$EVTYPE <- gsub("wintry mix", "winter weather", storm$EVTYPE)

storm$EVTYPE <- gsub("^wild fire.*", "wildfire", storm$EVTYPE)
storm$EVTYPE <- gsub("^wildfire.*", "wildfire", storm$EVTYPE)
storm$EVTYPE <- gsub("^wild/forest fire.*", "wildfire", storm$EVTYPE)

storm$EVTYPE <- gsub("^wind.*", "high wind", storm$EVTYPE)
storm$EVTYPE <- gsub("^wnd.*", "high wind", storm$EVTYPE)
storm$EVTYPE <- gsub("^tstm wind.*", "high wind", storm$EVTYPE)
storm$EVTYPE <- gsub("high winds.*", "high wind", storm$EVTYPE)

storm$EVTYPE <- gsub("^waterspout.*", "waterspout", storm$EVTYPE)
storm$EVTYPE <- gsub("^water spout.*", "waterspout", storm$EVTYPE)
storm$EVTYPE <- gsub("^wayterspout.*", "waterspout", storm$EVTYPE)

storm$EVTYPE <- gsub("^wet.*", "heavy rain", storm$EVTYPE)
storm$EVTYPE <- gsub("^heavy rain.*", "heavy rain", storm$EVTYPE)

storm$EVTYPE <- gsub("^volcanic.*", "volcanic ash", storm$EVTYPE)

storm$EVTYPE <- gsub("^cloud.*", "funnel cloud", storm$EVTYPE)

storm$EVTYPE <- gsub("^urban.*", "flood", storm$EVTYPE)

storm$EVTYPE <- gsub("^thunderstorm.*", "thunderstorm wind", storm$EVTYPE)
storm$EVTYPE <- gsub("^thundeerstorm.*", "thunderstorm wind", storm$EVTYPE)
storm$EVTYPE <- gsub("^thunderstrom.*", "thunderstorm wind", storm$EVTYPE)
storm$EVTYPE <- gsub("^thunerstorm.*", "thunderstorm wind", storm$EVTYPE)

storm$EVTYPE <- gsub("^tornado.*", "hurricane", storm$EVTYPE)
storm$EVTYPE <- gsub("^hurricane.*", "hurricane", storm$EVTYPE)

storm$EVTYPE <- gsub("^tropical storm.*", "tropical storm", storm$EVTYPE)

storm$EVTYPE <- gsub("^marine.*.wind.*", "marine thunderstorm wind", storm$EVTYPE)

storm$EVTYPE <- gsub("^lightning.*", "lightning", storm$EVTYPE)

storm$EVTYPE <- gsub("^hail.*", "hail", storm$EVTYPE)

storm$EVTYPE <- gsub("^heat.*", "heat", storm$EVTYPE)
storm$EVTYPE <- gsub("*.heat.*", "heat", storm$EVTYPE)
storm$EVTYPE <- gsub("excessiveheat", "heat", storm$EVTYPE)

storm$EVTYPE <- gsub("^blizzard.*", "blizzard", storm$EVTYPE)

storm$EVTYPE <- gsub("^heavy snow.*", "heavy snow", storm$EVTYPE)

storm$EVTYPE <- gsub("*.surf.*", "high surf", storm$EVTYPE)

storm$EVTYPE <- gsub("^coastal.*", "coastal flood", storm$EVTYPE)

storm$EVTYPE <- gsub("^cold.*", "cold/wind chill", storm$EVTYPE)

storm$EVTYPE <- gsub("^dry.*", "drought", storm$EVTYPE)



fatalities <- aggregate(FATALITIES ~ EVTYPE,storm, sum)
fatalities <- fatalities[order(fatalities$FATALITIES, decreasing = TRUE),]

injuries <- aggregate(INJURIES ~ EVTYPE, storm, sum)
injuries <- injuries[order(injuries$INJURIES, decreasing = TRUE),]



storm$PROPDMGEXP[storm$PROPDMGEXP == "b"] <- 10000000000
storm$PROPDMGEXP[storm$PROPDMGEXP == "m"] <- 1000000
storm$PROPDMGEXP[storm$PROPDMGEXP == "k"] <- 1000
storm$PROPDMGEXP[storm$PROPDMGEXP == "h"] <- 100
storm$PROPDMGEXP[storm$PROPDMGEXP %in% c("+","-")] <- 1
storm$PROPDMGEXP[storm$PROPDMGEXP == ""] <- 0

storm$prop <- as.numeric(storm$PROPDMGEXP) * as.numeric(storm$PROPDMG)
prop <- aggregate(prop ~ EVTYPE, storm, sum)
prop <- prop[order(prop$prop, decreasing = TRUE),]


storm$CROPDMGEXP[storm$CROPDMGEXP == "b"] <- 10000000000
storm$CROPDMGEXP[storm$CROPDMGEXP == "m"] <- 1000000
storm$CROPDMGEXP[storm$CROPDMGEXP == "k"] <- 1000
storm$CROPDMGEXP[storm$CROPDMGEXP == "?"] <- 0

storm$crop <- as.numeric(storm$CROPDMG) * as.numeric(storm$CROPDMGEXP)
crop <- aggregate(crop ~ EVTYPE, storm, sum)
crop <- crop[order(crop$crop, decreasing = TRUE),]


crop <- head(crop)
prop <- head(prop)
fatalities <- head(fatalities)
injuries <- head(injuries)



library(ggplot2)
pfata <- ggplot(data = fatalities, 
                aes(reorder(EVTYPE, FATALITIES), y= FATALITIES, fill = FATALITIES)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  xlab("Event") + ylab("Total number of fatalities") +
  theme(legend.position = "none")
pinju <- ggplot(data = injuries,
                aes(reorder(EVTYPE, INJURIES),
                    y=INJURIES, fill = INJURIES)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  xlab("Event") + ylab("Total number of injuries") + 
  theme(legend.position = "none")


par(mfrow = c(1,2))
barplot(crop$crop, col = "grey", 
        main = "Total number of crop damaged",
        names.arg = crop$EVTYPE)
barplot(prop$prop, col = "grey",
        main = "Total number of property damaged",
        names.arg = prop$EVTYPE)
mtext("Economic consequences throughout US (1950-2011)",
      outer = TRUE)