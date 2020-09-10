#  Parliament Members API
Crowl and serve data of parliament member through a django_restframework APIs.

# How to crowl the data:
command : python manage.py crowl
heads up: data is already saved in a sqlite database 

# How to start api service:
command : python manage.py runserver

# ENDPOINTS
Access API ENDPOINTS documentation through http://127.0.0.1:8000/redoc/

#Avaliable endpoints:

**'/pmapi/list'**  : Parameters avaliable: fn(first name), prof, ln (last name), dob(date of birth), pob(place of birth), pp (political party)
                
                **Example request** : http://127.0.0.1:8000/pmapi/list?pp=GERB
               
**'/pmapi/search'**: Search by first or last name
               
               **Example request** :  http://127.0.0.1:8000/pmapi/search?search=СЕВИМ
               
**'/pmapi/pm'**    : Serve single record based on ID from database / API ENDPOINT has Token Authentication 
               
               **Example request** : http://127.0.0.1:8000/pmapi/pm/4/
               
    
    
    
# Admin panel


Admin panel for managing users can be found under 'http://127.0.0.1:8000/admin/'

Existing users in database for testing purposes:

**superuser**: testadmin

**password**: testpass123


**basicuser**: testuser

**password**: bnm123bnm

**token**: 2f306b4e32bdfd3af7e185f63337c355e0b0358b

# Parsed data


Data was parsed using scrapy.


Following data was parsed for all 240 parliament members.

- First name

- Last name 

- Profession

- Languages

- Political party

- Email


# JSON Schema


Crowled data was validated using pydantic a json schema generator.

The validation takes place in spiders/schemavalidator.py




