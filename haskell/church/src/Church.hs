{-# LANGUAGE RankNTypes #-}

module Church (
    church, unchurch,
    succ, pred,
    _if, iszero, leq,
    add, mul, exp, sub,
    div, mod
    ) where
import Prelude hiding (succ, pred, exp, div, mod)


type Boolean = forall f. f -> f -> f
type Number = forall f. (f -> f) -> f -> f
newtype Church = Church { churched :: Number }


-- Church numeral
church :: Integer -> Church
church 0 = zero
church n = succ (church (n-1))

unchurch :: Church -> Integer
unchurch n = churched n (+ 1) 0


-- boolean
_if :: Boolean -> f -> f -> f
_if b t e = b t e

true :: Boolean
true = \x -> \y -> x

false :: Boolean
false = \x -> \y -> y


-- integer
zero :: Church
zero = Church $ \f -> \x -> x


-- operator
succ :: Church -> Church
succ n = Church $ \f -> \x -> f (churched n f x)

pred :: Church -> Church
pred n = Church $ \f -> \x -> churched n (\g -> \h -> h (g f)) (\u -> x) (\u -> u)


-- calculus on church numeral
add :: Church -> Church -> Church
add m n = Church $ \f -> \x -> churched m f (churched n f x)

mul :: Church -> Church -> Church
mul m n = Church $ \f -> churched m (churched n f)

exp :: Church -> Church -> Church
exp m n = Church $ (churched n) (churched m)

sub :: Church -> Church -> Church
sub m n = churched n pred m

div :: Church -> Church -> Church
div m n = _if (leq n m) (succ (div (sub m n) n)) zero

mod :: Church -> Church -> Church
mod m n = _if (leq n m) (mod (sub m n) n) m


-- logic
iszero :: Church -> Boolean
iszero n = churched n (\x -> false) true

leq :: Church -> Church -> Boolean
leq m n = iszero(sub m n)
