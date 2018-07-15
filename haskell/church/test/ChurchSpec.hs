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
            Church._if(Church.iszero a)(True)(False) `shouldBe` False
            Church._if(Church.iszero b)(True)(False) `shouldBe` True
        it "leq" $ do
            Church._if(Church.leq a b)(True)(False) `shouldBe` False
            Church._if(Church.leq b a)(True)(False) `shouldBe` True
            Church._if(Church.leq a a)(True)(False) `shouldBe` True


    describe "church numeral calculus" $ do
        let a = church 8
        let b = church 3

        it "add two church number" $ do
            unchurch (Church.add a b) `shouldBe` 11
        it "multiply two church number" $ do
            unchurch (Church.mul a b) `shouldBe` 24
        it "exponent two church number" $ do
            unchurch (Church.exp a b) `shouldBe` 512
        it "subtract two church number" $ do
            unchurch (Church.sub a b) `shouldBe` 5
        it "divide two church number" $ do
            unchurch (Church.div a b) `shouldBe` 2
        it "modulus operation for church number" $ do
            unchurch (Church.mod a b) `shouldBe` 2


    describe "church list" $ do
        let l = (cons 100 (cons 10 (cons 1 nil)))

        it "car church list" $ do
            car l `shouldBe` 100
        it "cdr church list" $ do
            car (cdr l) `shouldBe` 10
            car (cdr (cdr l)) `shouldBe` 1
        it "pick tail of church list" $ do
            Church._if (isnil nil)(True)(False) `shouldBe` True
            Church._if (isnil l)(True)(False) `shouldBe` False
