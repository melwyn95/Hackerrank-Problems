import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String[] input = br.readLine().split(" ");
            long n = Long.parseLong(input[0]);
            long m = Long.parseLong(input[1]);
            long s = Long.parseLong(input[2]);
            m = m % n - 1;
            if ((s + m) % n == 0) {
                System.out.println(n);
            } else {
                System.out.println((s + m) % n);
            }
        }

    }
}
