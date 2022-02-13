 

 function processData(input) {
    
    
    function AlldigitSame(input){
      input=input.toString()
      var count=0;
      var s=0;
        for(var i=0; i<input.length; i++){
           for( var j=0; j<input.length; j++){
             if(input[i]!=input[j]){
               count=-1
               break
             }
             
           }
           if(count==-1){
             break;
           }
           else{
             count=count+1;
           }
}

        if(count==input.length){
          s=1;
        }
        else{
          s=0;
        }
        return s;
          
}


function Palindrome(input){
  
  var x=input.toString();
  var i=0;
  var j=x.length-1;
  var count=0;
  var s=0;
  while(i<x.length/2 &&  j> x.length/2){
    if(x[i]!=x[j]){
      count=-1;
      break;
    }
    i=i+1;
    j=j-1;
    
  }
  if(count==-1){
      s=0;
    }
  else{
    s=1;
  }
 return s;


}


function followszero(input){
  var i=1;
  var sum=0;
  var s=0;
  var x=input.toString();
 
  while(i<x.length){
    if(x[i]==='0'){
     // sum=sum+parseInt(x[i]);
     sum=sum+parseInt(x[i]);
    }
    else{
    sum=-1;
    break;
    }
    i=i+1;
  }

   if(sum==0){
      s=1;
    }
    else{
      s=0;
    }
   return s;
  
}



function occurTwice(input){
  y=[];
  var x=input.toString();
  for (var i=0; i<x.length;i++){
 //   console.log(x[i]);
    var value=parseInt(x[i]);
    y.push(value);
  }
  y.sort();
  
  var i=0;
  var s=1;
  
  while(i<y.length-1){
    var count=0;
    if(y[i]==y[i+1]){
      count=+1;
      i=i+1;
    }
    
    if(count>1 || count==0){
      s=0;
      break;
    }
    i=i+1;
    
    if(s==0){
         s=0;
    }
    else{
         s=1;
    }
  }
  
  return s;
  

}



function consecutive(input){
  y=[];
  var x=input.toString();
  for (var i=0; i<x.length;i++){
 //   console.log(x[i]);
    var value=parseInt(x[i]);
    y.push(value);
  }
  y.sort();
  
  var i=0;
  var s=1;
  while(i<y.length-1){
    var t1=y[i];
    var t2=y[i+1];
    var v=parseInt(t2)-parseInt(t1);
    
    if(v==0 || v==1){
       i=i+1;
    }
    else if( v>0 || v>1){
      s=-1;
      break;
    }
  }
  if(s==-1){
    s=0;
  }
  else{
    s=1;
  }
  return s;
}
        //console.log(consecutive(input));

        //console.log(occurTwice(input));
        // console.log(followszero(input));

        // console.log(AlldigitSame(input))
        
        // console.log(Palindrome(input))
        
        
function start(input){
   var x=input.toString();
    var y=input;
        if(x.length>=3){
          
          var s=0;
          
          for (var i=0; i<5; i++){
            
          if(i==0){
          s=AlldigitSame(y);
            if(s==1){
             console.log("Yes");
             break;
            }
          }
          else if(i==1){
            s=followszero(y);
             if(s==1){
             console.log("Yes")
             break
         }
        }
         
        else if(i==2){
         s=consecutive(y);
         if(s==1){
             console.log("Yes")
             break;
         }
        }
         
        else if(i==3){
            s=Palindrome(y);
            if(s==1){
             console.log("Yes")
             break;
            }
        }
        else if(i==4){
            s=occurTwice(y);
            if(s==1){
              console.log("Yes");
             break;
            }
        }
        }
        
        if(s==0){
          console.log("No"); 
          }
          
        }
        
        else{
          console.log("No");
        }
}
start(input);
}

 processData(123456787678)