# -*- coding: utf-8 -*-

class View:
    def __init__(self, bot, userId):
        """This class is responsible for sending and controlling the message
        flow for a single user. It assumes it is working for a complete user."""
        self.bot = bot
        self.id = userId
        self.controller = None
        self.POSSIBLE_QUERIES = ('id', 'name', 'email', 'origin')
        self.SIGNED_MESSAGE = 'Presença assinada!'
        self.NAME_MESSAGE = 'Qual é o seu nome?'
        self.EMAIL_MESSAGE = 'Qual é o seu e-mail?'
        self.ORIGIN_MESSAGE = 'Onde você estuda/trabalha? (Detalhe o curso caso estude)'
        self.LOCKED_ATTENDANCE = 'A chamada está indisponível agora!'
        self.HELP_MESSAGE = """Comandos de admin:
- /lock: Trava a lista de presença
- /unlock: Destrava a lista de presença"""

        self.queries_to_make = [ ]

    def setController(self, controller):
        """Sets the controller for this view."""
        self.controller = controller

    def sendMessage(self, message):
        """Sends a message"""
        self.bot.sendMessage(self.id, message)

    def setupQuery(self):
        """Prepares the list of information to be queried by the user. This
        view expects the query to follow something on these lines:

            def loop(update):
                if self.view.shouldQuery():
                    message = update['message']['text']
                    user = self.view.receiveQuery(user, message)
                    # Updated user can be used for something
                    self.view.sendNextQuery()

        Given this function is running on a handle for the specified user
        on the constructor"""
        self.queries_to_make = list(self.POSSIBLE_QUERIES[:])

    def shouldQuery(self):
        """Check `setupQuery`"""
        return len(self.queries_to_make) is not 0

    def receiveQuery(self, user, answer):
        """Check `setupQuery`"""
        query = self.queries_to_make[0]
        if query != 'id':
            user[query] = answer
        self.queries_to_make = self.queries_to_make[1:]
        return user

    def sendNextQuery(self):
        """Check `setupQuery`"""
        message = 'Obrigado por preencher os dados! Envie /sign para preencher a presença.'
        if len(self.queries_to_make) > 0:
            query = self.queries_to_make[0]
            if query == 'name':
                message = self.NAME_MESSAGE
            elif query == 'email':
                message = self.EMAIL_MESSAGE
            elif query == 'origin':
                message = self.ORIGIN_MESSAGE
        self.sendMessage(message)
