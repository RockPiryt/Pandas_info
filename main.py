import pandas

data = pandas.read_csv('central_park_squirrel.csv')
# print(data)

#choose column
column = data['Primary Fur Color']
# print(column)

list_column = data['Primary Fur Color'].to_list()
# print(list_column)


#count squirrels_______________________________
gray_count = list_column.count('Gray')
cinnamon_count = list_column.count('Cinnamon')
black_count = list_column.count('Black')
print(gray_count)
print(cinnamon_count)
print(black_count)

#2 method_____________________________________
# count row with gray squirrels

#ilość wierszy
gray_fur = len(data[data['Primary Fur Color'] == 'Gray'])
print(gray_fur)

#create dict______________________________________
#dict have to have title!!!
count_squirrels = {
    'Fur color': ["Gray", "Cinnamon", "Black" ],
    'Count': [gray_count, cinnamon_count, black_count],
}
print(count_squirrels)

bad_dict_count_squirrels = {
    'Gray': gray_count,
    'Cinamon': cinnamon_count,
    'Black': black_count,
}

#Create file csv_________________________________________
#change dict to DataFrame
count_squirrels_df = pandas.DataFrame(count_squirrels)

#save DataFrame to csv
count_squirrels_df.to_csv('count_furs2.csv')
