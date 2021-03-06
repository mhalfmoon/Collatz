def collatz(n):
  i = 0 
  while n > 1:
    if n % 2 == 0:
      n = n/2
      i += 1
    else:
      n = 3*n+1
      i += 1
  return i 

def test(got,expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = ' X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
  print
  print 'collatz'
  test(collatz(4),2)
  test(collatz(3),7)
  test(collatz(32),5)

if __name__ == '__main__':
  main()   
