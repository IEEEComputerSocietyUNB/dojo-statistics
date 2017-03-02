import telepot
import model

class App:
    def __init__(self):
        apiCode = input()
        self.bot = telepot.Bot(apiCode)
        print('Loading...')
        # TODO Load stored users
        self.model = model.Model()
        self.ids = self.model.getIds()
        self.offset = 0

    def loop(self):
        updates = self.bot.getUpdates(self.offset)

        for update in updates:
            userId = update['message']['chat']['id']
            if userId not in self.ids:
                # TODO Create a MVC structure for this user
                self.ids[userId] = update['message']['chat']['first_name']
            # TODO Update user state
            # TODO Sign attendance
            print(self.ids[userId])

            # Taking care of offset
            self.offset = updates[-1]['update_id'] + 1


if __name__ == '__main__':
    print('---')
    app = App()
    while True:
        try:
            app.loop()
        except KeyboardInterrupt:
            print('...')
            break
