#include <stdio.h>
#include "reverse_integer.h"

int main() {
    int res = 0;
    res = reverse(1534236469);
    printf("res: %d\n", res);
    res = reverse(1);
    printf("res: %d\n", res);
    res = reverse(123);
    printf("res: %d\n", res);
    return 0;
}
