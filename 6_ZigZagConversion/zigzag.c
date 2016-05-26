#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "zigzag.h"

char *convert(char *s, int numRows) {
    int i = 0, j = 0, row = 0;
    int len = strlen(s);
    char *res = malloc((len+1) * sizeof(char));
    bzero(res, (len+1) * sizeof(char));

    if ( numRows == 1 ) {
        return s;
    }
    for ( row = 0; row < numRows; row++ ) {
        int  count = 0;
        for ( i = row; i < len; i += 2 ) {
            if ( count == 0 || count == (numRows - row - 1) ) {
                res[j] = s[i];
                j++;
            }
            if ( count == (numRows - 1 - 1 ) ) {
                count = 0;
            } else {
                count++;
            }
        }
    }
    return res;
}
