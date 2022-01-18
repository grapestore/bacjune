import java.util.*;
import java.io.*;


public class Solution {

    public int game(int k, int a, int b, int depth){

        if(depth == k){
            return depth;
        }

        if(a%2 == 0 && a-b==1){
            return depth;
        }
        else if(a%2==1 && b-a==1){
            return depth;
        }
        else{
            return game(k,(int) Math.ceil((double)a/2),(int) Math.ceil((double)b/2),depth+1);
        }
    }
    public int solution(int n, int a, int b)
    {
        int k = 1;
        while(true){
            if(n == (int) Math.pow(2,k)){
                break;
            }
            k += 1;
        }
        return game(k,a,b,1);

    }


    public static void main(String[] args) throws Exception {
        Solution sol = new Solution();
        System.out.println(sol.solution(8,4,7));
    }
}
