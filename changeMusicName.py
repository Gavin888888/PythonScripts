#coding=utf-8
#!/usr/bin/python
import sqlite3
import os
import os.path
def replace():
    #音乐文件路径
    music_name = os.listdir('/Users/leili/Desktop/Music')
    #连接数据库
    con = sqlite3.connect('/Users/leili/Desktop/cloud.db')
    cur = con.cursor()
    #遍历所有文件
    for temp in music_name:
        print(temp)
        #通过文件名 查询到对应的音乐名
        sql = "select title from musicResource where file = '{}';".format(temp)
        print(sql)
        musics_title = cur.execute(sql)
        new_name = ''
        for temp1 in musics_title:
            new_name = temp1[0]
        old_file_path = '/Users/leili/Desktop/Music/{}'.format(temp)
        new_file_path = '/Users/leili/Desktop/Music/{}.flac'.format(new_name.replace('/', ''))
        print(old_file_path)
        print(new_file_path)
        #替换名字
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
replace()
