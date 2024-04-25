import click
import configparser
import json
import os
import shutil
from api import fetch_match_history

def get_config_path():
    """Constructs the config file path dependent on OS."""
    if os.name == 'posix':  # Linux or macOS
        path = os.path.expanduser('~/.config/lol-recent-match/config.ini')
    elif os.name == 'nt':  # Windows
        path = os.path.join(os.getenv('APPDATA'), 'lol-recent-match', 'config.ini')
    return path

CONFIG_FILE_PATH = get_config_path()

def ensure_config_directory():
    """Ensure the configuration directory exists."""
    config_dir = os.path.dirname(CONFIG_FILE_PATH)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

def save_api_key(key):
    ensure_config_directory()
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    if 'DEFAULT' not in config.sections():
        config['DEFAULT'] = {}
    config['DEFAULT']['api_key'] = key
    with open(CONFIG_FILE_PATH, 'w') as configfile:
        config.write(configfile)

def get_api_key():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    try:
        return config['DEFAULT']['api_key']
    except KeyError:
        return None
    
@click.group()
def cli():
    pass

# TODO: number checking
@cli.command()
@click.argument('api_key',)
def configure(api_key):
    """Configure the Riot Developement API key."""
    save_api_key(api_key)
    click.echo('API Key saved successfully.')

@cli.command()
@click.option(
            '--name', 
            prompt='Please enter player game name',
            help='Player game name')
@click.option(
            '--tagline', 
            prompt='Please enter player tagline', 
            help='Player tagline')
@click.option(
            '--number',
            default=1,
            help='Number of recent matches to fetch',
            )
def get_match(name, tagline, number):
    """Get the match history of a player."""
    api_key = get_api_key()
    if not api_key:
        click.echo('API key not set. Please use the configure command first.')
        return
    click.echo(f'Player Game Name: {name}')
    click.echo(f'Player Tagline: {tagline}')
    click.echo(f'Using API Key: {api_key}')
    match_history = fetch_match_history(api_key, name, tagline, number)
    # print(match_history)
    #write match history to a file as json
    with open('match_history.json', 'w') as f:
        json.dump(match_history, f)
    

@cli.command()    
def clear():
    """Clears the relating configuration file and directory."""
    config_dir = os.path.dirname(CONFIG_FILE_PATH)
    try:
        if os.path.exists(config_dir):
            shutil.rmtree(config_dir) 
            click.echo("Configuration directory and file have been deleted.")
        else:
            click.echo("No configuration directory found.")
    except Exception as e:
        click.echo(f"An error occurred while trying to delete the configuration directory: {e}")

cli.add_command(clear, name='reset')

if __name__ == '__main__':
    cli()