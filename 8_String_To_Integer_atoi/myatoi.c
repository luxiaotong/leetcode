#include <stdio.h>
#include <string.h>
#include <limits.h>
#include "myatoi.h"

int myAtoi(char* str) {
    int len = strlen(str);
    int i = 0;
    int rst = 0;
    int sign = 0;
    int number = 0;

    for ( i = 0; i < len; i ++ ) {
        if ( str[i] == 32 ) {
            if ( number == 0 ) {
                continue;
            } else {
                break;
            }
        }
        
        number = 1;

        if ( sign == 0 ) {
            if ( str[i] == 45 ) {
                sign = -1;
                continue;
            } else if ( str[i] == 43 ) {
                sign = 1;
                continue;
            } else {
                sign = 1;
            }
        }

        if ( str[i] >= 48 && str[i] <= 57 ) {
            if ( rst >= (INT_MAX / 10) ) {
                rst = INT_MAX;
                break;
            }
            //printf("rst1:%d\n", rst);
            rst = rst * 10 + (str[i] - '0');
            //printf("rst2:%d\n\n", rst);
        } else {
            break;
        }
    }
    
    if ( sign < 0 ) rst *= -1;
    
    return rst;
}
