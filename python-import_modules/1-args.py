import sys

def args():
  """Prints the number of and the list of its arguments."""
  num = len(sys.argv)
  print("Number of arguments:", num)
  for i in range(1, num):
    print("Argument {}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
  args()