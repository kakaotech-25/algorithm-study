import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];

        arr[0] = sc.nextInt();
        for(int i=1; i<n; i++){
          arr[i] = arr[i-1] + sc.nextInt();
        }

        int max = arr[k-1];
        for(int i=k; i<n; i++){
            int sum = arr[i] - arr[i-k];
            if(sum > max) max = sum;
        }

        System.out.print(max);
    }
}
