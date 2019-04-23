# Art-Logic

A very small amount of setup required to launch the website where you can play with the encoder. 
This setup is due to there being a single dependency (Flask).

## Setup
1. `git clone git@github.com:vaer-k/Art-Logic.git`
2. `pipenv install`
3. `pipenv shell`
4. `FLASK_APP=server.py flask run`
5. Visit `localhost:5000`

## Testing
You can test the encoder by running `python encoder.py` from the root directory of the project. 
This will run all doctests in `encoder.py`. If no results are displayed, that means all tests passed.

Alternatively, you can run iPython or the builtin interpreter and import the functions in
`encoder.py` to manually test the emplementation.
