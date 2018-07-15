module Main where

import Primitive
import Math

main :: IO ()
main = do
    let a = church 3
    let b = church 5
    let sum = Math.add a b
    print(unchurch sum)
