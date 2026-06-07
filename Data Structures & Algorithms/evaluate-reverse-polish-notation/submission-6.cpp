#include <cctype>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        
        for(int x = 0; x < tokens.size(); x++){
            if( tokens[x] == "*" || tokens[x] == "/" || tokens[x] == "+" || tokens[x] == "-" ){
                int res = 0;
                int num2 = stk.top();
                stk.pop();
                int num1 = stk.top();
                stk.pop();
            
                if(tokens[x] == "*") res = num1 * num2;
                else if (tokens[x] == "/") res = num1 / num2;
                else if (tokens[x] == "-") res = num1 - num2;
                else if (tokens[x] == "+") res = num1 + num2;

                stk.push(res);
                
            } else{
                stk.push(stoi(tokens[x]));
            }
        }
        return stk.top();
    }
};
