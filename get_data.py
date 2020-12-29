import autheticate
import requests
import base_url

# dept_list=[]
# session=requests.Session()
# session2=autheticate.auth(session,"arsal.azeem@vizteck.com","12345678")
# session2=session2.get(base_url.base_url_nesma+"departments")
# print(session2.get)

def get_dept(s):
    response = s.get(base_url.base_url_nesma + "departments")
    global dept_dict
    dept_dict = response.json()
    print(dept_dict)



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
def get_site_id():
    s = autheticate.auth2("arsal.azeem@vizteck.com", "12345678")
    response = s.get(base_url.base_url_aw+ "departments/sites")
    temp=response.json()
    print(temp["data"]["sitesArr"])
    print(temp["data"]["departmentsArr"])
    print(temp["data"]["categoriesArr"])
# def gets_cats():
get_site_id()
# print(get_dept_list())
