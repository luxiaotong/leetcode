#include "max_depth.h"

int maxDepth(struct TreeNode *root) {
    static int depth = 0;
    int lDepth = 0, rDepth = 0;
    if ( root == NULL ) {
        depth = 0;
    } else if ( root->left == NULL && root->right == NULL ) {
        depth = 1;
    } else {
        if ( root->left != NULL ) {
            lDepth = maxDepth(root->left);
        }
        if ( root->right != NULL ) {
            rDepth = maxDepth(root->right);
        }

        depth += (lDepth >= rDepth) ? lDepth : rDepth;
    }
    printf("step: %d, val: %d\n", depth, root->val);
    return depth;
}

struct TreeNode *deserializer(int tree_arr[], int len) {
    int i = 0;
    Queue *q = initQueue(len);

    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = 0;
    root->left = NULL;
    root->right = NULL;

    enqueue(q, root);

    while ( i < len ) {
        struct TreeNode *fnode = front(q);
        dequeue(q);

        fnode->val = tree_arr[i];
        if ( i + 1 < len ) { //has left child
            struct TreeNode *lnode = malloc(sizeof(struct TreeNode));
            lnode->val = 0;
            lnode->left = NULL;
            lnode->right = NULL;
            enqueue(q, lnode);
            fnode->left = lnode;
        } else {
            fnode->left = NULL;
        }
        if ( i + 2 < len ) { //has right child
            struct TreeNode *rnode = malloc(sizeof(struct TreeNode));
            rnode->val = 0;
            rnode->left = NULL;
            rnode->right = NULL;
            enqueue(q, rnode);
            fnode->right= rnode;
        } else {
            fnode->right = NULL;
        }

        i++;
    }

    return root;
}
