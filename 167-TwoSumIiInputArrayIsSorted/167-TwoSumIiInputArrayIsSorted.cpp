// Last updated: 7/29/2026, 10:13:28 AM
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // two pointers, i and j. i at front and j at back. 
        // conditionals: if the sum equal(return indices), the sum is less(increment i), the sum is greater(decrement j)
        int i = 1;
        int j = numbers.size();
        while(i != j){
            if(numbers[i - 1] + numbers[j -1] == target)
                return {i, j};
            else if(numbers[i - 1] + numbers[j -1] <= target)
                i++;
            else
                j--;
        }
        return {0};
    }
};