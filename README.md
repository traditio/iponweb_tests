Algorithm test
==============

This task is supposed to test your algorithm implementation abilities. What you need to do is to implement an algorithm for searching shortest path length in weighted graph (aka Dijkstra) in nlog(n) time.

In attachment, you can find a simple file to start with (`graph_path.py`) that reads data from stdin and launches the path length search function for nodes 1 to 7, and file with graph data (`path_data.csv`) that contains graph edges in format of node1,node2,edge_weight and a comment of what's the shortest path and its length are. You don't have to use these, meaning you're free to write it the way you want - however these two might help you avoiding unnecessary routine.

Some hints on the task:

* you need to find the shortest path length only, no need to implement the output of path itself
* you might want to use Python's heapq module as a heap implementation to save time, that's OK
* however you still need to write the path length code yourself, i.e. no modules allowed on this part


Bash scripting test
===================

This one is to briefly test your bash scripting skills. Please write a set of commands that would perform following procedure:

* find files in some directory, but not deeper than 2 directories
* files should be recent, changed 2 days ago max
* for each file, do an in-place change, adding tab to the end of every line
* print file size before and after the tab addition


Django test
===========

This test is to validate your skills in using Django framework. It's mocking the (hypothetical) real estate agency to let you improve and enhance the functionality of Django-based web site.

Please submit the files you have changed, or a diff of changes - no need to send the whole project back.

Introduction
------------

Real estate agency has developed a tiny application to simplify storing information about selling houses and automatically assign one of agent to process every deal.

You are the second developer of this application and should improve it by adding new functions and fixing mistakes made by your predecessor.

Please don't pay too much attention to beauty of HTML and whole UI, this is more Django usage validation.

If some part of this task consumes too much time but you feel like you know how to solve it, please write a few sentences about the ways you could have (given enough time) used to solve it. And why those ways in particular.

Part 0 - Installation
---------------------

Main application called "realtdb". You should connect it to the project before starting work on the other tasks.

Useful info:

* Project already configured to use SQLite as main database engine.
* When you finish connecting of "realtdb" you should create database and install initial data set by using command `manage.py loaddata realtor houses`.

Now please run the project in development mode by using `runserver`.

Part 1 - Validation of the user's input
---------------------------------------

Find a start URL to open application in a browser (and open it). You will see a simple interface containing a list of all available houses with a form to add more.

Now this form does not perform validation of input data. For instance, try adding new house using this form but with a string instead of number for a "price" field. You should implement validation of input data in a way that is natural for Django. Users should be able to see what is wrong with their data (meaning, there should be some feedback messages).

Part 2 - Analyzing queries
--------------------------

Press button "Show SQL" in the footer of the page. You will see the list of all SQL queries performed during loading the page.
Are all of those queries are necessary? Please try reducing their number, if you see a way for that.

Part 3 - Extension
------------------

Your agency now starts to sell apartments. And you need to make additional page to manage them. Take a look at top navigation bar - there you can find already prepared "Apartments" link.

Apartments page is pretty similar to houses but contains three additional fields:

* number of rooms in apartment
* floor number
* total number of floors in the apartment's building

You should make a separate page for adding apartments, similarly to houses. Please keep in mind that eventually future you might need to deal with other kinds of the real estate like rooms, offices etc.

Also, please, ensure that user is not able to enter number of floor greater than total number of floors in building.