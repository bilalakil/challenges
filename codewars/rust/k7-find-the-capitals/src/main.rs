struct Capital<'a> {
    country: Option<&'a str>,
    state: Option<&'a str>,
    capital: &'a str,
}

impl<'a> Capital<'a> {
    fn new_country(capital: &'a str, country: &'a str) -> Capital<'a> {
        Capital {
            country: Some(country),
            state: None,
            capital: capital,
        }
    }
    fn new_state(capital: &'a str, state: &'a str) -> Capital<'a> {
        Capital {
            country: None,
            state: Some(state),
            capital: capital,
        }
    }
}

fn capital(capitals: &[Capital]) -> Vec<String> {
    capitals
        .iter()
        .map(
            |Capital {
                 country,
                 state,
                 capital,
             }| {
                format!(
                    "The capital of {} is {}",
                    country.unwrap_or_else(|| state.unwrap()),
                    capital
                )
            },
        )
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    // `test_basic` is unchanged from that at Codewars
    #[test]
    fn test_basic() {
        let state_capitals = &[Capital::new_state("Augusta", "Maine")];
        let country_capitals = &[Capital::new_country("Madrid", "Spain")];
        let mixed_capitals = &[
            Capital::new_state("Augusta", "Maine"),
            Capital::new_country("Madrid", "Spain"),
        ];
        assert_eq!(
            capital(state_capitals).get(0).unwrap(),
            "The capital of Maine is Augusta",
        );
        assert_eq!(
            capital(country_capitals).get(0).unwrap(),
            "The capital of Spain is Madrid",
        );
        assert_eq!(
            capital(mixed_capitals),
            vec![
                "The capital of Maine is Augusta".to_string(),
                "The capital of Spain is Madrid".to_string(),
            ]
        );
    }
}
