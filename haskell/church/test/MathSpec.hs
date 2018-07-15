module MathSpec (spec) where

import Test.Hspec
import Primitive
import Math


spec :: Spec
spec = do
    describe "comparison operators" $ do
        let a = church 8
        let b = church 0

        it "iszero" $ do
            _if (iszero a) True False `shouldBe` False
            _if (iszero b) True False `shouldBe` True
        it "leq" $ do
            _if (leq a b) True False `shouldBe` False
            _if (leq b a) True False `shouldBe` True
            _if (leq a a) True False `shouldBe` True


    describe "church numeral calculus" $ do
        let a = church 8
        let b = church 3

        it "add two church number" $ do
            unchurch (Math.add a b) `shouldBe` 11
        it "multiply two church number" $ do
            unchurch (Math.mul a b) `shouldBe` 24
        it "exponent two church number" $ do
            unchurch (Math.exp a b) `shouldBe` 512
        it "subtract two church number" $ do
            unchurch (Math.sub a b) `shouldBe` 5
        it "divide two church number" $ do
            unchurch (Math.div a b) `shouldBe` 2
        it "modulus operation for church number" $ do
            unchurch (Math.mod a b) `shouldBe` 2


    describe "general algorithms" $ do
        let a1 = church 12
        let a2 = church 24
        let b = church 64

        it "gcd" $ do
            unchurch (Math.gcd a1 b) `shouldBe` 4
            unchurch (Math.gcd a2 b) `shouldBe` 8
