import time
import os

class Attendance:
    def __init__(self):
        self.today = time.strftime("%Y%m%d", time.gmtime())
        self.participants = [ ]

    def sign(self, userId):
        in_list = False
        for participant in self.participants:
            if participant is userId:
                in_list = True
        if not in_list:
            self.participants.append(userId)
            # TODO Save list
            self.save()

    def save(self):
        # TODO Generating list name
        file_name = 'data/{0}.csv'.format(self.today)
        # TODO Storing data
        with open(file_name, 'w') as fp:
            for participant in self.participants:
                fp.write('{0}\n'.format(participant))
