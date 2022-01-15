import java.util.*;

class Solution {
    
    public void dfs(int[][] matrix, Integer[] visit, int start, int way, int n){
        visit[start] = way;
        for(int i=0; i<n; i++){
            if(i!=start && matrix[start][i] == 1 && visit[i]==-1){
                dfs(matrix, visit, i, way, n);
            }
        }
    }


    public int solution(int n, int[][] computers) {
        int answer = 0;
        Integer[] visit = new Integer [n];
        for(int i=0; i<n; i++){ visit[i] = -1;}
        for(int i=0; i<n; i++){
            if(visit[i] == -1){
                dfs(computers, visit, i, i, n);
            }
        }
        Set<Integer> set = new HashSet<Integer>();
        set.addAll(Arrays.asList(visit));

        return set.size();
    }
}