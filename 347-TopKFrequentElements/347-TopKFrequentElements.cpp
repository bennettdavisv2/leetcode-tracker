// Last updated: 7/29/2026, 10:13:17 AM
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freqMap;
        for (int num : nums) {
            freqMap[num]++;
        }
        // Define comparator lambda to convert maxHeap to minHeap
        auto comp = [&freqMap](int i, int k){
            return freqMap[i] > freqMap[k];
        };
        std:priority_queue<int, std::vector<int>, decltype(comp)> minHeap(comp);
        for(const auto& pair: freqMap){
            minHeap.push(pair.first);
            if(minHeap.size() > k){
                minHeap.pop(); 
            } 
        }
        std::vector<int> answer;
        while (!minHeap.empty()) {
            answer.push_back(minHeap.top());
            minHeap.pop();
        }

        return answer;
    }
};