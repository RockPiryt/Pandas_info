
#___________________________________________WITH OPEN_________________________________
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()# read each line
#     print(data)

#     #print list ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


#______________________________________CSV MODULE_______________________________________
# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # print(data)#we can loop through this object (csv.reader object)
#     temperatures = []
#     for row in data:
#         #print(row)#one by one['Monday', '12', 'Sunny'], ['Tuesday', '14', 'Rain'] itp
#         single_temp = row[1] # print one by one (temp,12,14,15,14 itp) -string format with temp on 1 place
#         # print(single_temp)
#         if single_temp != 'temp':
#             temperatures.append(int(single_temp))#add ony number - convert to integer, without 'temp'
#     print(temperatures)#print list [12, 14, 15, 14, 21, 22, 24] 



#___________________________________________________PANDAS____________________________________________
import pandas

data = pandas.read_csv('weather_data.csv')
print(data)

#read column/ series_____________________________________
print(data.temp)
#or
print(data['temp'])

# read row____________________________________________________
row_monday = data[data['day'] == 'Monday']
print(row_monday)

# read row day with max temp
whole_temp_column = data['temp']#whole column temp
print(whole_temp_column)
day_wit_max_temp = data[data['temp'] == data['temp'].max()]
print(day_wit_max_temp)

#read atributes from row__________________________
tuesday = data[data['day'] == 'Tuesday']
print(tuesday['condition'])
print(tuesday.condition)#like atribute from object

temp in thursday in fahrenheit
thursday = data[data['day'] == "Thursday"]
temp_in_c = thursday.temp
print(temp_in_c)
fahrenheit_temp = temp_in_c * 1.8 + 32
print(fahrenheit_temp)

# convert whole table (DataFrame) to dict_____________________
data_in_dict= data.to_dict()
print(data_in_dict)

#convert column(series) to list__________________________
list_condition = data['condition'].to_list()
print(list_condition)
print(len(list_condition))

list_temp = data['temp'].to_list()
print(list_temp)


#calc average________________________________________________
#calc average temp
add_all_temp = sum(list_temp)
average_temp = add_all_temp/len(list_temp)
# print(average_temp)

#calc average temp using pandas
average_temp_pandas = data['temp'].mean()
print(average_temp_pandas)

#calc max__________________________________________________
max_temp = data['temp'].max()
print(max_temp)

#create DateFrame from dict______________________________________
student_dict = {
    "students": ["Anna", "Tom", "Olgierd"],
    "scores": [76, 56, 65],
}

date_in_dict = pandas.DataFrame(student_dict)
print(date_in_dict)

#convert dict to csv____________________________________________
date_in_dict.to_csv('new_data.csv')

