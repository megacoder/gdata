
# Just use the MD5 module from the Python standard library

__revision__ = "$Id: MD5.py,v 1.1.1.1 2010/06/13 06:31:09 reynolds Exp $"

from md5 import *

import md5
if hasattr(md5, 'digestsize'):
    digest_size = digestsize
    del digestsize
del md5

