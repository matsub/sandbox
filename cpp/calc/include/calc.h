// vim: set ft=cpp:
#ifndef CALC_H
#define CALC_H

namespace calc {
    /* primitive.cpp */
    int succ(int x);
    int pred(int x);
    bool iszero(int x);
    /* logic.cpp */
    bool leq(int m, int n);
    /* calc.cpp */
    int add(int m, int n);
    int sub(int m, int n);
    int mul(int m, int n);
    int div(int m, int n);
    int rem(int m, int n);
}

#endif /* CALC_H */
