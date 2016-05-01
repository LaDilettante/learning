library(Rcpp)

cppFunction('
  int add(int x, int y, int z) {
    int sum = x + y + z;
    return sum;
  }            
')

add
add(1, 2, 3)

add(NA, 2, 3)

cppFunction('NumericVector pdistC(double x, NumericVector ys) {
  int n = ys.size();
  NumericVector out(n);

  for (i = 0; i < n; ++i) {
    out[i] = sqrt(pow(x - ys[i], 2.0))
  }
  return out;
}')

Rcpp::sourceCpp("Rcpp/timesTwo.cpp")
timesTwo(4)
timesTwo