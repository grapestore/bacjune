function solution(citations) {
  var answer = 0;
  for(let i=0; i<1001; i++){
      let cnt = 0;
      citations.forEach((x)=>{
          if(x>=i) cnt+=1;
      })
      if(cnt>=i) answer=i;
  }
  return answer;
}