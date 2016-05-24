# #########################
#     exploratory data analysis
############################

# # # # project1

#plot 2

library(data.table); library(dplyr)
#read data
d <- read.table("D:/RStudio/household_power_consumption.txt", 
                sep = ";", header = TRUE, 
                na.strings = "?")#missing value is represented by ?
p <- filter(d, Date == "1/2/2007" | Date == "2/2/2007")
rm(d)#remove the data won't be used to release memory

#clean data
p$time <- strptime(paste(p$Date, p$Time), format = "%d/%m/%Y %H:%M:%S")

windows()
plot(p$time, p$Global_active_power, col = "black",
     xlab = "", ylab = "Global Active Power (kilowatts)", type = "l")
dev.copy(png, file = "plot2.png")
dev.off()

#plot 3

library(data.table); library(dplyr)
#read data
d <- read.table("D:/RStudio/household_power_consumption.txt", 
                sep = ";", header = TRUE, 
                na.strings = "?")#missing value is represented by ?
p <- filter(d, Date == "1/2/2007" | Date == "2/2/2007")
rm(d)#remove the data won't be used to release memory

#clean data
p$time <- strptime(paste(p$Date, p$Time), format = "%d/%m/%Y %H:%M:%S")

windows()
plot(p$time, p$Sub_metering_1, col = "black", type = "l",
     xlab = "", ylab = "energy sub metering")
lines(p$time, p$Sub_metering_2, col = "red")
lines(p$time, p$Sub_metering_3, col = "blue")
legend("topright", c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"),
       lty = c(1,1,1), 
       col = c("black", "red", "blue"))
dev.copy(png, file = "plot3.png")
dev.off()

# plot 4

library(data.table); library(dplyr)
#read data
d <- read.table("D:/RStudio/household_power_consumption.txt", 
                sep = ";", header = TRUE, 
                na.strings = "?")#missing value is represented by ?
p <- filter(d, Date == "1/2/2007" | Date == "2/2/2007")
rm(d)#remove the data won't be used to release memory

#clean data
p$time <- strptime(paste(p$Date, p$Time), format = "%d/%m/%Y %H:%M:%S")

windows()
par(mfrow = c(2,2))
#1st plot
plot(p$time, p$Global_active_power, col = "black",
     xlab = "", ylab = "Global Active Power", type = "l")
#2nd plot
plot(p$time, p$Voltage, type = "l",
     col = "black", xlab = "datetime", ylab = "Voltage")
#3rd plot
plot(p$time, p$Sub_metering_1, col = "black", type = "l",
     xlab = "", ylab = "energy sub metering")
lines(p$time, p$Sub_metering_2, col = "red")
lines(p$time, p$Sub_metering_3, col = "blue")
legend("topright", c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"),
       lty = c(1,1,1), 
       col = c("black", "red", "blue"))
#4th plot
plot(p$time, p$Global_reactive_power, type = "l",
     col = "black", xlab = "datetime", ylab = "Global reactive power")

dev.copy(png, file = "plot4.png")
dev.off()


# # # # project 2

# plot 1
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

total <- aggregate(Emissions ~ year, NEI, sum)

windows()
barplot(total$Emissions, col = "grey",
        xlab = "year", ylab = "PM2.5 Emissions", 
        names.arg = total$year,
        main = "Total PM2.5 Emission from all sources")

dev.copy(png, file = "plot1.png")
dev.off()


#plot 2

NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

Baltimore <- NEI[NEI$fips == "24510", ]
aggBal <- aggregate(Emissions ~ year, Baltimore, sum)

windows()
barplot(aggBal$Emissions, col = "grey",
        xlab = "year", ylab = "PM2.5 Emissions",
        names.arg = aggBal$year,
        main = "PM2.5 Emissions of Baltimore City")

dev.copy(png, file = "plot2.png")
dev.off()

#plot 3
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

Baltimore <- NEI[NEI$fips == "24510", ]

windows()
library(ggplot2)
plot3 <- ggplot(Baltimore, aes(factor(year), Emissions, fill = type)) + 
  geom_bar(stat = "identity") + 
  facet_grid(.~type,scales = "free",space="free") + 
  guides(fill = FALSE) +
  labs(x = "year", y = "PM2.5 Emissions (TONS)", 
       title = "Total PM2.5 Emissions of Baltimore City")
print(plot3)
dev.copy(png, file = "plot3.png")
dev.off()


#plot 4
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

#clean data
combustion <- SCC[grep("Combustion", SCC$SCC.Level.One),]
coal <- combustion[grep("Coal", combustion$SCC.Level.Four),]
coal1 <- NEI[NEI$SCC %in% coal$SCC,]
total <- aggregate(Emissions ~ year, coal1, sum)

#make plot
windows()
barplot(total$Emissions, col = "gray",
        names.arg = total$year,
        xlab = "year", ylab = "PM2.5 Emissions",
        main = "PM2.5 Emissions From Coal Combustion-related Sources")
dev.copy(png, file = "plot4.png")
dev.off()