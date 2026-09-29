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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        int count = 0;
        ListNode* c = head;

        while (c) {
            count++;
            c = c->next;
        }

        int depth = count - n;
        c = head;
        ListNode* prev = nullptr;

        while (depth != 0) {
            prev = c;
            c = c->next;
            depth--;
        }
        if (prev) {
            prev->next = c->next;
            return head;
        } else {
            return head->next;
        }
        
    }
};
