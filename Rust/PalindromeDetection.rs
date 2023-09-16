fn is_palindrome(s: &str) -> bool {
    let s = s.chars().filter(|c| c.is_alphanumeric()).collect::<String>().to_lowercase();
    let reversed = s.chars().rev().collect::<String>();
    s == reversed
}

fn main() {
    let input = "A man, a plan, a canal, Panama";
    if is_palindrome(input) {
        println!("The input is a palindrome.");
    } else {
        println!("The input is not a palindrome.");
    }
}