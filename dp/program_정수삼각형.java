import java.util.*;

class Solution {
    public int game(int[][] tri, int[][] dp){

        int n = tri.length;
        Queue<int []> queue = new LinkedList<>();
        queue.add(new int[] {0,0});
        int [] dx = {0,1};
        while(queue.size()>0){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            for(int i=0; i<2; i++){
                int nx = x + dx[i];
                int ny = y + 1;
                if (0<=ny && ny<n && dp[ny][nx] < tri[ny][nx] + dp[y][x]){
                    dp[ny][nx] = tri[ny][nx] + dp[y][x];
                    queue.add(new int[] {nx,ny});
                }
            }
        }

        return Arrays.stream(dp[n-1]).max().getAsInt();
    }

    public int solution(int[][] tri) {
        int[][] cost = new int [tri.length][tri.length];
        for(int i=0; i< tri.length; i++){
            Arrays.fill(cost[i],0);
        }
        cost[0][0] = tri[0][0];
        int answer = game(tri, cost);
        return answer;
    }
}