#pip install -r requirements.txt
import requests
import autheticate
import generate_random_values
import random
from faker import Faker
import generate_random_images
import get_data
import pdb
import inspect
import brand_list
import base_url
import create_location



# login()
fake=Faker()
description2_list=["In order to understand recursion, one must first understand recursion","Deleted code is debugged code","The best thing about a boolean is even if you are wrong, you are only off by a bit","It is a long established","There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration","Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature"]


piclist=generate_random_images.getimagelist()
cat_list=[1,2,3,4,5,6,7]

def return_cost():
    a = random.choice([1, 2, 3, 4, 5, 6, 7, 8,9])
    b=random.choice([1,2,3,4,5,6,7,8,9])
    return int(str(a)+str(b))


def write_log(description,site_id,location_id,cat_id):
    with open("log.txt", "a") as file:
        file.write("*************************************** \n")
        file.write("Asset Description:" + description + "\n")
        file.write("Asset Site ID:" + str(site_id) + "\n")
        file.write("Asset Location ID:" + str(location_id) + "\n")
        file.write("Asset  Catagorey ID:" + str(cat_id) + "\n")
        file.write("\n")
        file.close()



def post_asset(session):
    company_obj=get_data.get_company_id(session)
    company_obj2=get_data.get_location_site_id(session)
    # pdb.set_trace()
    payload = {
        "description": brand_list.return_brand(),
        "tagId": generate_random_values.generate_phone_number(),
        "siteId": company_obj2["site_id"],
        "locationId":company_obj2["location_id"],
        "categoryId": random.choice(company_obj["catagories_list"]),
        "departmentId": random.choice(company_obj["departments_list"]),
        "purchaseDate":str(generate_random_values.generate_random_date()),
        "cost": return_cost(),
        "brand": brand_list.return_brand(),
        "model": generate_random_values.get_random_string(5),
        "serialNo": generate_random_values.generate_phone_number(),
        "image":"https://p2.hiclipart.com/preview/666/313/317/business-strategy-icon-money-icon-management-icon-financial-management-cash-flow-finance-asset-management-accounting-management-accounting-project-management-png-clipart.jpg",
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

    write_log(payload["description"],payload["siteId"],payload["locationId"],payload["categoryId"])
    # session = requests.Session()
    # session=autheticate.auth(email, password)
    # pdb.set_trace()
    try:
        response=session.post(base_url.base_url + "asset/add-asset", data=payload, timeout=0.000000001)
        print(response.content)
    except Exception as e:
        pass



def create_asset(session,asset_range):
    # try:
    for i in range(0, asset_range):
        post_asset(session)
        print("Asset Number=", i)




def post_departments(session,limit):
    for x in range(1,limit+1):
        payload = {
            "name": "Vizteck Department"+" "+str(x)
        }




        response=session.post(base_url.base_url + "add/edit/departments", data=payload)
        print(response.content)





# print(return_cost())
#methods
# if __name__ == "__main__":
# get_data.get_sites_list("arsalanazeem@yopmail.com","12345678")
# create_location.add_site(2,"ragnor@yopmail.com","12345678")
# create_location.add_loc(100,"ragnor@yopmail.com","12345678")
# post_departments(2,"arsal.azeem@vizteck.com","12345678")
# create_asset(100,"ragnor@yopmail.com","12345678")







