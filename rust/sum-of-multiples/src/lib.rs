pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    let mut mult = Vec::new();
    let mut new_factors: Vec<u32> = factors.to_vec();
    new_factors.retain(|x| *x != 0);
    for x in 1..limit {
        for f in &new_factors {
            if x % f == 0 {
                if !mult.contains(&x) {
                    mult.push(x);
                }
                println!("{}", x.to_string());
            }
        }
    }
    if mult.len() == 0 {
        0
    } else {
        mult.iter().sum()
    }
}
