# -*- coding: utf-8 -*-
import time
import os

class Attendance:
    def __init__(self):
        """This class implements the attendance list operations, such as
        signing and saving it on memory on a appropriate file."""
        self.today = time.strftime("%Y%m%d", time.gmtime())
        self.participants = [ ]

    def sign(self, userId):
        """Adds another id to the attendance list."""
        in_list = False
        for participant in self.participants:
            if participant is userId:
                in_list = True
        if not in_list:
            self.participants.append(userId)
            self.save()

    def save(self):
        """This method saves the current list of present people on
        a file whose name is coded with the current date."""
        # Generating list name
        file_name = 'data/{0}.csv'.format(self.today)
        # Storing data
        with open(file_name, 'w+') as fp:
            for participant in self.participants:
                fp.write('{0}\n'.format(participant))
