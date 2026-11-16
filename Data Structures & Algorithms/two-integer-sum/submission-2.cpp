#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums,const int& target) {
        std::unordered_map<int, int> prevMap;

        for(int i = 0; i < static_cast<int>(nums.size()); i++){
            int diff = target - nums[i];

            auto it = prevMap.find(diff);

            if (it != prevMap.end()){
                return std::vector<int>{it->second, i};
            }

            prevMap[nums[i]] = i;
        }

        return {};
    }
};
