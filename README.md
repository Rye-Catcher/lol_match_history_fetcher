# LoL recent match fetcher

A simple CLI (command line interface) tool to fetch your recent match history of League of Legend game.

### Installation  
This project requires Python 3.8 or later. Please make sure it is installed and the environment is correctly configured.

1. **Clone the repository**
Open your terminal (Recommend using [Windows terminal](https://apps.microsoft.com/detail/9n0dx20hk701?rtc=1&hl=en-sg&gl=SG) for Windows users) and direct to the place you want to install the tool:

```bash
git clone https://github.com/yourusername/lol-recent-match.git
cd lol-recent-match
```

2. **Set up a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install dependencies**:
```bash
pip install -r requirements.txt
```
4. **Install the local package**:
```bash
pip install -e .
```
Now the CLI tool should be installed. Run:
```bash
lol-recent-match --help
```

should print relevant help information in your terminal.

### Quick start

First, please configure and save your Riot Development API key:

```bash
lol-recent-match configure --set-api-key [YOUR_API_KEY]
```
Note that please do not enter sqaure bracket. 

It will save your key at `~/.config/lol-recent-match/config.ini`

Then, you can fetch your recent match by simply entering:
```bash
lol-recent-match player --name [GAME_NAME] --tagline [TAGLINE] --number [FETCH_NUMBER]
```

You can obtain your game name and tagline from account detail on Riot website. `FETCH_NUMBER` is the number of records you want to fetch from your match history, from most recent to oldest (max 20).

### To-do
:white_large_square: Parse the JSON, pick useful information and export as a pdf file.

:white_large_square: Add locale option to requesting URLs



