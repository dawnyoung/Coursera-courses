#####graphs
#boxplot
boxplot(x$var1,col = "blue")
boxplot(var1~var2, data = x, col = "blue")
#按照var2分开var1，绘制var1的boxplot

#histogram
hist(x$var1, col = "green", breaks = 100)
#breaks: change the number of bars
rug(x$var1)#show all the data points underneath the histogram
hist(subset(x, var2 = "blabla")$var1, col = "red")
#plot of var1, where var2=blabla

#barplot
barplot(table(x$var1), col = "wheat", main = "title")
#main : define the tile of the figure

#scatterplot
with(x, plot(var1, var2))
abline(h = 1, lwd = 2, lty = 3)
#add straigth line to the current plot
#h: the y-value for horizontal line
with(x, plot(var1, var2, col = var3))
#var1,var2分别是横纵坐标，不同的颜色表示不同的var3的值


############################plotting system
#####basic system
library(graphics); library(grDevices)
library(datasets)
hist(x$var1)
with(x, plot(var1, var2))
x <- transform(x, var3 = factor(var3))
boxplot(var1 ~ var3, x, xlab = "var3", ylab = "var1")
#pch: plotting symbol
#lty: the line tpe, can be dashed, dotted...
#lwd: the line width (integer multiple)
#col: plotting color

par()#affect all plots in an R session
#las: the orientation of the axis labels on the plot
#bg: the background color
#mar: the margin size. 
#oma: the outer margin size
#mfrow, mfcol: number of plots per row, column
par(mfrow = c(1,2))#2 plot in one row
with(x,{
  plot(var1, var2, main = "title1")
  plot(var1, var3, main = "title2")
  mtext("main title", outer = TRUE)#add a general heading
})

lines()#add lines to a plot
points(var1, var2, col = "blue")#add points to a plot
text()#add text labels to a plot using specified coordinates
title#add annotations to x, y, title, subtitle, outer margin
mtext()#add arbitrary text to the margins of the plot
axis()#add axis ticks/labels

legend("topright", #position of legend
       pch = 1, #空心圆
       col = c("blue", "red"), #color of the legend
       legend = c("var1", "var2"))#name of the legend

model <- lm(var1 ~ var2, x)
abline(model, lwd = 2)#add aggregation line





#####lattice system
#usually created in a single function call 
library(lattice); library(grid)
xyplot()#main function for creating scatterplots
bwplot()#box-and-whiskers plots
histogram()#histograms
stripplot()#like a boxplot but with actual points
dotplot()#plot dots on violin strings
splom()#scatterplot matrix
levelplot()
contourplot()#for plotting image data

#examples
library(lattice)
library(datasets)

xyplot(var1 ~ var2, data = x)#scatterplot

x <- transform(x, var3 = factor(var3))#use var3 as factor
xyplot(var1 ~ var2 | var3, data = x, 
       layout = c(5,1))#5 plots in 1 row

#panel function
xyplot(y ~ x | f, panel = function(x, y, ...){
  panel.xyplot(x, y, ...)
  panel.lmline(x, y, col = 2)#simple linear regression line
})





#####ggplot2 system
library(ggplot2)
data(x)
qplot(var1, var2, data = x, 
      #data should be labeled by var3. 
      #different colors from different factors of var3
      color = var3,
      #show the points and regregation line with 95% confidence level
      geom = c("points", "smooth"))

qplot(var1, data = x, fill = var3)#histgram, using factors of var3

qplot(var1, data = x, facets = var3~.)
#separate the histgram into various plots by factors of var3
#~. at left, plots are in one row and several cols

qplot(var1, var2, data = x, facets = ~.var3)
#separate the scatter plot into several plots by factors of var3
#~. at right, one col and several rows

#ggplot can be made layer by layer
a <- ggplot(x, aes(var1, var2))#initial call; no plot
b <- a + geom_point(color = "blue", size = 2, 
                    alpha = 1/2)#transparance
b1 <- a + geom_point(aes(color = var3), #color vaires from different factors
                     size = 2, alpha = 1/2)
print(b)#scatter plot
c <- b + geom_smooth(method = "lm", linetype = 3, se = FALSE, zise = 2)
print(c)#add agregation line
d <- c + facet_grid(.~var3)#separate the plot
e <- d + labs(title = "title")
f <- e + labs(x = "x", y = "y")#add lebels and title
g <- f + theme_bw(base_family = "Times")#change the background color
h <- a + geom_line() + ylim(-1,1)
h1 <- a + geom_line() +
  coord_cartesian(ylim = c(-1,1))#define the limit of y

#cut the data at deciles and create a new factor variable
cutpoints <- quantile(x$var4, seq(0, 1, length = 4), na.rm = TRUE)
x$var_new <- cut(x$var4, cutpoints)
g <- ggplot(data = x, aes(var1, var2))
f <- g + geom_point(alpha = 1/3) + 
  facet_wrap(var3 ~ var_new, nrow = 2, ncol = 3)
#separate the plot by the factor of var3 and var_new

  




###############################graphic device
#screen device
windows()
#PDF
pdf(file = "myplot.pdf")#create a pdf device
with(x, plot(var1, var2))
title(main = "title")#make a plot in this pdf
dev.off()#close the pdf device

with(x, plot(var1, var2))
title(main = "title")#make a plot on the screen device
dev.copy(png, file = "myplot.png")#copy the plot into a png file
dev.off()#close the device





#############################################project1
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
#plot1
p1 <- hist(p$Global_active_power, main = "Global Active Power", 
           xlab = "Global Active Power (kilowatts)",
           ylab = "Frequency", col = "red")
dev.copy(png, file = "plot1.png")
dev.off

#plot2
plot(p$time, p$Global_active_power, col = "black",
     xlab = "", ylab = "Global Active Power", type = "l")

#plot3
plot(p$time, p$Sub_metering_1, col = "black", type = "l",
     xlab = "", ylab = "energy sub metering")
lines(p$time, p$Sub_metering_2, col = "red")
lines(p$time, p$Sub_metering_3, col = "blue")
legend("topright", c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"),
       lty = c(1,1,1), 
       col = c("black", "red", "blue"))

#plot4
library(graphics); library(grDevices)

windows()

par(mfrow = c(2,2))

plot(p$time, p$Global_active_power, col = "black",
     xlab = "", ylab = "Global Active Power", type = "l")

plot(p$time, p$Voltage, type = "l",
     col = "black", xlab = "datetime", ylab = "Voltage")

plot(p$time, p$Sub_metering_1, col = "black", type = "l",
     xlab = "", ylab = "energy sub metering")
lines(p$time, p$Sub_metering_2, col = "red")
lines(p$time, p$Sub_metering_3, col = "blue")
legend("topright", c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"),
       lty = c(1,1,1), 
       col = c("black", "red", "blue"))

plot(p$time, p$Global_reactive_power, type = "l",
     col = "black", xlab = "datetime", ylab = "Global reactive power")




######################################################project2
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

#plot1
total <- aggregate(Emissions ~ year, NEI, sum)

windows()
barplot(total$Emissions, col = "grey",
        xlab = "year", ylab = "PM2.5 Emissions", 
        names.arg = total$year,
        main = "Total PM2.5 Emission from all sources")

dev.copy(png, file = "plot1.png")
dev.off()

#plot2
Baltimore <- NEI[NEI$fips == "24510", ]
aggBal <- aggregate(Emissions ~ year, Baltimore, sum)

windows()
barplot(aggBal$Emissions, col = "grey",
        xlab = "year", ylab = "PM2.5 Emissions",
        names.arg = aggBal$year,
        main = "PM2.5 Emissions of Baltimore City")

dev.copy(png, file = "plot2.png")
dev.off()

#plot3
Baltimore <- NEI[NEI$fips == "24510", ]

library(ggplot2)
plot3 <- ggplot(Baltimore, aes(factor(year), Emissions, fill = type)) + 
  geom_bar(stat = "identity") + 
  facet_grid(.~type,scales = "free",space="free") + 
  guides(fill = FALSE) +
  labs(x = "year", y = "PM2.5 Emissions (TONS)", 
       title = "Total PM2.5 Emissions of Baltimore City")
print(plot3)

#plot4
combustion <- SCC[grep("Combustion", SCC$SCC.Level.One),]
coal <- combustion[grep("Coal", combustion$SCC.Level.Four),]
coal1 <- NEI[NEI$SCC %in% coal$SCC,]
total <- aggregate(Emissions ~ year, coal1, sum)

windows()
barplot(total$Emissions, col = "gray",
        names.arg = total$year,
        xlab = "year", ylab = "PM2.5 Emissions",
        main = "PM2.5 Emissions From Coal Combustion-related Sources")

#plot5
mob <- SCC[grep("vehicles", SCC$SCC.Level.Two, ignore.case = TRUE),]
mob1 <- NEI[NEI$SCC %in% mob$SCC,]
batMobile <- mob1[mob1$fips == "24510", ]
total <- aggregate(Emissions ~ year, batMobile, sum)

windows()
barplot(total$Emissions, col = "grey",
        names.arg = total$year,
        xlab = "year", ylab = "PM2.5 Emissions",
        main = "Total PM2.5 Emissions From Mobile Sources in Baltimore City")
dev.copy(png, file = "plot5.png")
dev.off()

#plot6
#read data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

mob <- SCC[grep("vehicles", SCC$SCC.Level.Two, ignore.case = TRUE),]
mob1 <- NEI[NEI$SCC %in% mob$SCC,]
bal <- mob1[mob1$fips =="24510"  ,]
bal <- mutate(bal, city <- "Baltimore City")
colnames(bal) <- c("fips", "SCC", "Pollutant", "emissions",
                   "type", "year", "city")
los <- mob1[mob1$fips =="06037",]
los <- mutate(los, city <- "Los Angeles County")
colnames(los) <- c("fips", "SCC", "Pollutant", "emissions",
                   "type", "year", "city")

total <- rbind(bal, los)

library(ggplot2)
windows()
plot6 <- ggplot(total, aes(factor(year), emissions, fill = city)) +
  geom_bar(stat = "identity") + 
  facet_grid(.~city, scales = "free", space = "free") + 
  guides(fill = FALSE) + 
  labs(x = "year", y = "Emissions",
       title = "Emissions From Motor Vehicle Sources")
print(plot6)
dev.copy(png, file = "plot6.png")
dev.off()