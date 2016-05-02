#include <stdio.h>
#include "reverse_integer.h"
int reverse(int x) {
    int remainder = 0, quotient = 0;
    int number = 0;
    int i = 0;
    int res = 0;
    int arr[12] = {};
    while( x != 0 ) {
        remainder = x % 10;
        arr[number] = remainder;

        quotient = (int) (x / 10);
        x = quotient;

        number ++;
    }

    for ( i = 0; i < number; i++ ) {
        res = res * 10 + arr[i];
    }

    return res;
}
