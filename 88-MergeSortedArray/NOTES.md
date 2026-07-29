# 88. Merge Sorted Array

## Problem

Given two sorted arrays nums1 (length m+n, with the last n slots
empty) and nums2 (length n), merge nums2 into nums1 in place so
nums1 becomes one sorted array.

## Notes

<!-- Add your notes and lessons learned here -->
Two-pointers (really three) approach where we had deadspace to populate and were abel to traverse the arrays and in-place update. One edgecase was if nums i pointer hit 0 but there were still numbers in nums2.