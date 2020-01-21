#ifndef TREE
#define TREE

#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *lnode;
    struct TreeNode *rnode;
};

struct TreeNodeQueue {
    struct TreeNode *node;
    struct TreeNodeQueue *next;
};

struct TreeNode *deserialize(int arr[], size_t len);

struct TreeNodeQueue *initTreeNodeQueue(void);
struct TreeNodeQueue *pushNode(struct TreeNodeQueue *treeNodeQueue, struct TreeNode *treeNode);
struct TreeNode *popNode(struct TreeNodeQueue *treeNodeQueue);

#endif
