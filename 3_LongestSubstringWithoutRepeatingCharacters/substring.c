#include <stdio.h>
#include "substring.h"
#include "uthash.h"

int lengthOfLongestSubstring(char* s) {
    int len = strlen(s);    
    int i = 0, j = 0, k = 0, count = 0, max = 0;
    int target = 0;

    struct substr_hash {
        int id;
        int pos;
        UT_hash_handle hh;
    };

    struct substr_hash *tables = NULL;
    for ( i = 0; i < len; i ++ ) {
        for ( j = i; j < len; j ++ ) {
            //Find
            struct substr_hash *f;
            int fid = (int) s[j];
            //printf("find %c\n", s[j]);
            HASH_FIND_INT(tables, &fid, f);
            if ( f ) {
                count = HASH_COUNT(tables);
                if ( count > max ) {
                    max = count;
                }

                if ( max > len - i + 1 ) {
                    return max;
                }

                for ( k = i; k < f->pos; k ++ ) {
                    struct substr_hash *d;
                    target = (int) s[k];
                    HASH_FIND_INT(tables, &target, d);
                    if ( d ) {
                        //printf("del: %c, ", d->id);
                        HASH_DEL(tables, d);
                    }
                }
                //printf("del: %c\n", f->id);
                i = f->pos + 1;
                HASH_DEL(tables, f);
            }

            //Add
            struct substr_hash *sub = malloc( sizeof(struct substr_hash) );
            sub->id = s[j];
            sub->pos = j;
            HASH_ADD_INT(tables, id, sub);
            //printf("add %c\n", s[j]);
        }
    }

    if ( max == 0 ) {
        max = HASH_COUNT(tables);
    }

    return max;
}
