import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int task = sc.nextInt();
        sc.nextLine();

        for(int i=0; i<task; i++){
            int n = sc.nextInt();
            sc.nextLine();
            int answer = 1;
            HashMap<String, Integer> map = new HashMap<>();
            for(int j=0; j<n; j++){
                String wear = sc.nextLine();
                String[] arr = wear.split(" ");
                map.put(arr[1], map.getOrDefault(arr[1], 0) + 1);
            }
            for (int count : map.values()) {
                answer *= (count + 1);
            }
            System.out.println(answer-1);
        }
    }
}
