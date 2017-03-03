# -*- coding: utf-8 -*-

class View:
    def __init__(self, bot, userId):
        """This class is responsible for sending and controlling the message
        flow for a single user. It assumes it is working for a complete user."""
        self.bot = bot
        self.id = userId
        self.controller = None
        self.POSSIBLE_QUERIES = ('id', 'name', 'email', 'origin')
        self.queries_to_make = [ ]

    def setController(self, controller):
        self.controller = controller
        self.controller.id = self.id

    def sendMessage(self, message):
        """Answers an user message"""
        self.bot.sendMessage(self.id, message)

    def queryInfo(self, update, user):
        # TODO: Discover what is wrong here
        return user

    def setupQuery(self):
        self.queries_to_make = list(self.POSSIBLE_QUERIES[:])

    def shouldQuery(self):
        return len(self.queries_to_make) is not 0

    def receiveQuery(self, user, answer):
        query = self.queries_to_make[0]
        if query != 'id':
            user[query] = answer
        self.queries_to_make = self.queries_to_make[1:]
        return user

    def sendNextQuery(self):
        message = 'Obrigado por preencher os dados!'
        if len(self.queries_to_make) > 0:
            query = self.queries_to_make[0]
            if query == 'name':
                message = 'Qual é o seu nome?'
            elif query == 'email':
                message = 'Qual é o seu e-mail?'
            elif query == 'origin':
                message = 'Qual a sua procedência?'
        self.sendMessage(message)
