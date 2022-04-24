# Fast and easy connection checker
Useful for monitoring the status of a large number of sites

## Usage
-u or --urls allows you to provide one or more target URLs at the comment line.

`python -m conn_checker -u python.org pypi.org peps.python.org`

-f or --input-file allows you to supply a file containing a list of URLs to check.

`python -m conn_checker -f urllist.txt`


`-a` or `--asynchronous` allows you to run the connectivity checks asynchronously.

`python -m conn_checker -u python.org pypi.org peps.python.org -a`

You can write logs to the file

`python -m conn_checker -u python.org pypi.org peps.python.orgd -lf 'mylogs.log'`


## Status
There are plans to expand the logic:
- checking phrases from blacklist.txt (Access denied, not available, hosting not paid, not available in your country)
since the resource can return 200 response code, but be blocked, or not actually working.
- To upload in json format at the end of the work
- Using a proxy to check availability in different countries




This script is made according to the tutorial https://realpython.com/site-connectivity-checker-python/
