import hello;

def test_hello():
    assert hello.hello_world() == "Hello, World!"
    
def test_hello_name():
  assert hello.hello_world("Ed") == "Hello, Ed!"
