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
    ListNode* reverseList(ListNode* head) {
        ListNode* c = head;

        if (head == nullptr or head->next == nullptr) {
            return head;
        }

        ListNode* n = c->next;

        c->next = nullptr;

        while (n->next) {
            ListNode* t = n->next;
            n->next = c;
            c = n;
            n = t;
        }

        n->next = c;
        return n;
    }
};
