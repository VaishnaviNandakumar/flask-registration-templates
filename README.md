## Flask Login-Registration Templates 
Customizable login and registration templates made with Flask that offers a choice of DB to be used between MySQL and MongoDB.

### Templates Available

![Template1](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template1.gif)
![Template2](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template2.gif)
![Template3](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template3.gif)


### To Use
Set up a virtual environment and install dependencies
```
pip install -r requirements.txt
```

#### Initial Setup
For SQL database, create a table in MySQL and add required information in the .env file. A sample file is given for reference. It can be initally set up like the following.
```
cd sql
python app.py --t template1 --u root --p samplepw --h localhost --db tablename --s skey
```

For a NoSQL database, intialize the .env file with the requried information.
```
cd mongo
python app.py --t template1 --c connection_string --s sskey
```

Once the .env file is set, the application can be run by going to the required directory.
```
python app.py
```
