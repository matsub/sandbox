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
newtype Church = Church { churched :: forall f. (f -> f) -> f -> f }

church :: Integer -> Church
church 0 = zero
church n = succ (church (n-1))

unchurch :: Church -> Integer
unchurch n = churched n (+ 1) 0


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
cdr (List xs) = first (xs ss nn)
    where nn = pair nil nil
          ss a p = pair (second p) (cons a (second p))
