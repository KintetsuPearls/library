def fib(n):
  p = 5**0.5
  re = 1/p*(((1+p)/2)**n-((1-p)/2)**n)
  return int(re)
