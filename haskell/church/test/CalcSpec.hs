module CalcSpec (spec) where

import Test.Hspec
import qualified Calc


spec :: Spec
spec = do
    describe "convertion" $ do
        it "church and unchurch" $ do
            Calc.unchurch (Calc.church 10) `shouldBe` 10


    describe "primitive" $ do
        let x = Calc.church 8

        it "successor" $ do
            Calc.unchurch (Calc.c_succ x) `shouldBe` 9
        it "predecessor" $ do
            Calc.unchurch (Calc.c_pred x) `shouldBe` 7


    describe "church logics" $ do
        let a = Calc.church 8
        let b = Calc.church 0

        it "iszero" $ do
            Calc.c_if(Calc.c_iszero b)(10)(0) `shouldBe` 10


    describe "church numeral calculus" $ do
        let a = Calc.church 8
        let b = Calc.church 2

        it "add two church number" $ do
            Calc.unchurch (Calc.c_add a b) `shouldBe` 10
        it "multiply two church number" $ do
            Calc.unchurch (Calc.c_mul a b) `shouldBe` 16
        it "exponent two church number" $ do
            Calc.unchurch (Calc.c_exp a b) `shouldBe` 64
--        it "exponent two church number" $ do
--            Calc.unchurch (Calc.c_sub a b) `shouldBe` 6
