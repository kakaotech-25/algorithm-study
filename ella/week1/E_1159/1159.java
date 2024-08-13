import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] alphabet = new int[26];
        boolean play = false;
        int num = Integer.parseInt(sc.nextLine());

        for(int i=0; i<num; i++){
            String name = sc.nextLine();
            char eng = name.charAt(0);
            alphabet[eng - 97]++;
        }

        for (int j=0; j<alphabet.length; j++) {
            if (alphabet[j] >= 5) {
                System.out.print((char) (j + 97));
                play = true;
            }
        }
        if(!play) System.out.print("PREDAJA");

    }
}
