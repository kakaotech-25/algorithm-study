import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    static int n, m;
    static int[] arr;

    public static int binarySearch(int target) {
        int st = 0;
        int en = n - 1;

        while(st <= en) {
            int mid = (st + en) / 2;

            if(arr[mid] == target) {
                return 1;
            }

            else if(arr[mid] < target) {
                st = mid + 1;
            }

            else if(arr[mid] > target) {
                en = mid - 1;
            }
        }
        return 0; // st > en 일 경우 (st 가 en 을 역전할 경우) 이라면, 원하는 원소가 배열에 존재하지 않는 뜻이다.
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
        for(int i=0; i<m; i++) {
            int target = scanner.nextInt();
            System.out.println(binarySearch(target));
        }
    }
}
