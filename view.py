class View:
    def __init__(self, bot):
        self.bot = bot

    def setController(self, controller):
        self.controller = controller

    def sendMessage(self, update, message):
        chat_id = update['message']['chat']['id']
        self.bot.sendMessage(chat_id, message)
