#!/usr/bin/env stack
-- stack --resolver=lts-8.2 --install-ghc runghc
{-
Knight's Metric
========

- https://redd.it/6coqwk
- Posted at: https://www.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/di3zkmf/ 

I tried to come up with something instead of using a search algorithm but the end result is wrong.
You can read more about the algorithm where it was posted.
-}
module Main where

import Data.List
import Text.Printf

type Point = (Int, Int)

euclideanDistance :: Point -> Point -> Float
euclideanDistance (x1, y1) (x2, y2) =
  sqrt $ fromIntegral ((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

potentialMoves =
  [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

knightMoves :: Point -> Point -> [Point]
knightMoves s@(sx, sy) d@(dx, dy)
  | s == d = []
  | otherwise = m : knightMoves n d
  where
    ((n, m):_) =
      sortOn
        (\(n@(nx, ny), _) ->
           if (dx - nx, dy - ny) `elem` potentialMoves
             then 0
             else euclideanDistance d n) $
      [((sx + x, sy + y), m) | m@(x, y) <- potentialMoves]

main :: IO ()
main = interact (unlines . map (output . input . words) . lines)
  where
    input (x:y:[]) = knightMoves (0, 0) ((read x), (read y))
    output [] = "0"
    output (points) =
      printf
        "%d\n%s"
        (length points)
        (intercalate "\n" $ map (\(x, y) -> printf "%d %d" x y) $ points)
