from setuptools import setup
setup(name='autogit',
      description='autosave using git',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords='git autosave',
      url='https://github.com/youngrok/autogit',
      version='0.0.3',
      package_dir={'':'.'},
      scripts=['bin/autogit'],
      classifiers = [
                     'Development Status :: 3 - Alpha',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'Topic :: Software Development :: Version Control',
                     'License :: OSI Approved :: BSD License']
      
      )
