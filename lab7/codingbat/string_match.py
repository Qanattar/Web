def string_match(a, b):
  
  cnt = 0
  for i in range(min(len(a), len(b))-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      cnt+= 1

  return cnt