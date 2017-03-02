import telepot

class App:
    def __init__(self):
        apiCode = input()
        self.bot = telepot.Bot(apiCode)

    def setup(self):
        print('Loading...')

    def loop(self):
        print(self.bot.getMe())
        raise Exception()

if __name__ == '__main__':
    print('---')
    app = App()
    app.setup()
    while True:
        try:
            app.loop()
        except:
            print('...')
            break
