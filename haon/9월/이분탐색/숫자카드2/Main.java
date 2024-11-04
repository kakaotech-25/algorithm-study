package 바킹독.이진탐색.숫자카드2;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int n, m;
    static int[] arr;

    static int lower_idx(int target, int len) {
        int st = 0;
        int en = len;

        while (st < en) {
            int mid = (st + en) / 2;

            if(arr[mid] >= target) {
                en = mid;
            }

            else {
                st = mid + 1;
            }
        }
        return st;
    }

    static int upper_idx(int target, int len) {
        int st = 0;
        int en = len;

        while (st < en) {
            int mid = (st + en) / 2;

            if(arr[mid] > target) {
                en = mid;
            }

            else {
                st = mid + 1;
            }
        }
        return st;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = scanner.nextInt();
        }
        Arrays.sort(arr);

        m = scanner.nextInt();

        StringBuilder sb = new StringBuilder();

        for(int i=0; i<m; i++) {
            int target;
            target = scanner.nextInt();

            sb.append(upper_idx(target, n) - lower_idx(target, n)).append(' ');
        }
        System.out.println(sb);
    }
}
