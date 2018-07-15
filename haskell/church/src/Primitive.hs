{-# LANGUAGE RankNTypes #-}

module Primitive where
import Prelude hiding (succ, pred)



-- boolean
newtype Boolean = Boolean (forall f. f -> f -> f)

_if :: Boolean -> f -> f -> f
_if (Boolean b) t e = b t e

true :: Boolean
true = Boolean $ \x -> \y -> x

false :: Boolean
false = Boolean $ \x -> \y -> y


-- Church numeral
newtype Number = Number (forall f. (f -> f) -> f -> f)

church :: Integer -> Number
church 0 = zero
church n = succ (church (n-1))

unchurch :: Number -> Integer
unchurch (Number n) = n (+ 1) 0


-- natural number according to Peano's axiom
zero :: Number
zero = Number $ \f -> \x -> x

succ :: Number -> Number
succ (Number n) = Number $ \f -> \x -> f (n f x)

pred :: Number -> Number
pred (Number n) = Number $ \f -> \x -> n (\g -> \h -> h (g f)) (\u -> x) (\u -> u)


-- pair
newtype Pair a b = Pair (forall r. (a -> b -> r) -> r)

pair :: a -> b -> Pair a b
pair a b = Pair $ \p -> p a b

first :: Pair a b -> a
first (Pair p) = p (\x -> \y -> x)

second :: Pair a b -> b
second (Pair p) = p (\x -> \y -> y)


-- list
newtype List a = List (forall r . (a -> r -> r) -> r -> r)

nil :: List a
nil = List $ \x -> \y -> y

isnil :: List a -> Boolean
isnil (List xs) = xs (\h -> \t -> false) true

cons :: a -> List a -> List a
cons x (List xs) = List $ \con ni -> con x (xs con ni)

car :: List a -> a
car (List xs) = xs (\x -> \y -> x) undefined

cdr :: List a -> List a
cdr (List xs) = first (xs seconds ns)
    where ns = pair nil nil
          seconds a p = pair (second p) (cons a (second p))
