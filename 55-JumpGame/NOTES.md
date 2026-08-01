# 55. Jump Game

## Problem

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Notes

<!-- Add your notes and lessons learned here -->
Use this example: [1,3,1,0,4]
Moving goal post greedy method. Goal post is last index, let's call it 4. Starting from the end of the array. For each, if the current index + the value at the current index is >= to the goal, move the goal to i. It's an excellent greedy algorithm, I'm just unsure how to recognize if a problem will need a greedy solution. And if you make it to the front, then return True, else false.
