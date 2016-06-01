#include <stdio.h>
#include <stdlib.h>
#include "addtwo.h"

int main() {
    int arr1[] = {2, 4, 3};
    int arr2[] = {5, 6, 4};
    int i = 0;

    struct ListNode *l1 = malloc( sizeof(struct ListNode) );
    struct ListNode *h1 = l1;
    l1->val = 0; 
    l1->next = NULL;

    struct ListNode *l2 = malloc( sizeof(struct ListNode) );
    struct ListNode *h2 = l2;
    l2->val = 0; 
    l2->next = NULL;

    for ( i = 0; i < 3; i ++ ) {
        struct ListNode *node1 = malloc( sizeof(struct ListNode) );
        node1->val = arr1[i];
        node1->next = NULL;
        l1->next = node1;
        l1 = l1->next;

        struct ListNode *node2 = malloc( sizeof(struct ListNode) );
        node2->val = arr2[i];
        node2->next = NULL;
        l2->next = node2;
        l2 = l2->next;
    }

    h1 = h1->next;
    h2 = h2->next;

    struct ListNode *h3 = addTwoNumbers(h1, h2);
    while ( h3 != NULL ) {
        printf("node3: %d\n", h3->val);
        h3 = h3->next;
    }
    /*
    while ( h1 != NULL ) {
        printf("node1: %d\n", h1->val);
        h1 = h1->next;
    }
    while ( h2 != NULL ) {
        printf("node2: %d\n", h2->val);
        h2 = h2->next;
    }
    */
    return 0;
}
