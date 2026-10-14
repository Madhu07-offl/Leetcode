class Solution {
public:
    vector<string> ans;
    string mp[10]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    void solve(string& digits,int i,string cur) {
        if(i==digits.size()) {
            ans.push_back(cur);
            return;
        }

        for(char c:mp[digits[i]-'0']) {
            solve(digits,i+1,cur+c);
        }
    }

    vector<string> letterCombinations(string digits) {
        if(digits.empty())
            return {};

        solve(digits,0,"");
        return ans;
    }
};