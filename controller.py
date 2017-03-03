class Controller:
    def __init__(self, model, view):
        """"The goal of this class is to coordinate the model's and the view's
        efforts, routing the current update to an appropriate action."""
        self.model = model
        self.view = view
        self.model.setController(self)
        self.view.setController(self)

        # Verifying user state
        user = self.model.getUser(self.view.id)
        if not user:
            user = { }
            user['id'] = self.view.id
            self.model.addUser(user)
            self.view.setupQuery()

    def answer(self, update):
        """This function coordinate the message flow!"""
        user = self.model.getUser(self.view.id)
        # Getting information from users
        if self.view.shouldQuery():
            message = update['message']['text']
            user = self.view.receiveQuery(user, message)
            self.model.addUser(user)
            self.view.sendNextQuery()
        # Signing attendance list
        # TODO Turn /sign into the command for signing the attendance list
        else:
            if not self.model.locked_attendance:
                self.model.signAttendance(self.view.id)
                self.view.sendMessage(self.view.SIGNED_MESSAGE)
            else:
                self.view.sendMessage(self.view.LOCKED_ATTENDANCE)
        # TODO React to message accordingly, if those are admin messages
        if self.model.isAdmin(self.view.id):
            reaction = self.model.reactToAdmin(update)
            if reaction: self.view.sendMessage(reaction)

    def sendHelp(self):
        self.view.sendMessage(self.view.HELP_MESSAGE)
