class Solution {
public:
    void branch(int open, int close, int n, string& stk, vector<string>& res){
        if(open == n && close == open){
            res.push_back(stk);
            return;
        }

        if(open > close){
            stk += ")";
            branch(open, close + 1, n, stk, res);
            stk.pop_back();
        }
        if(open < n){
            stk += "(";
            branch(open + 1, close, n, stk, res);
            stk.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        string stk;
        vector<string> res;
        branch(0, 0, n, stk, res);
        return res;
    }
};
