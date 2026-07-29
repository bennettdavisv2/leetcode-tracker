// Last updated: 7/29/2026, 10:13:55 AM
class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::sort(nums.begin(), nums.end()); // Sort the array

        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicate elements
            
            int target = -nums[i];
            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum == target) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    ++left;
                    --right;

                    // Skip duplicates for the left pointer
                    while (left < right && nums[left] == nums[left - 1]) {
                        ++left;
                    }

                    // Skip duplicates for the right pointer
                    while (left < right && nums[right] == nums[right + 1]) {
                        --right;
                    }
                } else if (sum < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }

        return result;
    }
};