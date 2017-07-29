# Dojo Statistics

Data parser for attendance on dojo sessions.

# Installation

This app requires [Telepot](https://github.com/nickoala/telepot).

# Usage


To run it, first create a `data` folder in the root of this repository with an `admins.csv`, whose each line must be a valid Telegram id that can open or close the attendance list. To start the bot, run:
```
make API=SOME_RANDOM:TELEGRAM_NUMBER
```
This will start the bot. To enable people to sign the list, one of the admins must run the `/unlock` command. To close the list, run the `/lock` command.
