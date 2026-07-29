// Last updated: 7/29/2026, 10:13:46 AM
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // return an array of arrays
        // word is an anagram if the letters in a different order are those of a different word
        // approach is going to be a hashmap<char, string array>

    std::unordered_map<std::string, std::vector<std::string>> map;

        for (std::string word : strs) {
            // Sort the word to get the anagram signature
            std::string sortedWord = word;
            std::sort(sortedWord.begin(), sortedWord.end());
            
            // Add the original word to the list of its anagram group
            map[sortedWord].push_back(word);
        }
            std::vector<std::vector<std::string>> results;
            for(auto& pair: map){
                results.push_back(pair.second);
            }
            return results;
    }
};