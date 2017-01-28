#!/usr/bin/env runhaskell

module Test where 

import Test.HUnit
import Main hiding (main)

{-
Note that the `elify` tests depend on the available Elements -
changing that list would have dire effects.

The list is, at the date of 2017/02/19
matching that in [the problem](https://redd.it/5seexn).
-}

bacon =
    [ Element "Boron" "B" 10.81
    , Element "Actinium" "Ac" 227
    , Element "Oxygen" "O" 15.9994
    , Element "Nitrogen" "N" 14.0067
    ]

poison = 
    [ Element "Polonium" "Po" 210
    , Element "Iodine" "I" 126.904
    , Element "Sulfur" "S" 32.06
    , Element "Oxygen" "O" 15.9994
    , Element "Nitrogen" "N" 14.0067
    ]

sickness =
    [ Element "Sulfur" "S" 32.06
    , Element "Iodine" "I" 126.904
    , Element "Carbon" "C" 12.011
    , Element "Potassium" "K" 39.098
    , Element "Nitrogen" "N" 14.0067
    , Element "Einsteinium" "Es" 254
    , Element "Sulfur" "S" 32.06
    ]

ticklish =
    [ Element "Titanium" "Ti" 47.90
    , Element "Carbon" "C" 12.011
    , Element "Potassium" "K" 39.098
    , Element "Lithium" "Li" 6.941
    , Element "Sulfur" "S" 32.06
    , Element "Hydrogen" "H" 1.0079
    ]

testElifyBlank =
    TestCase $ assertEqual
        "Should return empty List for blank String"
        [] (elify "")

testElifyNumerical =
    TestCase $ assertEqual
        "Should return empty List for numerical String"
        [] (elify "999")

testElifyHasNumber =
    TestCase $ assertEqual
        "Should return empty List for String which contains a number"
        [] (elify "bacon999")

testElifyBacon =
    TestCase $ assertEqual
        "Should return the expected List provided \"bacon\" as input"
        bacon (elify "bacon")

testElifyPoison =
    TestCase $ assertEqual
        "Should return the expected List provided \"poison\" as input"
        poison (elify "poison")

testElifySickness =
    TestCase $ assertEqual
        "Should return the expected List provided \"sickness\" as input"
        sickness (elify "sickness")

testElifyTicklish =
    TestCase $ assertEqual
        "Should return the expected List provided \"ticklish\" as input"
        ticklish (elify "ticklish")

testElifyCaseInsensitive =
    TestCase $ assertEqual
        "Should return the same List provided \"bacon\" or \"BaCoN\""
        (elify "bacon") (elify "BaCoN")

testElsToStrEmpty =
    TestCase $ assertEqual
        "Should return a blank String provided an empty List"
        "" (elsToStr [])

testElsToStrOnlyBad =
    TestCase $ assertEqual
        "Should return a blank String provided a List with only BadSymbols"
        "" (elsToStr [BadSymbol,BadSymbol])

testElsToStrBacon =
    TestCase $ assertEqual
        "Should return the expected String provided bacon's elements."
        "BAcON" (elsToStr bacon)

testElsToStrPoison =
    TestCase $ assertEqual
        "Should return the expected String provided poison's elements."
        "PoISON" (elsToStr poison)

testElsToStrSickness =
    TestCase $ assertEqual
        "Should return the expected String provided sickness' elements."
        "SICKNEsS" (elsToStr sickness)

testElsToStrTicklish =
    TestCase $ assertEqual
        "Should return the expected String provided ticklish's elements."
        "TiCKLiSH" (elsToStr ticklish)

testElsToStrWithBads =
    TestCase $ assertEqual
        "Should return the expected String provided a List with good and bad elements."
        "BAcON" (elsToStr
            [ Element "Boron" "B" 10.81
            , BadSymbol
            , Element "Actinium" "Ac" 227
            , BadSymbol
            , Element "Oxygen" "O" 15.9994
            , BadSymbol
            , Element "Nitrogen" "N" 14.0067
            ])

allTests = TestList
    [ testElifyBlank
    , testElifyNumerical
    , testElifyHasNumber
    , testElifyBacon
    , testElifyPoison
    , testElifySickness
    , testElifyTicklish
    , testElifyCaseInsensitive
    , testElsToStrEmpty
    , testElsToStrOnlyBad
    , testElsToStrBacon
    , testElsToStrPoison
    , testElsToStrSickness
    , testElsToStrTicklish
    , testElsToStrWithBads
    ]

main = runTestTT allTests
