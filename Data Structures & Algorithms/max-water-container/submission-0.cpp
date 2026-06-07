class Solution {
public:
    int maxArea(vector<int>& heights) {
        int p1 = 0;
        int p2 = heights.size() - 1;
        int ans = min(heights[p1], heights[p2]) * (heights.size() - 1);
        while(p1 < p2){
            if(heights[p1] < heights[p2]){
                p1++;
            } else{
                p2--;
            }
            ans = max(min(heights[p1], heights[p2]) * (p2-p1), ans);
        }
        return ans;
    }
};
