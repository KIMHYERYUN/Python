#function(something)
#Do this with something
#Then do this
#Finally do this

def function(something):
    print(something)
function(0)
function("Hello")

#functions with more than 1 put
#위치인자 : something1, something2

#function(a, b, c):
#Do this with a
#Then do this with b
#Finally do this with c


def function(something1, something2):
    print(something1 + something2)
function(1,2)
function("Hello", "Everyone")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jayden", "Korea")
