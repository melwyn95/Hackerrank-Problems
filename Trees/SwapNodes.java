
import java.util.Arrays;
import java.io.*;
public class Solution {

	static class Node {
		int data;
		int depth;
		Node left;
		Node right;
		public Node(int data) {
			this.data = data;
		}

	}

	static class Tree {
		Node root;
		public Tree(Node root) {
			this.root = root;
		}
		public void inorder(Node root) {
			if (root != null) {
				inorder(root.left);
				if (root.data != -1){
					System.out.print(root.data + " ");
				}
				inorder(root.right);
			}
		}
		public void inorderDepth(Node root) {
			if (root != null) {
				inorderDepth(root.left);
				if (root.data != -1){
					System.out.print(root.depth + " ");
				}
				inorderDepth(root.right);
			}
		}
		public void assginDepth(Node root, int level) {
			if (root != null) {
				root.depth = level + 1;
				assginDepth(root.left, level+1);
				assginDepth(root.right, level+1);
			}
		}
		public void swapNode(Node root, int K) {
			if (root != null && root.data != -1) {
				if (root.depth % K == 0) {
					Node temp = root.left;
					root.left = root.right;
					root.right = temp;
				}
				swapNode(root.left, K);
				swapNode(root.right, K);
			}
		}
	}

	public static void main(String[] args) throws IOException{
		Node root = new Node(1);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Node[][] a = new Node[n][2];
        String[] inp;
        for (int i=0;i<n;i++) {
            inp = br.readLine().split(" ");
            a[i][0] = new Node(Integer.parseInt(inp[0]));
            a[i][1] = new Node(Integer.parseInt(inp[1]));
        }
		int currentX = 0;
		int currentY = 0;
		int childRow = 1;
		while (childRow < n && currentX < n) {
			if (a[currentX][currentY].data != -1) {
				a[currentX][currentY].left = a[childRow][0];
				a[currentX][currentY].right = a[childRow][1];
			} else {
				while (a[currentX][currentY].data == -1) {
					if (currentY == 0) {
						currentY++;
					} else {
						currentY = 0;
						currentX++;
					}
				}
				a[currentX][currentY].left = a[childRow][0];
				a[currentX][currentY].right = a[childRow][1];
			}
			if (currentY == 0) {
				currentY++;
			} else {
				currentY = 0;
				currentX++;
			}
			childRow++;
		}
		root.left = a[0][0];
		root.right = a[0][1];
		Tree tree = new Tree(root);
        tree.assginDepth(root, 0);
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            tree.swapNode(root, Integer.parseInt(br.readLine()));
	        tree.inorder(root);
		    System.out.println();
        }
	}

}
