import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        char[] arr = str.toCharArray();
        for(int i=0; i<arr.length; i++){
            if(arr[i] >= 'a' && arr[i] <= 'z'){
                if(arr[i] + 13 > 'z') arr[i] = (char)(arr[i] + 13 - 26);
                else arr[i] = (char)(arr[i] + 13);
            }
            if(arr[i] >= 'A' && arr[i] <= 'Z'){
                if(arr[i] + 13 > 'Z') arr[i] = (char)(arr[i] + 13 - 26);
                else arr[i] = (char)(arr[i] + 13);
            }
            System.out.print(arr[i]);
        }
    }
}
