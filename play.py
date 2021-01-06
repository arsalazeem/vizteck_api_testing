import post_requests
import get_data
import autheticate
import create_location
import create_user

session=autheticate.auth("arsalanazeem@yopmail.com","12345678")
# create_location.add_loc(session,3,"arsalanazeem@yopmail.com","12345678")
create_user.create_user_asset_wise(session,3)
# create_location.add_site(session,3,"arsalanazeem@yopmail.com","12345678")
# post_requests.create_asset(session,3,"arslanazeem@yopmail.com","12345678")