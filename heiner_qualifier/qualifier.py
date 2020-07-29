"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import re
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):

        self.field_type = field_type
        self.values = {}

    def get_att_name(self, obj):
        obj_dict = type(obj).__dict__
        for att in obj_dict.keys():
            if obj_dict[att] == self:
                return att
        raise Exception

    def __set__(self, obj, val):
        if not isinstance(val, self.field_type):
            raise TypeError(f'expected an instance of type \'{self.field_type.__name__}\' for attribute \'{self.get_att_name(obj)}\', got \'{type(val).__name__}\' instead')
        else:
            self.values[id(obj)] = val


    def __get__(self, instance, owner):
        return self.values[id(instance)]

class Article:
    """The `Article` class you need to write for the qualifier."""

    _id = -1

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

        self.id = self._get_id()

        self.last_edited = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self.last_edited = datetime.datetime.now()
        self._content = value

    @classmethod
    def _get_id(cls):
        cls._id += 1
        return cls._id

    def __repr__(self):
        return f'<{self.__class__.__name__} title="{self.title}" author=\'{self.author}\' publication_date=\'{self.publication_date.isoformat()}\'>'

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def short_introduction(self,n_characters) -> str:
        return self.content[:n_characters+1].rsplit(maxsplit=1)[0]

    def most_common_words(self, n_words):

        clean_list = [word.lower() for word in re.split(r'[^A-Za-z]', self.content) if word != '']

        count_dict = {}

        for word in clean_list:
            try:
                count_dict[word] += 1
            except KeyError:
                count_dict[word] = 1


        return dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:n_words])
