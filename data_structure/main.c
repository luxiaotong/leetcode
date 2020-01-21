#include <stdio.h>
#include "tree.h"

int main() {

    int arr[] = {1, 0, 2, 3};
    deserialize(arr, sizeof(arr)/sizeof(int));
    return 0;
}
