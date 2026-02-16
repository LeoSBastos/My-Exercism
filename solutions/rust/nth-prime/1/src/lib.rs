pub fn is_prime(p: u32) -> bool {
    if p < 2 {
        false
    } else if p == 2 {
        true
    } else {
        for t in 2..p {
            if p % t == 0 {
                return false;
            }
        }
        true
    }
}

pub fn nth(n: u32) -> u32 {
    let mut counter = 0;
    let mut prime_number = 2;
    loop {
        if is_prime(prime_number) {
            if counter == n {
                break prime_number;
            } else {
                counter += 1;
            }
        }
        prime_number += 1;
    }
}
