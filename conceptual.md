### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
The way functions are described and how the code is run

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  Using get()

- What is a unit test?
A test that tests a single component 

- What is an integration test?
A test that tests multiple components

- What is the role of web application framework, like Flask?
To help test and debug your web app

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  By asking yourself "Does this need to be it's own route?"

- How do you collect data from a URL placeholder parameter using Flask?
Using the same id

- How do you collect data from the query string using Flask?
Using request.args

- How do you collect data from the body of the request using Flask?
Using request.form

- What is a cookie and what kinds of things are they commonly used for?
Small files stored generally on the local pc and used to keep track of logins page visits and anything the website wants

- What is the session object in Flask?
used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values

- What does Flask's `jsonify()` do?
Converts json into a response object and makes it pretty