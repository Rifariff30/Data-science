library(class)
set.seed(1)
survey <- read.csv("survey.csv", stringsAsFactors = TRUE)
student <- data.frame(X = 5, Y = 7)
survey1 <- survey[, c("X", "Y")]
pred <- knn(train = survey1, test = student, cl = survey$Z, k = 3)
cat("Predicted Classification of Student:\n")
print(pred)