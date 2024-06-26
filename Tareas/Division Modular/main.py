
def extended_gcd(a, b):
  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def divide(a, b, n):  #b/a mod n
  d,s,t = extended_gcd(a, n)
  if d!=1: raise 'a and b are not relative primes'
  return (s*b)%n
  
a, b, n = map(int, input().split());
print(divide(a, b, n))