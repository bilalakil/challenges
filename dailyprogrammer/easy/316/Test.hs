#!/usr/bin/env stack
-- stack --resolver=lts-9.12 --install-ghc runghc --package=HUnit-1.5.0.0
module Test where

import           Main       hiding (main)
import           Test.HUnit

testKnightMoves =
  TestCase $
  uncurry
    (assertEqual
       "Should return the expected number of moves for each invocation.") $
  unzip $
  map
    (\(e, d) -> (e, length $ knightMoves (0, 0) d))
    [ (0, (0, 0))
    , (1, (1, 2))
    , (1, (-2, 1))
    , (2, (-4, 0))
    , (5, (8, 7))
    , (9, (13, 12)) -- FAILING
    ]

allTests = TestList [testKnightMoves]

main = runTestTT allTests
