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
def return_list(list,keyname):
    for i in range(0,len(list)):
        if i==0:
             temp_sites_list=[]
        temp_sites_list.append(list[i][keyname])
    print(temp_sites_list)
    return temp_sites_list

def get_company_id(email,password):
    s = autheticate.auth2(email, password)
    response = s.get(base_url.base_url_aw+ "departments/sites")
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