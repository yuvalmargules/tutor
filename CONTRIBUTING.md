# Guidelines

## Issues
Use project-board to handle issues status.
We also will create issues for discussions on things that will affect our app, like DB models, what linter we will use or is we should upload our app to AWS or other cloud.


## PRs and branches
- On the PR's description, start with mentioned the issue. Use '#' and just choose the right issue or fill the issue's id.
- The name of the new branch might start with #issueid#desciprtion_of_branch, so we will have one branch per issue. 
For example: 153_creating_login_page


## General Guidelines
### linter and coding style
We will follow a set of coding style rules and use linter to keep the order.
Recommended flake8 or pylint (need to choose).

### routes and controllers
We need to keep routes short, in intent to follow rest-api rules.
To keep the backend synchronized with the frontend, we need to talk one language.
GET routes will always return templates(using render_template function) and POST routes always return a JSON.
That way GET routes its for representing a view to the user, and POST routes its for getting data from the backend.


### MVC design
Models - we will add new models into 'tutor/models.py' file.
Views - we will add new views into 'tutor/templates' folder. We will use a layout as a base for all our templates. 
Controllers - we will add controllers into 'tutor/controllers' folder. 
Routing - we will add new routes into 'tutor/routing.py' with a route function named '%desciption%_route'.
