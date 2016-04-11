#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    //int *res = malloc(2*sizeof(int));
    static int res[2] = {};
    int i = 0, j = 0;
    for ( i = 0; i < numsSize; i++ ) {
        for ( j = i + 1; j < numsSize; j++ ) {
            if ( nums[i] + nums[j] == target ) {
                res[0] = i;
                res[1] = j;
            }
        }
    }
    return res;
}
