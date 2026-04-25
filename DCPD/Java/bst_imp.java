class Node {
    int data;
    Node left;
    Node right;
 
    Node(int val) {
        this.data = val;
        this.left = null;
        this.right = null;
    }
 
}
 
class bst {
    Node root=null;
 
    void insert(int val) {
        if (root == null) {
            root = new Node(val);
            return;
        }
 
        Node curr_node = root;
        while (true) {
            if (curr_node.data > val) {
                if (curr_node.left == null) {
                    curr_node.left = new Node(val);
                    return;
                }
                // else
                curr_node = curr_node.left;
            }
            if (curr_node.data < val) {
                if (curr_node.right == null) {
                    curr_node.right = new Node(val);
                    return;
                }
                // else
                curr_node = curr_node.right;
            }
        }
 
    }
 
    // boolean search(int key) {
        
    // }
 
    void inorder(Node curr_node) {
        if (curr_node == null) {
            return;
        }
        inorder(curr_node.left);
        System.out.println(curr_node.data);
        inorder(curr_node.right);
    }
 
    Node deleteRec(Node root, int value) {
        if (root == null) {
            return root;
        }
        if (value > root.data) {
            root.right = deleteRec(root.right, value);
        } else if (value < root.data) {
            root.left = deleteRec(root.left, value);
        } else {
            // Node with only one child or no child
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
 
            // Node with two children: Get the inorder successor (smallest in the right subtree)
            root.data = minValue(root.right);
 
            // Delete the inorder successor
            root.right = deleteRec(root.right, root.data);
        }
        return root;
    }
 
    int minValue(Node root) {
        int minv = root.data;
        while (root.left != null) {
            minv = root.left.data;
            root = root.left;
        }
        return minv;
    }
 
    Node delete(int value) {
        if (root == null) {
            return null;
        }
        return deleteRec(root, value);
 
    }
}
 
 
public class bst_imp {
    public static void main(String[] args) {
        bst bst_obj = new bst();
        bst_obj.insert(40);
        bst_obj.insert(30);
        bst_obj.insert(20);
        bst_obj.insert(50);
        bst_obj.insert(45);
        bst_obj.insert(55);  
        bst_obj.inorder(bst_obj.root);
        bst_obj.delete(50);
        System.out.println("After deletion:");
        bst_obj.inorder(bst_obj.root);
 
 
    }
}