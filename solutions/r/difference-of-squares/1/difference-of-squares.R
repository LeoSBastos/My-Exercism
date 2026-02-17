# this is a stub function that takes a n
# and should return the difference-of-squares as described
# in the README.md
square_of_sum <- function(n) {
    return (sum(seq(1,n))^2)
}

sum_of_squares <- function(n) {
    return (sum(seq(1,n)^2))
}

difference_of_squares <- function(n) {
    return (square_of_sum(n) - sum_of_squares(n))
}