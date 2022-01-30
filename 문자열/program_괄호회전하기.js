function solution(s) {
    
  const check = (strs) => {
      const stack = [];
  for(let i=0, size=strs.length; i<size; i++){
      if(strs[i] === ']' || strs[i] === ')' || strs[i] === '}'){
          if(!stack.length){
              return false;
          }
          if(strs[i] === ']' && stack[stack.length - 1] === '['){
              stack.pop();
          }
          else if(strs[i] === '}' && stack[stack.length - 1] === '{'){
              stack.pop();
          }
          else if(strs[i] === ')' && stack[stack.length - 1] === '('){
              stack.pop();
          }
          else{
              return false;
          }
      }
      else{
          stack.push(strs[i]);
      }
  }
  if(stack.length) return false;
  return true;
  };
  
  
  
  var answer = 0;
  const arr = [];
  let temp = s;
  for(let i=0, size=s.length; i<size; i++){
      arr.push(temp);
      temp = temp.substring(1,size) + temp.substring(0,1);
  }
  arr.forEach((e)=>{
      if(check(e)){
          answer += 1;
      }
  })
  
  
  return answer;
}