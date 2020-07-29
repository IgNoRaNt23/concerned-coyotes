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
import typing
from collections import defaultdict, Counter
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value: "ArticleField"):
        if isinstance(value, self.field_type):
            instance.__dict__[self.name] = value
        else:
            error_msg = "expected an instance of type '{type}' for attribute '{name}', got '{provided_type}' instead"
            raise TypeError(
                error_msg.format(
                    type=self.field_type.__name__,
                    name=self.name,
                    provided_type=type(value).__name__
                )
            )

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Article:
    """The `Article` class you need to write for the qualifier."""

    counter = 0

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.id = Article.counter
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.last_edited = None

        Article.counter += 1

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def short_introduction(self, n_characters):
        if len(self) < n_characters:
            n_characters = len(self)

        intro = []
        for word in self.content.split():
            if self.content.index(word) + len(word) < n_characters:
                intro.append(word)
        return ' '.join(intro)

    def most_common_words(self, n_words):
        pattern = re.compile(r'\w+')
        words = pattern.findall(self.content.lower())
        result = Counter(words)
        return dict(result.most_common(n_words))

    def __repr__(self):
        text = "<Article title=\"{title}\" author='{author}' publication_date='{date}'>"
        return text.format(
            title=self.title,
            author=self.author,
            date=self.publication_date.isoformat()
        )

    def __len__(self):
        return len(self.content)

    def __lt__(self, other: "Article"):
        return self.publication_date < other.publication_date

"""
====================================================================================================
Test Suite Summary
----------------------------------------------------------------------------------------------------
                                                   PASSED   FAILED   TOTAL   RESULT
Tests for the basic requirements                      3        2       5      FAIL
Additional tests for the basic requirements           1        4       5      FAIL
Tests for the intermediate requirements               3        0       3      PASS
Additional tests for the intermediate requirements    4        0       4      PASS
Tests for the advanced requirements                   4        0       4      PASS
Additional tests for the advanced requirements        0        1       1      FAIL
====================================================================================================
Total running time: 0.066s
"""