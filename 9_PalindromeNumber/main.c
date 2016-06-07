#include <stdio.h>
#include "palindrome.h"

int main() {
    printf("rst: %d\n", isPalindrome(1234567));
    printf("rst: %d\n", isPalindrome(1234321));
    printf("rst: %d\n", isPalindrome(1234322));
    printf("rst: %d\n", isPalindrome(2222222));
    return 0;
}
