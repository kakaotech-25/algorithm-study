import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int m = Integer.parseInt(sc.nextLine());
        String str = sc.nextLine();
        String[] arr = str.split(" ");
        int answer = 0;

        for(int i=0; i<n; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if (Integer.parseInt(arr[i]) + Integer.parseInt(arr[j]) == m) answer++;
            }
        }
        System.out.print(answer);
    }
}
