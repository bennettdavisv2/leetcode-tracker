# LeetCode Tracker

A log of LeetCode problems I've solved, with notes on my approach and lessons learned.

Solutions are synced automatically by the LeetCode tracker Chrome extension. Each problem folder also has a NOTES.md (written by hand, never touched by the extension) with the problem description and my notes/lessons. This README is generated from those NOTES.md files - after solving a new problem (and filling in your notes), regenerate it with:

```
python3 scripts/generate_readme.py
```

_Last generated: 7/29/2026, 12:10:24 PM_

## Solved Problems (8)

### 26. Remove Duplicates from Sorted Array

Solution: [26-RemoveDuplicatesFromSortedArray.py](26-RemoveDuplicatesFromSortedArray/26-RemoveDuplicatesFromSortedArray.py)

**Problem:** Given a sorted array `nums`, remove the duplicates in place so each
unique element appears only once, preserving relative order. Return
the count k of unique elements; the first k elements of nums should
hold the result.

**Notes / Lessons:** Two pointers. Because there's a sorted array, our lives get easier. We keep an index, and compare to that index, then update the next index value if a target is found. Basically building our target array.

---

### 27. Remove Element

Solution: [27-RemoveElement.py](27-RemoveElement/27-RemoveElement.py)

**Problem:** Given an array `nums` and a value `val`, remove all occurrences of
val in place. Return the count k of remaining elements; order may
change and elements beyond k don't matter.

**Notes / Lessons:** Two pointers approach. If a value is not the target value, place it in the valid sub array and increment index.

---

### 80. Remove Duplicates from Sorted Array II

Solution: [80-RemoveDuplicatesFromSortedArrayIi.py](80-RemoveDuplicatesFromSortedArrayIi/80-RemoveDuplicatesFromSortedArrayIi.py)

**Problem:** Given a sorted array `nums`, remove duplicates in place so each
unique element appears at most twice, preserving relative order.
Return the count k of elements that should remain.

**Notes / Lessons:** Tricky start case, but the first two will never be change. The algorithm checks for 3 in a row using two pointers and updates if there is not 3 in a row to build the target list. One thing I'm learning is that you want to build the target list, not necessarily build around finding the wrongs. Build for the right that will filter out the wrongs.

---

### 88. Merge Sorted Array

Solution: [88-MergeSortedArray.py](88-MergeSortedArray/88-MergeSortedArray.py)

**Problem:** Given two sorted arrays nums1 (length m+n, with the last n slots
empty) and nums2 (length n), merge nums2 into nums1 in place so
nums1 becomes one sorted array.

**Notes / Lessons:** Two-pointers (really three) approach where we had deadspace to populate and were abel to traverse the arrays and in-place update. One edgecase was if nums i pointer hit 0 but there were still numbers in nums2.

---

### 121. Best Time to Buy and Sell Stock

Solution: [121-BestTimeToBuyAndSellStock.py](121-BestTimeToBuyAndSellStock/121-BestTimeToBuyAndSellStock.py)

**Problem:** You are given an array `prices` where prices[i] is the price of a stock
on day i. Choose one day to buy and a later day to sell to maximize
profit. Return the max achievable profit, or 0 if none is possible.

**Notes / Lessons:** Two pointers approach where you bring L to R if R - L is >=0 and keep track of max profit.

---

### 122. Best Time to Buy and Sell Stock II

Solution: [122-BestTimeToBuyAndSellStockIi.py](122-BestTimeToBuyAndSellStockIi/122-BestTimeToBuyAndSellStockIi.py)

**Problem:** Given an array `prices`, you may buy and sell the stock multiple times
(one share at a time, must sell before buying again). Return the
maximum total profit achievable.

**Notes / Lessons:** Same approach as I, but keep track of total profit and always shift L to R if profitable.

---

### 169. Majority Element

Solution: [169-MajorityElement.py](169-MajorityElement/169-MajorityElement.py)

**Problem:** Given an array `nums` of size n, return the majority element — the
element that appears more than floor(n / 2) times. It is guaranteed
to exist.

**Notes / Lessons:** Boyer-Moore Majority Vote algorithm. Incremented and decremented a count based on if values were equivalent. Algorithm is reliant on there being a majority voter and that voter will be the left pointers value and have ended the iterations with a <= +1 count.

---

### 189. Rotate Array

Solution: [189-RotateArray.py](189-RotateArray/189-RotateArray.py)

**Problem:** Given an array `nums`, rotate the array to the right by `k` steps,
where k is non-negative, modifying the array in place.

**Notes / Lessons:** This threw me for a loop. Originally I tried to algorithmically shift, store, and replace values in the array using two pointers, but then googled the solution and it said the reverse the array, then reverse [0:k], then reverse [k:]. The other approach used modulo and exra space. A good lesson here was the modulo operator a is great tool for shifting values.
