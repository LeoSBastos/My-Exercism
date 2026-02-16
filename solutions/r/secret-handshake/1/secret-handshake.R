library(R.utils)

handshake <- function(n) {
  binS = unlist(strsplit(intToBin(n), split = ""))
  len = length(binS)
  res = c()
  if(len == 1){
    if(binS == "1"){
      return (c("wink"))
    }
  }
  for (i in seq(len,1)) {
    if (binS[i:i] == "1") {
      switch(len-i+1,
       "1" = {res = c(res,"wink")},
       "2" = {res = c(res,"double blink")},
       "3" = {res = c(res,"close your eyes")},
       "4" = {res = c(res,"jump")},
       "5" = {res = rev(res)}
             )
    }
  }
  return(res)
}
