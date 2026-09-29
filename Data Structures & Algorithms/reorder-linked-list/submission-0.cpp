/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        ListNode* mid = head;
        ListNode* fast = head;

        while (fast->next && fast->next->next) {
            mid = mid->next;
            fast = fast->next->next;
        }

        ListNode* temp = mid;
        ListNode* l2 = mid->next;
        temp->next = nullptr;

        ListNode* c = l2;
        ListNode* n = l2->next;
        ListNode* t = nullptr;
        l2->next = nullptr;

        while (n) {
            t = n->next;
            n->next = c;
            c = n;
            n = t;
        }

        l2 = c;
        ListNode* l1 = head->next;
        ListNode* reordered = head;

        while(l1) {

            reordered->next = l2;
            reordered = reordered->next;
            l2 = l2->next;

            reordered->next = l1;
            reordered = reordered->next;
            l1 = l1->next;
        }  

        reordered->next = l2;  
    }
};
