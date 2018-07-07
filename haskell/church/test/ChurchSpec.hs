module ChurchSpec (spec) where

import Test.Hspec
import Church


spec :: Spec
spec = do
    describe "convertion" $ do
        it "church and unchurch" $ do
            unchurch (church 10) `shouldBe` 10


    describe "primitive" $ do
        let x = church 8

        it "successor" $ do
            unchurch (Church.succ x) `shouldBe` 9
        it "predecessor" $ do
            unchurch (Church.pred x) `shouldBe` 7


    describe "church logics" $ do
        let a = church 8
        let b = church 0

        it "iszero" $ do
            Church._if(Church.iszero b)(10)(0) `shouldBe` 10


    describe "church numeral calculus" $ do
        let a = church 8
        let b = church 2

        it "add two church number" $ do
            unchurch (Church.add a b) `shouldBe` 10
        it "multiply two church number" $ do
            unchurch (Church.mul a b) `shouldBe` 16
        it "exponent two church number" $ do
            unchurch (Church.exp a b) `shouldBe` 64
        it "subtract two church number" $ do
            unchurch (Church.sub a b) `shouldBe` 6
