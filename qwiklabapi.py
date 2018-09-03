import requests
import json
import sys, os
import csv
import datetime

email = "publisher+jitesh@qwiklab.com"
password = "istanbul"

headers = {'Content-Type': 'application/json'}
base_url =  "https://cuke.qwiklab.com/api/v1/admin" #Change the deployment URL accordingly

AUTH_TOKEN = "/users/sign_in/"
SEARCH_USER = "/users/user_search/"
CREATE_USER = "/users/user_create/"
ASSIGN_CREDIT = "/lab_credits/create_lab_credits"

pathname = os.path.dirname(sys.argv[0])        
path =  os.path.abspath(pathname) 

def error_account(email):
	now = datetime.datetime.now()
	file_name = now.strftime("%Y-%m-%d %H:%M")
	f= open(path+ "/user_error_email_list_"+file_name,"a+")
	f.write(email)
	f.write("\n")

def check_auth_user():
	"""
	This function retrieve auth token value
	"""
	url = base_url + AUTH_TOKEN
	payload = json.dumps({"email":email, "password":password})
	response = requests.post(url=url, data=payload, headers=headers)
	return response
		
def search_user(search_user_payload):
	"""
	This function check user account present on Qwiklab or not
	"""
	url = base_url + SEARCH_USER
	payload = json.dumps(search_user_payload)
	response = requests.post(url=url, data=payload, headers=headers)
	return response

def create_user(create_user_payload):
	"""
	This function create user account on Qwiklab
	"""
	url = base_url + CREATE_USER
	payload = json.dumps(create_user_payload)
	response = requests.post(url=url, data=payload, headers=headers)

	if response.status_code == 200:
		return response		
	else:
		error_account(json.dumps(create_user_payload['email']))
		return 1	
	
def user_credit(assign_credit_payload):
	"""
	This function assign credit to user's account
	"""
	url = base_url + ASSIGN_CREDIT
	payload = json.dumps(assign_credit_payload)
	response = requests.post(url=url, data=payload, headers=headers)
	return response

             
