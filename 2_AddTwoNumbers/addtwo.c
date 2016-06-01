#include <stdlib.h>
#include "addtwo.h"
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;
    int sum = 0;

    struct ListNode *l3 = malloc( sizeof(struct ListNode) );
    struct ListNode *h3 = l3;
    l3->val = 0;
    l3->next = NULL;

    while ( l1 != NULL || l2 != NULL || carry != 0 ) {
        struct ListNode *node3 = malloc( sizeof(struct ListNode) );

        if ( l1 != NULL && l2 != NULL ) {
            sum = l1->val + l2->val + carry;
            l1 = l1->next;
            l2 = l2->next;
        } else if ( l1 != NULL && l2 == NULL ) {
            sum = l1->val + carry;
            l1 = l1->next;
        } else if ( l1 == NULL && l2 != NULL ) {
            sum = l2->val + carry;
            l2 = l2->next;
        } else {
            sum = carry;
        }

        if ( sum < 10 ) {
            node3->val = sum;
            carry = 0;
        } else {
            node3->val = sum%10;
            carry = 1;
        }
        node3->next = NULL;

        l3->next = node3;
        l3 = l3->next;
    }

    return h3->next;
}
