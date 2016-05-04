#include <stdio.h>
#include "myatoi.h"

int main() {
    printf("%d\n", myAtoi("19216811"));
    printf("%d\n", myAtoi("www.niu.com"));
    printf("%d\n", myAtoi("3334445556"));
    printf("%d\n", myAtoi("1"));
    printf("%d\n", myAtoi("010"));
    printf("%d\n", myAtoi("     +004500"));
    printf("%d\n", myAtoi("  -0012a42"));
    printf("%d\n", myAtoi("   +0 123"));
    printf("%d\n", myAtoi("2147483648"));
    printf("%d\n", myAtoi("-2147483647"));
    printf("%d\n", myAtoi("-2147483648"));
    printf("%d\n", myAtoi("-2147483649"));
}
