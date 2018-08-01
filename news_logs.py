#! /usr/bin/env python

import psycopg2


def connect():
    """ Connects to the database """
    dbName = "news"
    return psycopg2.connect("dbname=" + dbName)


def get_popular_articles():
    """ Solves the question #1:
    What are the most popular three articles of all time? """

    print ('1. What are the most popular three articles of all time?')
    query = "SELECT title, views FROM articles_view LIMIT 3"
    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(len(result)):
        title = result[i][0]
        views = result[i][1]
        print ('\t- \"' + str(title) + '\" -- ' + str(views) + ' views')
    db.close()


def get_popular_authors():
    """ Solves the question #2:
    Who are the most popular article authors of all time? """

    print ('\n2. Who are the most popular article authors of all time?')
    query = "SELECT * FROM authors_view"
    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(len(result)):
        author = result[i][0]
        total_views = result[i][1]
        print ('\t- \"' + str(author) + '\" -- ' + str(total_views) + ' views')
    db.close()


def get_error_percentage():
    """ Solves the question #3:
    On which days did more than 1% of requests lead to errors? """

    print ('\n3. On which days did more than 1% of requests lead to errors?')
    query = """ SELECT to_char(total_requests.date, 'fmMonth DD, YYYY') AS date,
round((100.0 * error_requests.count) /
total_requests.count, 2) AS error_percentage
FROM error_requests, total_requests
WHERE error_requests.date = total_requests.date
AND round((100.0 * error_requests.count) / total_requests.count, 2) > 1.0;
    """

    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(len(result)):
        date = result[i][0]
        error_percentage = result[i][1]
        print ('\t- ' + str(date) + ' -- ' + str(error_percentage) + '%')
    db.close()

get_popular_articles()
get_popular_authors()
get_error_percentage()
