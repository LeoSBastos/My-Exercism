# This is a stub function to take two strings
# and calculate the hamming distance
chars <- function(string) {
  return (strsplit(string, "")[[1]])
}
hamming <- function(strand1, strand2) {
  stopifnot(nchar(strand1) == nchar(strand2))
  return (sum(chars(strand1) != chars(strand2)))
}
