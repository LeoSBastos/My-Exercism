raindrops <- function(n) {
  res = ""
  if (n %% 3 == 0) {
    res = paste(res,"Pling",sep = "")
  }
  if (n %% 5 == 0) {
    res = paste(res,"Plang",sep = "")
  }
  if (n %% 7 == 0) {
    res = paste(res,"Plong",sep = "")
  }
  if (res == "") {
    return (toString(n))
  } else {
    return (res)
  }
}