import requests


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
    session=requests.Session()
    temp =session.post("http://54.186.118.166:3000/api/v1/en/company/login", data=payload)
    # print("""auth called""")
    # print(temp.content)
    # print("respone messege ends here")
    # print(temp.content)
    # print(temp.content)
    return session

