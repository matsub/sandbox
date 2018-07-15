module Math (
    gcd
    ) where

import Church
import Prelude hiding (gcd)

gcd :: Church.Number -> Church.Number -> Church.Number
gcd a b = _if (iszero b) a (gcd b (Church.mod a b))
