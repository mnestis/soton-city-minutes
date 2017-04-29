from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from .scraper import _fetch_list_of_committees


def run_incremental_update():
    _fetch_list_of_committees()
    print("This is working.")
