#include <stdio.h>

bool canWinNim(int n) {
    if ( n % 4 == 0 ) {
        return 0;
    } else {
        return 1;
    } 
}

int main() {
    canWinNim(4);
    return 0;
}
