#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* reverseString(char* s);

int main() {

    printf("hello: %s\n", reverseString("hello"));
    printf("asdfghjklqwertyuiopzxcvbnm1234567890: %s\n", reverseString("asdfghjklqwertyuiopzxcvbnm1234567890"));
    printf("race car: %s\n", reverseString("race car"));
    return 0;
}

char* reverseString(char* s) {
    int len = strlen(s);
    char *revStr = malloc( (len+1) * sizeof(char) );
    bzero(revStr, (len+1)*sizeof(char));
    revStr[len] = '\0';

    int head = 0;
    int tail = len - 1;

    while ( head <= tail ) {
        revStr[head] = s[tail];
        revStr[tail] = s[head];

        head ++;
        tail --;
    }

    return revStr;
}
