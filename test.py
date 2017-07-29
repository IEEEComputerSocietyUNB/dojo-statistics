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
        self.nameMessage = {
            'id': 1,
            'message': {
                'text': 'Josh'
            }
        }
        self.emailMessage = {
            'id': 1,
            'message': {
                'text': 'vox@qotsa.com'
            }
        }
        self.originMessage = {
            'id': 1,
            'message': {
                'text': 'QOTSA'
            }
        }
        self.signMessage = {
            'id': 1,
            'message': {
                'text': '/sign'
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

        v1.answer(self.startMessage)
        self.assertEqual('A chamada está indisponível agora!', self.bot.lastMessages[-1])
        v100.answer(self.unlockMessage)
        self.assertEqual('Unlocked! :D', self.bot.lastMessages[-1])
        v1.answer(self.startMessage)
        self.assertEqual('Qual é o seu nome?', self.bot.lastMessages[-1])

    # TODO Check if help message can be sent
    # TODO Test if admin can lock attendance list
    # TODO Test if only users that have answered the form can sign the attendance

    # TODO Check if data can be saved after the conversation is done
    def test_can_get_all_answers(self):
        v1 = view.View(self.bot, 1)
        c1 = controller.Controller(self.model, v1)
        v100 = view.View(self.bot, 100)
        c100 = controller.Controller(self.model, v100)

        v100.answer(self.unlockMessage)
        v1.answer(self.startMessage)
        self.assertEqual('Qual é o seu nome?', self.bot.lastMessages[-1])
        v1.answer(self.nameMessage)
        self.assertEqual('Qual é o seu e-mail?', self.bot.lastMessages[-1])
        v1.answer(self.emailMessage)
        self.assertEqual('Onde você estuda/trabalha/colabora? (Detalhe o curso caso estude ou a comunidade da qual faz parte, ex.: Grupy)', self.bot.lastMessages[-1])
        v1.answer(self.originMessage)
        self.assertEqual('Obrigado por preencher os dados! Envie /sign para preencher a presença.', self.bot.lastMessages[-1])

        expected = [1, 'Josh',  'vox@qotsa.com', 'QOTSA']
        answers = v1.getAnswers()
        self.assertEqual(len(expected), len(answers))
        for i in range(len(answers)):
            self.assertEqual(expected[i], answers[i])

        v1.answer(self.signMessage)
        self.assertEqual('Presença assinada!', self.bot.lastMessages[-1])
        self.assertTrue(1 in self.model.getIds())


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
