class Solution {
public:
    bool isValid(string s) {
        // if(s.size() < 2){
        //     return false;
        // }
        stack<char> stk;
        for(int x = 0; x < s.size(); x++){
            if(s[x] == ')'){
                if(stk.empty() || stk.top() != '(') return false;
                stk.pop();
            }
            else if (s[x] == ']'){
                if(stk.empty() || stk.top() != '[') return false;
                stk.pop();
            }
            else if (s[x] == '}'){
                if(stk.empty() || stk.top() != '{') return false;
                stk.pop();
            } else{
                stk.push(s[x]);
            }
            
        }
        return stk.empty();
    }
};
