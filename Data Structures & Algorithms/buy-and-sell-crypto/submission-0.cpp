#include <vector>
#include <algorithm>
#include <limits>

class Solution {
public:
    int maxProfit(const vector<int>& prices) {
        int minPrice = std::numeric_limits<int>::max();
        int maxProfit = 0;

        for(int price : prices){
            minPrice = min(minPrice, price);
            maxProfit = max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};
