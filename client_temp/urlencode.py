# 
# Descr.: 
# Url encode
#
# Exemplo de uso:
# $ python ./script.py "2025-03-21 10:39:39"
# 2025-03-21%2010%3A39%3A39
#
# Autor:
# Jose G. Faisca
#

import urllib.parse, sys 

if len(sys.argv) > 1: 
   print(urllib.parse.quote(sys.argv[1]))
else: 
   sys.stdin.read()[:-1]
