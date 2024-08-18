//스택 이용 -> top에 같은 문자가 나오면 pop
//top과 문자가 같으면 쌍을 지어 스택을 비움, 같지 않으면 스택에 쌓임
//문자열을 모두 돌고 스택이 비어있으면 좋은 단어
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        Stack<String> stack = new Stack<>(); //스택 이용
        int answer = 0;

        for(int i=0; i<n; i++) {
            String str = sc.nextLine();
            String[] arr = str.split("");
            for (String s : arr) {
                if (!stack.empty() && s.equals(stack.peek())) stack.pop();
                else stack.push(s);
            }
            if(stack.isEmpty()) answer++;
            stack.clear();
        }
        System.out.print(answer);
    }
}
