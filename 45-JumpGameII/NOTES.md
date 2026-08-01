# 45. Jump Game II

## Problem

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:


	0 <= j <= nums[i] and
	i + j < n


Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

## Notes

<!-- Add your notes and lessons learned here -->
We are told this algorithm will never run on a false case. That lends itself to a greedy algorithm. 
We create buckets and go to the farthest value that the bucket can bring us to.