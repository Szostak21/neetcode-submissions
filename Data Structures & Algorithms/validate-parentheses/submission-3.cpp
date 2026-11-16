#include <stack>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;

        for(char c : s){
            if(c == '('){
                st.push(')');
            }
            else if(c == '['){
                st.push(']');
            }
            else if(c == '{'){
                st.push('}');
            }
            else if(!st.empty() && c == st.top()){
                st.pop();
            }
            else{
                return false;
            }
        }
        if (st.empty()){return true;}
        return false;
    }
};
