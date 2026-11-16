/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <limits>
#include <algorithm>

class Solution {
    int dfs(TreeNode* root, int& maxSum){
        if(!root)return 0;

        int leftGain = max(0, dfs(root->left, maxSum));
        int rightGain = max(0, dfs(root->right, maxSum));

        maxSum = max(leftGain + rightGain + root->val, maxSum);

        return root->val + max(leftGain, rightGain);
    }
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = std::numeric_limits<int>::min();
        dfs(root, maxSum);
        return maxSum;
    }
};
