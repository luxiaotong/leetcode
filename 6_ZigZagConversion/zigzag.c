#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "zigzag.h"

char *convert(char *s, int numRows) {
    int i = 0, j = 0, row = 0;
    int len = strlen(s);
    int step = numRows > 2 ? 2 : 1;
    char *res = malloc(len * sizeof(char));
    for ( row = 0; row < numRows; row++ ) {
        int  count = 0;
        //printf("row: %d\n", row);
        for ( i = row; i < len; i += step ) {
            if ( count == 0 || count == numRows - row - 1 ) {
                //printf("%d, %c, count:%d\n", i, *(s+i), count);
                *(res + j) = *(s + i);
                j++;
            }
            //printf("count:%d\n", count);
            if ( count == numRows - step) {
                count = 0;
            } else {
                count++;
            }
            //printf("count:%d\n", count);
        }
        //printf("\n");
    }
    return res;
}
