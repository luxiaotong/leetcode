#include <stdio.h>
#include "zigzag.h"
int main() {
    char *s = "PAYPALISHIRING"; 
    char *res = convert(s, 5);
    //char *s = "AB"; 
    //char *res = convert(s, 1);
    printf("%s\n", res);
    return 0;
}
