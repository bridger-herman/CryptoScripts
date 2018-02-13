import sys
DB = 'debug' in sys.argv
dbprint = print if DB else lambda *args, **kwargs: None
