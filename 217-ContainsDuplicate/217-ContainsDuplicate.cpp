// Last updated: 7/29/2026, 10:13:24 AM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> mySet;
        for(int num:nums){
            mySet.insert(num);
        }
        return (mySet.size() != nums.size());
    }
};