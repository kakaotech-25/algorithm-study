import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int[] height = new int[9];
        boolean check = false;
        for(int i=0; i<9; i++){
            height[i] = sc.nextInt();
            sum += height[i];
        }

        for(int i=0; i<8; i++){
            for(int j = i+1; j<9; j++){
                if(sum - height[i] - height[j] == 100){
                    height[i] = 0;
                    height[j] = 0;
                    check = true;
                    break;
                }
            }
            if(check == true) break;
        }

        Arrays.sort(height);
        for(int i=2; i<9; i++){
            System.out.println(height[i]);
        }
    }
}
