{-# LANGUAGE RankNTypes #-}

type F = forall a. a -> a
f :: F
f x = x

type G = F -> F
g :: G
g fnc x = fnc x

main = do
    print $ g f 10
