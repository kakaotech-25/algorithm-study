package 바킹독.이진탐색.좌표압축;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    // 1. 정렬
    // 2. 중복제거
    // 3. 이분탐색 수행
    static int n;
    static int[] arr;
    static int[] sort;

    public static int binarySearch(int[] sort, int target, int st, int en) {
        int mid = (st + en) / 2;

        if(sort[mid] == target) {
            return mid;
        }

        else if(sort[mid] > target) {
            return binarySearch(sort, target, st, mid-1);
        }

        else {
            return binarySearch(sort, target, mid+1, en);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
         n = Integer.parseInt(br.readLine());
        arr = new int[n];
        sort = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sort[i] = arr[i];
        }

        // 1. 정렬
        Arrays.sort(sort);

        // 2. 중복제거
        sort = Arrays.stream(sort).distinct().toArray();

        // 3. 이분탐색 수행
        for(int i=0; i<n; i++) {
            bw.write(binarySearch(sort, arr[i], 0, sort.length) + " ");
        }

        bw.flush();
        bw.close();
    }
}