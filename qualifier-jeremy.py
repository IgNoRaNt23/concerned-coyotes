import datetime
import re
import typing


class ArticleField:
    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> typing.Type[typing.Any]:
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        if isinstance(value, self.field_type):
            obj.__dict__[self.name] = value
        else:
            err = (f"expected an instance of type "
                   f"'{self.field_type.__name__}' "
                   f"for attribute {repr(self.name)}, "
                   f"got '{type(value).__name__}' instead")
            raise TypeError(err)


class Article:
    id_counter = 0

    title = ArticleField(str)
    author = ArticleField(str)
    publication_date = ArticleField(datetime.datetime)
    content = ArticleField(str)

    def __init__(
        self,
        title: str,
        author: str,
        publication_date: datetime.datetime,
        content: str
    ):
        # Assign unique id
        self.id = self.__class__.id_counter
        self.__class__.id_counter += 1

        # Article attributes
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content

        # Last edited
        self.last_edited = None

    def __repr__(self) -> str:
        return (
            f"<Article title={repr(self.title)} "
            f"author={repr(self.author)} "
            f"publication_date={repr(self.publication_date.isoformat())}>"
        )

    def __len__(self) -> int:
        return len(self.content)

    def __lt__(self, other: "Article") -> bool:
        return self.publication_date < other.publication_date

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        self._content = new_content
        self.last_edited = datetime.datetime.now()
    
    def short_introduction(self, n_characters: int) -> str:
        string = re.split(" |\n", self.content[:n_characters+1])[:-1]
        return " ".join(string).strip()

    def most_common_words(self, n_words: int) -> dict:
        # split words
        content_words = re.split(r"\W+", self.content.lower())

        # using dict.fromkeys to get a list with each word
        # only once and still ordered
        unique_words = dict.fromkeys(content_words)

        # Create a list with tuples (word, count, index)
        # to sort later
        words = [(word, content_words.count(word))
                 for word in unique_words if word]

        # sort first by count, then by index
        words.sort(key=lambda t: t[1], reverse=True)

        return {word: count for word, count in words[:n_words]}
