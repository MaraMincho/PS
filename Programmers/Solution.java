import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int solution(int n, int[][] lighthouse) {
         int answer = 0;
        List<Set<Integer>> list = new ArrayList<>();
        for(int idx = 0; idx <= n; idx++) {
            list.add(new HashSet<>());
        }
        for(int[] lh : lighthouse) {
            list.get(lh[0]).add(lh[1]);
            list.get(lh[1]).add(lh[0]);
        }
        int[] visit = new int[n + 1];
        dfs(list, 1, visit);

        for(int v : visit) {
            if(v == 2) {
                answer++;
            }
        }
        return answer;
    }
    public void dfs(List<Set<Integer>> list, int pos, int[] visit) {
        visit[pos] = 1;
        Set<Integer> set = list.get(pos);
        for(int way : set) {
            if(visit[way] == 0) {
                dfs(list, way, visit);
                if(visit[way] == 1) {
                    visit[pos] = 2;
                }
            }
        }
    }
    public static void main(String[] args) {
        Solution cur = new Solution();
        cur.solution(8, null)
    }
}
