class Controller:
    def __init__(self, model, view):
        """"The goal of this class is to coordinate the model's and the view's
        efforts, routing the current update to an appropriate action."""
        self.model = model
        self.view = view
        self.model.setController(self)
        self.view.setController(self)

    def answer(self, update):
        text = update['message']['text']

        if text == '/unlock': # Processando
            if self.model.isAdmin(self.view.id) and self.model.lockedAttendance:
                self.model.lockedAttendance = False
                self.view.sendMessage('Unlocked! :D')
            else:
                self.view.sendMessage('what?')
        else: # Coletando dados
            if self.model.lockedAttendance:
                self.view.sendMessage(self.view.LOCKED_ATTENDANCE)
            elif self.view.thereAreMoreQueries():
                self.view.sendMessage(self.view.receiveQuery(text))
            else:
                self.view.sendMessage(self.view.THANK_YOU)


    def sendHelp(self):
        self.view.sendMessage(self.view.HELP_MESSAGE)
