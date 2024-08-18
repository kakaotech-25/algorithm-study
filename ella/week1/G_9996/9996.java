import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        String pattern = sc.nextLine();
        String[] ptr = pattern.split("\\*");
        int[] answer = new int[num];

        for(int i=0; i<num; i++){
            String str = sc.nextLine();
            if(str.length() < ptr[0].length() + ptr[1].length()) answer[i] = 0; //파일 이름이 패턴 길이보다 짧은 경우
            else{
                String front = str.substring(0, ptr[0].length()); //패턴 앞 
                String back = str.substring(str.length() - ptr[1].length()); //패턴 뒤
                if(front.equals(ptr[0]) && back.equals(ptr[1])) answer[i] = 1; //앞, 뒤 패턴이 일치할 경우
                else answer[i] = 0;
            }
        }

        for(int i=0; i<num; i++){
            if(answer[i] == 0) System.out.println("NE");
            else System.out.println("DA");
        }
    }
}
