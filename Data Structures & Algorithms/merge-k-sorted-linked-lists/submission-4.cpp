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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return nullptr;
        }
        if (lists.size() == 1) {
            return lists[0];
        }
        vector<ListNode*> left(lists.begin(), lists.begin() + lists.size() / 2);
        vector<ListNode*> right(lists.begin() + lists.size() / 2, lists.end());

        ListNode* l1 = mergeKLists(left);
        ListNode* l2 = mergeKLists(right);

        if (!l1) {
            return l2;
        }
        if (!l2) {
            return l1;
        }

        
        ListNode* head = nullptr;

        if (l1->val > l2->val) {
            head = l2;
            l2 = l2->next;
        } else {
            head = l1;
            l1 = l1->next;
        }

        ListNode* start = head;

        while (l2 && l1) {
            if (l1->val > l2->val) {
                head->next = l2;
                l2 = l2->next;
                head = head->next;
            } else {
                head->next = l1;
                l1 = l1->next;
                head = head->next;
            }
        }

        if (!l1) {
            head->next = l2;
        }
        if (!l2) {
            head->next = l1;
        }

        return start;
    }
        
};
