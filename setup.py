from setuptools import setup, find_packages

setup (
       name='BitBot',
       version='0.1',
       packages=find_packages(),
       test_suite='tests.bitbot_test',
       # Declare your packages' dependencies here, for eg:
       test_requirements=['tests'],
       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Sofiane Taleb',
       author_email='sofiane.taleb.94@mail.com',

       #summary = 'Just another Python package for the cheese shop',
       url='https://github.com/Neolium/BitBot',
       license='Open Source',
       long_description='Looooooooong description of the package',

       # could also include long_description, download_url, classifiers, etc.
  
       )