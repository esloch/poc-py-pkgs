from setuptools import setup, find_packages

setup(name='esloch',
      version='0.1',
      url='https://github.com/esloch/esloch',
      license='MIT',
      author='@esloch',
      author_email='es.loch@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)