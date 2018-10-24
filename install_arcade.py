from pip._internal import main

def install(package):
    main(['install', package])

if __name__ == '__main__':
    install('arcade')