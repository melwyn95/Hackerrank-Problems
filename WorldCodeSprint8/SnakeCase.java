import java.io.*;

public class SnakeCase {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] answer = s.split("_");
        System.out.println(answer.length);
    }
}
