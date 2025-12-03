from abc import ABC, abstractmethod
from datetime import datetime


class Content(ABC):
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._created_at = datetime.now()
        self._published = False
        self._views = 0

    @abstractmethod
    def preview(self):
        ...

    def publish(self):
        if not self._published:
            self._published = True
            print(f'Контент {self._title} опубликован')

    def view(self):
        if self._published:
            self._views += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value in ('', None):
            raise ValueError

        self._title = value

    def get_stats(self):
        return {
            'title': self._title,
            'author': self._author,
            'views': self._views,
            'is_published': self._published
        }


class Article(Content):
    def __init__(self, title, author, text):
        super().__init__(title, author)
        self._text = text
        self._comments = []

    def preview(self):
        return f"СТАТЬЯ: [{self.title}] {self._text[:100]}"

    def add_comment(self, comment: str):
        self._comments.append(comment)

    def get_comments(self):
        return self._comments.copy()


class Video(Content):
    def __init__(self, title, author, duration, url):
        super().__init__(title, author)
        self._duration = duration
        self._url = url
        self._likes = 0
        self._dislikes = 0

    def preview(self):
        minutes = self._duration // 60
        if minutes < 10:
            minutes = f'0{minutes}'

        seconds = self._duration % 60
        if seconds < 10:
            seconds = f'0{seconds}'

        return f"{self._title} {minutes}:{seconds} {self._url}"

#     Добавьте метод get_rating(), возвращающий словарь с
    #     количеством лайков и дизлайков

    def rate(self, like: bool):
        if like:
            self._likes += 1
        else:
            self._dislikes += 1

    def get_rating(self):
        return {
            'likes': self._likes,
            'dislikes': self._dislikes
        }


video = Video('video title', 'avezov', 125, 'https://vk.com/video123')
print(video.preview())



