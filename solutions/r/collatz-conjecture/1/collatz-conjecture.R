collatz_step_counter <- function(num) {
  steps = 0
  if(length(num) == 1){
    if (num <=0) {
      stop()
    } else{
      initial = num;
      while (initial > 1) {
        if(initial %% 2 == 0){
          initial = initial / 2
        } else {
          initial = 3*initial + 1
        }
        steps = steps + 1
      }
      return(steps)
    }
    
  } else {
    res = c()
    for (i in num) {
      steps = 0
      initial = i;
      while (initial > 1) {
        if(initial %% 2 == 0){
          initial = initial / 2
        } else {
          initial = 3*initial + 1
        } 
        steps = steps + 1
      }
      res = c(res,steps)
    }
    return (res)
  }
}
