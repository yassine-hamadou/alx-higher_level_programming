# 0x0D. SQL - Introduction

## concepts

Reading through the documentation and working on the tasks i was able to understand


    What a database is
    What a relational database is
    What SQL stand for
    What MySQL is
    How to create a database in MySQL
    What DDL and DML stand for
    How to CREATE or ALTER a table
    How to SELECT data from a table
    How to INSERT, UPDATE or DELETE data
    What subqueries are
    How to use MySQL functions


## Table of content

| Task     | Description          |
| -------- | -------------- |
| [0-list_databases.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/fb0e380425c59d8ca787ce96b297cea2167a69cb/0x0D-SQL_introduction/0-list_databases.sql) | script that lists all databases of your MySQL server |
| [1-create_database_if_missing.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/fb0e380425c59d8ca787ce96b297cea2167a69cb/0x0D-SQL_introduction/1-create_database_if_missing.sql) | script that creates the database hbtn_0c_0 in your MySQL server |
| [2-remove_database.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/2-remove_database.sql) | script that deletes the database hbtn_0c_0 in your MySQL server |
| [3-list_tables.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/3-list_tables.sql) | script that lists all the tables of a database in your MySQL server |
| [4-first_table.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/4-first_table.sql) | script that creates a table called first_table in the current database in your MySQL server |
| [5-full_table.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/5-full_table.sql) | script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server |
| [6-list_values.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/6-list_values.sql) | script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server |
| [7-insert_value.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/7-insert_value.sql) | script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server |
| [8-count_89.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/8-count_89.sql) | a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server |
| [9-full_creation.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/9-full_creation.sql) | a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows |
| [10-top_score.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/10-top_score.sql) | script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server |
| [11-best_score.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/11-best_score.sql) | a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server |
| [12-no_cheating.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/12-no_cheating.sql) | script that updates the score of Bob to 10 in the table second_table |
| [13-change_class.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/13-change_class.sql) | script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server |
| [14-average.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/14-average.sql) | a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server |
| [15-groups.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/15-groups.sql) | a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server |
| [16-no_link.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/16-no_link.sql) | script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server |
| [100-move_to_utf8.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/100-move_to_utf8.sql) | script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server. |
| [101-avg_temperatures.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/101-avg_temperatures.sql) | a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending) |
| [102-top_city.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/102-top_city.sql) | a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending) |
| [103-max_state.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/309bde136a648ab290e13980795f13a78f67f201/0x0D-SQL_introduction/103-max_state.sql) | a script that displays the max temperature of each state (ordered by State name) |
