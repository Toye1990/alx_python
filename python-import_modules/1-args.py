def print_arguments(args):
  """Prints the number and list of arguments."""
  number_of_arguments = len(args)
  if number_of_arguments == 0:
    print("No arguments.")
  else:
    print(f"Number of arguments: {number_of_arguments} argument(s):")
    for i, arg in enumerate(args):
      print(f"{i + 1}: {arg}")

if __name__ == "__main__":
  args = ["tack", "ball", "mask"]
  print_arguments(args)