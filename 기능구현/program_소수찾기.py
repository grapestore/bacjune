from itertools import permutations

def prime(n):
    prime_num[0] = False
    prime_num[1] = False
    for i in range(2,n//2):
        if prime_num[i] == True:
            for j in range(i*2,n,i):
                prime_num[j] = False

def solution(numbers):
    global prime_num
    n = len(numbers)
    prime_num = [True]*(10**n)
    prime(10**n)
    answer = []
    arr = list(map(str,numbers))
    for i in range(1,n+1):
        for j in set(permutations(arr,i)):
            temp = int(''.join(j))
            if prime_num[temp] == True:
                print(temp)
                answer.append(temp)
    return len(set(answer))


    import java.util.*;


# java 풀이
# class Solution {
    
#     HashSet<Integer> result = new HashSet<>();

#     private boolean[] prime_num;


#     public void permutation(ArrayList<String> arr, boolean[] visit, ArrayList<String> output, int length, int n, int k) {

#         if (length == n) {
#             String temp = String.join("", output);
#             Integer num = Integer.parseInt(temp);
#             if(prime_num[num] == true){
#                 result.add(num);
#             }
#             return;
#         }
#         for (int i = 0; i < k; i++) {
#             if (visit[i] == false) {
#                 visit[i] = true;
#                 output.add(arr.get(i));
#                 permutation(arr, visit, output, length, n + 1, k);
#                 output.remove(arr.get(i));
#                 visit[i] = false;
#             }
#         }
#         return;
#     }

#     public void prime(int n) {
#         prime_num[0] = false;
#         prime_num[1] = false;
#         for (int i = 2; i < n / 2; i++) {
#             if (prime_num[i] == true) {
#                 for (int j = 2 * i; j < n; j += i) {
#                     prime_num[j] = false;
#                 }
#             }
#         }
#     }

#     public int solution(String numbers) {
#         int n = numbers.length();
#         int len = (int) Math.pow(10, n);

#         prime_num = new boolean[len];
#         boolean[] visit = new boolean[len];
#         ArrayList<String> list = new ArrayList();

#         Arrays.fill(prime_num, true);
#         Arrays.fill(visit, false);
#         prime(len);
#         for (Character x : numbers.toCharArray()) {
#             list.add(Character.toString(x));
#         }

#         for(int i=1;i<=n;i++){
#             permutation(list, visit, new ArrayList(), i, 0, n);
#         }

#         int answer = 0;
#         return result.size();
#     }
# }