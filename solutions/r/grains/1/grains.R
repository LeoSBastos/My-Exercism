square <- function(n) {
    if (n > 64 || n < 1) {
        stop();
    }
    grains <- 1;
    if(n != 1) {
        for (i in seq(1,n-1)) { 
            grains <- grains * 2;
        }
    }
    return (grains)
}

total <- function() {
    grains <- 1;
    vetor <- c();
    for (i in seq(1,64)) {
        vetor <- c(vetor,grains);
        if (i < 64) {
            grains <- grains * 2;
        }
    }
    return (sum(vetor))
}

    