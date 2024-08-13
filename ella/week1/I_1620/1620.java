import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        HashMap<Integer, String> map1 = new HashMap<>();
        HashMap<String, Integer> map2 = new HashMap<>();

        for(int i=1; i<=n; i++){
            String name = sc.nextLine();
            map1.put(i, name);
            map2.put(name, i);
        }

        for(int i=1; i<=m; i++){
            String p = sc.nextLine();
            if(49 <= p.charAt(0) && p.charAt(0) <= 57){
                System.out.println(map1.get(Integer.parseInt(p)));
            }
            else System.out.println(map2.get(p));
        }
    }
}
