function processData(input) {
     

    function Palindrome(input){
      
      var x=input.toString();
      var i=0;
      var j=x.length-1;
      var count=0;
      var s=1;
      var l=x[0];
      var r=x[x.length-1];
      
      while(i<x.length/2 && j>x.length/2){
        if(x[i]!=x[j]){
          count=-1;
         // console.log("Hello");
          break;
        }
        else if((x[i]==x[j] ) && (l==x[i] && r==x[j])){
          count=2;
        }
        
        else if((x[i]==x[j] ) && (l!=x[i] && r!=x[j])){
          count=5;
        }
        i=i+1;
        j=j-1;
      }
      
      if(count==-1){
          s=0;
         // console.log("WW")
        }
      else if(count==5){
        s=4;
      }
      else if(count==2){
          s=2;
      }
      
     return s;
    
    }
    
    
    
    
    
    function consecutive(input){
      y=[];
      var counter=0;
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
        
        if(v==1){
           i=i+1;
        }
        else if(v==0){
          i=i+1;
          counter=counter+1;
        }
        else if( v>0 || v>1){
          s=-1;
          break;
        }
      }
      if(s==-1){
        s=0;
      }
      else if(counter==y.length()){
        s=1;
      }
      return s;
    }
        
            
            
    function start(input){
       var x=input.toString();
        var y=input;
            if(x.length>=3){
              
              var s=0;
              
              for (var i=0; i<5; i++){
    
            if(input%10==0){
              console.log("Yes");
              break;
            }
             
            else if(i==1){
             s=consecutive(y);
             if(s==1){
                 console.log("Yes");
                 break;
             }
             else if(s==0){
                  console.log("No");
                  break;
                }
            }
             
            else if(i==2){
                s=Palindrome(y);
                if(s==1){
                 console.log("YEs")
                 break;
                }
                if(s==0){
                  console.log("No");
                  break;
                }
            }
            }
    }
            
            else{
              console.log("No");
            }
    }
    start(input);
    }
    processData(1551)
    