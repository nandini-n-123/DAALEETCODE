 
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    // Base case
    if (root == NULL || root == p || root == q) {
        return root;
    }

    // Recur for left and right subtrees
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);

    // If both left and right are not null, it means p and q are found in
    // left and right subtrees respectively, so root is the LCA.
    if (left != NULL && right != NULL) {
        return root;
    }

    // Otherwise, if one of them is non-null, return that non-null value.
    return left != NULL ? left : right;
}