from collections import defaultdict,deque

def solution(n, results):
    answer = 0
    win = {}
    lose = {}
    for i in range(1,n+1):
        win[i] = set()
        lose[i] = set()
    for w,l in results:
        win[w].add(l)
        lose[l].add(w)
    
    for i in range(1,n+1):
      for winner in lose[i]:
        win[winner].update(win[i])
      for loser in win[i]:
        lose[loser].update(lose[i])

    for i in range(1, n+1):
      if len(win[i]) + len(lose[i]) == n-1:
        answer += 1

    return answer

if __name__ == "__main__":
  print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


# java로 hashmap 자료구조 만들기도 빡세네 ;;
#   import java.util.*;
# import java.io.*;


# public class Solution {

#     public void set(int n, int[][] results, HashMap<Integer,Set<Integer>> win, HashMap<Integer,Set<Integer>> lose){
#         for(int i=1; i<results.length+1; i++) {
#             Set<Integer> tmp = new HashSet<>();
#             win.put(i,tmp);
#             lose.put(i,tmp);
#         }

#         for(int i=0; i<results.length; i++) {
#             Set<Integer> wtmp = new HashSet<>();
#             Set<Integer> ltmp = new HashSet<>();
#             Set<Integer> w_set = win.get(results[i][0]);
#             Set<Integer> l_set = lose.get(results[i][1]);
#             wtmp.add(results[i][1]);
#             ltmp.add(results[i][0]);
#             if(w_set!=null){
#                 wtmp.addAll(w_set);
#             }
#             if(l_set!=null){
#                 ltmp.addAll(l_set);
#             }
#             win.put(results[i][0],wtmp);
#             lose.put(results[i][1],ltmp);
#         }
#     }

#     public int solution(int n, int[][] results) {
#         HashMap<Integer,Set<Integer>> win = new HashMap<>();
#         HashMap<Integer,Set<Integer>> lose = new HashMap<>();
#         this.set(n,results,win,lose);
#         System.out.println(win);
#         System.out.println(lose);

#         int answer = 0;
#         return answer;
#     }


#     public static void main(String[] args) throws Exception {
#         Solution sol = new Solution();
#         int[][] arr = {{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}};
#         System.out.println(sol.solution(5, arr));
#     }
# }
