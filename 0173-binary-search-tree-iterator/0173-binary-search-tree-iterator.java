import java.util.Stack;

class BSTIterator {
    // Stack to store the path from root to the current smallest node
    private Stack<TreeNode> stack;

    public BSTIterator(TreeNode root) {
        this.stack = new Stack<>();
        // Initialize by pushing all left children of the root
        pushLeftChildren(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        // The top of the stack is always the current smallest element
        TreeNode node = stack.pop();
        
        // If the popped node has a right child, we need to find 
        // the smallest element in that right subtree
        if (node.right != null) {
            pushLeftChildren(node.right);
        }
        
        return node.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        // If the stack is not empty, there is at least one more element
        return !stack.isEmpty();
    }

    /** * Helper function to push a node and all its left descendants 
     * onto the stack.
     */
    private void pushLeftChildren(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}