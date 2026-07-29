# 189. Rotate Array

## Problem

Given an array `nums`, rotate the array to the right by `k` steps,
where k is non-negative, modifying the array in place.

## Notes

<!-- Add your notes and lessons learned here -->
This threw me for a loop. Originally I tried to algorithmically shift, store, and replace values in the array using two pointers, but then googled the solution and it said the reverse the array, then reverse [0:k], then reverse [k:]. The other approach used modulo and exra space. A good lesson here was the modulo operator a is great tool for shifting values.
