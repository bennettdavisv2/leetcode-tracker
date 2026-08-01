# 238. Product of Array Except Self

## Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Notes

<!-- Add your notes and lessons learned here -->
Create an answer array and do prefix and postfix calculations for each value, then return the answer array.