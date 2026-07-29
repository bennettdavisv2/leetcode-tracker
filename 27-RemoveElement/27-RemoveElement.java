// Last updated: 7/29/2026, 10:13:51 AM
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = nums.length - 1;
       for(int i = nums.length - 1; i >= 0; i --) {
           if( nums[i] == val){
               for(int j = i; j <= k-1; j++ ){
                   nums[j] = nums[j+1];
               }
               nums[k] = 0;
               k--;
           }
       }
       return k + 1;
    }
}