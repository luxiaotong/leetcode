#include <stdio.h>
#include <stdlib.h>
#include "max_depth.h"

int main() {
    int i = 0;

    int tree_arr[] = {1, 2, 3, 4, 0, 0, 5};
    int len = sizeof(tree_arr)/sizeof(int);
    struct TreeNode *root = deserializer(tree_arr, len);
    visualize(root, len);


    int rst = maxDepth(root);
    printf("depth: %d\n", rst);

    return 1;
}
