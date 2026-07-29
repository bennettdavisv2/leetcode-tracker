// Last updated: 7/29/2026, 10:14:04 AM
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // To ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.length;
        int n = nums2.length;
        int left = 0;
        int right = m;
        int partitionX, partitionY;
        int maxX, maxY;
        int minX, minY;
        double median;

        while (left <= right) {
            partitionX = (left + right) / 2;
            partitionY = (m + n + 1) / 2 - partitionX;

            maxX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            maxY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];

            minX = (partitionX == m) ? Integer.MAX_VALUE : nums1[partitionX];
            minY = (partitionY == n) ? Integer.MAX_VALUE : nums2[partitionY];

            if (maxX <= minY && maxY <= minX) {
                if ((m + n) % 2 == 0) {
                    median = (Math.max(maxX, maxY) + Math.min(minX, minY)) / 2.0;
                } else {
                    median = Math.max(maxX, maxY);
                }
                return median;
            } else if (maxX > minY) {
                right = partitionX - 1;
            } else {
                left = partitionX + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}
