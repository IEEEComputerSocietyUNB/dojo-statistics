# Dojo Statistics

Data parser for attendance on dojo sessions.

# Installation

This app requires [Telepot](https://github.com/nickoala/telepot) and must run using Python 3.4+.

# Usage


To run it, first create a `data` folder in the root of this repository with an `admins.csv`, whose each line must be a valid Telegram id that can open or close the attendance list. To start the bot, run:
```
make API=SOME_RANDOM:TELEGRAM_NUMBER
```
This will start the bot. To enable people to sign the list, one of the admins must run the `/unlock` command. To close the list, run the `/lock` command. Don't forget to lock the list by the end of the session!

To sign the list, the users must `/start` the bot, answer all the required questions and then call the `/sign` command. The idea is to make the participant fill the question form only once, and the sign the list as many times as they want.
