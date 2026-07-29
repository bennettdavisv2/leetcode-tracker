# 169. Majority Element

## Problem

Given an array `nums` of size n, return the majority element — the
element that appears more than floor(n / 2) times. It is guaranteed
to exist.

## Notes

<!-- Add your notes and lessons learned here -->
Boyer-Moore Majority Vote algorithm. Incremented and decremented a count based on if values were equivalent. Algorithm is reliant on there being a majority voter and that voter will be the left pointers value and have ended the iterations with a <= +1 count.
