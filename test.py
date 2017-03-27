def test(got,expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = ' X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
def main():
  print
  print 'collatz'
  test(collatz(4),'2')
  test(collatz(3),'7')
if __name__ == '__main__':
  main()
