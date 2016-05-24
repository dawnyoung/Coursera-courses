######################Note
#file.exists("directory name"): check if directory exists
#dir.create("directory name"): create a new directory

#downloda.file(url, destfile, method): download a file from internet

#read.table("trace and file name",sep=",", header = TRUE)
#sep: separated by , (csv)

#head(file name): show the first 6 rows

#when read xlsx, use library(xlsx) first.
#read.xlsx("file name", sheetIndex = 1, header = TRUE)
#sheetIndex means which sheet the data is stored on.

##data.table
library(data.table)
tables()#see all the tables in memory
#create new data frame
DF <- data.frame(x=rnorm(9),y=rep(c("a","b","c"), each = 3), 
                 z=rnorm(9))
#create a new data table
DT <- data.table(x=rnorm(9),y=rep(c("a","b","c"), each = 3), 
                 z=rnorm(9))
DT[,list(mean(x),sum(z))]#shwo the mean of all x and sum of all z
DT[,w:=z^2]#add a new col named w, which is the square of z
DT[,m:={t<-x+z; log2(t+5)}]#add a new col with multiple operations
setkey(DT,y)
DT["b"]#show where y==b



#read JSON
library(jsonlite)
j <- fromJSON("url")
myjson <- toJSON(i, pretty = TRUE)
#pass the data of i into my json as a json file


#read from mysql
d <- dbConnect(MySQL(),...)#connect a database


#read from HDF5
h5read


#read from web
#1st method
con = url("url")#create a connection
htmlcode = readLines(con)#read data from this connection
close(con)#cut the connection
#2nd method
library(XML)
htmlcode <- htmlTreeParse("url",useInternalNodes = T)


##sorting
sort(x,decreasing = TRUE, na.last = TRUE)
#if no argument about decreasing, it is increasing order
#if na.last is true, na is at the end of the numbers. 
#if false, at the beginning.
#if no argument on na, neglect na
x[order(x$var1, x$var3),]
#sorting by var1 first. 
#if some values of var1 are the same, order by var3
library(plyr)
arrange(x,var1)#order by var1
arrange(x,desc(var1))#order by var1, decreasing


##adding variables
#if x has 3 variables
x$var4 < rnorm(5)#the 4th variable is added to x
y<-cbind(x,rnorm(5))
#the 4th vaiable is added, and the new data frame y is created.

##summary
head(x,n)#look at the first n rows of x
tail(x,n)#look at the last n ros of x
summary(x)#give the summary of x, such as median, max, min
str(x)
quantile(x,na.rm = TRUE, probs = c(0.5,075))
#setting the pecentage by probs
table(x)#tell the number of each value in x
sum(is.na(x))#the number of missing value in x
table(x$var1 %in% c("222"))#give the number of values in var1 equal to 222
x[x$var1 %in% c("22","33"),]#show all the values when var1 equal to 22 or 33
xtabs(freq~var1+var2,data = x)
ftable(x)#make large talbe easier to see
object.size(x)
print(object.size(x),units = "Mb")#show the size of x in Mb

##creating new variables
cut()
mutate()


#########dplyr: for data frame
#select: ruturn a subset of columns of a data frame
#filter: extract a subset of row from a data frame based on logical condition
#arrange: reorder rows of a data frame
#mutata: add new variables/columns or transform exsisting variables
#summarise/summarize: generate summary statistics
#rename: rename variables in data frame
library(dplyr)
#assume x is a data frame
names(x)
select(x,var1:var3)#give the var1 to var3
select(x,-(var1))#give all the var except var1
filter(x,var3 < 2)#geive all the data when var3<2
arrange(x,var2)#order by var2
x <- rename(x, newname1 =  oldname1, newname2 = oldname2)
x <- mutate(x, newvar <- var1+var2)#create a new var which is the sum of var1&var2
summarize(x,a = mean(var1), b =  max(var2))
#show the mean of var1, and the max of var2

######merge
library(data.table)
merge(x,y,all)#merge all data
library(dplyr)
arrange(join(x,y),id)#merge x and y by id
listdata <- list(x,y,z)
join_all(listdata)#merge more than 3 data frames

######editing text variables
tolower(x)#x is a character vector. change all capital into lower case
strsplit(names(x), "\\.")#change the [name.1] into [name, 1]
sub("_","",names(x))#change _ in the names of x into nothing
#sub only change the first _ in each name
gsub("_","",names(x))#change all the _ in each name
grep("bad",x$var1)#show the places where bad is included in var1
grep("bad", x$var1, value = TRUE)#return the value
library(stringr)
nchar("abc")#show how many times abc shows
paste("abc","def")#the result is "abc def"
paste0("abc","def")#"abcdef"
substr("abcdefg",1,3)
#show the 1st through 3rd characters in the string, which is abc
str_trim("ddd     ")#"ddd", remove all the spaces at the end of the string




########quiz 1
##Q1
#读取csv中某一个变量等于特定值的数量
nrow(c[which(c$VAL ==24),])



##Q3
#
library(xlsx)
rowIndex = 18 : 23
colIndex = 7 : 15#set rows and cols we need
dat <- read.xlsx("D:/RStudio/getdata-data-DATA.gov_NGAP.xlsx",
                 sheetIndex = 1, rowIndex = rowIndex, 
                 colIndex = colIndex, header = TRUE)
sum(dat$Zip * dat$Ext, na.rm=T)



##Q4
#select specific data from xml
library(XML)
download.file(url = "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml",
              destfile = "q.xml", method = "curl")
##destfile:rename the file
d <- xmlTreeParse(file = "q.xml", useInternalNodes = TRUE)
#xmlTreeParse: load the data in q.xml into d
rootNode <- xmlRoot(d)
sum(xpathSApply(doc = rootNode,path = "//zipcode",
                fun= xmlValue) == 21231)


##Q5
#fread
#calculate the mean of pwgtp15 by sex
DT <- fread("getdata-data-ss06pid.csv",header = TRUE)#fread:fast read
DT[,mean(pwgtp15),by=SEX]


###########quiz 2

##Q1
library(httr)
library(httpuv)
library(jsonlite)
#github oauth setting
myapp <- oauth_app("github",key = "58b7eb160d54cffabcc0", 
                   secret = "6af6fa56361b9c387a2b40e5299c01dbe9ff6947")
#get oauth credentials
github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)
gtoken <- config(token = github_token)
req <- GET("https://api.github.com/users/jtleek/repos", gtoken)
stop_for_status(req)
jsondata <- fromJSON(toJSON(content(req)))
subset(jsondata, name == "datasharing", select = c(created_at))

#Q4
con <- url("http://biostat.jhsph.edu/~jleek/contact.html")
htmlcode <- readLines(con)
close(con)
a <- c(nchar(htmlcode[10]),nchar(htmlcode[20]),
       nchar(htmlcode[30]),nchar(htmlcode[100]))

#Q5
q5 <- read.fwf("https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for",
               skip = 4, 
               widths = c(12,7,4,9,4,9,4,9,4))
sum(q5[,4])


#####quiz 3
#Q1
q1 <- read.csv("D:/RStudio/getting_3_1.csv")
library(dplyr)
names(q1)
dataselected <- q1[which(q1$ACR == 3 & q1$AGS ==6),]

#Q2
library(jpeg)
q2 <- readJPEG("D:/RStudio/q2.jpg",native = TRUE)
quantile(q2,na.rm = TRUE, probs = c(0.3,0.8))

#Q3

q3_1 <- read.csv("D:/RStudio/getting_3_3.csv", skip = 3)
q3_1 <- q3_1[,c(1,2,4,5)]
colnames(q3_1) <- c("CountryCode", "Rank", "Country.Name", "GDP.Value")
q3_2 <- read.csv("D:/RStudio/getting_3_3_2.csv")
library(dplyr)
q3 <- merge(q3_1,q3_2,by=c("CountryCode"))
sum(!is.na(unique(q3$Rank)))#give the number that matches
q3$Rank <- as.numeric(q3$Rank)
sortdata <- arrange(q3,desc(Rank))
sortdata[13,3]

#Q4

ig <- group_by(q3,Income.Group)
summarise(ig,mean(Rank,na.rm = TRUE))

#Q5
q3$Rankgroup <- cut(q3$Rank, breaks = 5)
table(q3$Rankgroup,q3$Income.Group)


##quiz 4
#Q1
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv",
                    destfile = "getting_4_1.csv", method = curl)
q1 <- read.csv("D:/RStudio/getting_4_1.csv")
strsplit(names(q1),split = "wgtp")[[123]]

#Q2
library(plyr)
library(dplyr)
q2 <-read.csv("D:/RStudio/getting_4_2.csv", header = TRUE, skip = 3)
#reshape data
q2 <- q2[2:191, c(1,2,4,5)]
#remove the "," in numbers
q2$US.dollars. <- gsub(",","", x = q2$US.dollars.)
q2$US.dollars. <- as.numeric(as.character(q2$US.dollars.))
mean(q2$US.dollars., na.rm = TRUE)


#Q4
q4_1 <- read.csv("D:/RStudio/getting_4_4_1.csv", header = TRUE, skip = 3)
q4_1 <- q4_1[2:327, c(1,2,4,5)]
q4_2 <- read.csv("D:/RStudio/getting_4_4_2.csv", header = TRUE)
q4 <- join(q4_1,q4_2)
sum(grepl("^[Ff]iscal(.*)[Yy]ear(.*)[Ee]nd(.)*[Jj]une", 
          q4$Special.Notes) == TRUE)


#Q5
library(quantmod)
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)
# create a data fram from amzn
amzn <- data.frame(amzn)
# count the values collected in 2012
sum(format(as.Date(x = rownames(amzn), format = "%Y-%m-%d"), "%Y") == 2012)
# count the values collected in Mondays 2012
sum(format(as.Date(x = rownames(amzn), 
                   format = "%Y-%m-%d"), "%Y%a") == "2012Mon")