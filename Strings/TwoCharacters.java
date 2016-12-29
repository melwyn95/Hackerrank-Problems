import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int len = in.nextInt();
        String s = in.next();
        boolean[] characters = new boolean[26];
        char[] a = new char[26];
        int count = 0;
        for (int i=0; i<len ; i++) {
            if (!characters[s.charAt(i)-'a']) {
                characters[s.charAt(i)-'a'] = true;
                a[count++] = s.charAt(i);
            }
        }
        int answer = 0;
        if (count < 2) {
            System.out.println(0);
        } else {
            int maxCount = 0;
            for (int i=0 ; i < count ; i++) {
                for (int j = i+1 ; j < count ; j++) {
                    int count1 = 0;
                    char prev = ' ';
                    boolean flag = true;
                    for (char c : s.toCharArray()) {
                        if (c == a[i] || c == a[j]) {
                            if (prev == ' ') {
                                prev = c;
                                count1++;
                            } else {
                                if (prev == c) {
                                    flag = false;
                                    break;
                                } else {
                                    prev = c;
                                    count1++;
                                }
                            }
                        }
                    }
                    if (flag) {
                        answer++;
                        if (count1 > maxCount) {
                            maxCount = count1;
                        }
                    }
                }
            }
             System.out.println(maxCount);
        }

    }
}
