import requests


def auth(n_requests,eemail,ppassowrd):
    payload = {"email": eemail,
               "password": ppassowrd
               }
    temp = n_requests.post("http://54.186.118.166:3000/api/v1/en/company/login", data=payload)
    # print("""auth called""")
    # print(temp.content)
    # print("respone messege ends here")
    return temp.status_code