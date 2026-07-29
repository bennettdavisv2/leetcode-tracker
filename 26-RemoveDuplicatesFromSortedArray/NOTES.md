# 26. Remove Duplicates from Sorted Array

## Problem

Given a sorted array `nums`, remove the duplicates in place so each
unique element appears only once, preserving relative order. Return
the count k of unique elements; the first k elements of nums should
hold the result.

## Notes

Two pointers. Because there's a sorted array, our lives get easier. We keep an index, and compare to that index, then update the next index value if a target is found. Basically building our target array.
