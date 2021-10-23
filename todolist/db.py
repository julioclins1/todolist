#!/usr/bin/env python

#----------------------------------------------------------------------
# db.py
# Authors: Julio Lins
#----------------------------------------------------------------------

from contextlib import closing
from sqlite3 import connect

#----------------------------------------------------------------------

DATABASE_URL = "file:todo.sqlite?mode=rw"

def insert_task(task, author):
    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:

            if not author:
                author = "Anonymous"

            # Get author_id
            cursor.execute("SELECT id FROM authors WHERE author_name = ?", [author])
            result = cursor.fetchone()

            if not result:
                cursor.execute("INSERT INTO authors (author_name) VALUES ( ? )", [author])
                cursor.execute("SELECT id FROM authors WHERE author_name = ?", [author])
                result = cursor.fetchone()

            author_id = int(result[0])

            # Add new task
            cursor.execute("INSERT INTO tasks (content, author_id) VALUES ( ?, ? )",
                            [task, author_id])
            connection.commit()

def get_tasks():
    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT tasks.id, tasks.content, authors.author_name "
                            "FROM tasks, authors "
                            "WHERE tasks.author_id = authors.id")
            rows = cursor.fetchall()
            return rows

def remove_task(task_id):
    task_id = int(task_id)
    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("DELETE FROM tasks WHERE id=?", [task_id])
            connection.commit()

