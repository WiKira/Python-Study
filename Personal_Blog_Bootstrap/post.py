import datetime


class Post:

    def __init__(self,
                 _id: int,
                 _title: str,
                 _subtitle: str,
                 _date: datetime.date,
                 _author: str,
                 _img_link: str,
                 _body: str):
        self.id = _id
        self.title = _title
        self.subtitle = _subtitle
        self.date = _date
        self.author = _author
        self.img_link = _img_link
        self.body = _body