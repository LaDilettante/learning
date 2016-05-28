#include <Rcpp.h>
using namespace Rcpp;


// [[Rcpp::export]]
NumericVector timesTwo(NumericVector x) {
  return x * 2;
}

// [[Rcpp::export]]
bool allC(LogicalVector x) {
  int n = x.size();
  for (int i = 0; i < n; i++) {
    if (!x[i]) return false;
  }
  return true;
}

// [[Rcpp::export]]
NumericVector cumprodC(NumericVector x) {
  NumericVector res(x.size());
  
  res[0] = x[0];
  for (int i = 1; i < x.size(); i++) {
    res[i] = res[i - 1] * x[i];
  }
  return res;
}

// [[Rcpp::export]]
NumericVector cumminC(NumericVector x) {
  int n = x.size();
  NumericVector res(n);
  
  res[0] = x[0];
  double currentMin = res[0];
  for (int i = 1; i < n; i++) {
    if (x[i] < currentMin) {
      res[i] = x[i];
      currentMin = x[i];
    } else {
      res[i] = res[i - 1];
    }
  }
  return res;
}


// cummax()
// [[Rcpp::export]]
NumericVector cummaxC(NumericVector x) {
  int n = x.size();
  NumericVector res(n);
  
  res[0] = x[0];
  double currentMax = res[0];
  for (int i = 1; i < n; i++) {
    if (x[i] > currentMax) {
      res[i] = x[i];
      currentMax = x[i];
    } else {
      res[i] = res[i - 1];
    }
  }
  return res;
}

/*** R
dat <- rnorm(100)
all(cummaxC(dat) == cummax(dat))
*/

// diff
// [[Rcpp::export]]
NumericVector diffC(NumericVector x) {
  int n = x.size();
  NumericVector res(n - 1);
  
  for (int i = 0; i < n - 1; i++) {
    res[i] = x[i + 1] - x[i];
  }
  return res;
}

/*** R
dat <- rnorm(100)
all(diffC(dat) == diff(dat))
*/


// range
// [[Rcpp::export]]
NumericVector rangeC(NumericVector x) {
  int n = x.size();
  NumericVector res(2);
  
  // Find min value
  double currentMin = x[0];
  double currentMax = x[0];
  for (int i = 0; i < n; i++) {
    currentMin = std::min(currentMin, x[i]);
    currentMax = std::max(currentMax, x[i]);
  }
  
  res[0] = currentMin;
  res[1] = currentMax;
  return(res);
}

/*** R
dat <- rnorm(100)
all(rangeC(dat) == range(dat))
*/

// var
// [[Rcpp::export]]
double varC(NumericVector x) {
  // Computing shifted data algorithm (Wikipedia)
  int n = x.size();
  double sum = 0;
  double sumsq = 0;
  double k = x[0];
  
  for (int i = 0; i < n; i++) {
    sum += x[i] - k;
    sumsq += pow(x[i] - k, 2);
  }
  
  double res = (sumsq - sum * sum / n) / (n - 1);
  return res;
}

/*** R
data <- rnorm(100)
all.equal(varC(data), var(data))
*/