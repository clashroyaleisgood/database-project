from flask import Flask, render_template, url_for, request, redirect, flash
from db_support import Database, get_whole_table

app = Flask(__name__)

@app.route('/')
def main_page():
    playlist_sequence=['name', 'artist', 'album', 'series', 'time']
    data = get_whole_table(db.playlist(), playlist_sequence)
    
    return render_template('init.html', data=data)

@app.route('/add_to_list/<int:id>', methods=['GET'])
def add_to_list(id):
    if db.insert('playlist', [id], default=True):
        song_name=db.select_one('song', 'name', id=id)[0]
        flash("add song: {} to list".format(song_name))
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

    song_attr_seq=['id', 'name', 'artist', 'album', 'series', 'time']
    data = get_whole_table(db.song(request.args), song_attr_seq)

    return render_template('song.html', data = data)

@app.route('/artist/', methods=['GET'])
def artist():
    artist_attr_seq=['name', 'company']
    data= get_whole_table(db.artist(), artist_attr_seq)
    return render_template('artist.html', data=data)

@app.route('/album/', methods=['GET'])
def album():
    album_attr_seq=['name', 'artist', 'year']
    data= get_whole_table(db.album(), album_attr_seq)
    
    return render_template('album.html', data=data)

@app.route('/series/', methods=['GET'])
def series():
    return render_template('series.html')

@app.route('/info/', methods=['GET'])
def info():
    return render_template('info.html')
#----------------------------------------------------------------------------------------------------
@app.route('/song/create/', methods=['GET', 'POST'])
def create_song():
    song_attr_seq=('name', 'link', 'artist', 'album', 'series', 'time')
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
@app.route('/song/edit/<int:id>/', methods=['GET', 'POST'])
def edit_song(id):
    song_attr_seq=('name', 'artist', 'link', 'album', 'series', 'time')
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
@app.route('/song/_delete/<int:id>/', methods= ['POST'])
def delete_song(id):
    if db.delete('song', id=id):
        flash('刪除成功')
    else:
        flash('刪除失敗')
    return redirect(url_for('song'))

@app.route('/album/create/', methods=['GET', 'POST'])
def create_album():
    # album_attr_seq=['name', 'artist', 'year'] 這是錯的順序...
    album_attr_seq=('name', 'year', 'artist')
    if request.method == 'GET':
        return render_template('edits/edit album.html')
    elif request.method == 'POST':
        for e in request.values:
            print(e, ':', request.values[e])
        result= db.insert('album', (request.values[e] for e in album_attr_seq))
        if result:
            flash('新增成功! ')
            return redirect(url_for('album'))
        else:
            flash('新增失敗! ')
            return redirect(url_for('create_album'))
@app.route('/album/edit/<name>/', methods=['GET', 'POST'])
def edit_album(name):
    album_attr_seq=['name', 'year', 'artist']
    data = db.select_one('album', album_attr_seq, name=name)  # tuple
    data = dict(zip(album_attr_seq, data))   # 先 zip 成[(attr, val), ()...] 再轉成 dict

    if request.method == 'GET':
        for e in data:
            if data[e] == None:
                data[e] = ''
        print(data)
        return render_template('edits/edit album.html', **data)

    elif request.method == 'POST':
        for e in request.values:
            print(e, ':', request.values[e])

        result=db.update('album', request.values, data, name=name)
        if result:
            flash('更新成功! ')
            return redirect(url_for('album'))
        else:
            flash('更新失敗! ')
            return redirect(url_for('edit_album', **request.values, name=name))
@app.route('/album/_delete/<name>/', methods=['POST'])
def delete_album(name):
    if db.delete('album', name=name):
        flash('刪除成功')
    else:
        flash('刪除失敗')
    return redirect(url_for('album'))

@app.route('/artist/create/', methods=['GET', 'POST'])
def create_artist():
    artist_attr_seq=('name', 'company')
    if request.method == 'GET':
        return render_template('edits/edit artist.html')
    elif request.method == 'POST':
        for e in request.values:
            print(e, ':', request.values[e])
        result= db.insert('artist', (request.values[e] for e in artist_attr_seq))
        if result:
            flash('新增成功! ')
            return redirect(url_for('artist'))
        else:
            flash('新增失敗! ')
            return redirect(url_for('create_artist'))
@app.route('/artist/edit/<name>', methods=['GET', 'POST'])
def edit_artist(name):
    artist_attr_seq=['name', 'company']
    data = db.select_one('artist', artist_attr_seq, name=name)  # tuple
    data = dict(zip(artist_attr_seq, data))   # 先 zip 成[(attr, val), ()...] 再轉成 dict

    if request.method == 'GET':
        for e in data:
            if data[e] == None:
                data[e] = ''
        print(data)
        return render_template('edits/edit artist.html', **data)

    elif request.method == 'POST':
        for e in request.values:
            print(e, ':', request.values[e])

        result=db.update('artist', request.values, data, name=name)
        if result:
            flash('更新成功! ')
            return redirect(url_for('artist'))
        else:
            flash('更新失敗! ')
            return redirect(url_for('edit_artist', **request.values, name=name))
@app.route('/artist/_delete/<name>/', methods=['POST'])
def delete_artist(name):
    if db.delete('artist', name=name):
        flash('刪除成功')
    else:
        flash('刪除失敗')
    return redirect(url_for('artist'))

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.select_db(db = 'temp_muxic')

    app.secret_key = 'my secret key'
    app.run(debug = True, port = 5000)
    # db.close()