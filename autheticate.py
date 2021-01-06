import requests
import sys
import post_requests
import base_url
import pdb
import inspect

def auth(eemail,ppassowrd):
    #
    pdb.set_trace()
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('caller name:', calframe[1][3])
    #
    payload = {"email": eemail,
               "password": ppassowrd
               }
    api= base_url.base_url + "company/login"
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

# auth("arsal.azeem@vizteck.com","12345678")

# auth("arsalanazeem@yopmail.com","12345678")