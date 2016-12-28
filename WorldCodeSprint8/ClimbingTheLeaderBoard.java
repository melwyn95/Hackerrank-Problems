import java.io.*;
import java.util.*;

public class ClimbingTheLeaderBoard {

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

        int pointer = n - 1;
        for (int score : alice) {
            while (score > leaderBoard[pointer] && pointer > 0) {
                pointer--;
            }
            if (score == leaderBoard[pointer]) {
                System.out.println(rankings[pointer]);
            } else if (score < leaderBoard[pointer]) {
                System.out.println(rankings[pointer] + 1);
            }else if (pointer == 0) {
                System.out.println(1);
            }
        }

    }
}
