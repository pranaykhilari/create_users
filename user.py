import requests
import json

from qwiklabapi import *

def credit_assign(auth_token, info, number_of_credits):
	"""
	This function provide credit payload for user_credit function
	"""
	assign_credit_payload = { 
						   "auth_token": auth_token, 
						   "credit": { 
						       "invoice_id": info['email'], 
						       "number_credits": number_of_credits, #Assign credits to user 
						       "email": info['email'] 
						   } 
						}

	return user_credit(assign_credit_payload)

def user_creation(info, auth_token, search_user_response, number_of_credits):
	"""
	This function check user account is present or not
	"""
	if search_user_response.json()['count'] == 0:
		"""
		It will create user account and assign credit to user's Qwiklab account
		"""
		create_user_payload = {
					"auth_token": auth_token,
					"email": info['email'],  
					"first_name": info['first_name'], 
					"last_name": info['last_name'], 
					"company_name": info['company_name'],
					"password":"test123"
				   }
		create_user_response = 	create_user(create_user_payload)
		user_credit_response = credit_assign(auth_token, info, number_of_credits)					
	else:
		"""
		Assign credit to already existed user's Qwiklab account
		"""
		user_credit_response = credit_assign(auth_token, info, number_of_credits)
	 	return 1	
