#include "roman.h"
#include <string.h>

int romanToInt(char* s) {
    int len = strlen(s);
    int i = 0, j = 0;
    int rst = 0;
    int valueArr[]  = {1000, 500, 100, 50, 10, 5, 1};
    char symbolArr[] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};

    for ( i = 0; i < len; i ++ ) {
        switch ( s[i] ) {
            case 'M':
                rst += 1000;
                break;
            case 'D':
                rst += 500;
                break;
            case 'C':
                if ( i < len - 1 && s[i+1] == 'M' ) {
                    rst += 900;
                    i ++;
                } else if ( i < len - 1 && s[i+1] == 'D' ) {
                    rst += 400;
                    i ++;
                } else {
                    rst += 100;
                }
                break;
            case 'L':
                rst += 50;
                break;
            case 'X':
                if ( i < len - 1 && s[i+1] == 'C' ) {
                    rst += 90;
                    i ++;
                } else if ( i < len - 1 && s[i+1] == 'L' ) {
                    rst += 40;
                    i ++;
                } else {
                    rst += 10;
                }
                break;
            case 'V':
                rst += 5;
                break;
            case 'I':
                if ( i < len - 1 && s[i+1] == 'X' ) {
                    rst += 9;
                    i ++;
                } else if ( i < len - 1 && s[i+1] == 'V' ) {
                    rst += 4;
                    i ++;
                } else {
                    rst += 1;
                }
                break;
        }
    }

    return rst;
}
