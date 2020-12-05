## Login-Registration Templates 
Customizable login and registration templates made with Flask that offers a choice of DB to be used between MYSQL and MongoDB.

### Templates Available

![Template1](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template1.gif)
![Template2](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template2.gif)
![Template3](https://github.com/VaishnaviNandakumar/python-flask/blob/main/docs/template3.gif)


### Set Up
Activate
```
.venv\Scripts\activate
```

### To Use
To use the SQL database, set up the XAMPP control panel and create a table.
```
cd sql
python app.py --t template1 --u root --p samplepw --db tablename
```

```
cd mongo
python app.py --t template2
```
