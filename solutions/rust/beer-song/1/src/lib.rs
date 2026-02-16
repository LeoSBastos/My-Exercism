pub fn verse(n: u32) -> String {
    if n > 2 {
        return format!("{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n", n.to_string(), n.to_string(), (n-1).to_string())
    } else if n == 2 {
        return format!("{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottle of beer on the wall.\n", n.to_string(), n.to_string(), (n-1).to_string())
    }
    if n == 1 {
        return format!("{} bottle of beer on the wall, {} bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n", n.to_string(), n.to_string())
    } else {
        "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n".to_string()
    }
}

pub fn sing(start: u32, end: u32) -> String {
    let mut res = "".to_string();
    for i in (end..=start).rev()  {
        if i == end{
            res += &verse(i);
        } else {
            res += &(verse(i) + "\n");
        }
    }
    res
}
