pub fn is_armstrong_number(num: u32) -> bool {
    let num_string = num.to_string();
    let digits_char: Vec<char> = num_string.chars().collect();
    let digits: Vec<u32> = digits_char.iter().map(|x| x.to_digit(10).unwrap()).collect();
    let count = digits.len() as u32;
    let mut sum = 0;
    for i in digits {
        sum += i.pow(count);
    }
    if sum == num{
        true
    } else {
        false
    }
}
