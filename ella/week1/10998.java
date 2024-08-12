import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] arr = str.split("");
        int check = 1;

        for(int i=0; i<arr.length/2; i++){
            if(!arr[i].equals(arr[arr.length-1 - i])){
                check = 0;
                break;
            }
        }
        System.out.print(check);
    }
}
