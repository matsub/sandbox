#include "include/calc.h"

namespace calc {
    int add(int m, int n) {
        if (iszero(n)) {
            return m;
        }
        return succ(add(m, pred(n)));
    }

    int sub(int m, int n) {
        if (iszero(n)) {
            return m;
        }
        return pred(sub(m, pred(n)));
    }

    int mul(int m, int n) {
        if (iszero(n)) {
            return 0;
        }
        return add(m, mul(m, pred(n)));
    }

    int div(int m, int n) {
        if (leq(n, m)) {
            return succ(div(sub(m, n), n));
        }
        return 0;
    }

    int rem(int m, int n) {
        if (leq(n, m)) {
            return rem(sub(m, n), n);
        }
        return m;
    }
} // namespace calc
