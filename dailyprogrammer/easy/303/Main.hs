#!/usr/bin/env stack
-- stack --resolver=lts-8.2 --install-ghc runghc

{-
Ricochet
========

- https://redd.it/5vb1wf
- Posted at: https://www.reddit.com/r/dailyprogrammer/comments/5vb1wf/20170221_challenge_303_easy_ricochet/de7323p/
- Asked for some Code Review help here: http://codereview.stackexchange.com/q/156273/131994

My journey to finding the formulas is commented beneath the code.
-}

module Main where

data Corner = UL | UR | LR | LL deriving (Show, Eq)

ricochet :: (Integral a, Fractional b) => a -> a -> a -> a -> b -> (Corner, a, b)
ricochet h w m n v
    = (c,b,fromIntegral d / v)

    where
    h' = h - m
    w' = w - n
    d  = lcm w' h'

    b  = d `div` h' + d `div` w' - 2
    c  =
        case (
            ((d `div` h' - 1) `mod` 2),
            ((d `div` w' - 1) `mod` 2)
        ) of
            (0,0) -> LR
            (0,1) -> LL
            (1,0) -> UR
            (1,1) -> UL

main :: IO ()
main = interact ( unlines
                . map (output . input . words)
                . lines
                )
    
    where
    -- How to make these less fragile and more idiomatic?
    input (h:w:m:n:v:[]) = ricochet (read h) (read w) (read m) (read n) (read v)
    output (c,b,t) = show c ++ " " ++ show b ++ " " ++ show t

{-
## Finding the Formulas

__Simplifying the bonus__

I quickly nailed the bonus "for free" thanks to a neat observation:

> If checking the top-right corner of the grid for a match,
> you only need to check the top-right corner of the moving rectangle,
> and so forth with the other corners:
>
>     UL of both      UR of both
>     @--+--------+---@
>     |oo|        |ooo|
>     |oo|        +---+
>     +--+            |
>     |               |
>     +---+          ++
>     @---+----------+@
>     LL of both      LR of both

Somehow (perhaps ironically) this helped me soon realise that:

> The two questions `10 7 3 2 1` and `7 5 0 0 1` are identical.
>
>     10 7 3 2 1    7 5 0 0 1
>     @-+-----@-+   @-------@
>     |o|     |o|   |       |
>     |o|     |o|   |       |
>     +-+     +-|   |       |
>     |       . |   |       |
>     |       . |   |       |
>     |       . |   |       |
>     @-+ . . @-+   @-------@
>     |o|     |o|   
>     |o|     |o|   
>     +-+-----+-+   

That's why the variables `h' = h - m` and `w' = w - n` are used.
They're the solution to the bonus.

__The answer__

Whilst searching for relationships between the example inputs and outputs,
I quickly discovered that the time taken (`t` for demonstration) was simply:

> `d = h' * w'`
> `t = d / v`

I also reduced the number of bounces to:

> `d / h' + d / w' - 2`

However, these formulas failed tests on other examples, like `1 2 0 0 1`.

Unfortunately, I happened to see the term "LCM" while skimming the problem page,
and thus led my train of thought went in that direction.
I'm not sure if I'd have made the connection without seeing those three letters.

It turned out my initial attempt was only correct when `h * w == lcm h w`,
which coincidentally covered each sample on the problem page.
Using `d = lcm h w` instead yielded correct results.
-}
