pub fn square_of_sum(n: u32) -> u32 {
    let vetor: Vec<u32> = (1..=n).collect();
    let sum: u32 = vetor.iter().sum();
    sum.pow(2)
}

pub fn sum_of_squares(n: u32) -> u32 {
    let vetor: Vec<u32> = (1..=n).collect();
    let power_vetor: Vec<u32> = vetor.iter().map( |x| x.pow(2) ).collect();
    power_vetor.iter().sum()
}

pub fn difference(n: u32) -> u32 {
    square_of_sum(n) - sum_of_squares(n)
}
