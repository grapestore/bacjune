import java.util.*;
import java.io.*;


public class Solution {

    public void game(HashMap<String, String> user, HashMap<String, Integer> cash, String sell, Integer cost){
        Integer nextCost = (Integer) cost/10;
        Integer remain = cost-nextCost;
        if(cost>=10){
            cash.put(sell, cash.get(sell) + remain);
            if(user.get(sell) != null)
                game(user, cash, user.get(sell), nextCost);
        }
        else{
            cash.put(sell, cash.get(sell) + cost);
        }

    }

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        HashMap<String, String> user = new HashMap();
        HashMap<String, Integer> cash = new HashMap();

        for(int i=0; i< enroll.length; i++){
            if(referral[i].equals("-"))
                user.put(enroll[i],null);
            else
                user.put(enroll[i],referral[i]);
            cash.put(enroll[i],0);
        }

        for(int i=0; i< seller.length; i++){
            game(user, cash, seller[i], amount[i]*100);
        }

        int[] answer = new int [enroll.length];
        for(int i=0; i<enroll.length; i++){
            answer[i] = cash.get(enroll[i]);
        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }


    public static void main(String[] args) throws Exception {
        Solution sol = new Solution();
        String[] a = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] b = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] c = {"young", "john", "tod", "emily", "mary"};
        int[] d = {12, 4, 2, 5, 10};
        System.out.println(sol.solution(a,b,c,d));
    }
}
