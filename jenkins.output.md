# Jenkins Build Output

After integration with jenkins and build

```
Started by user Jay Dihenkar
Building in workspace /var/jenkins_home/workspace/myapp
 > git rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/jkdihenkar/testing_python_build_pkgs.git # timeout=10
Fetching upstream changes from https://github.com/jkdihenkar/testing_python_build_pkgs.git
 > git --version # timeout=10
 > git fetch --tags --progress https://github.com/jkdihenkar/testing_python_build_pkgs.git +refs/heads/*:refs/remotes/origin/*
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
 > git rev-parse refs/remotes/origin/origin/master^{commit} # timeout=10
Checking out Revision a3e7065cef0ba2a03098891cfc9163d245539d29 (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f a3e7065cef0ba2a03098891cfc9163d245539d29
 > git rev-list 9ac6113f117e7a6fc9e0fa9ba79b127fcd30513f # timeout=10
[myapp] $ /bin/sh -xe /tmp/hudson6884362362019133040.sh
+ python3 setup.py test
running nosetests
running egg_info
writing top-level names to test_build_package_deploy.egg-info/top_level.txt
writing dependency_links to test_build_package_deploy.egg-info/dependency_links.txt
writing test_build_package_deploy.egg-info/PKG-INFO
writing requirements to test_build_package_deploy.egg-info/requires.txt
writing entry points to test_build_package_deploy.egg-info/entry_points.txt
reading manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'test_build_package_deploy.egg-info/SOURCES.txt'
nose.config: INFO: Set working dir to /var/jenkins_home/workspace/myapp
nose.config: INFO: Ignoring files matching ['^\\.', '^_', '^setup\\.py$']
nose.plugins.cover: INFO: Coverage report will include only packages: ['myapp.worker_lib']
test_positive_addition_np (tests.test_myapp.TestWorkerLib) ... ok
test_positive_addition_pn (tests.test_myapp.TestWorkerLib) ... ok
test_positive_addition_pp (tests.test_myapp.TestWorkerLib) ... ok
test_positive_assition_nn (tests.test_myapp.TestWorkerLib) ... ok
test_selfintro (tests.test_myapp.TestWorkerLib) ... ok

----------------------------------------------------------------------
XML: /var/jenkins_home/workspace/myapp/nosetests.xml
Name                  Stmts   Miss  Cover
-----------------------------------------
myapp/worker_lib.py       8      0   100%
----------------------------------------------------------------------
Ran 5 tests in 0.013s

OK
[myapp] $ /bin/sh -xe /tmp/hudson4049419086989407509.sh
+ python3 setup.py sdist
running sdist
running egg_info
writing top-level names to test_build_package_deploy.egg-info/top_level.txt
writing dependency_links to test_build_package_deploy.egg-info/dependency_links.txt
writing test_build_package_deploy.egg-info/PKG-INFO
writing entry points to test_build_package_deploy.egg-info/entry_points.txt
writing requirements to test_build_package_deploy.egg-info/requires.txt
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
[myapp] $ /bin/sh -xe /tmp/hudson6536868945159965695.sh
+ python3 -m pylint -f parseable myapp
+ tee pylint.out
No config file found, using default configuration
************* Module myapp.worker_lib
myapp/worker_lib.py:20: [C0326(bad-whitespace), ] Exactly one space required after comma
    def do_addition(self, a,b):
                           ^
myapp/worker_lib.py:28: [C0304(missing-final-newline), ] Final newline missing
myapp/worker_lib.py:20: [C0103(invalid-name), Worker.do_addition] Invalid argument name "a"
myapp/worker_lib.py:20: [C0103(invalid-name), Worker.do_addition] Invalid argument name "b"
myapp/worker_lib.py:27: [W0201(attribute-defined-outside-init), Worker.do_addition] Attribute 'last_result' defined outside __init__
************* Module myapp.__main__
myapp/__main__.py:9: [C0304(missing-final-newline), ] Final newline missing
myapp/__main__.py:1: [C0111(missing-docstring), ] Missing module docstring
myapp/__main__.py:4: [C0111(missing-docstring), main] Missing function docstring
myapp/__main__.py:5: [C0103(invalid-name), main] Invalid variable name "w"

------------------------------------------------------------------
Your code has been rated at 3.57/10 (previous run: 3.57/10, +0.00)

[xUnit] [INFO] - Starting to record.
[xUnit] [INFO] - Processing JUnit
[xUnit] [INFO] - [JUnit] - 1 test report file(s) were found with the pattern 'nosetests.xml' relative to '/var/jenkins_home/workspace/myapp' for the testing framework 'JUnit'.
[xUnit] [INFO] - Check 'Failed Tests' threshold.
[xUnit] [INFO] - Check 'Skipped Tests' threshold.
[xUnit] [INFO] - Setting the build status to SUCCESS
[xUnit] [INFO] - Stopping recording.
Finished: SUCCESS
```