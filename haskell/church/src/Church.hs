{-# LANGUAGE RankNTypes #-}

module Church (
    church, unchurch,
    succ, pred,
    _if, iszero, --leq,
    add, mul, exp, sub,
    -- div, mod
    ) where
import Prelude hiding (succ, pred, exp, div, mod)


type Boolean = forall f. f -> f -> f
type ChurchNum = forall f. (f -> f) -> f -> f
newtype Church = Church { unChurch :: ChurchNum }


-- converter
church :: Integer -> Church
church 0 = zero
church n = succ (church (n-1))

unchurch :: Church -> Integer
unchurch n = unChurch n (+ 1) 0


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
succ n = Church $ \f -> \x -> f (unChurch n f x)

pred :: Church -> Church
pred n = Church $ \f -> \x -> unChurch n (\g -> \h -> h (g f)) (\u -> x) (\u -> u)


-- calculus on church numeral
add :: Church -> Church -> Church
add m n = Church $ \f -> \x -> unChurch m f (unChurch n f x)

mul :: Church -> Church -> Church
mul m n = Church $ \f -> unChurch m (unChurch n f)

exp :: Church -> Church -> Church
exp m n = Church $ (unChurch n) (unChurch m)

sub :: Church -> Church -> Church
sub m n = unChurch n pred m

--div = \m -> \n -> _if (leq n m) (succ (div (sub m n) n)) zero
--mod = \m -> \n -> _if (leq n m) (mod (sub m n) n) zero


-- logic
iszero :: Church -> Boolean
iszero n = unChurch n (\x -> false) true
--leq m n = iszero(sub m n)
