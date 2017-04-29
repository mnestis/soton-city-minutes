
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import requests
import re

SCC_BASE = "http://www.southampton.gov.uk/modernGov/"

COMMITTEE_LIST_PAGE = SCC_BASE + "ieDocHome.aspx?Year=0"
MEETING_LIST_PAGE = SCC_BASE + "ieListMeetings.aspx?Year=0&CId={}"
MINUTES_PAGE = SCC_BASE + "ieListDocuments.aspx?CId={}&MId={}&Ver={}"


class CouncilHttpError(Exception):
    pass


def _fetch_list_of_committees():
    list_page = requests.get(COMMITTEE_LIST_PAGE)

    if list_page.status_code != 200:
        raise CouncilHttpError("Unable to load the committee list page.")

    committee_re = re.compile("ieListMeetings\.aspx\?CId=(\d+).*>(.*)</a>")

    committees = committee_re.findall(list_page.text)

    for comm_id, comm_name in committees:
        print("{}: {}".format(comm_id, comm_name))
