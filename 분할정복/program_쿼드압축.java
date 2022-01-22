import java.util.*;
import java.io.*;


public class Solution {

    protected int[][] matrix;
    public int[] answer = {0,0};

    public int divide(int size, int x, int y){

        if(size == 1){
            int a = (matrix[y][x]==1) ? 1 : 0;
            return answer[a]+=1;
        }

        int zero_cnt = 0;
        int one_cnt = 0;
        boolean status = true;
        for(int j=y; j<y+size; j++){
            for(int i=x; i<x+size; i++){
                if(matrix[j][i] == 1){
                    one_cnt += 1;
                }
                else{
                    zero_cnt += 1;
                }
                if(one_cnt>0 && zero_cnt>0){
                    status = false;
                    break;
                }
            }
            if(status==false) break;
        }

        if(zero_cnt == 0)
            return this.answer[1] += 1;
        else if(one_cnt == 0)
            return this.answer[0] += 1;

        int nextSize = (int) Math.floor((double) size/2);
        divide(nextSize, x+nextSize*0, y+nextSize*0);
        divide(nextSize, x+nextSize*1, y+nextSize*0);
        divide(nextSize, x+nextSize*0, y+nextSize*1);
        divide(nextSize, x+nextSize*1, y+nextSize*1);
        return 0;
    }

    public int[] solution(int[][] arr) {
        this.matrix = arr;
        divide(arr.length, 0, 0);
        return answer;
    }



    public static void main(String[] args) throws Exception {
        Solution sol = new Solution();
        int[][] a = {{1,1,0,0},{1,0,0,0},{1,0,0,1},{1,1,1,1}};
        System.out.println(Arrays.toString(sol.solution(a)));
    }
}
