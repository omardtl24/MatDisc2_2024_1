def fast_mod_exp(b, k, m):
  if k==0: return b%m
  prev = fast_mod_exp(b, k-1, m)
  return (prev*prev)%m

b, k, m = map(int, input().split());
print(fast_mod_exp(b, k, m))