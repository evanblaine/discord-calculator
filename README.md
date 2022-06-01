## Discord Calculator

An attempt at an operational calculator within Discord

Uses Pycord and Python 3.9+

#

<img src="./assets/calculator.png" title="Calculator">

#

## How to Start Environment

Create a virtual environment

> For Windows
```
py -m venv venv
```

Install the requirements.txt file

> For Windows
```
pip install -r requirements.txt
```
---

## How to Start Developing

### Register a Discord bot application

First off, you need a Discord Developer account

1. Go to Discord's [Developer Portal](https://discord.com/developers/applications).
2. Create a new application.

3. Go to the Bot tab and add a bot user to your application.

   > Take note of the `TOKEN` on the Bot tab page.

   > Keep your token and any file containing it **private**. If it ever leaks or you suspect it may have leaked, simply `regenerate` a new token to invalidate your compromised token.

4. Under the Discord Developer Portal, Navigate to OAuth2, then URL Generator and choose the scopes `bot` and `applications.commands`

5. Now Create your own server on Discord and invite your newly created bot from the invite link in the Developer Portal

### Dependency information

[Pycord](https://docs.pycord.dev/en/master/index.html)
