import telepot
import model
import view
import controller

class App:
    def __init__(self):
        apiCode = input()
        self.bot = telepot.Bot(apiCode)
        print('Loading...')
        # TODO Load stored users
        self.model = model.Model()
        # TODO Generate MVC structures for each ids
        self.ids = { }
        for userId in self.model.getIds():
            self.ids[userId] = self.generateMVC(userId)
        self.offset = 0

    def loop(self):
        updates = self.bot.getUpdates(self.offset)

        for update in updates:
            userId = update['message']['chat']['id']
            if userId not in self.ids:
                # TODO Create a MVC structure for this user
                self.ids[userId] = self.generateMVC(userId)
            # TODO Update user state
            # TODO Sign attendance
            self.ids[userId].answer(update)

            # Taking care of offset
            self.offset = updates[-1]['update_id'] + 1

    def generateMVC(self, userId):
        v = view.View(self.bot)
        c = controller.Controller(self.model, v)
        return c

if __name__ == '__main__':
    print('---')
    app = App()
    while True:
        try:
            app.loop()
        except KeyboardInterrupt:
            print('...')
            break
