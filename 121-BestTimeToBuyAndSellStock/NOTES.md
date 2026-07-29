# 121. Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where prices[i] is the price of a stock
on day i. Choose one day to buy and a later day to sell to maximize
profit. Return the max achievable profit, or 0 if none is possible.

## Notes

<!-- Add your notes and lessons learned here -->
Two pointers approach where you bring L to R if R - L is >=0 and keep track of max profit.
