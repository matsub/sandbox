module Math where

import Primitive
import Prelude hiding (succ, pred, exp, div, mod, gcd)


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


-- comparison operator
iszero :: Number -> Boolean
iszero (Number n) = n (\x -> false) true

leq :: Number -> Number -> Boolean
leq m n = iszero (sub m n)


-- general algorithms
gcd :: Number -> Number -> Number
gcd a b = _if (iszero b) a (gcd b (mod a b))
