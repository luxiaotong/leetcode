#include <stdio.h>
#include "roman.h"

int main() {
    printf("IX: %d\n", romanToInt("IX"));
    printf("XCI: %d\n", romanToInt("XCI"));
    printf("CVIII: %d\n", romanToInt("CVIII"));
    printf("CDLXIX: %d\n", romanToInt("CDLXIX"));
    printf("CMXXVIII: %d\n", romanToInt("CMXXVIII"));
    printf("MMCDLV: %d\n", romanToInt("MMCDLV"));
    return 0;
}
