# encoding: utf-8
"""
This module provides compatibility between Python 2 and 3. Hardly
anything is used by this project to constitute including `six`_.

.. _`six`: http://pythonhosted.org/six
"""

import sys

if sys.version_info[0] < 3:
	# Python 2.
	unicode = unicode
	string_types = (basestring,)

	from itertools import izip_longest

	def iterkeys(mapping):
		return mapping.iterkeys()

else:
	# Python 3.
	unicode = str
	string_types = (unicode,)

	from itertools import zip_longest as izip_longest

	def iterkeys(mapping):
		return mapping.keys()

try:
	# Python 3.3+
	import collections.abc as collections_abc
except ImportError:
	# Python 2.6 - 3.2
	import collections as collections_abc
