module Calc (
    church, unchurch,
    c_succ, c_pred,
    c_if, c_iszero, c_leq,
    c_add, c_mul, c_exp, c_sub,
    -- c_div, c_rem
    ) where


-- boolean
c_if = \b -> \t -> \e -> b t e
c_true = \x -> \y -> x
c_false = \x -> \y -> y

-- integer
c_zero = \f -> \x -> x

-- operator
c_succ = \n -> \f -> \x -> f (n f x)
c_pred = \n -> \f -> \x -> n (\g -> \h -> h (g f)) (\u -> x) (\y -> y)

-- calculus on church numeral
c_add = \m -> \n -> n c_succ m
c_mul = \m -> \n -> \f -> m (n f)
c_exp = \m -> \n -> n m
c_sub = \m -> \n -> n c_pred m
--c_div = \m -> \n -> c_if (c_leq n m) (c_succ (c_div (c_sub m n) n)) c_zero
--c_rem = \m -> \n -> c_if (c_leq n m) (c_rem (c_sub m n) n) c_zero

-- logic
c_iszero = \n -> n (\x -> c_false) c_true
c_leq = \m -> \n -> c_iszero(c_sub m n)

-- converter
church n
  | n==0 = c_zero
  | otherwise = c_succ (church (n-1))
unchurch = \n -> n (+ 1) 0
