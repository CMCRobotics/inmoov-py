from setuptools import setup, find_packages

setup(
      install_requires=['distribute', 'adafruit-pca9685>=1.0.0'],
      name = '${PROJECT_NAME}',
      description = 'InMoov python API',
      author = 'CERN MicroClub',
      url = 'https://github.com/cmcrobotics/inmoov-cmc',
      keywords = ['inmoov'],
      version = '${VERSION}',
      packages =  find_packages('.')
)