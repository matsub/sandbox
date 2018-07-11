{-# LANGUAGE RankNTypes #-}

newtype Type = Type { foo :: Integer }

f :: Type -> Integer
f x = foo x

main = do
    print $ f (Type 10)
