use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let to_lowercase_s = |c: char| {
        if !c.is_lowercase() {
            c.to_lowercase().to_string()
        } else {
            c.to_string()
        }
    };
    let wc = word.chars().map(to_lowercase_s).collect::<Vec<_>>();
    let mut swc = word.chars().map(to_lowercase_s).collect::<Vec<_>>();
    swc.sort_unstable();
    let result = possible_anagrams
        .iter()
        .filter(|&anagram| {
            let mut anagram_chars: Vec<String> = anagram.chars().map(to_lowercase_s).collect();
            let same_word = wc == anagram_chars;
            println!(
                "wc: {:?} - anagram_chars: {:?} - same_word: {:?}",
                wc, anagram_chars, same_word
            );
            anagram_chars.sort_unstable();
            println!("wc: {:?} - anagram_chars: {:?}", wc, anagram_chars);
            swc == anagram_chars && !same_word
        })
        .map(|&anagram| anagram);

    HashSet::from_iter(result)
}
