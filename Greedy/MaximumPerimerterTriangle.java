import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static int C(int n, int r) {
        int f = 1;
        for (int i=n-r;i<=n;i++) {
            f *= i;
        }
        return f / 6;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int index = 0;
        for (String s : br.readLine().split(" ")) {
            a[index++] = Integer.parseInt(s);
        }
        int[][] answer = new int[C(n, 3)][3];
        index = 0;
        Arrays.sort(a);
        int longestMaxSide = -1;
        int longestMinSide = -1;
        for (int i = 0 ; i <= n - 3 ; i++) {
            for (int j = i + 1 ; j <= n - 2 ; j++) {
                for (int k = j + 1 ; k <= n - 1 ; k++) {
                    if ((a[i] + a[j] > a[k]) && (a[j] + a[k] > a[i]) && (a[k] + a[i] > a[j])) {
                            answer[index][0] = a[i];
                            answer[index][1] = a[j];
                            answer[index][2] = a[k];
                            index++;
                    }
                }
            }
        }
        if (index > 0) {
            System.out.println(answer[index-1][0] + " " + answer[index-1][1] + " " + answer[index-1][2]);
        } else {
            System.out.println(-1);
        }
    }
}           
