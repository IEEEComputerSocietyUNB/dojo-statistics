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
            user['id'] = update['message']['chat']['id']
            self.model.addUser(user)
            self.view.setupQuery()

    def answer(self, update):
        """This function needs to be rewritten!!!"""
        # TODO Determine if this user is old or not
        # TODO Determine if this user is already present or not.
        user = self.model.getUser(self.view.id)
        # TODO Check if user has already filled the form
        if user:
            # TODO Sign attendance
            # Checking if user needs to save more information
            if 'origin' not in user:
                user = self.view.queryInfo(user)
            self.model.addUser(update, user)
        # TODO Create a new user when needed
        else:
            user = { }
            user['id'] = update['message']['chat']['id']
            self.model.addUser(user)
            self.view.queryInfo(update, user)

        # TODO React to message accordingly, if those are admin messages
