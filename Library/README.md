Python modules for accessing the Pearson LearningStudio REST APIs.

Steps to build and install:

1.    The authentication module has a dependency on the Cryptopp C++ library.
      Package managers of most popular GNU/Linux distributions can install and configure 
      the libcrypto++-dev package. (Versions 5.6.1 and 5.6.2 have been tested).
      Otherwise you may have to build and install the Crypto++ source tarball. 
      (Visit http://www.cryptopp.com for more details).

2.    Issue the command `sudo python setup.py install' from this folder to build and install the modules.
