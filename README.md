# "Logs Analysis" - Reporting Tool

This project aims to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. It will run from the command line (it won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions. This project was done as a part of the Full Stack Web Developer Nanodegree on [Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### The report analysis should answer these three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project Setup

To set up the environment for the project:
1. You must download [Python](https://www.python.org/downloads). It's supported for Windows, Linux/UNIX, Mac OS X, and other operating systems.
2. Download and install [Vagrant](https://www.vagrantup.com/).
3. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
4. Download the newsdata.sql file.

Once your environment is ready, you can download the project ZIP file or clone it to your local machine by clicking on the green "Clone or download" button on the upper right side of the page
`or`
clone it to your local machine using Git's command line
```
git clone https://github.com/dalia-maher/Logs-Analysis
```

## To run this project

1. Open the unzipped / cloned directory of the repo in your local machine
2. Launch the Vagrant VM inside Vagrant sub-directory in the repository using command: 
  ```
    $ vagrant up
  ```
3. Then log in using this command:
  ```
    $ vagrant ssh
  ```
4. Change directory to /vagrant.
5. Setup the database by running:
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  You can explore the tables using the `\dt` (to display the tables) and `\d table` (to show the database schema for a particular table) commands and select statements.
6. Use `psql -d news` to connect to database.
7. Create the views in the database which are:

### articles_view:
```SQL
CREATE VIEW articles_view AS
SELECT title, author, count(*) AS views
FROM articles, log
WHERE log.path like concat('/article/', articles.slug)
GROUP BY title, author
ORDER BY views DESC;
```

### authors_view:
```SQL
CREATE VIEW authors_view AS
SELECT name, sum(articles_view.views) AS total_views
FROM articles_view, authors
WHERE articles_view.author = authors.id
GROUP BY authors.name
ORDER BY total_views DESC;
```

### total_requests:
```SQL
CREATE VIEW total_requests AS
SELECT date(time) AS date, count(*) AS count
FROM log
GROUP BY date
ORDER BY date;
```

### error_requests:
```SQL
CREATE VIEW error_requests AS
SELECT date(time) AS date, count(*) AS count
FROM log where status != '200 OK'
GROUP BY date
ORDER BY date;
```
8. Once views are successfully created, press CTRL + D to exit.
9. Run the python module in the terminal
  ```
    python news_logs.py
  ```
`or`
run the output to a file using:
  ```
python news_logs.py > output.txt
  ```
`or`
run the output to both file and terminal using:
  ```
python news_logs.py | tee output.txt
  ```

  
