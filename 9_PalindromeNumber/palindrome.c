#include "palindrome.h"
#include <stdio.h>
#include <limits.h>

bool isPalindrome(int x) {
    if ( x < 0 ) {
        return 0;
    }

    int quotient = x;
    int reverse = 0;

    while ( quotient > 0 ) {
        if ( reverse > (INT_MAX/10) ) {
            return 0;
        }
        reverse  = reverse * 10 + quotient % 10;
        quotient = quotient / 10;
    }

    return x == reverse;
}
