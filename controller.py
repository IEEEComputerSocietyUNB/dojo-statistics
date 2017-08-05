class Controller:
    def __init__(self, model):
        """"The goal of this class is to coordinate the model's and the view's
        efforts, routing the current update to an appropriate action."""
        self.model = model
        self.views = { }
        self.model.setController(self)

    def addView(self, view):
        self.views[view.id] = view
        view.setController(self)

    # MODEL FUNCTIONS

    def tryToUnlock(self, user):
        """Tries to unlock the attendance list."""
        answer = 'Not enabled!'
        if user in self.model.admins:
            self.model.lockedAttendance = False
            answer = 'Unlocked! :D'
        return answer

    def tryToLock(self, user):
        """Tries to lock the attendance list."""
        answer = 'What are you doing here?'
        if user in self.model.admins:
            self.model.lockedAttendance = True
            answer = 'Locked! :x'
        return answer

    def isLocked(self):
        """Checks if the attendance list is locked."""
        return self.model.lockedAttendance

    def saveUser(self, answers):
        """Saves the answer for the given user. Must be a list as
        described: [int(id), str(name), str(email), str(origin)]."""
        queries = ('id', 'name', 'email', 'origin')
        user = { }
        for i in range(len(queries)):
            user[queries[i]] = answers[i]
        self.model.addUser(user)


    # VIEW FUNCTIONS

    def deal(self, view, text):
        """Central function for dealing with regular user messages."""
        if text == '/start':
            return self.start(view)
        elif text == '/sign':
            return self.sign(view)
        elif view.isInFillMode():
            return self.fill(view, text)
        else:
            return view.THANK_YOU

    def start(self, view):
        """Answers to the /start command."""
        if view.id in self.model.getIds():
            view.leaveFillMode()
            return view.THANK_YOU
        else:
            view.firstQuestion()
            return self.fill(view, view.id)


    def sign(self, view):
        """Answers to the /sign command."""
        if view.id in self.model.getIds():
            view.leaveFillMode()
        if not view.isInFillMode():
            self.saveUser(view.getAnswers())
            self.model.signAttendance(view.id)
            return view.SIGNED_MESSAGE
        else:
            return view.ANSWER_EVERYTHING

    def fill(self, view, text):
        """Implements the workflow for filling the attendance list."""
        view.addAnswer(text)

        if view.currentQuestion < len(view.POSSIBLE_QUERIES):
            question = view.POSSIBLE_QUERIES[view.currentQuestion]
            if question == 'name':
                answer = view.NAME_MESSAGE
            elif question == 'email':
                answer = view.EMAIL_MESSAGE
            elif question == 'origin':
                answer = view.ORIGIN_MESSAGE
            view.nextQuestion()
        else:
            answer = view.THANK_YOU
            view.leaveFillMode()

        return answer
