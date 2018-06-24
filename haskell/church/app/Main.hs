module Main where

import Calc

main :: IO ()
main = do
    let a = church 3
    let b = church 5
    let sum = c_add a b
    print(unchurch sum)
