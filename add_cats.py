import autheticate



def create_cat(session):
    payload={"name": "Equipments", "status": 1}
    response=session.post("http://54.186.118.166:3000/api/v1/en/company/signUp/add/bulk/categories" , data=payload)
    print(response.json())
