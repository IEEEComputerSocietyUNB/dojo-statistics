class Attendance:
    def __init__(self):
        self.today = '170303'
        self.participants = [ ]

    def sign(self, userId):
        in_list = False
        for participant in self.participants:
            if participant is userId:
                in_list = True
        if not in_list:
            self.participants.append(userId)
            # TODO Save list
