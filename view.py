class View:
    def __init__(self, bot, userId):
        """This class is responsible for sending and controlling the message
        flow for a single user. It assumes it is working for a complete user."""
        self.bot = bot
        self.id = userId
        self.controller = None
        self.POSSIBLE_QUERIES = ('name', 'email', 'origin')
        self.queries_to_make = [ ]

    def setController(self, controller):
        self.controller = controller
        self.controller.id = self.id

    def sendMessage(self, update, message):
        """Answers an user message"""
        self.bot.sendMessage(self.id, message)

    def queryInfo(self, update, user):
        # TODO: Discover what is wrong here
        return user

    def setupQuery(self):
        self.queries_to_make = list(self.POSSIBLE_QUERIES[:])
