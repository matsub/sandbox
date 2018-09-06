module PrimitiveSpec (spec) where

import Test.Hspec
import Primitive


spec :: Spec
spec = do
    describe "boolean" $ do
        it "if sentence" $ do
            _if true True False `shouldBe` True
            _if false True False `shouldBe` False


    describe "convertion" $ do
        it "church and unchurch" $ do
            unchurch (church 10) `shouldBe` 10


    describe "Peano's naturals" $ do
        let x = church 8

        it "successor" $ do
            unchurch (Primitive.succ x) `shouldBe` 9
        it "predecessor" $ do
            unchurch (Primitive.pred x) `shouldBe` 7


    describe "church list" $ do
        let l = (cons 100 (cons 10 (cons 1 nil)))

        it "car church list" $ do
            car l `shouldBe` 100
        it "cdr church list" $ do
            car (cdr l) `shouldBe` 10
            car (cdr (cdr l)) `shouldBe` 1
        it "isnil" $ do
            _if (isnil nil) True False `shouldBe` True
            _if (isnil l) True False `shouldBe` False
