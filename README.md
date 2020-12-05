## Flask Login-Registration Templates 
Customizable login and registration templates made with Flask that offers a choice of DB to be used between MySQL and MongoDB.

### Templates Available

![Template1](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template1.gif)
![Template2](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template2.gif)
![Template3](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template3.gif)


### To Use

1. Set up a virtual environment and install dependencies
```
pip install -r requirements.txt
```
2. For SQL database, create a table in MySQL and configure the username and password for use.
```
cd sql
python app.py --t template1 --u root --p samplepw --db tablename
```
3. For NoSQL database, add the connection string to userClass.py.
```
cd mongo
python app.py --t template2
```
