from utils import new_message

text_for_ban = new_message({'ru': 'Пользователь {USERNAME} был успешно забанен модератором {MOD_USERNAME} за {REASON}',
                            'eng': 'Member {USERNAME} was banned by {MOD_USERNAME} moderator. Reason: {REASON}'})
text_for_kick = new_message({'ru': 'Пользователь {USERNAME} был успешно кикнут модератором {MOD_USERNAME} за {REASON}',
                             'eng': 'Member {USERNAME} was kicked by {MOD_USERNAME} moderator. Reason: {REASON}'})
text_for_mute = new_message({'ru': 'Пользователь {USERNAME} был успешно замутен модератором {MOD_USERNAME} за {REASON}',
                             'eng': 'Member {USERNAME} was muted by {MOD_USERNAME} moderator. Reason: {REASON}'})

text_for_unban = new_message({'ru': 'Пользователь {USERNAME} был успешно разбанен модератором '
                                    '{MOD_USERNAME} за {REASON}',
                              'eng': 'Member {USERNAME} was unbanned by {MOD_USERNAME} moderator. Reason: {REASON}'})
text_for_unmute = new_message({'ru': 'Теперь пользователь {USERNAME} не замутен модератором '
                                     '{MOD_USERNAME} за {REASON}',
                               'eng': 'Member {USERNAME} was unmuted by {MOD_USERNAME} moderator. Reason: {REASON}'})


text_for_not_found = new_message({'ru': 'Пользователь под именем {USERNAME} не был найден',
                                  'eng': 'Member {USERNAME} not found'})

text_for_not_allowed_using = new_message({'ru': 'Только модераторы могут использовать эту команду',
                                          'eng': 'Only moderators can use this command'})
text_for_mod_kick = new_message({'ru': 'Пользователь {USERNAME} не может быть кикнут так как он модератор',
                                 'eng': 'Member {USERNAME} cannot to be kicked because he is moderator'})
text_for_mod_ban = new_message({'ru': 'Пользователь {USERNAME} не может быть кикнут так как он модератор',
                                'eng': 'Member {USERNAME} cannot to be kicked because he is moderator'})
text_for_mod_mute = new_message({'ru': 'Пользователь {USERNAME} не может быть замутен так как он модератор',
                                'eng': 'Member {USERNAME} cannot to be muted because he is moderator'})

text_for_not_muted_unmuting = new_message({'ru': 'Пользователь {USERNAME} итак не замутен',
                                           'eng': 'Member {USERNAME} not muted '})

text_on_ready = new_message({'ru': 'Подключен!', 'eng': 'Joined!'})
#