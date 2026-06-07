class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()) return "";
        string encodedString;
        for(int x = 0; x < strs.size(); x++){
            encodedString += strs[x] + '/';
        }
        cout << encodedString << endl;
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        string temp;
        for(int x = 0; x < s.size(); x++){
            if(s[x] == '/'){
                ans.push_back(temp);
                temp = "";
                continue;
            } else {
                temp += s[x];
            }
        }
        return ans;
    }
};
