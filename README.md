# dextra
Python data converter from mysql to csv files. Can be used to extract current mysql data from one database and convert for compatible to import in another database with csv file or to prepare data for DL alghoritms  

### Requirements: 
- pandas - Pandas python package
- mysql-connector - Mysql connector package for python

Use of this scripts is as follows:  
  
`python import.py -h localhost -u root -p root -d test_db -port=3306 users`

Flags are:
- -h: Host, ex. localhost (for local) or any other
- -u: DB username, ex. root
- -p: Password for mysql user
- -d: Database you wanna export
- -port: Port for the database
- users: actual table you want to export


This script will take all the columns from the table and data for those columns and dump it all in csv file