import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder res = new StringBuilder();
        
        IntStream.range(0,a.length()).forEach(ind -> {
            var cur = a.charAt(ind);
            var curRes = Character.isUpperCase(cur) ? Character.toLowerCase(cur) : Character.toUpperCase(cur);
            res.append(curRes);
        });
        System.err.println(res.toString());
    }
}