#include <stdio.h>
#include <stdlib.h>

#define PRECISION 1e-10

typedef struct{
    int x;
    int y;
} Vector;

// return sum of a and b
int sum(int a, int b){
    return a+b;
}

// call Mr.Hankey
void MrHankey(void){
    printf("Howdy Folks!!\n");
    return;
}

// return the `k` power of `a`
int power(int a, int k){
    if(k>0)
        return a * power(a, k-1);
    return 1;
}

// return the square root of `n`
double newton(int n){
    double x=1;
    do{
        x = x - (x*x - n)/(2 * x);
    } while((x*x-n) > PRECISION);
    return x;
}

// return scalar
double scalar(Vector v){
    return newton(power(v.x, 2) + power(v.y, 2));
}
