# -*- coding: utf-8 -*-

class View:
    def __init__(self, bot, userId):
        """This class is responsible for sending and controlling the message
        flow for a single user."""
        self.bot = bot
        self.id = userId
        self.controller = None
        self.POSSIBLE_QUERIES = ('id', 'name', 'email', 'origin')
        self.SIGNED_MESSAGE = 'Presença assinada!'
        self.NAME_MESSAGE = 'Qual é o seu nome?'
        self.EMAIL_MESSAGE = 'Qual é o seu e-mail?'
        self.ORIGIN_MESSAGE = 'Onde você estuda/trabalha/colabora? (Detalhe o curso caso estude ou a comunidade da qual faz parte, ex.: Grupy)'
        self.LOCKED_ATTENDANCE = 'A chamada está indisponível agora!'
        self.HELP_MESSAGE = """Comandos de admin:
- /lock: Trava a lista de presença
- /unlock: Destrava a lista de presença"""
        self.THANK_YOU = 'Obrigado por preencher os dados! Envie /sign para preencher a presença.'
        self.ANSWER_EVERYTHING = 'Responda todo o formulário antes de preencher a chamada!'

        self.currentQuestion = 0
        self.answers = [ ]

    def setController(self, controller):
        """Sets the controller for this view."""
        self.controller = controller

    def sendMessage(self, message):
        """Sends a message"""
        self.bot.sendMessage(self.id, message)

    def answer(self, update):
        """Prepares the answer for the bot based upon what the view and the controller
        can offer here."""
        text = update['message']['text']
        answer = self.LOCKED_ATTENDANCE

        if text == '/unlock':
            answer = self.controller.tryToUnlock(self.id)
        elif text == '/lock':
            answer = self.controller.tryToLock(self.id)
        elif not self.controller.isLocked():
            answer = self.controller.deal(self, text)

        self.sendMessage(answer)
        return answer

    def getAnswers(self):
        """Packs the answers given by the user."""
        return self.answers

    def isInFillMode(self):
        """Checks if the user still have something to fill in the attendance list."""
        return self.currentQuestion <= len(self.POSSIBLE_QUERIES)

    def addAnswer(self, answer):
        """Temporarily store the answer by the user to save later."""
        self.answers.append(answer)

    def nextQuestion(self):
        """Goes for the next question."""
        self.currentQuestion += 1

    def leaveFillMode(self):
        """Arbitrarily stops filling the attendance list."""
        self.currentQuestion = 1 + len(self.POSSIBLE_QUERIES)

    def firstQuestion(self):
        """Sets the current question to the name one."""
        self.currentQuestion = 1
