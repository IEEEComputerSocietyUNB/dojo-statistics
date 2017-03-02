class Model:
    def __init__(self):
        """ This class expects a `ids.csv` file in the data folder which will store the whole
        bot's data. Each line of this file is expected to follow this pattern:

            telegram id; person name; e-mail; origin

        Based off that, we can store the user's data and make sense of it later. The data will
        be stored on a list called `users`, relating this data on a map. """
        # TODO Load data
        self.users = [ ]
        try:
            self.loadData()
        except FileNotFoundError:
            pass

    def loadData(self):
        with open('data/ids.csv', 'r') as fp:
            # Lines are expected to follow this pattern:
            for line in fp:
                user = { }
                rows = list(map(lambda s: s.strip(), line.split(';')))
                user['id'] = rows[0]
                user['name'] = rows[1]
                # user['email'] = rows[2]
                # user['origin'] = rows[3]
                self.users.append(user)

    def saveData(self):
        with open('data/ids.csv', 'w') as fp:
            for user in self.users:
                fp.write('{0}; {1}\n'.format(user['id'], user['name']))


    def getIds(self):
        # TODO Get ids
        return list(map(lambda user: user['id'], self.users))

    def addUser(self, user):
        if user not in self.users:
            self.users.append(user)
            self.saveData()
