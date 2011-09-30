# -*- coding: utf-8 -*-
# Copyright (c) 2011 Ionuț Arțăriși <iartarisi@suse.cz>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from urllib import quote_plus

from popcorn.configs import rdb

class Vendor(object):
    """A vendor is the provider of a repository.

    It is identified by a quoted url of the target repository.  The key
    'global:nextVendorId' is incremented to generate a new id which is
    stored in 'vendor:%(url)s'. All the ids are stored in the set
    'vendors'.

    The key 'vendor:%(vendor)s:packages' holds a set of all the package
    ids belonging to this vendor.

    """
    @classmethod
    def get_all_ids(cls):
        """Return a set of all the vendor ids we currently have"""
        return rdb.smembers('vendors')

    def __init__(self, url):
        """
        Retrieves or creates a Vendor object.

        :url: the url string of this Vendor

        """
        self.url = url
        self.key = quote_plus(url)
        try:
            self.id = rdb['vendor:%s' % self.key]
        except KeyError:
            self.id = str(rdb.incr('global:nextVendorId'))
            rdb.set('vendor:%s' % self.key, self.id)
            rdb.sadd('vendors', self.id)

    def __repr__(self):
        return self.id
