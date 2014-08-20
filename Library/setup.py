import os
import sys
import platform
import fnmatch
import shutil
import subprocess
from distutils.core import setup, Extension
from distutils.command.install import install as _install

os.environ['CC'] = 'g++'

extn_name = 'pyauthcode'
pyauthcode = Extension(extn_name,
                       include_dirs = ['./lib/cryptopp'],
                       library_dirs = ['./lib/cryptopp'],
                       libraries = ['cryptopp'],
                       sources = [os.path.join('lib', extn_name + '.cpp')])

def find_file(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def build_cryptopp():
    if os.name == 'posix':
        libs = find_file('libcrypto*.*', './lib/cryptopp')
        if len(libs) == 0:
            r = subprocess.call(['make', '-C', './lib/cryptopp', 'static'])
            if r != 0:
                raise RuntimeError('Failed to build cryptopp library.')
        else:
            print('Reusing the prebuilt cryptopp libraries: %s.' % (str(libs)))
    else:
        print('Cryptopp shared library and headers are required for building the extension.')

build_cryptopp()

def _post_install(dir):
    if os.name == 'posix':
        pver = platform.python_version_tuple()
        pver = '%s.%s' % (pver[0], pver[1],)
        so_path = 'lib.%s-%s-%s' % (platform.system().lower(), 
                                    platform.machine().lower(),
                                    pver,)
        so_path = os.path.join('build', so_path)
        so_file = find_file(extn_name + '*.so', so_path)
        if so_file == []: raise Exception('Failed to find shared library in ' + so_path)
        so_file = so_file[0]
        target = os.path.join(sys.exec_prefix, 'lib', extn_name + '.so')
        print ('Copying ' + so_file + ' to ' + target)
        shutil.copyfile(so_file, target)
        
class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg = 'Running post install task ...')

setup(
    name='Learning Studio API',
    version='0.1dev',
    packages=['learningstudio', 
              'learningstudio.test',
              'learningstudio.oauth', 
              'learningstudio.oauth.test', 
              'learningstudio.core', 
              'learningstudio.core.test', 
              'learningstudio.exams',
              'learningstudio.exams.test', 
              'learningstudio.grades', 
              'learningstudio.grades.test', 
              'learningstudio.content',
              'learningstudio.content.test'],
    ext_modules=[pyauthcode],
    long_description=open('README.md').read(),
    cmdclass={'install': install}
)
