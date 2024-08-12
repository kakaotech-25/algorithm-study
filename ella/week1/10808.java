import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String eng = sc.nextLine();
        int[] alphabet = new int[26];

        for (int i = 0; i < eng.length(); i++) {
            char ch = eng.charAt(i);
            alphabet[ch - 97]++;
        }

        for (char i = 0; i < 26; i++) {
            System.out.print(alphabet[i] + " ");
        }
    }
}
