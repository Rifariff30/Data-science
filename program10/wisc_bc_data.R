set.seed(100)
wisc_bc_data <- read.csv("wisc_bc_data.csv")
wisc_bc_data2 <- wisc_bc_data[, !(names(wisc_bc_data) %in% c("id", "diagnosis"))]
wisc_bc_data2 <- data.frame(lapply(wisc_bc_data2, as.numeric))
wisc_bc_data_clusters <- kmeans(wisc_bc_data2, centers = 2, nstart = 25)
print(wisc_bc_data_clusters)
print(table(wisc_bc_data$diagnosis, wisc_bc_data_clusters$cluster))