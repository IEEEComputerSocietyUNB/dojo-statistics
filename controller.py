class Controller:
    def __init__(self, model, view):
        """"The goal of this class is to coordinate the model's and the view's efforts, routing the corrent"""
        self.model = model
        self.view = view
        self.view.setController(self)

    def answer(self, update):
        # TODO Determine if this user is already present or not.
        chat_id = update['message']['chat']['id']
        user = self.model.getUser(chat_id)
        if user:
            # TODO Sign attendance
            # Checking if user needs to save more information
            if 'origin' not in user:
                user = self.view.queryInfo(user)
            self.model.addUser(update, user)
        else:
            user = { }
            user['id'] = update['message']['chat']['id']
            self.model.addUser(user)
            self.view.queryInfo(update, user)
