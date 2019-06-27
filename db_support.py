import pymysql

def temp_exec(cmd):
    print(cmd)

def format_str(s):
    return '\"{}\"'.format(s) if isinstance(s, str) else str(s)

def format_kwargs(kwargs, sep=', ', insert=False):
    # {'a': 1, 'b': '2'}
    args = ''
    if kwargs:
        if not insert:
            args += sep.join( e+'='+format_str(kwargs[e]) for e in kwargs if kwargs[e] != '')
        else:
            args += sep.join( e+'='+format_str(kwargs[e]) if kwargs[e] !='' else 'NULL' for e in kwargs)
    return args

def format_args(args, is_attr):
    # (1, 2, '3')
    if not is_attr:
        return ', '.join(format_str(e) for e in args)
    else:
        return ', '.join(e for e in args)


class Database():
    def __init__(self):
        self.db = None
        self.cursor = None
    def connect(self, host='localhost', user="root", passwd="12345678"):
        try:
            self.db = pymysql.connect(host=host, user=user, passwd=passwd)
            self.cursor = self.db.cursor()
        except:
            print("Error: Connect denied")
    def select_db(self, db='university'):
        try:
            self.cursor.execute("USE " + db)
            return True
        except:
            print("Error: Can\'t use database " + db)
            return False

    def select_one(self, table, args, **restrict):  # args can be str or list/tuple
        if isinstance(args, str):
            self.exec('SELECT '+args+' FROM '+table+' WHERE '+format_kwargs(restrict)+';')
        else:
            self.exec('SELECT '+format_args(args, True)+' FROM '+table+' WHERE '+format_kwargs(restrict)+';')
        return self.cursor.fetchone()
        
    def insert(self, table, args, default = False):
        return self.exec('INSERT INTO {} VALUES({}{});'.format(
                         table, 'default, 'if default else '', format_args(args, False)))

    def update(self, table, kwargs, **restrict):
        temp_exec('UPDATE {} SET {} WHERE {};'.format(
                  table, format_kwargs(kwargs), format_kwargs(restrict, sep=' and ') ))
        
    def delete(self, table, **restrict):
        temp_exec('DELETE FROM {} WHERE {};'.format(table, format_kwargs(restrict, sep=' and ')))

    def output(self, table, args='*', kwargs=None):
        formated = format_kwargs(kwargs, ' and ')
        if formated != '':
            self.exec("SELECT " + args + ' FROM ' + table + ' WHERE ' + formated)
        else:
            self.exec("SELECT " + args + ' FROM ' + table)
        return self.cursor

    def exec(self, command, commit=False):
        print("try exec{}: {}".format('+commit' if commit else '', command))
        try:
            self.cursor.execute(command)
            if commit:
                self.db.commit()
            return self.cursor
        except Exception as e:
            print('ERROR {}: {}'.format(e.args[0], e.args[1]))
            #print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            return False

    def __del__(self):
        print('close connection')
        if self.db:
            self.db.close()

    def song(self, kwargs=None):
        empty = True
        for e in kwargs:
            if kwargs[e] != '':
                empty = False
        if empty:
            self.output('song', 'id, name, artist, album, series, time')
        else:
            self.output('song', 'id, name, artist, album, series, time', kwargs=kwargs)
        return self.cursor
    def artist(self, kwargs=None):
        self.output('artist', 'name, company', kwargs=kwargs)
        return self.cursor
    def album(self, kwargs=None):
        self.output('album', 'name. artist, year', kwargs=kwargs)
        return self.cursor
    def series(self, kwargs=None):
        self.output('series', 'name, type', kwargs=None)
        return self.cursor
    def playlist(self):
        self.exec('SELECT name, artist, album, series, time, Sequence FROM song JOIN playlist ON ID = song_id ORDER BY Sequence;')
        return self.cursor

if __name__ == "__main__":
    my_db = Database()
    my_db.connect()
    my_db.select_db(db = 'temp_muxic')
    print(my_db.select_one('song', 'ID, name, link', **{'name': 'glagla'}))
    sql='select'
    # my_db.exec('insert into song values(default, \'name\', \'華晨宇\', Null, Null, Null, 123);', True)
    while sql:
        if sql.split(',')[-1] == 'commit':
            result=my_db.exec(sql.split(',')[0], True)
        else:
            result=my_db.exec(sql)
        if not isinstance(result, int):
            for e in result:
                print(e)
        else:
            print('return:', result)
        sql=input('mysql> ')