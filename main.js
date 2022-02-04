const tt = (param) => {
return new Promise((resolve,reject)=>{
  console.log(param);
  const hi = function(res){
    console.log(res);
    resolve(res);
  }
  setTimeout(hi.call(this,param),1000);
})
.then((res)=>{
  console.log(res);
})
.catch(()=>{
  console.log('hello error');
});
}

tt('hello');
