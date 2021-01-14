import base_url
import pdb

custom_list=[]
def fetch(session):
   response= session.get(base_url.base_url+"departments?limit=10000&offset=0")
   dept_obj=response.json()
   lent=len(dept_obj["data"]["departments"])
   for i in range(0,lent):
       custom_list.append(dept_obj["data"]["departments"][i]["did"])

   print("This is the length of custom list",len(custom_list))
   return custom_list


def delete_dept(session):
    print(fetch(session))
    try:
        custom_list2 = []
        custom_list2 = fetch(session)
        length = len(custom_list2)
        for i in range(0, length):
            payload = {
                "departmentId": custom_list2[i],
                "status": 2
            }
            print(custom_list2[i])
            response = session.post(base_url.base_url + "delete/deactivate/department/", data=payload)
            print(response.json())
    except:
        delete_dept(session)
