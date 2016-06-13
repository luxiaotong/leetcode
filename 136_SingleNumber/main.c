#include <stdio.h>
#include <stdlib.h>

int singleNumber(int* nums, int numsSize) {
    int i = 0;
    int rst= 0;

    for ( i = 0; i < numsSize; i ++ ) {
        rst ^= nums[i];
    }

    return rst;
}

int main() {

    return 0;
}
