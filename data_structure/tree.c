#include "tree.h"

struct TreeNode *deserialize(int arr[], size_t len) {
    int i = 0;

    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val   = 0;
    root->lnode = NULL;
    root->rnode = NULL;

    struct TreeNodeQueue *treeNodeQueue = initTreeNodeQueue();
    treeNodeQueue = pushNode(treeNodeQueue, root);


    while ( treeNodeQueue != NULL ) {
        if ( i < len ) {
            struct TreeNode *node = popNode(treeNodeQueue);
            node->val = arr[i];
            node->lnode = malloc(sizeof(struct TreeNode));
            node->rnode = malloc(sizeof(struct TreeNode));

            treeNodeQueue = pushNode(treeNodeQueue, node->lnode);
            treeNodeQueue = pushNode(treeNodeQueue, node->rnode);
            i ++;
        } else {
            struct TreeNode *node = popNode(treeNodeQueue);
            node = NULL;
        }
    }

    return root;
}

struct TreeNodeQueue *initTreeNodeQueue(void) {

    struct TreeNodeQueue *treeNodeQueue = malloc(sizeof(struct TreeNodeQueue));
    treeNodeQueue->node = NULL;
    treeNodeQueue->next = NULL;

    return treeNodeQueue;
}

struct TreeNodeQueue *pushNode(struct TreeNodeQueue *treeNodeQueue, struct TreeNode *treeNode) {

    struct TreeNodeQueue *queueFirst = NULL;

    if ( treeNodeQueue->node != NULL ) {
        queueFirst = malloc(sizeof(struct TreeNodeQueue));
        queueFirst->node = treeNode;
        queueFirst->next = treeNodeQueue;
    } else {
        queueFirst = treeNodeQueue; 
        queueFirst->node = treeNode;
    }

    return queueFirst;
}

struct TreeNode *popNode(struct TreeNodeQueue *treeNodeQueue) {
    struct TreeNode *node = treeNodeQueue->node;
    treeNodeQueue = treeNodeQueue->next;

    return node;
}
