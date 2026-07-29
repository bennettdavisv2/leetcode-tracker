// Last updated: 7/29/2026, 10:13:20 AM
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> sln(nums.size(), 1);
        int prefix = 1;
        int postfix = 1;
        // prefix loop
        for(int i = 0; i < nums.size(); ++i){
                sln[i] = prefix;
                prefix *= nums[i];
            }
        // postfix loop
        for(int i = nums.size()-1; i >= 0 ; --i){
                sln[i] *= postfix;
                postfix *= nums[i];
            }
            return sln;

    }
};