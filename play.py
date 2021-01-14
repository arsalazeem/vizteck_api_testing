import post_requests
import get_data
import autheticate
import create_location
import create_user
import add_cats
import delete_departments

email="azeemarsal24@yopmail.com"
password="12345678"
session=autheticate.auth(email,password)
# delete_departments.delete_dept(session)
post_requests.post_departments(session,1)
# create_location.add_site(session,1)
create_location.add_loc(session,20)
# # add_cats.create_cat(session)
# for i in range(1,99999):
#     create_user.create_user_asset_wise(session)
# #
post_requests.create_asset(session,1000)

