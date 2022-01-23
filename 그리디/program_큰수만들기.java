import java.util.*;

class Solution {
    public String solution(String number, int k) {
        char[] nums = new char[number.length()];
        number.getChars(0, number.length(), nums, 0);
        Stack<Integer> stack = new Stack<>();
        int cnt = 0;
        for(char num : nums){
            Integer n = num - '0';
            while(stack.empty()==false && stack.peek()<n && cnt<k){
                stack.pop();
                cnt+=1;
            }
            stack.push(n);
        }
        while(cnt<k){
            stack.pop();
            cnt+=1;
        }
        String answer = "";
        for(Integer num : stack){
            answer += num.toString();
        }
        return answer;
    }
}