import java.util.*;
import java.io.*;

public class program_게임맵 {

    public int game(int[][] maps){
        Integer m = maps[0].length;
        Integer n = maps.length;

        Integer [][] cost = new Integer[n][m];
        for(int i=0; i<n; i++){
            Arrays.fill(cost[i],10000);
        }
        cost[0][0] = 1;

        Integer [] dx = {0,1,0,-1};
        Integer [] dy = {-1,0,1,0};

        Queue<Integer []> queue = new LinkedList<>();
        queue.add(new Integer[] {0, 0});

        while(queue.size()>0){
            Integer [] temp = queue.poll();
            Integer x = temp[0];
            Integer y = temp[1];
            maps[y][x] = 0;
            for(int i=0; i<4; i++){
                Integer nx = x + dx[i];
                Integer ny = y + dy[i];
                if(0<=nx && nx<m && 0<=ny && ny<n && maps[ny][nx] == 1){
                    if(cost[y][x]+1 < cost[ny][nx]){
                        cost[ny][nx] = cost[y][x]+1;
                        queue.add(new Integer[] {nx,ny});
                    }
                }
            }
        }

        return cost[n-1][m-1];
    }

    public int solution(int[][] maps) {
        int answer = game(maps);
        if(answer == 10000){
            return -1;
        }
        return answer;
    }


    public static void main(String[] args) throws Exception {
        Solution sol = new Solution();
        int[][] arr = {{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}};
        System.out.println(sol.solution(arr));
    }
}


