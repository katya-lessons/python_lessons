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
            print(f'Content "{self._title}" has been published')

    def view(self):
        if self._published:
            self._views += 1

    def get_stats(self):
        return {
            'Title': self._title,
            'Author': self._author,
            'Views': self._views,
            'Has been published': self._published
        }

    @property
    def title(self):
        return self._title

#     С помощью @title.setter создайте сеттер, который
#     проверяет, что новый заголовок не пустой
#     (иначе вызывает ValueError)
    @title.setter
    def title(self, new_title):
        if new_title in ('', None):
            raise ValueError

        self._title = new_title


class Article(Content):
    def __init__(self, title, author, text):
        super().__init__(title, author)
        self._text = text
        self._comments = []

    def preview(self):
        return f"СТАТЬЯ: [{self.title}] \n{self._text[:100]}"

    def add_comment(self, comment: str):
        self._comments.append(comment)

    def get_comments(self):
        return self._comments.copy()


class Video(Content):
    def preview(self):
        minutes = self._duration // 60
        seconds = self._duration % 60

        return f"{self.title}\n{str(minutes).zfill(2)}:{str(seconds).zfill(2)}\n{self._url}"

    def rate(self, like: bool):
        if like:
            self._likes += 1
        else:
            self._dislikes += 1

    def get_rating(self):
        return {
            'Likes': self._likes,
            'Dislikes': self._dislikes,
        }

    def __init__(self, title, author, duration, url):
        super().__init__(title, author)
        self._duration = duration
        self._url = url
        self._likes = 0
        self._dislikes = 0


class Podcast(Content):
    def __init__(self, title,  author, episode, guests):
        super().__init__(title, author)
        self._episode = episode
        self._guests = guests
        self._transcript = ''

    def preview(self):
        return f"Episode number: {self._episode}\nTitle: {self.title}\nGuests: {', '.join(self._guests)}"

    def set_transcript(self, transcript):
        self._transcript = transcript

    def search_in_transcript(self, keyword: str):
        return keyword in self._transcript


article = Article('article title', 'todyshev', 'some text')
video = Video('video title', 'orlov', 130, 'https://vk.com/video123')
podcast = Podcast('podcast title', 'Mansurov and Tyushin', 1, ['Afina', 'Spartak', 'Eldar'])

print(podcast.preview())

