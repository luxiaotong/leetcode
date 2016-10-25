#include <stdio.h>
#include <stdlib.h>
#include "max_depth.h"

int main() {
    int i = 0;

    int tree_arr[] = {1, 0, 2, 3};
    struct TreeNode *root = deserializer(tree_arr, sizeof(tree_arr)/sizeof(int));
    return 1;

    /*
    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val   = i++;
    node->left  = NULL;
    node->right = NULL;

    struct TreeNode *root = node;
    struct TreeNode *cnode= root;
    do {
        struct TreeNode *lnode = malloc(sizeof(struct TreeNode));
        lnode->val   = i++;
        lnode->left  = NULL;
        lnode->right = NULL;

        struct TreeNode *rnode = malloc(sizeof(struct TreeNode));
        rnode->val   = i++;
        rnode->left  = NULL;
        rnode->right = NULL;

        cnode->left  = lnode;
        cnode->right = rnode;

        cnode = lnode;
    } while ( i < 10 );
    */

    int rst = maxDepth(root);
    printf("depth: %d\n", rst);

    return 1;
}
