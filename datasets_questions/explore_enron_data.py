#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd 

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print (enron_data['METTS MARK'])

pois = []
for person in enron_data: 
	if enron_data[person]['poi'] == True: 
		pois.append(person)
print pois 
print len(pois)



enron_data2 = open("../final_project/poi_names.txt", "r")
datalist = [line for line in enron_data2 if line[0] == "("]
print len(datalist)

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']


nan_payments = []
for person in enron_data: 
	if enron_data[person]['total_payments'] == 'NaN': 
			nan_payments.append(person)
print len(nan_payments)
x = float(len(nan_payments))/len(enron_data)

print 'Percentage of people who are NaN for total payments:', x*100

pois_nan_payments = len(set(nan_payments) & set(pois))
y = float(pois_nan_payments)/len(enron_data)
print 'Percentage of people with NaN for total payments who are POIS:', y*100

