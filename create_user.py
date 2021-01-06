import base_url
import generate_random_values
def return_usertype(id):
    if id==2:
        return "sub manager"
    elif id==3:
        return "operator"
    elif id==4:
        return "employee"
    elif id==5:
        return "employee"



def create_user_asset_wise(session,usertype):
    if usertype>5:
        print("Please pass a user id between 2 to 5")
    payload={
    "firstName":generate_random_values.generate_random_first_name(),
    "lastName": "Operator",
    "retypePassword": "12345678",
    "email": generate_random_values.generate_random_email(),
    "userType": usertype,
    "password": "12345678"}
    print("Account created with these credentials")
    print("Email:" + payload["email"])
    print("Password:" +str(payload["password"]))
    print("usertype:" + return_usertype(payload["userType"]))
    response=session.post(base_url.base_url+"company/create/users",data=payload)
    print(response.json())





if __name__ == '__main__':
    print(return_usertype(2))




