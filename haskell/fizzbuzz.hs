main :: IO ()
main = printAll $ map fizzbuzz [1..30]
    where
        printAll [] = return ()
        printAll (x:xs) = putStrLn x >> printAll xs


fizzbuzz :: Integer -> String
fizzbuzz x
    | mod x 15 == 0 = "FizzBuzz"
    | mod x 5 == 0 = "Buzz"
    | mod x 3 == 0 = "Fizz"
    | otherwise = show x
