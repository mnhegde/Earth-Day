#Created by Manu Hegde in April 2020

workingdirectory <- "C:\\Users\\manuh\\Earth-Day\\data"
setwd(workingdirectory)

startingyear <- 1949
endingyear <- 2014


data <- read.csv(file.path(workingdirectory, "nation.1751_2014.csv"))


for (year in (startingyear: endingyear)) {
    data_Manu <- data.frame()
    for (row in (5:nrow(data))) {
        if (data[row,2] == year) {
            data_Manu <- rbind(data_Manu, data[row,1:3])
        }
    }

    
    
    filename <- paste('Countries_Carbon_Dioxide_', year, '.csv', sep='')
    write.csv(data_Manu, file.path(getwd(), filename), row.names = FALSE)

}

