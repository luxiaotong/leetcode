#include <stdio.h>
#include "zigzag.h"
int main() {
    printf("%s\n", convert("PAYPALISHIRING", 3));
    printf("%s\n", convert("PAYPALISHIRING", 4));
    printf("%s\n", convert("AB", 1));
    printf("%s\n", convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 2));
    return 0;
}
