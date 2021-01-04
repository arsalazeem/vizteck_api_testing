import requests
import sys
import base_url
# def auth(n_requests,eemail,ppassowrd):
#     payload = {"email": eemail,
#                "password": ppassowrd
#                }
#     temp = n_requests.post("http://54.186.118.166:4000/api/v1/en/company/login", data=payload)
#     # print("""auth called""")
#     # print(temp.content)
#     # print("respone messege ends here")
#     # print(temp.content)
#     return n_requests

def auth(eemail,ppassowrd):
    payload = {"email": eemail,
               "password": ppassowrd
               }
    api=base_url.base_url_aw+"company/login"
    print("****************|")
    print("url",api)
    print(eemail,ppassowrd)
    print("****************|")
    session=requests.Session()
    temp =session.post(api, data=payload)
    # print("""auth called""")
    # print(temp.content)
    # print("respone messege ends here")
    # print(temp.content)
    # try:
    if temp.json()["response"] == 400:
        print(temp.json())
        print("Please provide valid login credentials.")
        print("Quiting Program...........")
        quit()
    # except:
    #     if temp.json()["response"] == str(400):
    #         print("Please provide valid login credentials.")
    #         print("Quiting Program...........")
    #         quit()
    print(temp.json())
    return session

auth("arsal.azeem@vizteck.com","12345678")

