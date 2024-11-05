package 바킹독.이진탐색.과자나눠주기;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int m, n;
    static int[] arr;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        m = scanner.nextInt();
        n = scanner.nextInt();

        arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr);

        int st = 1;
        int en = arr[n-1];

        while(st <= en) {
            int mid = (st + en) / 2;

            int cnt = 0;
            for(int i=0; i<n; i++) {
                if(arr[i] >= mid) {
                    cnt += arr[i] / mid;
                }
            }

            if(cnt >= m) {
                st = mid + 1;
            }
            else {
                en = mid - 1;
            }
        }

        System.out.println(en);
    }
}
