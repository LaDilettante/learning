rm(list = ls())

f_gen <- function(samplesize) {
  z = rbinom(samplesize, size = 1, prob = 0.5)
  x1 = rnorm(samplesize, 40, 10)
  x0 = rnorm(samplesize, 20, 10)
  x = x1 * z + x0 * (1 - z)
  y0 = rnorm(samplesize, 72 + 3 * sqrt(x), rep(1, samplesize))
  y1 = rnorm(samplesize, 90 + exp(0.06 * x), rep(1, samplesize))
  y = y1 * z + y0 * (1 - z)
  pd = data.frame(y, y0, y1, x, x0, x1, z)
  return(pd)
}
set.seed(6329)
pd <- f_gen(120)

x = seq(0, 60, length.out = 100)
pd_line <- data.frame(x = x,
                      y0 = 72 + 3 * sqrt(x),
                      y1 = 90 + exp(0.06 * x))

library(ggplot2)
ggplot(data = pd) +
  geom_point(aes(x, y, color = factor(z))) +
  scale_shape_discrete(solid = F) +
  geom_line(data = pd_line, aes(x, y0)) +
  geom_line(data = pd_line, aes(x, y1))

f_Ey0 <- function(x) 72 + 3 * sqrt(x) 
f_Ey1 <- function(x) 90 + exp(0.06 * x)

# res = array(NA, dim = 1000)
# for (i in 1:1000) {
#   pd_pop = f_gen(10000)
#   res[i] = with(pd_pop, mean(y1[z == 1] - y0[z == 1], na.rm=T)) # PATT  
# }



with(pd, mean(f_Ey1(x[z == 1]) - f_Ey0(x[z == 1]))) # CATT
with(pd, mean(y1[z == 1] - y0[z == 1])) # SATT

# ---- BART ----
library("BayesTree")

m = bart(x.train = pd[, c("x", "z")], y.train = pd$y, 
          x.test = data.frame(x = rep(seq(0, 60, length.out = 100), 2),
                              z = rep(c(0, 1), each = 100)))
res = data.frame(ybart = m$yhat.test.mean,
                 xbart = rep(seq(0, 60, length.out = 100), 2),
                 z = rep(c(0, 1), each = 100))

res1 = data.frame(ybart = m1$yhat.test.mean, xbart = seq(0, 60, length.out = 100))
d0 = pd[pd$z == 0, c("x", "y")]
m0 = bart(x.train = matrix(d0$x), y.train = d0$y,
          x.test = matrix(seq(0, 60, length.out = 100)))
res0 = data.frame(ybart = m0$yhat.test.mean, xbart = seq(0, 60, length.out = 100))

ggplot(data = pd) +
  geom_point(aes(x, y, color = factor(z))) +
  scale_shape_discrete(solid = F) +
  geom_line(data = pd_line, aes(x, y0)) +
  geom_line(data = pd_line, aes(x, y1)) +
  geom_line(data = res1, aes(xbart, ybart), linetype = 3) +
  geom_line(data = res0, aes(xbart, ybart), linetype = 3)

ggplot(data = pd) +
  geom_point(aes(x, y, color = factor(z))) +
  scale_shape_discrete(solid = F) +
  geom_line(data = pd_line, aes(x, y0)) +
  geom_line(data = pd_line, aes(x, y1)) +
  geom_line(data = res, aes(xbart, ybart, linetype = factor(z)))


plot(m1$yhat.train.mean ~ d1$x)
plot(m0$yhat.train.mean ~ d0$x)
