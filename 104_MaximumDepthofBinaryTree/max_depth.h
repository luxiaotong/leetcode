#ifndef MAX_DEPTH
#define MAX_DEPTH

#include <stdio.h>
#include "fifo/queue.h"

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int maxDepth(struct TreeNode* root);
struct TreeNode *deserializer(int tree_arr[], int len);

#endif
