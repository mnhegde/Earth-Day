#Created by Manu Hegde in April 2020

workingdirectory <- "C:\\Users\\manuh\\Earth-Day\\data"
setwd(workingdirectory)

startingyear <- 2001
endingyear <- 2018


data <- read.csv(file.path(workingdirectory, 'ObservationData_gkvbmnf.csv'))


for (year in (startingyear: endingyear)) {
    data_Manu <- data.frame()
    for (row in (5:nrow(data))) {
        if (data[row,5] == year) {
            data_Manu <- rbind(data_Manu, data[row,c(1,5,6)])
        }
    }

    
    
    filename <- paste('Countries_Agriculture_', year, '.csv', sep='')
    write.csv(data_Manu, file.path(getwd(), filename), row.names = FALSE)

}

