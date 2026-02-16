fizz_buzz <- function(input) {
  res = c()
  for (i in 1:input) {
    if (i %% 3 == 0) {
      if (i %% 5 == 0) {
        res = c(res,"Fizz Buzz")
      } else{
        res = c(res,"Fizz")
      }
    } else if (i %% 5 == 0) {
      res = c(res,"Buzz")
    } else {
      res = c(res,as.character(i))
    }
  }
  res
}
