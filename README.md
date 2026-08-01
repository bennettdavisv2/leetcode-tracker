# LeetCode Tracker

A log of LeetCode problems I've solved, with notes on my approach and lessons learned.

Solutions are synced automatically by the LeetCode tracker Chrome extension. Each problem folder also has a NOTES.md (written by hand, never touched by the extension) with the problem description and my notes/lessons. This README is generated from those NOTES.md files - after solving a new problem (and filling in your notes), regenerate it with:

```
python3 scripts/generate_readme.py
```

_Last generated: 8/1/2026, 04:31:45 PM_

## Solved Problems (14)

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

### 45. Jump Game II

Solution: [45-JumpGameII.py](45-JumpGameII/45-JumpGameII.py)

**Problem:** You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:


	0 <= j <= nums[i] and
	i + j < n


Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

[Full problem statement](45-JumpGameII/README.md)

**Notes / Lessons:** _Not yet filled in._

---

### 55. Jump Game

Solution: [55-JumpGame.py](55-JumpGame/55-JumpGame.py)

**Problem:** You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

[Full problem statement](55-JumpGame/README.md)

**Notes / Lessons:** _Not yet filled in._

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

### 134. Gas Station

Solution: [134-GasStation.py](134-GasStation/134-GasStation.py)

**Problem:** There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

[Full problem statement](134-GasStation/README.md)

**Notes / Lessons:** _Not yet filled in._

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

---

### 238. Product of Array Except Self

Solution: [238-ProductofArrayExceptSelf.py](238-ProductofArrayExceptSelf/238-ProductofArrayExceptSelf.py)

**Problem:** Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

[Full problem statement](238-ProductofArrayExceptSelf/README.md)

**Notes / Lessons:** _Not yet filled in._

---

### 274. H Index

Solution: [274-H-Index.py](274-H-Index/274-H-Index.py)

**Problem:** Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

[Full problem statement](274-H-Index/README.md)

**Notes / Lessons:** _Not yet filled in._

---

### 380. Insert Delete GetRandom O(1)

Solution: [380-InsertDeleteGetRandomO(1).py](380-InsertDeleteGetRandomO(1)/380-InsertDeleteGetRandomO(1).py)

**Problem:** Implement the RandomizedSet class:


	RandomizedSet() Initializes the RandomizedSet object.
	bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
	bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
	int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


You must implement the functions of the class such that each function works in average O(1) time complexity.

[Full problem statement](380-InsertDeleteGetRandomO(1)/README.md)

**Notes / Lessons:** _Not yet filled in._
