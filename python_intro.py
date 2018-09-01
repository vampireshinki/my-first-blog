print('Hello, Django girls!')
list=[1,2,3]
print(list)
print(len(list))
member1={'name':'Jung Yunho', 'DOB':'19860206','Band':'DBSK','favorite_color':'red'}
print(member1['name'])
if 1<2:
    print('True')
True and True
a=False
print(a)
if 2>5:
    print('Hooray!')
else:
        print('BOOOOO!')
if member1['name'] != 'Jung Yunh':
    print('Uknow Yunho')
elif member2['name'] == 'Kim Jaejoong':
    print('Hero')
else:
    print('boooo')
member2={'name':'Kim Jaejoong', 'DOB':'19860126','Band':'JYJ'}
def hi():
    print('HELLO!')
    print('How you doin\'?')
hi()

def hi(name):
    if name == 'Lauren':
        print('Hi ' + name + '!')
    elif name == 'Bob':
        print('Hi Bob')
    else:
        print('Hi Anon')
hi('Lauren')
dbsk = ['Yunho', 'Jaejoong', 'Yoochun', 'Junsu', 'Changmin']
def hi(name):
    print('Hi ' + name + '!')

dbsk = ['Yunho', 'Jaejoong', 'Yoochun', 'Junsu', 'Changmin']
for name in dbsk:
    hi(name)
    print('next')
    