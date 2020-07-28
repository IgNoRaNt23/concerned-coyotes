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
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(
        self, title: str, author: str, publication_date: datetime.datetime, content: str
    ):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return f'<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.publication_date.isoformat("T")}\'>'

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters):
        test = self.content.split()
        original = self.content[:n_characters].split()
        if original[-1] not in test:
            original.remove(original[-1])
        return " ".join(original)

    def most_common_words(self, n_words):
        word_split = self.content.lower()
        word_split = re.findall(r"[\w]*", word_split)
        new_list = []
        for word in word_split:
            if word == "":
                continue
            else:
                new_list.append(word)
        my_dict = {}
        for word in new_list:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1
        sort_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        return dict(sort_dict[:n_words])


fairytale = Article(
    title="The emperor's new clothes",
    author="Hans Christian Andersen",
    content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
    publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
)
print(repr(fairytale))
print(len(fairytale.content))
print(fairytale.short_introduction(n_characters=60))
print(fairytale.most_common_words(5))
