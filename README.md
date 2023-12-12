# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

# Roberta De Cecco - She Codes News Project

## About This Project
This project was about creating a 'She Codes News!' website using Django framework and style it.
The purpose of the website is for users to read new stories and authors to create them.
Users need to be verified before being able to perform some actions, either logging in or creating an account else a graceful error message is displayed.

The website is NOT deployed so you can either check the screenshots provided, watch it: ![video](https://youtu.be/x0lGe3lwW7Q) or download the code and run the server locally - see instructions in the 'How to Run This Code' section.



## How To Run This Code
- Clone the repo to your local machine, 
- Create a virtual environment and activate it, 
- Install Django,
- Migrate the database (you need to be in the same directory of your `manage.py` file): `python manage.py migrate`  
- Launch the server: `python manage.py runserver`
- Copy the URL the above command returns (http://localhost.../) in the terminal and paste it into a web browser
- Once finished exploring the website, Quit the server in the terminal: `Ctrl+C`
- Deactivate your virtual environment


## Database Schema
![ERD](she_codes_news/static/images/DB_ERD.png)


## Project Features
- [x] Order stories by date (from latest to oldest - if a card is updated, card shown by last updated date)
![Order Story by date-created or last updated](./static/images/Order_Stories_byDate.PNG)

- [x] Styled "new story" form
![Styled New Story form](./static/images/NewStoryForm.PNG)

- [x] Story images
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Log-in/log-out
![Login link on Index page](./static/images/Login1.PNG)
![Actual login page](./static/images/Login2.PNG)
![Logout link once user's logged in](./static/images/Logout.PNG)

- [x] "Account view" page
![AccountView after user logs in](./static/images/AccountView_UsersLoggedIn.PNG)

- [x] "Create Account" page
![Create Account page](./static/images/Create_Account.PNG)
![User Profile page](./static/images/UserProfile.PNG)

- [x] View stories by author
![Search by Author returned](./static/images/Search_Filtered.PNG)
![Search mismatch](./static/images/Search_Mismatch.PNG)

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
Already captured in other screenshots above.

- [x] "Create Story" functionality only available when user is logged in
![No Login - No Create Story functionality](./static/images/NoLogin_NoCreateStoryLink.PNG)
![Yes Login - See Create Story functionality](./static/images/LoggedIn_SeeAddStoryLink.PNG)


## Additional Features:
- [P] Add categories to the stories and allow the user to search for stories bycategory.
![Category List at Story Creation](./static/images/CategoryOptions_CreateStory.png)
![Category displayed on Cards](./static/images/Category_onStoryCards.PNG)
 I haven't implemented the search by category but I display the chosen category at story creation, in each story card.

- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![Edit and Delete Stories](./static/images/Edit_Delete1.PNG)
![Confirm or Cancel stories deletion](./static/images/ConfirmDelete_CancelDelete.PNG)
![Confirmation of Deletion](./static/images/DeletionConfirmed.PNG)

- [x] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).
Already captured in other screenshots above.

- [x] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.
![Human error message](./static/images/GracefulErrorMsg.PNG)

- [N] Add the ability to “favourite” stories and see a page with your favouritestories.
Not implemented.


## Extras:
- [x] Add abililty to leave comments on a story.
![Comments feature](./static/images/Comments.PNG)

- [x] Used the contrast checker to choose colours for the main fonts and background, to facilitate accessibility.
![contrast checker1](./static/images/add-story_contrast_checker.PNG) and 
![contrast checker2]( ./static/images/create-account_contrast_checker.PNG)

