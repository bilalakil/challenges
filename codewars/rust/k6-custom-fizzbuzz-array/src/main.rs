const OUT_LEN: usize = 100;

fn fizz_buzz_custom_solver(
    string_one: &str,
    string_two: &str,
    num_one: usize,
    num_two: usize,
) -> Vec<String> {
    (1..=OUT_LEN)
        .map(|n| {
            let mut out = String::new();
            if n % num_one == 0 {
                out += string_one;
            }
            if n % num_two == 0 {
                out += string_two;
            }
            if out.len() == 0 {
                out = n.to_string();
            }
            out
        })
        .collect()
}

#[macro_export]
macro_rules! fizz_buzz_custom {
    () => {
        fizz_buzz_custom_solver("Fizz", "Buzz", 3, 5)
    };
    ($str_one:expr) => {
        fizz_buzz_custom_solver($str_one, "Buzz", 3, 5)
    };
    ($str_one:expr, $str_two:expr) => {
        fizz_buzz_custom_solver($str_one, $str_two, 3, 5)
    };
    ($str_one:expr, $str_two:expr, $num_one:expr) => {
        fizz_buzz_custom_solver($str_one, $str_two, $num_one, 5)
    };
    ($str_one:expr, $str_two:expr, $num_one:expr, $num_two:expr) => {
        fizz_buzz_custom_solver($str_one, $str_two, $num_one, $num_two)
    };
}

#[cfg(test)]
mod tests {
    use super::*;

    // Unchanged from that at Codewars
    #[test]
    fn test_basic() {
        assert_eq!(fizz_buzz_custom!()[3], "4".to_string());
        assert_eq!(fizz_buzz_custom!()[15], "16".to_string());
    }

    #[test]
    fn tests() {
        assert_eq!(fizz_buzz_custom!()[15], "16".to_string());
        assert_eq!(fizz_buzz_custom!()[44], "FizzBuzz".to_string());
        assert_eq!(fizz_buzz_custom!()[99], "Buzz".to_string());
        assert_eq!(fizz_buzz_custom!("Hey", "There")[25], "26".to_string());
        assert_eq!(fizz_buzz_custom!("Hey", "There")[11], "Hey".to_string());
        assert_eq!(
            fizz_buzz_custom!("What's ", "up?", 3, 7)[83],
            "What's up?".to_string()
        );
    }
}
