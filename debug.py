import sys
DB = 'debug' in sys.argv
print(sys.argv)
sys.argv = list(filter(lambda a: a != 'debug', sys.argv))
print(sys.argv)
dbprint = print if DB else lambda *args, **kwargs: None
