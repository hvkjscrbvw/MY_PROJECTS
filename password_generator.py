import string

list_of_acceptable_chars = [string.printable]

list_of_acceptable_chars = [x for x in str(list_of_acceptable_chars) if x.isalnum()]

if 'c' in list_of_acceptable_chars:
    print('found')
    

