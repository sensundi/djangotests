# djangotests
Create test data and django unit tests to query user data based on location

Dependencies - Python2.7, Django 1.8.0, GeoPy, sqlite, spatialite

Download - Download or clone the source and extract to your location if you have downloaded zip file.

Pre-requisites - Setup environment variable "LD_LIBRARY_PATH" based on your Operating System
You can use export LD_LIBRARY_PATH=nextdoor.settings
(or)
setenv LD_LIBRARY_PATH=nextdoor.settings

Running Tests - 
     cd nextdoor
    >> python manage.py test queryuser.tests

Note - Tests does not use the production database. 
The default database has been modified in nextdoor/settings.py as below.
TEST:{ "NAME": os.path.join(BASE_DIR, 'test_nextdoor.sqlite3'),}

To prevent the test database being deleted after execution, specify  the '--keepdb' option in CLI. like
~/djangotests/nextdoor> python manage.py test --keepdb queryuser.tests.UserTestcase
