#include <stdio.h>

void moveZeroes(int* nums, int numsSize);
    
int main() {
    int arr[] = {0, 1, 0, 3, 12};
    int len = sizeof(arr)/sizeof(int);
    moveZeroes(arr, len);
    for ( int i = 0; i < len; i ++ ) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}

void moveZeroes(int* nums, int numsSize) {
    int i = 0, j = 0;
    for ( i = 0; i < numsSize; i ++ ) {
        if ( nums[i] == 0 ) {
            for ( j = i+1; j < numsSize; j ++ ) {
                if ( nums[j] != 0 ) {
                    int tmp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = tmp;
                    break;
                }
            }
            if ( j == numsSize ) {
                break;
            }
        }
    }

    return;    
}
