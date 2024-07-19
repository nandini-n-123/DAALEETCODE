#include <limits.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// Helper function to check if the tree is a valid BST
bool isValidBSTHelper(struct TreeNode* node, long min, long max) {
    if (node == NULL) {
        return true; // An empty tree is a valid BST
    }

    // Check if the current node's value is within the valid range
    if (node->val <= min || node->val >= max) {
        return false;
    }

    // Recursively check the left subtree and right subtree
    return isValidBSTHelper(node->left, min, node->val) &&
           isValidBSTHelper(node->right, node->val, max);
}

// Main function to initiate the BST validation
bool isValidBST(struct TreeNode* root) {
    // Initialize the range for valid BST values
    return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
}