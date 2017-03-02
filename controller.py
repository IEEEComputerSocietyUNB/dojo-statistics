class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setController(self)

    def answer(self, update):
        user = { }
        user['id'] = update['message']['chat']['id']
        user['name'] = update['message']['chat']['first_name']
        self.model.addUser(user)
        self.view.sendMessage(update, 'ok')
