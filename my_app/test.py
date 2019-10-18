import requests
import grequests
from datetime import datetime

ICICI_POLICY_DETAILS_URL = "https://app9.icicilombard.com/ILServices/Misc/v1/Genus/FetchPolicyDetails"
ICICI_TOKEN_GEN_URL = "https://app9.icicilombard.com/cerberus/connect/token"

poilcies = ["3001/154791283/00/000"]*10
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def make_req():
	token_headers = {"Content-type": "application/x-www-form-urlencoded"}
	token_data = {"grant_type": "password",
				  "username": "chatbot",
				  "password": "c4@tb0!",
				  "scope": "esbgenus-fetchpolicydetails",
				  "client_id": "ro.chatbot",
				  "client_secret": "c4@tb0!cL!3nt"
				  }

	tok_res = requests.post(ICICI_TOKEN_GEN_URL, headers=token_headers, data=token_data, verify=False, timeout=30)
	token = tok_res.json().get("access_token")
	policy_API_headers = {"Authorization": "Bearer " + token}
	# pol_url = ICICI_POLICY_DETAILS_URL + "?policyNumber=" + policy_number
	# pol_res = requests.get(pol_url, headers=policy_API_headers, verify=False, timeout=20)
	dat_now = datetime.now()
	# rs = (grequests.get(ICICI_POLICY_DETAILS_URL + "?policyNumber=" + u, headers=policy_API_headers, verify=False, timeout=300) for u in poilcies)
	# rr = grequests.map(rs)
	# print rr
	# rs = (grequests.get(ICICI_POLICY_DETAILS_URL + "?policyNumber=" + u, headers=policy_API_headers, verify=False) for u in poilcies)
	# rr = grequests.map(rs)
	# print rr
	for i in range(10):
			rs = (grequests.get(ICICI_POLICY_DETAILS_URL + "?policyNumber=" + u, headers=policy_API_headers, verify=False, timeout= 300) for u in poilcies)
			rr = grequests.map(rs)
			print rr

	# x = list(divide_chunks(poilcies, 10))

	# y = list(divide_chunks(x, 10))
	# print y[-1]
	print datetime.now() - dat_now
	# return rr
	# return pol_res.json()

make_req()