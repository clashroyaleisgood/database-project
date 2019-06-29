# Database Project
[![](https://img.shields.io/badge/MySQL-yellow.svg)](https://www.mysql.com/)
[![](https://img.shields.io/badge/AppServ-lightgrey.svg)](https://www.appserv.org/en/)
[![](https://img.shields.io/badge/Python-PyMySQL-blue.svg)](https://pymysql.readthedocs.io/en/latest/)
[![](https://img.shields.io/badge/Python-Flask-blue.svg)](http://flask.pocoo.org/)
![](https://img.shields.io/badge/front_end-Bootstrap%20%7C%20jQuery-blueviolet.svg)
[![](https://img.shields.io/badge/YouTube_API-red.svg)](https://developers.google.com/youtube/iframe_api_reference)  
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
[/main.py line 298](main.py#L298)
```python
    # change db.connect() to
    db.connect(host="localhost", user="root", passwd="your pass word")
```
see detail in [db_support.py](db_support.py#L38)  

[/main.py line 299](main.py#L299)
```python
    # change db.select_db(db = 'Muxic') to
    db.select_db(db='databasename')
```
see detail in [db_support.py](db_support.py#L44)

## 4. Launch
just execute the [main.py](main.py)  
then go to [127.0.0.1:5000/](127.0.0.1:5000/)

---
# 資料庫架構
[![](https://i.imgur.com/kyxrnQ0.jpg)](/SQL/DDL.sql)
link 指的是 youtube 影片連結後的那一段  
/watch?v=這邊
