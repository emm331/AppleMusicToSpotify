
## Setup

Create and activate a virtual environment:

```sh
conda create -n playlist-env python=3.8

conda activate playlist-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
