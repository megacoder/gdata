
"""Cryptographic protocols

Implements various cryptographic protocols.  (Don't expect to find
network protocols here.)

Crypto.Protocol.AllOrNothing   Transforms a message into a set of message
                               blocks, such that the blocks can be
                               recombined to get the message back.

Crypto.Protocol.Chaffing       Takes a set of authenticated message blocks
                               (the wheat) and adds a number of
                               randomly generated blocks (the chaff).
"""

__all__ = ['AllOrNothing', 'Chaffing']
__revision__ = "$Id: __init__.py,v 1.1.1.1 2010/06/13 06:31:09 reynolds Exp $"
