fn is_anagram(str1: &str, str2: &str) -> bool {
    let mut s1 = str1.chars().collect::<Vec<_>>();
    let mut s2 = str2.chars().collect::<Vec<_>>();

    s1.sort();
    s2.sort();

    s1 == s2
}

fn main() {
    let str1 = "listen";
    let str2 = "silent";

    if is_anagram(str1, str2) {
        println!("{} and {} are anagrams.", str1, str2);
    } else {
        println!("{} and {} are not anagrams.", str1, str2);
    }
}