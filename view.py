class View:
    def __init__(self, bot, userId):
        """This class is responsible for sending and controlling the message flow for a single user."""
        self.bot = bot
        self.id = userId
        self.controller = None

    def setController(self, controller):
        self.controller = controller

    def sendMessage(self, update, message):
        """Answers an user message"""
        self.bot.sendMessage(self.id, message)

    def queryInfo(self, update, user):
        # TODO: Discover what is wrong here
        return user
