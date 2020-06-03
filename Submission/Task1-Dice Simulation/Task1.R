randomsum <- function(){
  
  rn <- floor(runif(3,1,6))
  return(sum(rn))
 
}

sim <- replicate(50, randomsum())
print(sim)

plot(table(sim), xlab='Sum', ylab='Frequency', main='50 Rolls of 3 dice')


tenruns<- replicate(10, replicate (50, randomsum()))
prob <- sum((14 <= tenruns) & (tenruns <= 16))/length(tenruns)
print(prob)

