about this
==========

This is an example to paginate with bottlepy.  To run this,

1. install `bottle` and `bottle_sqlite`
2. run `python db_init.py`
3. run `python bottle_pagination.py`


behavior
========

This runs at `localhost:8080/users/`.  This program shows users in a database
table using pagination.  The number of users per page can be specified with the
query string `per`.  (default is 10.)

e.g.

- http://localhost:8080/users/2
- http://localhost:8080/users/2?per=20

## The points of this example

- Request Routing  
    With dynamic routing, you can paginate from the URL string.  Watch below
    document about Request Routing.
    http://bottlepy.org/docs/dev/routing.html
- Fetching records from specific range  
    Fetch records from specific range using the page number which got from
    dynamic routes, and pass them to the template.
- Head and Tail of pagination  
    In the first and last page, links to paginate should be excluded.  To do
    this, you can use the template's control syntax.
