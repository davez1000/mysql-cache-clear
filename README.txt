Quick and dirty tiny python script for removing drupal insert cache lines from mysqldump file

========================================================================================

usage:

$ python remcache.py mysqldumpfile.sql

Creates a new file called 'output.sql' with all INSERT INTO `cache ...etc lines removed.
