class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int p1 = 0, p2 = 1;
        
        while(p2 < prices.size()){
            if(prices[p1] > prices[p2]){
                p1 = p2;
            } else{
                res = max(res, prices[p2] - prices[p1]);
            }
            p2++;
            
        }
        return res;
    }
};
