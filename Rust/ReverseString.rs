fn reverse_string(input: &str) -> String {
    let reversed: String = input.chars().rev().collect();
    return reversed;
}

fn main() {
    let input_str = "Hello, World!";
    let reversed_str = reverse_string(input_str);
    println!("Reversed: {}", reversed_str);
}