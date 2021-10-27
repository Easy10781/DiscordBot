import unittest

import utils
from localization.messages import *


class LocalizationTest(unittest.TestCase):
    def test_ru(self):
        """
        Tests a ru localization
        Ru localization test
        """
        utils.set_language('ru')
        # Пользователь {USERNAME} был успешно забанен модератором {MOD_USERNAME} за {REASON}
        self.assertEqual("Пользователь test_ был успешно забанен модератором test__ за test___",
                         text_for_ban.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Пользователь {USERNAME} был успешно кикнут модератором {MOD_USERNAME} за {REASON}
        self.assertEqual("Пользователь test_ был успешно кикнут модератором test__ за test___",
                         text_for_kick.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Пользователь {USERNAME} был успешно заткнут модератором {MOD_USERNAME} за {REASON}
        self.assertEqual("Пользователь test_ был успешно замутен модератором test__ за test___",
                         text_for_mute.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Пользователь под именем {USERNAME} не был найден
        self.assertEqual("Пользователь под именем test_ не был найден",
                         text_for_not_found.render(USERNAME='test_'))

        # Только модераторы могут использовать эту команду
        self.assertEqual("Только модераторы могут использовать эту команду",
                         text_for_not_allowed_using.render())

        # Подключен!
        self.assertEqual("Подключен!", text_on_ready.render())

    def test_eng(self):
        """
        Eng localization test
        """

        utils.set_language('eng')
        # Member {USERNAME} was banned by {MOD_USERNAME} moderator. Reason: {REASON}
        self.assertEqual("Member test_ was banned by test__ moderator. Reason: test___",
                         text_for_ban.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Member {USERNAME} was kicked by {MOD_USERNAME} moderator. Reason: {REASON}
        self.assertEqual("Member test_ was kicked by test__ moderator. Reason: test___",
                         text_for_kick.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Member {USERNAME} was muted by {MOD_USERNAME} moderator. Reason: {REASON}
        self.assertEqual("Member test_ was muted by test__ moderator. Reason: test___",
                         text_for_mute.render(USERNAME='test_', MOD_USERNAME='test__', REASON='test___'))

        # Member {USERNAME} not found
        self.assertEqual("Member test_ not found",
                         text_for_not_found.render(USERNAME='test_'))

        # Only moderators can use this command
        self.assertEqual("Only moderators can use this command",
                         text_for_not_allowed_using.render())

        # Joined!
        self.assertEqual("Joined!", text_on_ready.render())

        # 'Member {USERNAME} cannot to be kicked because he is moderator'
        self.assertEqual("Member test_ cannot to be kicked because he is moderator",
                         text_for_mod_kick.render(USERNAME='test_'))

        # Member {USERNAME} cannot to be banned because he is moderator
        self.assertEqual("Member test_ cannot to be banned because he is moderator",
                         text_for_mod_ban.render(USERNAME='test_'))

        # Member {USERNAME} cannot to be muted because he is moderator
        self.assertEqual("Member test_ cannot to be muted because he is moderator",
                         text_for_mod_mute.render(USERNAME='test_'))


if __name__ == '__main__':
    unittest.main()
