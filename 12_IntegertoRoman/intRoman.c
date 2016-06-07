#include "intRoman.h"
#include <stdio.h>
#include <stdlib.h>

char* intToRoman(int num) {
    int i = 0, j = 0;
    int quotient = 0;
    int divisor  = 0;
    int remainder= 0;
    int pos      = 0;
    int valueArr[]  = {1000, 500, 100, 50, 10, 5, 1};
    char symbolArr[] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
    char *romanStr = malloc( 20*sizeof(char) );

    for ( i = 0; i < 7; i ++ ) {
        divisor   = valueArr[i];
        quotient  = num / divisor;
        remainder = num % divisor;
        printf("%d\n", quotient);

        if ( quotient == 1 && i < 6 && num/valueArr[i+1] == 9 ) {
            continue;
        }

        if ( quotient == 9 ) {
            romanStr[pos++] = symbolArr[i];
            romanStr[pos++] = symbolArr[i-2];
        } else if ( quotient == 4 ) {
            romanStr[pos++] = symbolArr[i];
            romanStr[pos++] = symbolArr[i-1];
        } else {
            for ( j = 0; j < quotient; j ++ ) {
                romanStr[pos++] = symbolArr[i];
            }
        }
        romanStr[pos] = '\0';

        num = remainder;
    }

    return romanStr;
}
