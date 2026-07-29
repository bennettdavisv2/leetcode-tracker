// Last updated: 7/29/2026, 10:13:40 AM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // compare last unprocessed values of each array and have that be the last unprocessed value of the array
        int lastIndex = m + n - 1;
        int lastIndex1 = m - 1;
        int lastIndex2 = n - 1;

        while (lastIndex >= 0 && (lastIndex1 >= 0 || lastIndex2 >= 0)) {
            if (lastIndex1 >= 0 && (lastIndex2 < 0 || nums1[lastIndex1] >= nums2[lastIndex2])) {
                nums1[lastIndex] = nums1[lastIndex1];
                lastIndex1--;
            } else {
                nums1[lastIndex] = nums2[lastIndex2];
                lastIndex2--;
            }
            lastIndex--;
        }
    }
}
