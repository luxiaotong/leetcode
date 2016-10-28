#include <stdio.h>
#include <stdlib.h>


//https://github.com/junjizhi/fifo
#define QueueElement struct TreeNode *
#include "fifo/queue.h"

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* invertTree(struct TreeNode* root);
struct TreeNode *deserializer(int tree_arr[], int len);
void visualize(struct TreeNode *root, int len);


int main() {
    int tree_arr[] = {4, 2, 7, 1, 3, 6, 9};
    int len = sizeof(tree_arr)/sizeof(int);
    struct TreeNode *root = deserializer(tree_arr, len);
    visualize(root, len);

    root = invertTree(root);
    visualize(root, len);


    int tree_arr2[] = {};
    int len2 = sizeof(tree_arr2)/sizeof(int);
    struct TreeNode *root2 = deserializer(tree_arr2, len2);
    visualize(root2, len);


    return 0;
}


struct TreeNode* invertTree(struct TreeNode* root) {
    struct TreeNode *tmpnode = NULL;

    if ( root == NULL ) {
        
    } else if ( root->left == NULL && root->right == NULL ) {

    } else if ( root->left != NULL && root->right == NULL ) {
        root->right = invertTree(root->left);
        root->left = NULL;
    } else if ( root->left == NULL && root->right != NULL ) {
        root->left= invertTree(root->right);
        root->right = NULL;
    } else {
        printf("left: %d\nright: %d\n", root->left->val, root->right->val);
        tmpnode = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(tmpnode);
    }

    return root;
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
        if ( i*2 + 1 < len ) { //has left child
            struct TreeNode *lnode = malloc(sizeof(struct TreeNode));
            lnode->val = 0;
            lnode->left = NULL;
            lnode->right = NULL;
            enqueue(q, lnode);
            fnode->left = lnode;
        } else {
            fnode->left = NULL;
        }
        if ( i*2 + 2 < len ) { //has right child
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

void visualize(struct TreeNode *root, int len) {
    int count = 0, level = 1, width = 1;

    Queue *q = initQueue(len);
    enqueue(q, root);
    struct TreeNode *cnode = NULL;

    while ( q->size != 0 ) {
        count ++;
        if ( count == width ) {
            width *= 2;
            level += 1;
            printf("\n");
        }

        cnode = front(q);
        printf("%d ", cnode->val);
        dequeue(q);

        if ( cnode->left != NULL ) {
            enqueue(q, cnode->left);
        }
        if ( cnode->right != NULL ) {
            enqueue(q, cnode->right);
        }
    }
    printf("\n");

    return;
}
