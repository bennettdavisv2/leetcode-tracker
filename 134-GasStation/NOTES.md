# 134. Gas Station

## Problem

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

## Notes

<!-- Add your notes and lessons learned here -->
Initial check to guarantee a solution, then we perform a greedy algorithm where we change the start and check if we hit a place we can't go to. If we can make it to the end of the array, then we guarantee the right solution.