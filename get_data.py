import autheticate
import requests
import base_url
import pdb
import random
import inspect
import post_requests
# dept_list=[]
# session=requests.Session()
# session2=autheticate.auth(session,"arsal.azeem@vizteck.com","12345678")
# session2=session2.get(base_url.base_url_nesma+"departments")
# print(session2.get)

# session="undefined"
# if session!="undefined":
#     session = autheticate.auth("ragnor@yopmail.com", "12345678")

# session=post_requests.session


def get_dept(s):
    response = s.get(base_url.base_url + "departments")
    global dept_dict
    dept_dict = response.json()
    # print(dept_dict)



# session = autheticate.auth2("arsal.azeem@vizteck.com", "12345678")
# get_dept(session)

# for i in range(0, int(dept_dict["data"]["count"])):
#     print(i)
def get_dept_list():
    dept_list=[]
    lenght = dept_dict["data"]["count"]
    for i in range(0, lenght):
        dept_list.append(dept_dict["data"]["departments"][i]["did"])
        return dept_list
#http://54.186.118.166:3000/api/v1/en/departments/sites
# def get_loc_id():
def return_list(list,keyname):
    temp_sites_list = []
    for i in range(0,len(list)):
        temp_sites_list.append(list[i][keyname])
    # print(temp_sites_list)
    return temp_sites_list



def get_sites_list(session,email,password):
    #
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('caller name:', calframe[1][3])
    #
    locations_id=[]
    # s = autheticate.auth(email, password)
    response = session.get(base_url.base_url + "company/sites/list")
    custom_ob=response.json()
    list_lenght=len(custom_ob["data"]["sitesFound"])
    temp_list=custom_ob["data"]["sitesFound"]
    # print(list_lenght)
    # print(temp_list)
    for i in range(0,list_lenght):
        locations_id.append(temp_list[i]["sid"])
    print(locations_id)
    # pdb.set_trace()
    return locations_id

def get_location_site_id(session,email,password):
   try:
       location_id = []
       locationn_id=[]
       site_id = random.choice(get_sites_list(session,email, password))
       print(site_id)
       # pdb.set_trace()
       # s = autheticate.auth(email, password)
       response = session.get(base_url.base_url + "site/locations/" + str(site_id))
       print(response.json())
       # pdb.set_trace()
       first_list = response.json()
       first_list2 = first_list["data"]["siteslocationArr"]
       for i in range(0, len(first_list2)):
           location_id.append(first_list2[i]["slid"])

       print(location_id)
       # pdb.set_trace()
       locationn_id = random.choice(location_id)
       print(site_id)
       pdb.set_trace()
   except Exception as e:
       print("There is something wrong in get location site id")
       get_location_site_id(session,email,password)

   return {"site_id": site_id, "location_id": locationn_id}



#site/locations/:siteId


def get_company_id(session,email,password):
    # s = autheticate.auth(email, password)
    response = session.get(base_url.base_url + "departments/sites")
    temp=response.json()
    global sites_list,departments_list,cats_list
    sites_list=temp["data"]["sitesArr"]
    departments_list=temp["data"]["departmentsArr"]
    cats_list=temp["data"]["categoriesArr"]
    # print(sites_list)
    # print(departments_list)
    # print(cats_list)
    # return_list(sites_list,"sid")
    # return_list(departments_list, "did")
    # return_list(cats_list, "aid")
    # return return_list(sites_list,"sid"),return_list(departments_list, "did"),return_list(cats_list, "aid")
    return {"sites_list": return_list(sites_list,"sid") ,"departments_list":return_list(departments_list, "did") ,"catagories_list":return_list(cats_list, "aid")}
    # for i in range(0,len(sites_list)):
    #     if i==0:
    #          temp_sites_list=[]
    #     temp_sites_list.append(sites_list[i]["sid"])
    #     print(temp_sites_list)
# def gets_cats():
# get_site_id()
# print(get_dept_list())
# print(get_company_id())
# print(get_sites_list("arsalanazeem@yopmail.com","12345678"))
# print(get_location_site_id("nnarsalazeem@yopmail.com","12345678"))
# get_company_id("arsalazeem40@yopmail.com","12345678")