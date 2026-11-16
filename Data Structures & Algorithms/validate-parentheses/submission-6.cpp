#include <stack>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isValid(const string& s) {
        stack<char> st;
        unordered_map<char, char> brackets = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };

        for(char c : s){
            if(brackets.count(c)){
                st.push(brackets[c]);
            }
            else{
                if(st.empty() || st.top() != c){
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};
