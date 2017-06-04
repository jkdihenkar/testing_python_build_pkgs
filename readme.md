# Python Builds and Pkgs

Testing out Py build pipeline with - `python3`, `pydoc`, Jenkins, PYZ files.

# pydoc

`worker_lib` pydoc:

```
[jd@jaypc testing_python_build_pkgs]$ pydoc ./worker_lib.py
Help on module worker_lib:

NAME
    worker_lib - Defining a simple worker that does something

FILE
    /home/jd/PycharmProjects/testing_python_build_pkgs/worker_lib.py

CLASSES
    __builtin__.object
        Worker
    
    class Worker(__builtin__.object)
     |  A class that works! Others are lazy :P
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name)
     |  
     |  do_addition(self, a, b)
     |      Does simple addition
     |      :param a: expected numeric value a
     |      :param b: expected numeric value b
     |      :return: returns math added values
     |  
     |  whoami(self)
     |      My name is ....
     |      :return: name of worker
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)


```

# nosetests

Running nosetests (Ref: http://nose.readthedocs.io/en/latest/testing.html)

```
[jd@jaypc testing_python_build_pkgs]$ nosetests --with-coverage -v
test_positive_addition_np (test_myapp.TestWorkerLib) ... ok
test_positive_addition_pn (test_myapp.TestWorkerLib) ... ok
test_positive_addition_pp (test_myapp.TestWorkerLib) ... ok
test_positive_assition_nn (test_myapp.TestWorkerLib) ... ok
test_selfintro (test_myapp.TestWorkerLib) ... ok

Name            Stmts   Miss  Cover
-----------------------------------
worker_lib.py       8      0   100%
----------------------------------------------------------------------
Ran 5 tests in 0.008s

OK

```