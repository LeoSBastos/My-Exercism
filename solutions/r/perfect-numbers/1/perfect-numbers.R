factoring_sum = function(n) {
  vetor = c();
  for (i in seq(1,n-1)){
    if (n %% i == 0){
      vetor = c(vetor, i);
    }
  }
  return (sum(vetor))
}

number_type = function(n) {
  if (n < 1){
    stop();
  } else if(n==1){
    return ("deficient")
  } else {
  soma = factoring_sum(n);
  if(n == soma){
    return ("perfect")
  }else if(soma > n){
    return ("abundant")
  } else {
    return ("deficient")
  }
}
}