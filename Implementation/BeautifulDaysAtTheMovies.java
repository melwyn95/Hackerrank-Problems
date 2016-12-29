import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static int reverse(int n) {
        int answer = 0;
        while (n > 0) {
            answer = answer * 10 + (n % 10);
            n /= 10;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int i = Integer.parseInt(input[0]);
        int j = Integer.parseInt(input[1]);
        long k = Integer.parseInt(input[2]);
        int count = 0;
        for (; i <= j ; i++) {
            if (Math.abs(i - reverse(i)) % k == 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
