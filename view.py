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
        self.ORIGIN_MESSAGE = 'Onde você estuda/trabalha/colabora? (Detalhe o curso caso estude ou a comunidade da qual faz parte, ex.: Grupy)'
        self.LOCKED_ATTENDANCE = 'A chamada está indisponível agora!'
        self.HELP_MESSAGE = """Comandos de admin:
- /lock: Trava a lista de presença
- /unlock: Destrava a lista de presença"""
        self.THANK_YOU = 'Obrigado por preencher os dados! Envie /sign para preencher a presença.'

        self.currentQuestion = 1
        self.answers = [ ]

    def setController(self, controller):
        """Sets the controller for this view."""
        self.controller = controller

    def sendMessage(self, message):
        """Sends a message"""
        self.bot.sendMessage(self.id, message)

    def answer(self, update):
        text = update['message']['text']
        answer = self.LOCKED_ATTENDANCE

        if text == '/unlock':
            answer = self.controller.tryToUnlock(self.id)
        elif not self.controller.isLocked():
            if text == '/start':
                answer = self.NAME_MESSAGE
                self.currentQuestion += 1
            elif text == '/sign':
                if self.currentQuestion >= len(self.POSSIBLE_QUERIES):
                    self.controller.saveUser(self.getAnswers())
                    answer = self.SIGNED_MESSAGE
            else:
                self.answers.append(text)
                if self.currentQuestion >= len(self.POSSIBLE_QUERIES):
                    answer = self.THANK_YOU
                else:
                    question = self.POSSIBLE_QUERIES[self.currentQuestion]
                    if question == 'name':
                        answer = self.NAME_MESSAGE
                    elif question == 'email':
                        answer = self.EMAIL_MESSAGE
                    elif question == 'origin':
                        answer = self.ORIGIN_MESSAGE
                self.currentQuestion += 1

        self.sendMessage(answer)
        return answer

    def getAnswers(self):
        answers = [self.id]
        for answer in self.answers:
            answers.append(answer)
        return answers
