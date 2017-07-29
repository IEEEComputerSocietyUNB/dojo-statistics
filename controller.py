class Controller:
    def __init__(self, model, view):
        """"The goal of this class is to coordinate the model's and the view's
        efforts, routing the current update to an appropriate action."""
        self.model = model
        self.view = view
        self.model.setController(self)
        self.view.setController(self)

    def tryToUnlock(self, user):
        answer = 'Not enabled!'
        if user in self.model.admins:
            self.model.lockedAttendance = False
            answer = 'Unlocked! :D'
        return answer

    def isLocked(self):
        return self.model.lockedAttendance

    def sendHelp(self):
        self.view.sendMessage(self.view.HELP_MESSAGE)

    def saveUser(self, answers):
        queries = list(self.view.POSSIBLE_QUERIES)
        user = { }
        for i in range(len(queries)):
            user[queries[i]] = answers[i]
        self.model.addUser(user)
