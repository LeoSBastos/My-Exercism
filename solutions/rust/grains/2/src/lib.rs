pub fn square(s: u32) -> u64 {
    if s > 64 || s < 1{
        panic!("Square must be between 1 and 64")
    }
    let mut grains: u64 = 1;
    for _i in 1..s {
        grains*=2;
    }
    grains
}

pub fn total() -> u64 {
    let mut grains: u64 = 1;
    let mut sum: u64 = 0;
    for i in 1..=64{
        sum += grains;
        if i<64 {
            grains*= 2;
        }
    }
    sum
}
