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
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    id = 0

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.last_edited = None
        self.id = self.__class__.id
        self.__class__.id += 1

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def __repr__(self):
        return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def short_introduction(self, n_characters: int):
        last_whitespace = self.content[: n_characters + 1].rfind(" ")
        last_newline = self.content[: n_characters + 1].rfind("\n")
        last = last_whitespace if last_whitespace > last_newline else last_newline
        print(self.content[:last])
        return self.content[:last]

    def most_common_words(self, n_words: int):
        content = self.content.lower()
        words_counter = {}
        for word in re.split(r"[\s']", content):
            if word == "":
                continue
            try:
                words_counter[word.rstrip(",.")] += 1
            except KeyError:
                words_counter[word.rstrip(",.")] = 1

        return {
            k: v
            for k, v in sorted(words_counter.items(), key=lambda item: item[1], reverse=True)[
                :n_words
            ]
        }
