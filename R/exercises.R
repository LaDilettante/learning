rm(list = ls())
library(Rcpp)
Rcpp::sourceCpp("Rcpp/exercises.cpp")

cumprod(c(1, 4, 2, 2))
cumprodC(c(1, 4, 2, 2))


all(c(0, 3, 2) > 1)
allC(c(0, 3, 2) > 1)
