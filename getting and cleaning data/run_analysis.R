library(dplyr)
#read data
test_x <- read.table("D:/RStudio/UCI HAR Dataset/test/X_test.txt",
                   sep = "",quote = "\"")
test_y <- read.table("D:/RStudio/UCI HAR Dataset/test/y_test.txt",
                     sep = "", quote = "\"")
test_subject <- read.table("D:/RStudio/UCI HAR Dataset/test/subject_test.txt",
                           sep = "",quote = "\"")
train_x <- read.table("D:/RStudio/UCI HAR Dataset/train/X_train.txt",
                      sep = "", quote = "\"")
train_y <- read.table("D:/RStudio/UCI HAR Dataset/train/y_train.txt",
                      sep = "", quote = "\"")
train_subject <- read.table("D:/RStudio/UCI HAR Dataset/train/subject_train.txt",
                            sep = "", quote = "\"")

features <- read.table("D:/RStudio/UCI HAR Dataset/features.txt",
                       sep = "", quote = "\"")
activity_labels <- read.table("D:/RStudio/UCI HAR Dataset/activity_labels.txt",
                              sep = "", quote = "\"")

#give names to each variable
colnames(activity_labels) <- c("V1","activity")
colnames(test_x) <- features[,2]
colnames(train_x) <- features[,2]
test_subject <- rename(test_subject, subject = V1)
train_subject <- rename(train_subject, subject = V1)

#merge train data
train1 <- cbind(train_y, train_subject)
train <- merge(train1, activity_labels, by = "V1")
train2 <- cbind(train, train_x)[,-1]

#extract the measurements on the mean 
#and standard deviation for each measurement
train3 <- select(train2, contains("subject"), contains("mean"),
                 contains("activity"),contains("std"))

#merge test data
test <- cbind(test_y, test_subject)
test1 <- merge(test, activity_labels, by = "V1")
test2 <- cbind(test1, test_x)[,-1]

#extract the measurements on the mean 
#and standard deviation for each measurement
test3 <- select(test2, contains("subject"), contains("mean"),
                 contains("activity"),contains("std"))

#merge train data and test data
d <- rbind(train3, test3)

#calculate means
result <- (d %>%
             group_by(activity, subject) %>%
           summarise_each(funs(mean)) )

#create a new file
write.table(result, file = "D:/RStudio/getting_cleaning_data_program.txt", 
            row.names = FALSE)