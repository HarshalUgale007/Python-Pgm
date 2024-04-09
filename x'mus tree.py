def decorator(func):

  def wrapper(*a, **ar):
    print("*.*.*.*.*.*.*.*.*")
    func(*a, **ar)
    print("*.*.*.*.*.*.*.*.*")

  return wrapper


gui = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
@decorator
def get_a_tree(self):
  for row in gui:
    for pixel in row:
      if pixel:
        print('*', end='')
      else:
        print(' ', end='')
    print('')
    
get_a_tree("a")