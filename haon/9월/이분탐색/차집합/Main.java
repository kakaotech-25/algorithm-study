package 바킹독.이진탐색.차집합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static int[] arr1, arr2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        TreeSet<Integer> tree = new TreeSet<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++) {
            tree.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<m; i++) {
            int tmp = Integer.parseInt(st.nextToken());
            tree.remove(tmp);
        }

        sb.append(tree.size()).append("\n");
        for(Integer tmp : tree) {
            sb.append(tmp).append(" ");
        }

        System.out.println(sb);
    }

    /* public static boolean binarySearch(int target) {
        int st = 0;
        int en = m-1;

        while(st <= en) {
            int mid = (st + en) / 2;

            if(arr2[mid] == target) {
                return false;
            }

            else if (arr2[mid] < target) {
                st = mid + 1;
            }

            else if(arr2[mid] > target) {
                en = mid - 1;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        m = scanner.nextInt();

        arr1 = new int[n];
        for(int i=0; i<n; i++) {
            arr1[i] = scanner.nextInt();
        }

        arr2 = new int[m];
        for(int i=0; i<m; i++) {
            arr2[i] = scanner.nextInt();
        }

        List<Integer> result = new ArrayList<>();

        int cnt = 0;
        for(int i=0; i<n; i++) {
            int target = arr1[i];
            if(binarySearch(target)) {
                result.add(target);
                cnt++;
            }
        }

        System.out.println(cnt);
        for(Integer num : result) {
            System.out.print(num + " ");
        }

        if(cnt == 0) {
            System.out.print(0);
        }
    } */
}
