#!/usr/bin/env runhaskell

{-
Spelling With Chemistry
=======================

- https://redd.it/5seexn
- Posted at: https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/ddxljoi/

I've only read the Haskell Basics and Elementary Haskell chapters
of the [Haskell Wikibook](https://en.wikibooks.org/wiki/Haskell),
so I've only been able to use things based on principles introduced there.

A notable exception is the succinct use of `interact` in `main`,
which I found [here](https://wiki.haskell.org/Haskell_IO_for_Imperative_Programmers).
-}

module Main
    ( Element(..)
    , symToEl
    , elify
    , elsToStr
    , main
    ) where

import Data.List
import Data.Char

data Element = BadSymbol
               | Element {name::String, symbol::String, weight::Double}
               deriving (Show, Eq)

symToEl :: String -> Element -- The provided string should be lowercase!
symToEl "ac" = Element "Actinium" "Ac" 227
symToEl "al" = Element "Aluminum" "Al" 26.9815
symToEl "am" = Element "Americium" "Am" 243
symToEl "sb" = Element "Antimony" "sb" 121.75
symToEl "ar" = Element "Argon" "ar" 39.948
symToEl "as" = Element "Arsenic" "as" 74.9216
symToEl "at" = Element "Astatine" "At" 210
symToEl "ba" = Element "Barium" "Ba" 137
symToEl "bk" = Element "Berkelium" "Bk" 247
symToEl "be" = Element "Beryllium" "Be" 9.0122
symToEl "bi" = Element "Bismuth" "Bi" 208.980
symToEl "b"  = Element "Boron" "B" 10.81
symToEl "br" = Element "Bromine" "Br" 79.904
symToEl "cd" = Element "Cadmium" "Cd" 112.40
symToEl "ca" = Element "Calcium" "Ca" 40.08
symToEl "Cf" = Element "Californium" "Cf" 251
symToEl "c"  = Element "Carbon" "C" 12.011
symToEl "ce" = Element "Cerium" "Ce" 140.12
symToEl "cs" = Element "Cesium" "Cs" 132.9054
symToEl "cl" = Element "Chlorine" "Cl" 35.453
symToEl "cr" = Element "Chromium" "Cr" 51.996
symToEl "co" = Element "Cobalt" "Co" 58.9332
symToEl "cu" = Element "Copper" "Cu" 63.546
symToEl "cm" = Element "Curium" "Cm" 247
symToEl "dy" = Element "Dysprosium" "Dy" 162.50
symToEl "es" = Element "Einsteinium" "Es" 254
symToEl "er" = Element "Erbium" "Er" 167.26
symToEl "eu" = Element "Europium" "Eu" 151.96
symToEl "fm" = Element "Fermium" "Fm" 257
symToEl "f"  = Element "Fluorine" "F" 18.9984
symToEl "fr" = Element "Francium" "Fr" 223
symToEl "gd" = Element "Gadolinium" "Gd" 157.25
symToEl "ga" = Element "Gallium" "Ga" 69.72
symToEl "ge" = Element "Germanium" "Ge" 72.59
symToEl "au" = Element "Gold" "Au" 196.966
symToEl "hf" = Element "Hafnium" "Hf" 178.49
symToEl "he" = Element "Helium" "He" 4.00260
symToEl "ho" = Element "Holmium" "Ho" 164.930
symToEl "h"  = Element "Hydrogen" "H" 1.0079
symToEl "in" = Element "Indium" "In" 114.82
symToEl "i"  = Element "Iodine" "I" 126.904
symToEl "ir" = Element "Iridium" "Ir" 192.22
symToEl "fe" = Element "Iron" "Fe" 55.847
symToEl "kr" = Element "Krypton" "Kr" 83.80
symToEl "la" = Element "Lanthanum" "La" 138.905
symToEl "lr" = Element "Lawrencium" "Lr" 256
symToEl "pb" = Element "Lead" "Pb" 207.2
symToEl "li" = Element "Lithium" "Li" 6.941
symToEl "lu" = Element "Lutetium" "Lu" 174.97
symToEl "mg" = Element "Magnesium" "Mg" 24.305
symToEl "mn" = Element "Manganese" "Mn" 54.9380
symToEl "md" = Element "Mendelevium" "Md" 258
symToEl "gg" = Element "Mercury" "Hg" 200.59
symToEl "mo" = Element "Molybdenum" "Mo" 95.94
symToEl "nd" = Element "Neodymium" "Nd" 144.24
symToEl "ne" = Element "Neon" "Ne" 20.179
symToEl "np" = Element "Neptunium" "Np" 237.048
symToEl "ni" = Element "Nickel" "Ni" 58.70
symToEl "nb" = Element "Niobium" "Nb" 92.9064
symToEl "n"  = Element "Nitrogen" "N" 14.0067
symToEl "no" = Element "Nobelium" "No" 255
symToEl "os" = Element "Osmium" "Os" 190.2
symToEl "o"  = Element "Oxygen" "O" 15.9994
symToEl "pd" = Element "Palladium" "Pd" 106.4
symToEl "p"  = Element "Phosphorus" "P" 30.9738
symToEl "pt" = Element "Platinum" "Pt" 195.09
symToEl "pu" = Element "Plutonium" "Pu" 244
symToEl "po" = Element "Polonium" "Po" 210
symToEl "k"  = Element "Potassium" "K" 39.098
symToEl "pr" = Element "Praseodymium" "Pr" 140.908
symToEl "pm" = Element "Promethium" "Pm" 147
symToEl "pa" = Element "Protactinium" "Pa" 231.036
symToEl "ra" = Element "Radium" "Ra" 226.025
symToEl "rn" = Element "Radon" "Rn" 222
symToEl "re" = Element "Rhenium" "Re" 186.207
symToEl "rh" = Element "Rhodium" "Rh" 102.906
symToEl "rb" = Element "Rubidium" "Rb" 85.4678
symToEl "ru" = Element "Ruthenium" "Ru" 101.07
symToEl "rf" = Element "Rutherfordium" "Rf" 261
symToEl "sm" = Element "Samarium" "Sm" 150.4
symToEl "sc" = Element "Scandium" "Sc" 44.9559
symToEl "se" = Element "Selenium" "Se" 78.96
symToEl "si" = Element "Silicon" "Si" 28.086
symToEl "ag" = Element "Silver" "Ag" 107.868
symToEl "na" = Element "Sodium" "Na" 22.9898
symToEl "sr" = Element "Strontium" "Sr" 87.62
symToEl "s"  = Element "Sulfur" "S" 32.06
symToEl "ta" = Element "Tantalum" "Ta" 180.948
symToEl "tc" = Element "Technetium" "Tc" 98.9062
symToEl "te" = Element "Tellurium" "Te" 127.60
symToEl "tb" = Element "Terbium" "Tb" 158.925
symToEl "tl" = Element "Thallium" "Tl" 204.37
symToEl "th" = Element "Thorium" "Th" 232.038
symToEl "tm" = Element "Thulium" "Tm" 168.934
symToEl "sn" = Element "Tin" "Sn" 118.69
symToEl "ti" = Element "Titanium" "Ti" 47.90
symToEl "w"  = Element "Tungsten" "W" 183.85
symToEl "u"  = Element "Uranium" "U" 238.029
symToEl "v"  = Element "Vanadium" "V" 50.9414
symToEl "xe" = Element "Xenon" "Xe" 131.30
symToEl "yb" = Element "Ytterbium" "Yb" 173.04
symToEl "y"  = Element "Yttrium" "Y" 88.9059
symToEl "zn" = Element "Zinc" "Zn" 65.38
symToEl "zr" = Element "Zirconium" "Zr" 91.22
symToEl _    = BadSymbol

elify :: String -> [Element]
elify ""   = []
elify word =
    case filter (all (/= BadSymbol)) (recurse (map toLower word)) of
        []    -> []
        [[]]  -> []
        words -> maximumBy compareBySumOfWeights words

    where
    compareBySumOfWeights :: [Element] -> [Element] -> Ordering
    compareBySumOfWeights a b = 
        let sumOfWeights els = sum [ w | Element {weight=w} <- els ]
        in  compare (sumOfWeights a) (sumOfWeights b)

    recurse :: String -> [[Element]]
    recurse ""   = [[]]
    recurse word =
        concat [ let el = symToEl sym
                 in case el of
                    BadSymbol  -> [[el]]
                    Element {} -> map (el:) (recurse remaining)
               | (sym,remaining) <- map (`splitAt` word) [1 .. length word]
               ]

elsToStr :: [Element] -> String
elsToStr els = foldl' (++) "" [ sym | Element {symbol=sym} <- els ]

main = interact (unlines . map (elsToStr . elify) . lines)
