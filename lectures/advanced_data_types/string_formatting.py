print("Sammy has {}{} balloons.".format(5, 6))
print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
print("Sammy the {first} {second} a {pr}.".format(second="shark", first="made", pr="pull request"))
print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))

foo = 'test'
verb = "flies"
preposition = "like"

bar = 'Hi there. "How" are you?'

def test():
    return 'Hello'
num1 = 5
num2 = 4

print(f"Time {verb} {num1+num2} {test()} an arrow. Fruit {verb} {preposition} a banana.")

name = "boo"
friend_name = "foo"
print('Hey %s, there is you friend %s!' % (name, friend_name))

name = "boo"
friend_name = "foo"
data_dict = {"me": name, "friend": friend_name}
print('Hey %(me)s, there is you friend %(friend)s!' % data_dict)