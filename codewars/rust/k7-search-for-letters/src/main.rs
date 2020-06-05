fn change(s: &str) -> String {
    let relevant_chars = s
        .chars()
        .map(|c| c.to_ascii_lowercase())
        .filter(|c| *c >= 'a' && *c <= 'z');

    let mut answer = ['0'; 26];
    let a_ascii = 'a' as usize;

    for c in relevant_chars {
        answer[c as usize - a_ascii] = '1';
    }

    answer.iter().collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    // Unchanged from that at Codewars
    #[test]
    fn test_basic() {
        assert_eq!(change("a **&  bZ"), "11000000000000000000000001");
    }
}
