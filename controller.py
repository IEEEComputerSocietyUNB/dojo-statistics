class Controller:
    def __init__(self, model, view):
        """"The goal of this class is to coordinate the model's and the view's
        efforts, routing the current update to an appropriate action."""
        self.model = model
        self.view = view
        self.view.setController(self)

        # Verifying user state
        user = self.model.getUser(self.view.id)
        if not user:
            user = { }
            user['id'] = self.view.id
            self.model.addUser(user)
            self.view.setupQuery()

    def answer(self, update):
        """This function needs to be rewritten!!!"""
        user = self.model.getUser(self.view.id)
        if self.view.shouldQuery():
            message = update['message']['text']
            user = self.view.receiveQuery(user, message)
            self.model.addUser(user)
            self.view.sendNextQuery()
        # TODO Sign attendance list
        if not self.model.locked_attendance:
            self.model.signAttendance(self.view.id)
            self.view.sendMessage(self.view.SIGNED_MESSAGE)
        else:
            self.view.sendMessage(self.view.LOCKED_ATTENDANCE)
        # TODO React to message accordingly, if those are admin messages
