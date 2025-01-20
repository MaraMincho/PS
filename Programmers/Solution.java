import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        List<Integer> answer = new ArrayList<Integer>();
        for (var value: queries) {
            int s = value[0];
            int e = value[1];
            int k = value[2];
            int curAnswer = -1;
            for (int ind = s; ind <= e; ind += 1) {
                if (k < arr[ind] && (curAnswer == -1 ? 1_000_000 : curAnswer) > arr[ind]) {
                    curAnswer = arr[ind];
                }
            }
            answer.add(curAnswer);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}