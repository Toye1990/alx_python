
""""
def try_combinations():
    for i in range(10):
        for j in range(10):
            if i != j:
                print(f"{i}{j}")

try_combinations()
"""

def print_now():
    for i in range(5):
        for j in range(10):
            if i != j:
                print(f"{i}{j},")
                
print_now()