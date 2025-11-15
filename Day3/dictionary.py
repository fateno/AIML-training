print('Dictionary example')
our_dictionary=[
    {"id":'1', "name":'smiski', 'age':'35'},
    {"id":'2', "name":'sonny', 'age':'35'},
    {"id":'3', "name":'crybaby', 'age':'35'},
    {"id":'4', "name":'dimoo', 'age':'35'}
]

for k in our_dictionary: 
    print(k['id']+"->"+k['name']+"->"+k['age'])