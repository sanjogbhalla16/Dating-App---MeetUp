# First step to run a python script

is to create a virtual environment and install the required packages.
command to make environment - python3 -m venv .venv
and to activate it source .venv/bin/activate

# Important information

In FastAPI, the default location for parameters depends on how you define them in the endpoint function. Parameters without explicit declaration are treated as query parameters.

If you are expecting them to come in the request body, you need to specify it using a Pydantic model or a FastAPI parameter type.

Now we need to work upon the authentication of user

we will continue this again
