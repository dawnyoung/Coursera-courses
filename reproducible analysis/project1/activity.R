library(dplyr)


##Loading and preprocessing the data
#read data and make it clean
activity <- read.csv("repdata-data-activity/activity.csv", 
                     na.strings = "NA")
activity$date <- as.Date(activity$date)



##What is mean total number of steps taken per day?
#Calculate the total number of steps taken per day
totalno <- aggregate(steps ~ date, data = activity, na.rm = TRUE, sum)
#make a histogram
hist(totalno$steps, col = "grey", breaks = 10, 
     xlab = "Total steps per day",
     main = "Histogram of total steps per day")

#calculate the mean
mean(totalno$steps)

#calculate the median
medi_totalno <- median(totalno$steps)


##What is the average daily activity pattern?
average <- activity%>%
  group_by(interval)%>%
  summarize(meansteps = mean(steps, na.rm = TRUE))

with(average,plot(average$interval, average$meansteps, 
                  type = "l", xlab = "5 min interval",
                  ylab = "Average steps",
                  main = "Daily activity pattern"))

#output the max
with(average, interval[which.max(meansteps)])


##Imputing missing values
#the total number of rows with NAs
sum(is.na(activity$steps))
sum(is.na(activity$date))
sum(is.na(activity$interval))

newact <- inner_join(activity, average, by = "interval")
newact$steps <- ifelse(is.na(newact$steps), 
                       newact$meansteps, newact$steps)
##knitr: add warning = FALSE, message = FALSE

newact <- subset(newact, select = steps : interval)

totalno2 <- aggregate(steps ~ date, data = newact, sum)
hist(totalno2$steps, col = "grey", breaks = 10,
     xlab = "Total steps per day", 
     main = "Histogram of total steps per day")

mean(totalno2$steps)
median(totalno2$steps)


##Are there differences in activity patterns between weekdays and weekends?
newact$day <- weekdays(newact$date)
newact$day <- ifelse(newact$day %in% c("Saturday", "Sunday"),
                     "weekend", "weekday")

newact_mean <- newact%>%
  group_by(interval, day)%>%
  summarize(meansteps = mean(steps))

library(lattice)
xyplot(meansteps ~ interval | day, data = newact_mean,
       type = "l", layout = c(1,2),
       xlab = "5 min interval",
       ylab = "Average stpes")


