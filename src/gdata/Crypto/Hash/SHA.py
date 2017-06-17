
# Just use the SHA module from the Python standard library

__revision__ = "$Id: SHA.py,v 1.1.1.1 2010/06/13 06:31:09 reynolds Exp $"

from sha import *
import sha
if hasattr(sha, 'digestsize'):
    digest_size = digestsize
    del digestsize
del sha
