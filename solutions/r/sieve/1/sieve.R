sieve <- function(limit) {
  vetorPrimes = c()
  if(limit >= 2){
  vetorMultiplos = c()
  for (i in seq(2,limit)) {
    if (i %in% vetorMultiplos) {
      next
    }
    for (j in seq(i+1,limit)) {
      if (j %% i == 0) {
        vetorMultiplos = c(vetorMultiplos, j)
      }
    }
    vetorPrimes = c(vetorPrimes,i)
    }
  }
  return (vetorPrimes)
}
