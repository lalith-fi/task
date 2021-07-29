# task
The task project has two apps AuthController and Todocontroller.
AuthController app  has APIs related to:
register-takes the post request ang registers the users(required fields-first_name,last_name,email,password,role(user or admin))
login-takes the post request and the logs in the user if registered and creates a jwt,stores it in cookies(required fields-email,password)
logout-takes get request and logs out user by clearing the cookies.
TodoController app has APIs related to CRUD operations.
create-takes the post request and creates a todoitem if user is admin(required fields-item)
getall-takes get request and gets all todoitems.
getone-takes get request and gets a single todoitem which corresponds to id provided.
update-takes put request and updates the todoitem which corresponds to id provided.
delete-takes the delete request and deletes the todoitem which corresponds to id provided.

