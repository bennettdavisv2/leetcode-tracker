// Last updated: 7/29/2026, 10:13:14 AM
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int m;
        while (l < r) {
            m = l + (r-l)/2;
            int sum = 0;
            for (int num: piles) {
                sum += (num + m - 1)/m; // can also use ceil((float)num/m) instead
            }
            if (sum <= h) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
};