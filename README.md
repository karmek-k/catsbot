# catsbot
Cat facts Discord bot

Catsbot uses the [cat-facts](https://github.com/alexwohlbruck/cat-facts) and [TheCatAPI](https://thecatapi.com/).

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
.\env\Scripts\activate

# install dependencies
pip install -r requirements.txt

# create the .env file from template
mv env_template .env

# edit the .env with your favorite text editor
# set API_KEY to your bot token
vim .env
```

## Running the bot
```
python main.py
```
