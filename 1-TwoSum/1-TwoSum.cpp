// Last updated: 7/29/2026, 10:14:15 AM
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numberMap;
        for (int i = 0; i < nums.size(); i++) {
           if(numberMap.find(target - nums[i]) != numberMap.end()){
            return {numberMap[target - nums[i]], i};
           }
           numberMap[nums[i]] = i;
        }
        return {};  // Return an empty vector if no solution is found
    }
};
