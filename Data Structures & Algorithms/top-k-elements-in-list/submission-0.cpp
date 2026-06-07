class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freqMap;
        std::vector<int> returnVect;


        for (int num : nums) {
            freqMap[num]++;
        }
        
        std::vector<std::pair<int, int>> vectorPair;
        for (auto& it : freqMap) {
            vectorPair.push_back(std::make_pair(it.second, it.first));
        }

        std::sort(vectorPair.begin(), vectorPair.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.first > b.first; 
        });

        for (int i = 0; i < k; i++) {
            returnVect.push_back(vectorPair[i].second);
        }

        return returnVect;
    }
};
