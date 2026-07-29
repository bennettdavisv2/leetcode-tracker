# 27. Remove Element

## Problem

Given an array `nums` and a value `val`, remove all occurrences of
val in place. Return the count k of remaining elements; order may
change and elements beyond k don't matter.

## Notes

<!-- Add your notes and lessons learned here -->
Two pointers approach. If a value is not the target value, place it in the valid sub array and increment index.