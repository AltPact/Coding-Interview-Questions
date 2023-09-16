fn fibonacci(n: u64) -> u64 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

fn main() {
    let n = 10; // Change this to the desired Fibonacci sequence length
    for i in 0..n {
        println!("Fibonacci({}) = {}", i, fibonacci(i));
    }
}