#!/usr/bin/env stack
-- stack --resolver=lts-8.2 --install-ghc runghc --package=HUnit-1.5.0.0

module Test where 

import Test.HUnit
import Main hiding (main)

-- What's a more idiomatic way of doing this?
applyRicochet (e,i) = (e,(\ (h,w,m,n,v) -> ricochet h w m n v) i)

testRicochetBasicCases =
    TestCase $
        uncurry (assertEqual "Should return the expected tuple for each invocation.") $
            unzip $ map applyRicochet
                [((LR,0,1)  ,(1,1,0,0,1))
                ,((LR,0,2)  ,(2,2,0,0,1))
                ,((LR,0,4)  ,(4,4,0,0,1))
                ,((LL,1,2)  ,(2,1,0,0,1))
                ,((UR,1,2)  ,(1,2,0,0,1))
                ,((LL,1,4)  ,(4,2,0,0,1))
                ,((UR,1,4)  ,(2,4,0,0,1))
                ,((LR,2,6)  ,(2,6,0,0,1))
                ,((LR,2,6)  ,(6,2,0,0,1))
                ,((LL,3,8)  ,(8,2,0,0,1))
                ,((UR,3,8)  ,(2,8,0,0,1))
                ,((LL,9,24) ,(8,3,0,0,1))
                ,((UR,17,60),(15,4,0,0,1))
                ,((LR,10,35),(7,5,0,0,1))
                ]

testRicochetVelocityCases =
    TestCase $
        uncurry (assertEqual "Should return the expected tuple for each invocation.") $
            unzip $ map applyRicochet
                [((LR,0,1/4)  ,(1,1,0,0,4))
                ,((LR,0,2/3)  ,(2,2,0,0,3))
                ,((LR,0,4/2)  ,(4,4,0,0,2))
                ,((LL,1,2/4)  ,(2,1,0,0,4))
                ,((UR,1,2/3)  ,(1,2,0,0,3))
                ,((LL,1,4/2)  ,(4,2,0,0,2))
                ,((UR,1,4/4)  ,(2,4,0,0,4))
                ,((LR,2,6/3)  ,(2,6,0,0,3))
                ,((LR,2,6/2)  ,(6,2,0,0,2))
                ,((LL,3,8/4)  ,(8,2,0,0,4))
                ,((UR,3,8/3)  ,(2,8,0,0,3))
                ,((LL,9,24/2) ,(8,3,0,0,2))
                ,((UR,17,60/4),(15,4,0,0,4))
                ,((LR,10,35/3),(7,5,0,0,3))
                ]

testRicochetShapedVelocityCases =
    TestCase $
        uncurry (assertEqual "Should return the expected tuple for each invocation.") $
            unzip $ map applyRicochet
                [((LR,0,1/1)  ,(3,4,2,3,1))
                ,((LR,0,2/2)  ,(2,5,0,3,2))
                ,((LR,0,4/4)  ,(5,5,1,1,4))
                ,((LL,1,2/1)  ,(4,1,2,0,1))
                ,((UR,1,2/2)  ,(5,5,4,3,2))
                ,((LL,1,4/4)  ,(5,10,1,8,4))
                ,((UR,1,4/1)  ,(4,11,2,7,1))
                ,((LR,2,6/2)  ,(5,12,3,6,2))
                ,((LR,2,6/4)  ,(10,7,4,5,4))
                ,((LL,3,8/1)  ,(13,5,5,3,1))
                ,((UR,3,8/2)  ,(8,10,6,2,2))
                ,((LL,9,24/4) ,(15,4,7,1,4))
                ,((UR,17,60/1),(15,15,0,11,1))
                ,((LR,10,35/2),(35,35,28,30,2))
                ]

allTests = TestList
    [ testRicochetBasicCases
    , testRicochetVelocityCases
    , testRicochetShapedVelocityCases
    ]

main = runTestTT allTests
