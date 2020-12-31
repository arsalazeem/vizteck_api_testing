#pip install -r requirements.txt
import requests
import autheticate
import generate_random_values
import random
import generate_random_images
import get_data
import pdb
import brand_list

description2_list=["In order to understand recursion, one must first understand recursion","Deleted code is debugged code","The best thing about a boolean is even if you are wrong, you are only off by a bit","It is a long established","There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration","Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature"]


piclist=generate_random_images.getimagelist()
cat_list=[1,2,3,4,5,6,7]

def post_asset(email,password):
    company_obj=get_data.get_company_id(email,password)
    company_obj2=get_data.get_location_site_id(email,password)
    # pdb.set_trace()
    payload = {
        "description": brand_list.return_brand(),
        "tagId": generate_random_values.generate_phone_number(),
        "siteId": company_obj2["site_id"],
        "locationId":company_obj2["location_id"],
        "categoryId": random.choice(company_obj["catagories_list"]),
        "departmentId": random.choice(company_obj["departments_list"]),
        "purchaseDate":str(generate_random_values.generate_random_date()),
        "cost": generate_random_values.generate_random_zipcodes(),
        "brand": brand_list.return_brand(),
        "model": generate_random_values.get_random_string(5),
        "serialNo": generate_random_values.generate_phone_number(),
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
    session=autheticate.auth(email, password)
    # pdb.set_trace()
    try:
        response=session.post("http://54.186.118.166:3000/api/v1/en/asset/add-asset",data=payload, timeout=0.000000001)
        print(response.content)
    except Exception as e:
        pass



def create_asset(asset_range,email,password):
    # try:
    for i in range(0, asset_range):
        post_asset(email,password)
        print("Asset Number=", i)
    # except Exception as e:
    #     print("create asset function",e)



def post_departments(limit,email,password):
    session = autheticate.auth(email, password)
    print("this")
    for x in range(1,limit+1):
        payload = {
            "name": "Vizteck Department"+" "+str(x)
        }



        # try:
        response=session.post("http://54.186.118.166:3000/api/v1/en/add/edit/departments", data=payload )
        print(response.content)
        # except Exception as e:
        #     print(e)




#methods
create_asset(50,"nnarsalazeem@yopmail.com","12345678")
# post_departments(99,"narsalazeem@yopmail.com","12345678")







