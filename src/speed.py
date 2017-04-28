import os

PATH = ""


class Speed(object):
    """
    class Speed
    @param  year  - 年
    @param  month - 月
    @param  date  - 日
    """
    name = ""

    def __init__(self, year, month, date):
        self.file_path = "{year}_{month}.json".format(year=year, month=month)
        self.year = year
        self.month = month
        self.date = date
        self.param = {}

    def add(self, title, complete):
        pass

    def remove(self, id):
        pass

    def update(self, id):
        pass

    def list(self, date):
        pass

    def all(self):
        pass

    def post(self):
        pass


class Todo(Speed):
    """
    class Todo
    @param  year  - 年
    @param  month - 月
    @param  date  - 日
    """
    name = "todo"
    path = ""

    def __init__(self, year, month, date=1):
        super(Todo, self).__init__(year, month, date)
        from tinydb import TinyDB, Query

        # validate
        if not os.path.exists(PATH):
            print("you dont have directory....")
            return None

        db = TinyDB(PATH + self.file_path)
        self.table = db.table("todos")
        self.query = Query()

    def __get_todo(self, date):
        import datetime
        today = datetime.datetime.today().day
        day = 0
        if date == "today":
            day = today
        elif date == "yesterday":
            day = today - 1
        elif date == "tomorrow":
            day = today + 1
        else:
            day = self.date
        res = self.table.search(self.query.date == "{0}日".format(day))
        return res, day

    def add(self, title, complete, date=""):
        """ データの挿入
        @param title
        @param complete
        @param date
        """
        todos = self.__get_todo(date)
        self.table.insert({"title": title, "complete": complete, "date": "{0}日".format(todos[1])})
        print("add!!")

    def remove(self, id):
        """ データの削除
        @param id
        """
        self.table.remmove(self.query.id == id)

    def update(self, id, *args):
        """ データの更新
        - todoのコンプリートの更新などを行いたい
        - :Go todo delete id complete (True or False)
        - :Go todo delete id title ""
        @param id
        """
        params = {"title": args[0], "complete": args[1]}
        self.table.update(params, self.query.id == id)

    def list(self, date=""):
        """ データのリスト表示
        @param data
        """
        todos = self.__get_todo(date)
        print(" -------------- ", "{0}年{1}月{2}日".format(self.year, self.month, todos[1]), " -------------- ")
        for it in todos[0]:
            check = '| [x] |' if it['complete'] else '| [ ] |'
            print(check, it['title'])

    def all(self):
        """ データの全て表示 """
        print(" ------------- ", "{0}年{1}月: Todo".format(self.year, self.month), " ------------- ")
        for it in self.table.all():
            day = '0' + it['date'] if len(it['date']) == 2 else it['date']
            check = '| [x] |' if it['complete'] else '| [ ] |'
            title = it['title']
            print(day, check, title)


class Memo(Speed):
    """
    class Memo
    """
    pass


class Diary(Speed):
    """
    class Diary
    """
    pass
