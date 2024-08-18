import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        String pattern = sc.nextLine();
        String[] ptr = pattern.split("\\*"); //패턴
        int[] answer = new int[num];

        for(int i=0; i<num; i++){
            String str = sc.nextLine();
            if(str.length() < ptr[0].length() + ptr[1].length()) answer[i] = 0; //패턴의 길이가 단어의 길이보다 작을 때
            else{
                String front = str.substring(0, ptr[0].length());//패턴 앞
                String back = str.substring(str.length() - ptr[1].length());// 패턴 뒤
                if(front.equals(ptr[0]) && back.equals(ptr[1])){ //패턴 앞, 뒤가 같을 때
                    answer[i] = 1;
                }
                else answer[i] = 0;
            }
        }

        for(int i=0; i<num; i++){
            if(answer[i] == 0) System.out.println("NE");
            else System.out.println("DA");
        }
    }
}
