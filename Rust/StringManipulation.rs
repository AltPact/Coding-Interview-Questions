fn count_characters(input: &str) -> usize {
    input.len()
}

fn find_substrings(input: &str, substring: &str) -> usize {
    input.matches(substring).count()
}

fn reverse_words(input: &str) -> String {
    let words: Vec<&str> = input.split_whitespace().collect();
    let reversed_words: Vec<String> = words.iter().map(|word| word.chars().rev().collect()).collect();
    reversed_words.join(" ")
}

fn main() {
    let input_str = "Hello, World!";
    println!("{}", count_characters(input_str)); // Output: 13

    // Reverse word call
    input_str = "Hello, World!";
    println!("{}", reverse_words(input_str)); // Output: "olleH, dlroW!"

    // Find Substring call
    input_str = "Hello, World! Hello, Rust!";
    let substring = "Hello";
    println!("{}", find_substrings(input_str, substring)); // Output: 2
}