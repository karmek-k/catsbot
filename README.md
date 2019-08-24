# catsbot
Cat facts Discord bot

Catsbot uses the [cat-facts](https://github.com/alexwohlbruck/cat-facts) API.

## Installation
Make sure that you have Python 3.x and pip installed.
```
# clone the repo
git clone https://github.com/karmek-k/catsbot.git

# create a virtual environment
python -m venv venv

# activate it:
# on Linux (and possibly Mac)
source venv/bin/activate
# on Windows
venv/bin/activate.bat

# install dependencies
pip install -r requirements.txt

# create the .env file from template
mv env_template .env

# edit the .env with your favorite text editor
vim .env
```

## Running the bot
```
python main.py
```
