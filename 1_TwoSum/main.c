#include <stdio.h>
#include "two_sum.h"
int main() {
    int nums[] = {2, 7, 11, 15};
    int *res = twoSum(nums, sizeof(nums)/sizeof(int), 27);
    printf("Result: %d, %d\n", res[0], res[1]);
    return 0;
}
