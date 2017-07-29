# -*- coding: utf-8 -*-
import unittest
import model
import view
import controller

class TestMVC(unittest.TestCase):
    def setUp(self):
        # Creating data inside folder
        tf = 'data-test' # test folder
        admins = [100, 200, 300]
        with open('{0}/admins.csv'.format(tf), 'w+') as fp:
            for admin in admins:
                fp.write('%s\n' % (admin))

        # Creating mockup entities
        self.bot = Bot()
        self.unlockMessage = {
            'id': 100,
            'message': {
                'text': '/unlock'
            }
        }
        self.startMessage = {
            'id': 1,
            'message': {
                'text': '/start'
            }
        }

        # Starting new model
        self.model = model.Model('data-test')

    def test_can_load_admins(self):
        self.assertEqual(3, len(self.model.admins))

    def test_can_unlock_attendance(self):
        v1 = view.View(self.bot, 1)
        c1 = controller.Controller(self.model, v1)
        v100 = view.View(self.bot, 100)
        c100 = controller.Controller(self.model, v100)

        c1.answer(self.startMessage)
        self.assertEqual('A chamada está indisponível agora!', self.bot.lastMessages[-1])
        c100.answer(self.unlockMessage)
        self.assertEqual('Unlocked! :D', self.bot.lastMessages[-1])
        c1.answer(self.startMessage)
        self.assertEqual('Qual é o seu nome?', self.bot.lastMessages[-1])

    # TODO Check if help message can be sent
    # TODO Check if data can be saved after the conversation is done

class Bot:
    """Mockup class to be used with the View class"""
    def __init__(self):
        self.ids = [ ]
        self.lastMessages = [ ]

    def sendMessage(self, user, message):
        self.ids.append(user)
        self.lastMessages.append(message)

if __name__ == '__main__':
    unittest.main()
