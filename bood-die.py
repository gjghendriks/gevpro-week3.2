'''
Program for seaching languages where the word for blood is the same as die
By Gijs Hendriks
s2410540
'''

import json
import collections

json_data=open('blood-die.json').read()
data = json.loads(json_data)

Language = collections.namedtuple('Language', ['lang', 'clss'])

def format(string):
    r''' Used to format a string. It removes spaces and \n and splits the string at the , '''
    stringlst = string.replace(' ', '').replace('\n', '').split(',')
    return stringlst

lst = [Language(x[0], x[1]) for x in data for a in format(x[2]) for b in format(x[3]) if a == b]
print (lst)
