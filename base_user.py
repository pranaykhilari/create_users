import csv
import requests
import json
from qwiklabapi import *
from user import *

number_of_credits = 1 #Assign credit to user

user_info = None

auth_token_response = check_auth_user()
auth_token = auth_token_response.json()['auth_token'] #Retrieve auth_token from the response of the Auth Token API


with open('user_list.csv') as user_data:
	"""
	Open CSV file in read mode
	""" 
	data = csv.DictReader(user_data)
	
	for info in data:
		"""
		Parsing each row
		"""
		email = info['email']
		first_name = info['first_name']
		last_name = info['last_name']
		company_name = info['company_name']
		search_user_payload = {"auth_token":auth_token,"search_term":email}

		search_user_response = search_user(search_user_payload)		
		
		user_creation(info, auth_token, search_user_response, number_of_credits) #Call function which handle user creation and credit allocation