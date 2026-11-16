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
#include <vector>
#include <unordered_map>


class Solution {
    int pre_idx = 0;
    unordered_map<int,int> indexes;

    TreeNode* dfs(vector<int> &preorder, int l, int r){
        if (l > r) return nullptr;
        TreeNode* root= new TreeNode(preorder[pre_idx]);
        ++pre_idx;
        int mid = indexes[root->val];
        root->left = dfs(preorder, l, mid - 1);
        root->right = dfs(preorder, mid + 1, r);
        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for(int i = 0; i < inorder.size(); ++i){
            indexes[inorder[i]] = i;
        }
        return dfs(preorder, 0, static_cast<int>(inorder.size()) - 1);
    }
};
