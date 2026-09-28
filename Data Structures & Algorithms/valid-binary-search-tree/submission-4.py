class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # We create a helper function that takes the node, and its allowed boundaries
        def validate(node, min_val, max_val):
            # An empty node is valid
            if not node:
                return True
            
            # If the current node breaks the boundaries set by its ancestors, it's invalid
            if not (min_val < node.val < max_val):
                return False
            
            # Check the left subtree (update the max_val to current node's value)
            # AND check the right subtree (update the min_val to current node's value)
            return validate(node.left, min_val, node.val) and \
                   validate(node.right, node.val, max_val)
        
        # The root can be any number, so it starts with infinite boundaries
        return validate(root, float('-inf'), float('inf'))