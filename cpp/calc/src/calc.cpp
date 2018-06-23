#include <iostream>
#include "include/calc.h"

int main() {
    std::cout
        << "16 + 4 = " << 16 + 4 << ": "
        << calc::add(16, 4)
        << std::endl;

    std::cout
        << "16 - 4 = " << 16 - 4 << ": "
        << calc::sub(16, 4)
        << std::endl;

    std::cout
        << "16 * 4 = " << 16 * 4 << ": "
        << calc::mul(16, 4)
        << std::endl;

    std::cout
        << "16 / 4 = " << 16 / 4 << ": "
        << calc::div(16, 4)
        << std::endl;

    std::cout
        << "167 % 14 = " << 167 % 14 << ": "
        << calc::rem(167, 14)
        << std::endl;

    return 0;
}
