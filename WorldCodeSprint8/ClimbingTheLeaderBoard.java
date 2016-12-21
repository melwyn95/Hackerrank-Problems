import java.io.*;
import java.util.*;

public class ClimbingTheLeaderBoard {

    public static int bin(int[] a, int key, int start, int end) {

        if (start == end) {
            return end;
        }

        int mid = (start + end) / 2;


        if (key < a[mid]) {
            if (key >= a[mid + 1]) {
                return mid;
            }
            // System.out.println("--> " + a[mid] + " " + a[end]);
            return bin(a, key, mid + 1, end);
        } else {
            if (mid > 0 && key <= a[mid - 1]) {
                return mid;
            }
            // System.out.println("--> " + a[start] + " " + a[mid]);
            return bin(a, key, start, mid);
        }

        //return -1;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");
        int[] leaderBoard = new int[n];
        int[] rankings = new int[n];
        int index = 0;
        for (String i : s) {
            leaderBoard[index++] = Integer.parseInt(i);
        }
        index = 0;
        int rank = 0;
        int prev = -1;
        for (int score : leaderBoard) {
            if (prev != score) {
                rank++;
            }
            rankings[index++] = rank;
            prev = score;
        }

        int m = Integer.parseInt(br.readLine());
        int[] alice = new int[m];
        s = br.readLine().split(" ");
        index = 0;
        for (String i : s) {
            alice[index++] = Integer.parseInt(i);
        }

        for (int score : alice) {
            index = bin(leaderBoard, score, 0, leaderBoard.length - 1);
            if (index == (leaderBoard.length - 1)) {
                if (score == leaderBoard[leaderBoard.length - 1]) {
                    System.out.println(rankings[leaderBoard.length - 1]);
                }
                System.out.println(rankings[leaderBoard.length - 1] + 1);
            } else if (index == 0) {
                System.out.println(1);
            } else {
                if (leaderBoard[index - 1] == score) {
                    // System.out.println("Score : " + score);
                    System.out.println(rankings[index - 1]);
                } else {
                    System.out.println(rankings[index]);
                }
            }


            // System.out.println(score + " Index : " + index);
            // System.out.println(Arrays.toString(rankings));
            // System.out.println(Arrays.toString(leaderBoard));
        }


        // int[] a = new int[] {100, 100, 50, 50, 10, 5};
        // System.out.println(bin(a, 151, 0, 5));
    }
}
