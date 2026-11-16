class Solution {
public:
    bool isAnagram(string s, string t) {
        int counts[26] = {0};

        if(s.size() != t.size()){
            return false;
        }

        for(int i = 0; i < static_cast<int>(s.size()); i++){
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }

        for(int val: counts){
            if(val != 0){
                return false;
            }
        }
        return true;
    }
};
