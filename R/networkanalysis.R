library(igraph)
g <- graph(c( 1,2, 2,3, 4,5, 6,7) )

g <- graph.empty()
g

g <- graph.empty(n=10)
g

f <- graph.full(3)
f

f <- graph.full(3, directed=TRUE)
f
print(f, full=TRUE)

is.directed(graph.full(10))
is.directed(graph.full(10, directed=TRUE))

big <- graph.full(1000)
summary(big)

