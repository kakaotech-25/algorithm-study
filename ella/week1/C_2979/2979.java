import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] time = new int[100];
        int cost = 0;

        for(int i=0; i<3; i++){
            int timeIn = sc.nextInt();
            int timeOut = sc.nextInt();
            for(int j=timeIn; j<timeOut; j++){
                time[j]++;
            }
        }

        for(int i=0; i<time.length; i++){
            if(time[i] == 1) cost += a;
            else if(time[i] == 2) cost += (b * 2);
            else if(time[i] == 3) cost += (c * 3);
        }
        System.out.print(cost);
    }
}
