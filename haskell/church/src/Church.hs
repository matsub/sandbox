{-# LANGUAGE RankNTypes #-}

module Church (
    church, unchurch,
    succ, pred,
    _if, iszero, leq,
    add, mul, exp, sub, div, mod,
    cons, nil, isnil, car, cdr,
    ) where
import Prelude hiding (succ, pred, exp, div, mod, map)



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


-- integer
zero :: Number
zero = Number $ \f -> \x -> x


-- operator
succ :: Number -> Number
succ (Number n) = Number $ \f -> \x -> f (n f x)

pred :: Number -> Number
pred (Number n) = Number $ \f -> \x -> n (\g -> \h -> h (g f)) (\u -> x) (\u -> u)


-- calculus on church numeral
add :: Number -> Number -> Number
add (Number m) (Number n) = Number $ \f -> \x -> m f (n f x)

mul :: Number -> Number -> Number
mul (Number m) (Number n) = Number $ \f -> m (n f)

exp :: Number -> Number -> Number
exp (Number m) (Number n) = Number $ n m

sub :: Number -> Number -> Number
sub m (Number n) = n pred m

div :: Number -> Number -> Number
div m n = _if (leq n m) (succ (div (sub m n) n)) zero

mod :: Number -> Number -> Number
mod m n = _if (leq n m) (mod (sub m n) n) m


-- logic
iszero :: Number -> Boolean
iszero (Number n) = n (\x -> false) true

leq :: Number -> Number -> Boolean
leq m n = iszero(sub m n)


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
