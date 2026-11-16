#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<int> sub;
        int left = 0, longest = 0;

        for(int right = 0; right < static_cast<int>(s.size()); ++right){
            while(sub.contains(s[right]) && left < right){
                sub.erase(s[left]);
                ++left;
            }
            sub.insert(s[right]);
            longest = std::max(longest, right - left + 1);
        }
        return longest;
    }
};
