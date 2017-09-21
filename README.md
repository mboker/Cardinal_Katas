This solution is written in python, and requires a python3 installation with Pandas and Numpy.    
To install python3, go to www.python.org/downloads/ and click the 'Download Python 3.X.X'.   
   
Once python3 is installed, make sure to upgrade pip using the following:  
    * On Linux/MacOS :
         * pip install -U pip setuptools
    * On Windows :
        * python -m pip install -U pip setuptools 
  
When pip is upgraded, you will need to use it to install Pandas with the following command  
    * pip install pandas  
  
(Note, if you have a 2.X installation of python on your machine, you may want to create a  
 virtual environment to run my solutions, as they require python3.  You can accomplish this  
 with virtualenv or anaconda.  Virtualenv allows you to create virtual environments for   
 different versions of python with different libraries installed.  
 Anaconda is a data science package that has a large selection of libraries in it, and therefore is somewhat heavy.   
 You  will need to search for 'python3 virtualenv' or 'anacondas python3' for instructions on how to accomplish this.)  
  
Once you have pandas installed, you are ready to run my solutions (numpy is installed as a dependency of pandas, so   
 no need to do anything for that).
  
In the root directory, enter the following commands to run my kata one solution, kata one unit test, and kata two solution.  
    * python kata_one.py  
    * python kata_one_tests.py  
    * python kata_two.py  

Now, cd into the kata_three directory, and enter the following commands to run my refactored solutions and my shared code unit tests.  
    * python weather_solution.py  
    * python football_solution.py  
    * python shared_tests.py  
  
That's it! 
