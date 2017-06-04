# Python Builds and Pkgs

Testing out Py build pipeline with - `python3`, `pydoc`, Jenkins, PYZ files.

# Install the package

## run `test` and `sdist`

### step 1 - Running tests

```
[jd@jaypc testing_python_build_pkgs]$ python3.6 setup.py test
running nosetests
running egg_info
writing test_build_package_deploy.egg-info/PKG-INFO
writing dependency_links to test_build_package_deploy.egg-info/dependency_links.txt
writing entry points to test_build_package_deploy.egg-info/entry_points.txt
writing requirements to test_build_package_deploy.egg-info/requires.txt
writing top-level names to test_build_package_deploy.egg-info/top_level.txt
reading manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
nose.config: INFO: Set working dir to /home/jd/PycharmProjects/testing_python_build_pkgs
nose.config: INFO: Ignoring files matching ['^\\.', '^_', '^setup\\.py$']
nose.plugins.cover: INFO: Coverage report will include only packages: ['myapp.worker_lib']
test_positive_addition_np (tests.test_myapp.TestWorkerLib) ... ok
test_positive_addition_pn (tests.test_myapp.TestWorkerLib) ... ok
test_positive_addition_pp (tests.test_myapp.TestWorkerLib) ... ok
test_positive_assition_nn (tests.test_myapp.TestWorkerLib) ... ok
test_selfintro (tests.test_myapp.TestWorkerLib) ... ok

Name                  Stmts   Miss  Cover
-----------------------------------------
myapp/worker_lib.py       8      0   100%
----------------------------------------------------------------------
Ran 5 tests in 0.011s

OK

```

### step 2 - `sdist` build.

```
[jd@jaypc testing_python_build_pkgs]$ python3.6 setup.py sdist
running sdist
running egg_info
writing test_build_package_deploy.egg-info/PKG-INFO
writing dependency_links to test_build_package_deploy.egg-info/dependency_links.txt
writing entry points to test_build_package_deploy.egg-info/entry_points.txt
writing requirements to test_build_package_deploy.egg-info/requires.txt
writing top-level names to test_build_package_deploy.egg-info/top_level.txt
reading manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt

running check
creating test-build-package-deploy-1.0.1
creating test-build-package-deploy-1.0.1/data
creating test-build-package-deploy-1.0.1/myapp
creating test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying files to test-build-package-deploy-1.0.1...
copying LICENSE.md -> test-build-package-deploy-1.0.1
copying MANIFEST.in -> test-build-package-deploy-1.0.1
copying setup.cfg -> test-build-package-deploy-1.0.1
copying setup.py -> test-build-package-deploy-1.0.1
copying data/sample1.dat -> test-build-package-deploy-1.0.1/data
copying myapp/__init__.py -> test-build-package-deploy-1.0.1/myapp
copying myapp/__main__.py -> test-build-package-deploy-1.0.1/myapp
copying myapp/worker_lib.py -> test-build-package-deploy-1.0.1/myapp
copying test_build_package_deploy.egg-info/PKG-INFO -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying test_build_package_deploy.egg-info/SOURCES.txt -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying test_build_package_deploy.egg-info/dependency_links.txt -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying test_build_package_deploy.egg-info/entry_points.txt -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying test_build_package_deploy.egg-info/requires.txt -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
copying test_build_package_deploy.egg-info/top_level.txt -> test-build-package-deploy-1.0.1/test_build_package_deploy.egg-info
Writing test-build-package-deploy-1.0.1/setup.cfg
Creating tar archive
removing 'test-build-package-deploy-1.0.1' (and everything under it)

```

## step 3 - Installing via `pip3.6`

```
[jd@jaypc testing_python_build_pkgs]$ sudo `which python3.6` -m pip install --upgrade dist/test-build-package-deploy-1.0.1.tar.gz
Processing ./dist/test-build-package-deploy-1.0.1.tar.gz
Installing collected packages: test-build-package-deploy
  Found existing installation: test-build-package-deploy 1.0.1
    Uninstalling test-build-package-deploy-1.0.1:
      Successfully uninstalled test-build-package-deploy-1.0.1
  Running setup.py install for test-build-package-deploy ... done
Successfully installed test-build-package-deploy-1.0.1

```

## step 4 - Sample run of `myapp`

```
[jd@jaypc testing_python_build_pkgs]$ myapp
Worker AdditionWorker :: Result 15
```

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
