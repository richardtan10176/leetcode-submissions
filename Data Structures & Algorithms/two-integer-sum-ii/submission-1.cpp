class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int p1 = 0;
        int p2 = n-1;
        while((numbers[p1] + numbers[p2]) != target){
            if((numbers[p1] + numbers[p2]) < target){
                p1++;
            } else{
                p2--;
            }
        }
        return {p1+1,p2+1};
    }
};
