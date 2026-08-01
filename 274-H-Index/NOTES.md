# 274. H Index

## Problem

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

## Notes

<!-- Add your notes and lessons learned here -->
There were multiple approaches here, one was a sorting approach and another was an extra memory approach. I chose the sorting approach. After sorting, if you find a citation count that is more than the number of publications left, you've found the H-Index. The candidate is the largest value and decrements from there.