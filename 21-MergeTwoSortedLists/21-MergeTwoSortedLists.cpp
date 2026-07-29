// Last updated: 7/29/2026, 10:13:52 AM
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) 
            return list2;
        if (!list2) 
            return list1;

        ListNode answer;
        ListNode* tail = &answer;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        tail->next = list1 ? list1 : list2;

        return answer.next;
    }
};
