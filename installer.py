import pyderman as driver
from platform import system

print(f"Your system: {system()}")

path = driver.install(file_directory='chromedriver', verbose=True, chmod=True, overwrite=False, version=None)
print('Installed chromedriver to path: %s' % path)