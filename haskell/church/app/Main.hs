module Main where

import Church

main :: IO ()
main = do
    let a = church 3
    let b = church 5
    let sum = Church.add a b
    print(unchurch sum)
