#!/usr/bin/node
let count = process.argv[2];
if (isNaN(Math.floor(Number(count)))){
    console.log('Missing size');
}
else if (Number(count) <=0){
    return;
}
else{
   for (let i=0; i < count; i++){
      let result = '';
      for (let j=0; j < count; j++){
        result += 'X';
       }
    console.log(result);
   }
}

