# Project: CrowdFind
## Members
Michael Dresser, Maura Winstanley, Connor Shore, Connor Guerin, Sam Lamichhane

## Vision
Making the world a better place one jacket at a time

## Automated Tests
### How to Run Tests
To run the tests, in the CrowdFind directory run ./manage.py test (name of the package which you would like to test e.g. test).
### Test Results

## User Acceptance Tests
UAT 1: Register user

Data: Any email address and a zip code

Activity:
* User opens the CrowdFind site and selects “Register”
* User is prompted to enter an email address and zip code
* User enters email address and zip code
* User selects “Create User”
* New user data is deleted from the fields
* User can now log in

UAT 2: Log in

Data: Email address of registered user

Activity:
* If User is in the “Register” page, User selects “Login”
* User is prompted for an email address
* User enters email address of registered user into the field
* User selects “Login”
* The main CrowdFind page is opened, displaying the found map and the found table

UAT 3: Add Item

Prereq: Logged in

Data: Item type, item name, item description, date lost/found, (optional) lat/long

Activity:
* User selects “Post Found Item” from the main CrowdFind page
* User enters the above data into the fields
* If User does not have lat/long data, the pin can be dragged to fill the correct location into the fields
* User selects “Post Item”
* The new item appears in the Lost Table on the main CrowdFind page, displaying its name and description

