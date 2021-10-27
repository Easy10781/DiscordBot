from localization.exceptions import LanguageNotFound


class Message:
    message: dict

    def __init__(self, msg):
        if not isinstance(msg, dict):
            raise TypeError('Expected type dict, got %s' % type(msg).__name__)
        self.support_languages = [i for i in list(msg.keys())]
        self._default_lang = self.support_languages[0]
        self.message = msg

    def __repr__(self):
        return self.message[self.default_lang]

    def __str__(self):
        return self.__repr__()

    def render(self, language=None, **words):
        if language is None:
            language = self._default_lang
        keys_in_text = ['{' + i + '}' for i in list(words.keys())]
        keys = list(words.keys())
        t = self.translate(language)
        for key in range(len(keys)):
            t = t.replace(keys_in_text[key], words[keys[key]])
        return t

    def translate(self, language):
        if not isinstance(language, str):
            raise TypeError('Expected type str, got %s' % type(language).__name__)
        if language not in self.support_languages:
            raise LanguageNotFound('Language %s not supported' % language)

        return self.message[language]

    def is_supported(self, language):
        if language in self.support_languages:
            return True
        return False

    def add_lang(self, lang, msg):
        if not isinstance(lang, str):
            raise TypeError('Expected type str, got %s' % type(lang).__name__)
        if not isinstance(msg, str):
            raise TypeError('Expected type str, got %s' % type(lang).__name__)
        self.message[lang] = msg
        self.support_languages.append(lang)

    @property
    def default_lang(self):
        return self._default_lang

    @default_lang.setter
    def default_lang(self, value):
        t = self.is_supported(value)
        if not t:
            for lang in self.support_languages:
                if lang is not value:
                    self._default_lang = lang
                    return
        self._default_lang = value
