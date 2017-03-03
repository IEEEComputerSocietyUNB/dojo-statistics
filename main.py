import telepot
import model
import view
import controller
import sys

class App:
    """Here it is: this bot's entry point. Create a new app by giving it their
    API code as provided by Telegram and start running it. It will load the
    users' database file into memory and update their status."""
    def __init__(self, api):
        apiCode = api
        self.bot = telepot.Bot(apiCode)
        print('Loading...')
        self.model = model.Model()
        self.ids = { }
        for userId in self.model.getIds():
            self.ids[userId] = self.generateMVC(userId)
        self.offset = 0

    def loop(self):
        updates = self.bot.getUpdates(self.offset)

        for update in updates:
            userId = update['message']['chat']['id']
            if userId not in self.ids:
                self.ids[userId] = self.generateMVC(userId)
            # TODO Update user state
            # TODO Sign attendance
            self.ids[userId].answer(update)

            # Taking care of offset
            self.offset = updates[-1]['update_id'] + 1

    def generateMVC(self, userId):
        v = view.View(self.bot, userId)
        c = controller.Controller(self.model, v)
        return c

if __name__ == '__main__':
    api = sys.argv[1]
    app = App(api)
    print('---')
    while True:
        try:
            app.loop()
        except KeyboardInterrupt:
            print('...')
            break
