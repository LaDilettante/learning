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

// [[Rcpp::export]]
NumericVector cummaxC(NumericVector x) {
  
}

// You can include R code blocks in C++ files processed with sourceCpp
// (useful for testing and development). The R code will be automatically 
// run after the compilation.
//

/*** R
timesTwo(42)
*/
