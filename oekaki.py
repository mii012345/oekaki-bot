import pymysql.cursors

class Oekaki:
    def __init__(self, s_user, s_passwd):
        self.start = False
        self.level = 1
        
        self.conn = pymysql.connect(
            user=s_user,
            passwd=s_passwd,
            host='localhost',
            db='oekaki'
        )

    def start_oekaki(self):
        '''
        お絵描きをスタートします。
        Start oekaki.
        '''
        self.start = True

    def add_word(self, word, level):
        '''
        ユーザーがワードを追加できるようにします。
        User can add word.
        '''
        c = self.conn.cursor()

        s = 'INSERT INTO word_list(word, level) VALUES ("%s", %s)' % (word, level)
        c.execute(s)