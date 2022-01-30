function combination(arr, selectNumber) {
  const results = [];
    if (selectNumber === 1) {
      return arr.map((el) => [el]); }
 
    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1); 
      // 해당하는 fixed를 제외한 나머지 뒤
      const combinations = combination(rest, selectNumber - 1); 
      const attached = combinations.map((el) => [fixed, ...el]);
      results.push(...attached); 
    });
    return results; 
}

function main(orders, course) {
  const answer = [];
  
  for(let i = 0; i < course.length; i++){
      const result = {};
      
      orders.forEach((element) => {
          combination(element.split(""), course[i]).forEach((e) => {
              const str = e.sort().join("");
              if(!isNaN(result[str])){
                  result[str] += 1;
              }
              else{
                  result[str] = 1;
              }
          });
      });
          for(const [key, value] of Object.entries(result)){
              if(value > 2){
                  answer.push(key);
              }
          }
  }
  
  return answer.sort();
}

arr1 = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]];
arr2 = [[2,3,4],[2,3,5],[2,3,4]];

for(let i=0; i<arr2.length; i++){
  console.log(main(arr1[i],arr2[i]));
}