fn encrypt_word(word: &str) -> String {
    let chars = word.chars().collect::<Vec<_>>();
    let len = chars.len();
    let mut out = String::new();

    out += &(chars[0] as u32).to_string();
    if len > 1 {
        out.push(chars[len - 1]);
    }
    if len > 3 {
        out += &chars[2..len - 1].into_iter().collect::<String>();
    }
    if len > 2 {
        out.push(chars[1]);
    }

    out
}

fn encrypt_this(i: &str) -> String {
    i.split(' ').map(encrypt_word).collect::<Vec<_>>().join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    // Tests left as is
    #[test]
    fn test_basic() {
        assert_eq!(encrypt_this(&"A"), "65".to_string());
        assert_eq!(
            encrypt_this(&"A wise old owl lived in an oak"),
            "65 119esi 111dl 111lw 108dvei 105n 97n 111ka".to_string()
        );
        assert_eq!(
            encrypt_this(&"The more he saw the less he spoke"),
            "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp".to_string()
        );
        assert_eq!(
            encrypt_this(&"The less he spoke the more he heard"),
            "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare".to_string()
        );
        assert_eq!(
            encrypt_this(&"Why can we not all be like that wise old bird"),
            "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri".to_string()
        );
        assert_eq!(
            encrypt_this(&"Thank you Piotr for all your help"),
            "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple".to_string()
        );
    }
}
