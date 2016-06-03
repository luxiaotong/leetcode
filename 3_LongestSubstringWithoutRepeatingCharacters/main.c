#include <stdio.h>
#include "substring.h"

int main() {
    printf("len: %d, \n", lengthOfLongestSubstring("abcabcbb"));
    printf("len: %d, bbbbb\n", lengthOfLongestSubstring("bbbbb"));
    printf("len: %d, pwwkew\n", lengthOfLongestSubstring("pwwkew"));
    printf("len: %d, c\n", lengthOfLongestSubstring("c"));
    printf("len: %d, dvdf\n", lengthOfLongestSubstring("dvdf"));
    printf("len: %d, bppvuikicnhlvnsnklobqk\n", lengthOfLongestSubstring("bppvuikicnhlvnsnklobqk"));

    return 0;
}
