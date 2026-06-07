class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, vector<string>> map;
        for(int x = 0; x < strs.size(); x++){
            string sorted_str = strs[x];
            sort(sorted_str.begin(), sorted_str.end());
            map[sorted_str].push_back(strs[x]);
        }

        vector<vector<string>> groupedAnagrams;

        for(auto&it : map){
            groupedAnagrams.push_back(it.second);
        }
        return groupedAnagrams;
    }
};
