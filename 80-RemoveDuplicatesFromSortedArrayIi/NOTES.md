# 80. Remove Duplicates from Sorted Array II

## Problem

Given a sorted array `nums`, remove duplicates in place so each
unique element appears at most twice, preserving relative order.
Return the count k of elements that should remain.

## Notes

<!-- Add your notes and lessons learned here -->
Tricky start case, but the first two will never be change. The algorithm checks for 3 in a row using two pointers and updates if there is not 3 in a row to build the target list. One thing I'm learning is that you want to build the target list, not necessarily build around finding the wrongs. Build for the right that will filter out the wrongs.
