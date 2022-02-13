function processData(input) {
     
    function AllequalPallindrome(value){
      var x=value;
      var i=0;
      var j=x.length-1;
      var count=1;
      var s=1;
      var def=0;
      while (i<=x.length-1){
        
       def=parseInt(x[i+1])-parseInt(x[i]);
       if(def>1 && def!=9){
         s=0;
        i=i+1;
       }
       if(x[i]==x[j] && count==1){
          i=i+1;
          j=j-1;
       }
       else if(count==-1){
         i=i+1;
       }
       else{
         count=-1;
       }
      }
      if(count==-1 || s==0){
          count=0;
        }
      if(count==1 || s==1){
        count=1;
      }
     return count;
    }
    
    var x=input.toString();
    var s=0;
    if(x.length>=3){
      if(s==0){
       if(AllequalPallindrome(x)==1){
         console.log("Yes");
         s=1;
       }
       else{
            console.log("No");
          } } }
    else{
      console.log("No");
    }}
    processData(275973423954)
    