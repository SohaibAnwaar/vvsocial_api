First we have to make a signup- to set user credientials into the database

# Sign up 
http://127.0.0.1:8000/user/signup/

provide 3 things please (with front-end validations)
username
password
email

# Login: (you will get the login Token)
when user have to login this endpoint will be use: 
http://127.0.0.1:8000/user/login/
Give Parameter : username and password
Return dict value (true or false)


Get the authentication token when login is true
check it on curl : 

" http post http://127.0.0.1:8000/user/api-token-auth/ username=admin password=admin12345
"

# password reset :
send email in the post parameter
api :  http://127.0.0.1:8000/user/change_password/

Password reset mail will be sent to the email

copy the token and sent password and token to the end-point

# validate token end point:
http://127.0.0.1:8000/user/reset_password/validate_token/

# Change password end-point
http://127.0.0.1:8000/user/password_reset/confirm/

Get help from this link : https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password


you can also request like this
api params : 
headers = {"Authorization": Token JDNHDHFIEDEJKSNDKJI8768HJ}
response = requests.get("http://localhost:8002/user/change_password/", headers=headers)


# Update User

Now For updating user fields kindly use this end-point

http://127.0.0.1:8000/user/update_user/  

You can also check this end-point by the following command

 curl -X POST   http://127.0.0.1:8000/user/update_user/   -H 'Authorization: Token 5fbcdcb8b820402687b9fdc75cd7ce63370fd014'   -H 'Postman-Token: 7010a220-6a03-4853-b6db-8d8b453bb350'   -H 'cache-control: no-cache'   -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'   -F birht_date='1649-12-23' -F genre='F'

These are the values of the user which you can update


"birth_date"	"date"
"genre"	"character varying"
"address"	"character varying"
"postal_code_4"	"integer"
"postal_code_3"	"integer"
"locatity"	"character varying"
"marital_status"	"character varying"
"child_amount"	"smallint"
"about_user"	"jsonb"
"image"	"character varying"
"user_id"	"integer"




# Search user
If you want to search user you can use this endpoint 

http://127.0.0.1:8000/user/search_user/ 


"birth_date"	"date"
"genre"	"character varying"
"address"	"character varying"
"postal_code_4"	"integer"
"postal_code_3"	"integer"
"locatity"	"character varying"
"marital_status"	"character varying"
"child_amount"	"smallint"
"about_user"	"jsonb"





