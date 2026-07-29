// Last updated: 7/29/2026, 10:14:15 AM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0 ; i < nums.length; i++){
            for(int j = 1; j < nums.length; j++){
                if( i != j && nums[i] + nums[j] == target){
                    int[] myArray = new int[2];
                    myArray[0] = i;
                    myArray[1] = j;
                    return myArray;
                }
            }
        }
        return nums;
    }
}