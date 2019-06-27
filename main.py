from flask import Flask, render_template, url_for, request, redirect, flash
from db_support import Database

app = Flask(__name__)

@app.route('/')
def main_page():
    play_list_sequence=['name', 'artist', 'album', 'series', 'time']
    data = []
    for e in db.playlist():
        song={}
        for i in range(5):
            if e[i]:
                song[play_list_sequence[i]] = e[i]
            else:
                song[play_list_sequence[i]] = ''
        data += [song]
    return render_template('init.html', data=data)

@app.route('/add_to_list/<int:id>', methods=['GET'])
def add_to_list(id):
    # insert song(id) to playlist
    if db.insert('playlist', [id], default=True):
        flash("add song: {} to list".format(id))
    else:
        flash('新增失敗')
    return redirect(url_for('main_page'))

@app.route('/song/', methods=['GET'])       # 搜尋的內容放在 GET 區 ?abc=abc
def song():
    # id, name, artist, album, series, time
    outputstr= ""
    for e in request.args:
        print(e, ': ', repr(request.args[e]))
        outputstr += ' {}: {}'.format(e, request.args[e])
    if request.args:
        flash("search for"+ outputstr)

    data = []
    song_attr_seq=['id', 'name', 'artist', 'album', 'series', 'time']
    for e in db.song(request.args):
        song={}
        for i in range(6):
            if e[i]:
                song[song_attr_seq[i]] = e[i]
            else:
                song[song_attr_seq[i]] = ''
        data += [song]
    return render_template('song.html', data = data)

@app.route('/artist/', methods=['GET'])
def artist():
    return render_template('artist.html')

@app.route('/album/', methods=['GET'])
def album():
    return render_template('album.html')

@app.route('/series/', methods=['GET'])
def series():
    return render_template('series.html')

@app.route('/info/', methods=['GET'])
def info():
    return render_template('info.html')

@app.route('/song/edit/<int:id>', methods=['GET', 'POST'])
def edit_song(id):
    song_attr_seq=['name', 'artist', 'link', 'album', 'series', 'time']
    data = db.select_one('song', song_attr_seq, ID=id)  # tuple
    data = dict(zip(song_attr_seq, data))   # 先 zip 成[(attr, val), ()...] 再轉成 dict
    if request.method == 'GET':
        
        for e in data:
            if data[e] == None:
                data[e] = ''
        #print(data)
        return render_template('edits/edit song.html', **data)
    elif request.method == 'POST':
        print("POST create song...>")
        for e in request.values:
            print(e, ':', request.values[e])

        result=db.update('song', request.values, data, id=id)
        if result:
            flash('更新成功! ')
            return redirect(url_for('song'))
        else:
            flash('更新失敗! ')
            return redirect(url_for('edit_song', **request.values, id=id))

@app.route('/song/create/', methods=['GET', 'POST'])
def create_song():
    song_attr_seq=['name', 'link', 'artist', 'album', 'series', 'time']
    if request.method == 'GET':
        print("GET create song...>")
        for e in request.args:
            print(e, ':', request.args[e])
        
        return render_template('edits/edit song.html', **request.args)
    elif request.method == 'POST':
        print("POST create song...>")
        for e in request.values:
            print(e, ':', request.values[e])
        
        result= db.insert('song', [request.values[e] for e in song_attr_seq], default=True)
        if result:
            flash('新增成功! ')
            return redirect(url_for('song'))
        else:
            flash('新增失敗! ')
            return redirect(url_for('create_song'))
            #return redirect(url_for('create_song'), code=307)   # POST 過來的資料都會留著 讚!

@app.route('/song/_delete/<int:id>', methods= ['POST'])
def delete_song(id):
    if db.delete('song', id=id):
        flash('刪除成功')
    else:
        flash('刪除失敗')
    return redirect(url_for('song'))

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.select_db(db = 'temp_muxic')

    app.secret_key = 'my secret key'
    app.run(debug = True, port = 5000)
    # db.close()