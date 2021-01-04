#pip install -r requirements.txt
import requests
import autheticate
import generate_random_values
import random
from faker import Faker
import generate_random_images
import get_data
import pdb
import brand_list
import base_url




def _add_site(email,password):
    try:
        faker = Faker()
        payload = {
            "name": generate_random_values.generate_random_adress(),
            "description": faker.text(),
            "address": generate_random_values.generate_random_adress(),
            "aptSuite": generate_random_values.generate_bad_zip_code(),
            "city": generate_random_values.generate_random_city(),
            "state": generate_random_values.generate_bad_city(),
            "postalCode": generate_random_values.generate_random_zipcodes(),
            "countryId": random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        }
        session = autheticate.auth(email, password)
        response = session.post(base_url.base_url_aw + "company/signUp/add/sites", data=payload)
        print(response.json())
    except Exception as e:
        print(e)

def add_site(upper_range,email,password):
    for i in range(0,upper_range):
        _add_site(email,password)
        k=i
        print("Sites Added:",k)
    print("Done Adding Sites")


def add_loc(email,password):
    payload={
        "name":generate_random_values.get_random_string(4),
        "id":1
    }
    siteid=random.choice(get_data.get_sites_list(email,password))
    print(siteid)
    pdb.set_trace()
    session=autheticate.auth(email,password)
    response=session.post(base_url.base_url_aw+"company/signUp/add/site/locations?siteLocationId="+str(siteid),data=payload)
    print(response.json())


# add_loc("arsalanazeem@yopmail.com","12345678")

