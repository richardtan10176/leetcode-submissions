class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        for(int left = 0; left < n-1; left++){
            for(int right = left+1; right < n; right++){
                if((target - numbers[right]) == numbers[left]){
                    return {left+1, right+1};
                }
            }
        }
        return {0,0};
    }
};
