# Mini File storage like Google drive 
## Project Structure

```cpp
.
├── app
│   ├── blueprints
│   │   ├── auth
│   │   └── home
│   ├── __init__.py
│   ├── models.py
├── config.py
├── documentation
│   └── auth.md
├── instance
│   └── data.db
├── main.py
├── migrations
├── pyproject.toml
├── README.md
├── requirements.txt
├── run.py
└── uv.lock

13 directories, 20 files
```

# How to run the system
## Without Docker

1. Create a virtual environment
```sh
python -m venv .venv
OR 
uv venv # if uv is installed
```
2. Activate the vitual env
```sh
source .venv/bin/activate # linux/MacOs
.venv\Scripts\activate # windows
```
3. run the system
```sh
flask run
```


## Running tests
1. Make sure to be in the root directory
2. Run the following commands
```sh
pytest -v 

# If you get import errors, try running it as a script
python -m pytest -v
```
3. Check logs 



documented by: [Tom](https://github.com/tomi3-11)
