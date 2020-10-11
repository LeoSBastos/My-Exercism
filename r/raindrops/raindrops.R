raindrops <- function(n) {
  res = ""
  if (n %% 3 == 0) {
    res = paste0(res,"Pling")
  }
  if (n %% 5 == 0) {
    res = paste0(res,"Plang")
  }
  if (n %% 7 == 0) {
    res = paste0(res,"Plong")
  }
  if (res == "") {
    return (as.character(n))
  } else {
    return (res)
  }
}