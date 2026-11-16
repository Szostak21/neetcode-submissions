#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(const vector<int>& nums,int target) {
        unordered_map<int, int> num_to_idx;

        for(int i = 0; i < nums.size(); ++i){
            int rem = target - nums[i];

            auto it = num_to_idx.find(rem);
            if (it != num_to_idx.end()){
                return {it->second, i};
            }

            num_to_idx[nums[i]] = i;
        }
        return {};
    }
};
