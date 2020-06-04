import sys

def hello(name):
  print("hello")

if __name__ == "__main__":
  name = ""
  
  if len(sys.argv) >= 1:
    name = sys.argv[1]
    
  hello(name)
