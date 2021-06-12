Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # dictionaries are written with {}
>>> # it store values in key:value pairs
>>> #ordered,changeable and doesnt allow duplicates
>>> # keys should be unique.
>>> d1 = {
	'name':'rahul',
	'age': 25,
	'income':2500000,
	'city':'bangalore'
	}
>>> print(d1)
{'name': 'rahul', 'age': 25, 'income': 2500000, 'city': 'bangalore'}
>>> len(d1)
4
>>> #key() --> accessing the values using key method
>>> d1['age']
25
>>> d1['name']
'rahul'
>>> type(d1)
<class 'dict'>
>>> # we can also access values by using get()
>>> x = d1.get('city')
>>> print(x)
bangalore
>>> d1.get('income')
2500000
>>> # keys() --> to get list of all keys in the dict
>>> d1.keys()
dict_keys(['name', 'age', 'income', 'city'])
>>> # we can directly change any value
>>> d1['age'] = 24
>>> d1
{'name': 'rahul', 'age': 24, 'income': 2500000, 'city': 'bangalore'}
>>> # adding items to existing dict
>>> d1['religion'] = 'hindu'
>>> d1
{'name': 'rahul', 'age': 24, 'income': 2500000, 'city': 'bangalore', 'religion': 'hindu'}
>>> # values() --> to get values of dict
>>> d1.values()
dict_values(['rahul', 24, 2500000, 'bangalore', 'hindu'])
>>> # items() --> to get items i.e., keys and values
>>> d1.items()
dict_items([('name', 'rahul'), ('age', 24), ('income', 2500000), ('city', 'bangalore'), ('religion', 'hindu')])
>>> y = d1.items()
>>> print(y)
dict_items([('name', 'rahul'), ('age', 24), ('income', 2500000), ('city', 'bangalore'), ('religion', 'hindu')])
>>> d1['role'] = 'python developer'
>>> d1
{'name': 'rahul', 'age': 24, 'income': 2500000, 'city': 'bangalore', 'religion': 'hindu', 'role': 'python developer'}
>>> # we can change value by using update()
>>> k = d1.update({'age':'26'})
>>> print(k)
None
>>> 
>>> k = d1.update({'age':26})
>>> print(k)
None
>>> d1.update({'age':26})
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'bangalore', 'religion': 'hindu', 'role': 'python developer'}
>>> # del() --> to remove any key
>>> del d1['religion']
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'bangalore', 'role': 'python developer'}
>>> # pop() --> it can remove specified key name and by using popitem() it can remove last inserted item
>>> d1.pop('role')
'python developer'
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'bangalore'}
>>> d1['exp'] = 3
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'bangalore', 'exp': 3}
>>> d1.pop()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d1.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d1.popitem()
('exp', 3)
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'bangalore'}
>>> # del() --> it can remove item with specified key name
>>> d1['city'] = 'hyd'
>>> d1['skills'] = 'python','java'
>>> d1
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'hyd', 'skills': ('python', 'java')}
>>> d2=d1.copy()
>>> d2
{'name': 'rahul', 'age': 26, 'income': 2500000, 'city': 'hyd', 'skills': ('python', 'java')}
>>> # clear() --> it will empty the dict
>>> d1.clear()
>>> d1
{}
>>> # NESTED dictionary
>>> person1 = {'name':'krish','age':25}
>>> person2 = {'name':'siva','age':24}
>>> d3 = {1:person1,2|:person2}
SyntaxError: invalid syntax
>>> d3 = {1:person1,2:person2}
>>> d3
{1: {'name': 'krish', 'age': 25}, 2: {'name': 'siva', 'age': 24}}
>>> # we can also try this in another method
>>> d4 = {1:{'name':'krish','age':25},2:{'name':'siva','age':24}}
>>> d4
{1: {'name': 'krish', 'age': 25}, 2: {'name': 'siva', 'age': 24}}
>>> d4[1]
{'name': 'krish', 'age': 25}
>>> d4[1]['role'] = 'python developer'
>>> d4
{1: {'name': 'krish', 'age': 25, 'role': 'python developer'}, 2: {'name': 'siva', 'age': 24}}
>>> d4[2]['habits'] = 'gaming','riding','reading'
>>> d4
{1: {'name': 'krish', 'age': 25, 'role': 'python developer'}, 2: {'name': 'siva', 'age': 24, 'habits': ('gaming', 'riding', 'reading')}}
>>> # accessing the name of first person
>>> d4[1]['name']
'krish'
>>> # accessing the habits of second person
>>> d4[2]['habits']
('gaming', 'riding', 'reading')
>>> d4[2]['habits'][0:2)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> d4[2]['habits'][0:2]
('gaming', 'riding')
>>> 
>>> D1 = {
	'may_batch':{
		'student':{
			'name':'sivakrishna',
			'marks':{
				'python':95,
				'maths': 88,
				"full stack": 90,
				'science':80,
				'english':93
				}
			}
		}
	}
>>> D1
{'may_batch': {'student': {'name': 'sivakrishna', 'marks': {'python': 95, 'maths': 88, 'full stack': 90, 'science': 80, 'english': 93}}}}
>>> D1['may_batch']['student']['name']
'sivakrishna'
>>> D1['may_batch']['student']['marks'][1]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    D1['may_batch']['student']['marks'][1]
KeyError: 1
>>> D1['may_batch']['student']['marks'][0:2]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    D1['may_batch']['student']['marks'][0:2]
TypeError: unhashable type: 'slice'
>>> >>> D1['may_batch']['student']['marks']['math']
SyntaxError: invalid syntax
>>> D1['may_batch']['student']['marks']['math']
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    D1['may_batch']['student']['marks']['math']
KeyError: 'math'
>>> D1['may_batch']['student']['marks']['maths']
88
>>> D1['may_batch']['student']['marks']['english']
93
>>> D1['may_batch']['student']['marks']
{'python': 95, 'maths': 88, 'full stack': 90, 'science': 80, 'english': 93}
>>> D1['may_batch']['student']
{'name': 'sivakrishna', 'marks': {'python': 95, 'maths': 88, 'full stack': 90, 'science': 80, 'english': 93}}
>>> D1['may_batch']['student']['marks'].update({'hindi':85})
>>> D1['may_batch']['student']['marks']
{'python': 95, 'maths': 88, 'full stack': 90, 'science': 80, 'english': 93, 'hindi': 85}
>>> D1['may_batch']['student'].update({'section':'A'})
>>> D1
{'may_batch': {'student': {'name': 'sivakrishna', 'marks': {'python': 95, 'maths': 88, 'full stack': 90, 'science': 80, 'english': 93, 'hindi': 85}, 'section': 'A'}}}
>>> 