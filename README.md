# Database Project
[![](https://img.shields.io/badge/MySQL-yellow.svg)](https://www.mysql.com/)
[![](https://img.shields.io/badge/AppServ-lightgrey.svg)](https://www.appserv.org/en/)
[![](https://img.shields.io/badge/Python-PyMySQL-blue.svg?logo=python)](https://pymysql.readthedocs.io/en/latest/)
[![](https://img.shields.io/badge/Python-Flask-blue.svg?logo=flask)](http://flask.pocoo.org/)
![](https://img.shields.io/badge/front_end-Bootstrap%20%7C%20jQuery-blueviolet.svg)
[![](https://img.shields.io/badge/YouTube_API-orange.svg?logo=youtube&logoColor=red&labelColor=white)](https://developers.google.com/youtube/iframe_api_reference)  
[![](https://img.shields.io/badge/Just-Fun-yellow.svg)](https://shields.io/)

> database with music playlist  
> 師大資工 資料庫 期末專題 **MuXic**  
> 教師: **柯佳伶**  
> 成員: **林孟學 - 黃勁衡 - 溫博任**

# HOW TO USE

## 1. Install
- MySQL: 使用 [appserv](https://www.appserv.org/en/download/)，或任何包含 MySQL 引擎的軟體
- Python: 使用 Python3
- Flask & PyMySQL: 使用 pip 安裝套件
```
$ pip install flask
$ pip install pymysql
```
---

## 2. Create Database
in MySQL Command Line Interface
```sql
mysql> CREATE DATABASE databasename
mysql> USE databasename
mysql> source path/to/DDL.sql
mysql> source path/to/relations.sql
-- default path is: database-project/SQL/...
```

## 3. Connect to Database
> [/main.py line 298](main.py#L298)
> ```python
> # change db.connect() to
> db.connect(host="localhost", user="root", passwd="your pass word")
> ```
> see detail in [db_support.py](db_support.py#L38)  

> [/main.py line 299](main.py#L299)
> ```python
> # change db.select_db(db = 'Muxic') to
> db.select_db(db='databasename')
> ```
> see detail in [db_support.py](db_support.py#L44)

## 4. Launch
just execute the [main.py](main.py)  
then go to [127.0.0.1:5000/]()

---
# Database Structure
[![](https://i.imgur.com/kyxrnQ0.jpg)](/SQL/DDL.sql)  
link 指的是 youtube 影片連結後的那一段  
/watch?v=這邊

# ![](https://www.zwicon.com/img/icons/svg/development/deploy.svg) Feature
1. 音樂播畢會自動切換下一首，並且更新播放清單列
2. 乾淨簡潔的介面，而且旁邊都有小圖示
3. 功能簡單而完整，操作直覺
4. 有小彩蛋 feat. 嘎啦嘎拉

## Special Technique
- ### 自動影片連續播放
> 1. 使用 YouTube API，接收到"播放結束"的 event 後，post 到網址 '/play_next_song/'，告訴 server 要跳下一首了，並且要求下一個連結 (直接跟 server 拿 避免播放清單有更新，拿到錯的資料)
> 2. 拿到之後刪掉舊影片的 div，重新生成一個用來放新影片；再向伺服器要求目前最新的播放清單列表('/small_playlist/')，更新到表格中。
- ### 將許多相同的 html 區塊包成 macro