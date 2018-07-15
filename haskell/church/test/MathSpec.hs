module MathSpec (spec) where

import Test.Hspec
import Church
import Math


spec :: Spec
spec = do
    describe "general algorithms" $ do
        let a1 = church 12
        let a2 = church 24
        let b = church 64

        it "gcd" $ do
            unchurch (Math.gcd a1 b) `shouldBe` 4
            unchurch (Math.gcd a2 b) `shouldBe` 8
