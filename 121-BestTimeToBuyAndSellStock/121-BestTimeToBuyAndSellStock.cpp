// Last updated: 7/29/2026, 10:13:38 AM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;

        int l = 0, r = 1, maxTrade = 0;
        while(r < prices.size()){
            if(prices[l] > prices[r]){
                maxTrade = std::max(prices[r] - prices[l], maxTrade);
                l = r;
            }
            else{
                maxTrade = std::max(prices[r] - prices[l], maxTrade);
                r++;
            }

        }
        return maxTrade;
    }
};