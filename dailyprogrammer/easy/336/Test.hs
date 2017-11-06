#!/usr/bin/env stack
-- stack --resolver=lts-9.12 --install-ghc runghc --package=HUnit-1.5.0.0
module Test
  ( main
  ) where

import           Main       hiding (main)
import           Test.HUnit

main =
  runTestTT $
  TestCase $
  assertEqual
    ""
    [[4, 2], [4], [2], [7, 6, 5, 2, 1], [0], [1], [3, 3], [6], [3], [2]] $
  map
    cannibalise
    [ ([21, 9, 5, 8, 10, 1, 3], [10, 15])
    , ([3, 3, 3, 2, 2, 2, 1, 1, 1], [4])
    , ([1, 2, 3, 4, 5], [5])
    , ([10, 6, 1, 2, 8, 7, 9, 11], [3, 6, 9, 12, 15])
    , ([4, 4, 4, 4], [5])
    , ([4, 4, 4, 3], [6])
    , ([2, 2, 2, 2, 2, 2, 1, 1, 1], [4, 3])
    , ([3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1], [4])
    , ([2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1], [4])
    , ([3, 2, 2, 2, 1], [4])
    ]
