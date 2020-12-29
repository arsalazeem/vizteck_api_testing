#pip install -r requirements.txt
import requests
import autheticate
import generate_random_values
import random
import generate_random_images
import get_data
import pdb

description2_list=["In order to understand recursion, one must first understand recursion","Deleted code is debugged code","The best thing about a boolean is even if you are wrong, you are only off by a bit","It is a long established","There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration","Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature"]


piclist=generate_random_images.getimagelist()
cat_list=[1,2,3,4,5,6,7]

def post_asset(description, tagid, purchasedate, cost, brand, model, serialno):
    company_obj=get_data.get_company_id("arsal.azeem@vizteck.com","12345678")
    # print(get_data.get_company_id("arsal.azeem@vizteck.com","12345678"))
    pdb.set_trace()
    payload = {
        "description": random.choice(description2_list),
        "tagId": generate_random_values.generate_phone_number(),
        "siteId": random.choice(company_obj["sites_list"]),
        "locationId":random.choice([31,32,33]),
        "categoryId": random.choice(company_obj["catagories_list"]),
        "departmentId": random.choice(company_obj["departments_list"]),
        "purchaseDate":str(generate_random_values.generate_random_date()),
        "cost": generate_random_values.generate_random_zipcodes(),
        "brand": generate_random_values.generate_bad_zip_code(),
        "model": generate_random_values.get_random_string(5),
        "serialNo": serialno,
        "image":str(random.choice(piclist)),
        "customFields":""
        #     {
        #         "name": "Furniture",
        #         "fieldId": 2,
        #         "fieldType": "Text"
        #     },
        #     {
        #         "name": "Test 2",
        #         "fieldId": 2,
        #         "fieldType": "Text"
        #     }
        # ]
    }


    # session = requests.Session()
    session=autheticate.auth2("viztecktest@yopmail.com", "12345678")

    try:
        response=session.post("http://54.186.118.166:3000/api/v1/en/asset/add-asset",data=payload)
        print(response.content)
    except Exception as e:
        print(e)
    # response = session.post("http://54.186.118.166:3000/api/v1/en/asset/add-asset", data=payload)
    # print(response.content)
    # statuscode = response.status_code
    # print("Response Code")
    # print(response.content)
    # print("Response Code Ends here")
    # print(statuscode)



def create_asset(asset_range):
    try:
        for i in range(1, asset_range+1):
            post_asset("This is test asset", "#243434324", "24/02", random.choice([300, 400, 500, 90, 1300]), "Dell",
                       "Dell 5570", "12345345FD")

            print("Asset Number=", i)
    except Exception as e:
        print(e)

# try:
#     this_session=requests.Session()
#     autheticate.auth(this_session,"arsaltester@yopmail.com", "1234")
#     post_asset(this_session,"This is test asset", "#243434324", "24/02", 300, "Dell", "Dell 5570", "12345345FD")
# except:
#     autheticate.auth("user@mailinator.com", "12345678")
#     post_asset("This is test asset", "#243434324", "24/02", 300, "Dell", "Dell 5570", "12345345FD")
#create_asset(5000)

def post_departments(limit,email,password):
    print("this")
    for x in range(1,limit+1):
        payload = {
            "name": "Vizteck Department"+" "+str(x)
        }
        session = requests.Session()
        autheticate.auth(session, email, password)

        try:
            response=session.post("http://54.186.118.166:3000/api/v1/en/add/edit/departments", data=payload ,timeout=0.0000001)
            print(response.content)
        except Exception as e:
            print(e)





create_asset(200)
# post_departments(99,"arsal.azeem@vizteck.com","12345678")

# def generic_post (email,password,payload,limit,api):
#     print("this")
#     for x in range(1, limit + 1):
#         session = requests.Session()
#         autheticate.auth(session, email, password)
#
#         try:
#             response = session.post(api, data=payload,timeout=0.00001)
#             # print(response.content)
#         except Exception as e:
#             print(e)





