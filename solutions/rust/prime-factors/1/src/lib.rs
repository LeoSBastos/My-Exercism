pub fn factors(n: u64) -> Vec<u64> {
    let mut factors: Vec<u64> = Vec::new();
    let mut possible_factor = 2;
    let mut valor = n;
    while valor > 1 {
        while valor % possible_factor == 0 {
            valor /= possible_factor;
            factors.push(possible_factor);
        }
        possible_factor += 1;
    }
    factors
}
