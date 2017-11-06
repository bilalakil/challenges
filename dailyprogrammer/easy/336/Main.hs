#!/usr/bin/env stack
-- stack --resolver=lts-9.12 --install-ghc runghc
{-
Cannibal numbers
=======================

- https://redd.it/76qk58
- Posted at: https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/dpekqn0/

Sorts the input and makes the largest numbers eat the smallest, one at a time.

Maintains a list of "cannibalised" numbers (and their cannibals)
in case a switch needs to be made
(i.e. for a 3 to eat a 2 instead of a 1, such to make room for another 2 to eat a 1).

Unfortunately it's quite inefficient due to the recurring `sortBy s` of that list,
which could have been improved by using some kind of cursor.
-}
module Main
  ( main
  , cannibalise
  ) where

import           Data.List
import           Data.Ord

cannibalise :: ([Int], [Int]) -> [Int]
cannibalise (ns, qs) = map (recurse sns 0 []) qs
  where
    sns = sortBy (comparing Down) ns

recurse :: [Int] -> Int -> [(Int, Int)] -> Int -> Int
recurse ns c us q =
  case ns of
    (f:l)
      | f >= q -> recurse l (c + 1) us q
      | ll < 1 -> c
      | f > last l -> recurse ((f + 1) : init l) c ((f, last l) : us) q
      | otherwise ->
        case sortBy s us of
          ((fus, sus):tus)
            | f < fus && f > sus ->
              recurse ((f + 1) : init l) c ((fus, f) : (f, sus) : tus) q
            | otherwise -> c
          _ -> c
      where ll = length l
            s (fx, sx) (fy, sy)
              | sx == sy = compare fy fx
              | otherwise = compare sx sy
    _ -> c

main = interact io
  where
    io i =
      case lines i of
        (_:ns:qs:_) ->
          show $ cannibalise (map read (words ns), map read (words qs))
