package 바킹독.이진탐색.숫자카드;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int n, m;
    static int[] arr;

    public static int binarySearch(int target) {
        int st = 0;
        int en = n-1;

        while(st <= en) {
            int mid = (st + en) / 2;

            if(arr[mid] == target) {
                return 1;
            }

            else if(arr[mid] > target) {
                en = mid-1;
            }

            else {
                st = mid+1;
            }
        }

        return  0;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = scanner.nextInt();
        }
        Arrays.sort(arr);

        m = scanner.nextInt();
        for(int i=0; i<m; i++) {
            int target = scanner.nextInt();
            System.out.print(binarySearch(target) + " ");
        }
    }
}
