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

        depth = ((lDepth >= rDepth) ? lDepth : rDepth) + 1;
    }
    printf("val: %d, depth: %d\n", root->val, depth);
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
