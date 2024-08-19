//unsloved
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        long c = sc.nextInt();

        long answer = (long)Math.pow(a, b) % c;

        System.out.println(answer);
    }
}
