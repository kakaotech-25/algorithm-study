import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNextInt()){
            int n = sc.nextInt();
            int num = 0;
            int count = 0;
            while(true){
                num = (num*10) + 1; //1, 11, 111, ...
                num %= n; //0일 경우 각 자릿수가 모두 1로만 이루어진 n의 배수
                count++;
                if(num == 0) {
                    System.out.println(count);
                    break;
                }
            }
        }
    }
}
