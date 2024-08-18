//홀수인 알파벳이 2개 이상이면 X
//홀수인 알파벳이 중간에 들어가야함
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        int[] alp = new int[26]; //알파벳 개수
        int odd = 0; int n = 0; int c=0;
        boolean answer = true;
        int[] palin = new int[name.length()];

        for(int i=0; i<name.length(); i++){
            char ch = name.charAt(i);
            alp[ch - 'A']++; //name의 알파벳 개수
        }

        for(int i=0; i<26; i++){
            if(alp[i] % 2 != 0){
                odd++;
                n = i;
                if(odd > 1) {
                    answer = false;
                    break;
                }
            }
        }

        for (int i=0; i<alp.length; i++) {
            for (int j = 0; j < alp[i] / 2; j++) {
                palin[c] = i;
                palin[palin.length - c - 1] = i;
                c++;
            }
        }
        if(odd == 1) palin[c] = n;

        if(!answer) System.out.print("I'm Sorry Hansoo");
        else {
            for(int i=0; i<palin.length; i++)
                System.out.print((char)(palin[i] + 'A'));
        }
    }
}
