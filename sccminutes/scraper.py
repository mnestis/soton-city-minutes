
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import html
import re
import requests
import time

SCC_BASE = "http://www.southampton.gov.uk/modernGov/"

COMMITTEE_LIST_PAGE = SCC_BASE + "ieDocHome.aspx?Year=0"
MEETING_LIST_PAGE = SCC_BASE + "ieListMeetings.aspx?Year=0&CId={}"
MINUTES_PAGE = SCC_BASE + "ieListDocuments.aspx?CId={}&MId={}&Ver={}"

DOS_DELAY = 0.5


class CouncilHttpError(Exception):
    pass


def _fetch_list_of_committees():
    list_page = requests.get(COMMITTEE_LIST_PAGE)
    time.sleep(DOS_DELAY)

    if list_page.status_code != 200:  # pragma: no cover
        raise CouncilHttpError("Unable to load the committee list page.")

    committee_re = re.compile("ieListMeetings\.aspx\?CId=(\d+).*>(.*)</a>")

    committees = committee_re.findall(list_page.text)

    committees = [(int(comm_id), html.unescape(comm_name))
                  for comm_id, comm_name
                  in committees]

    return committees


def _fetch_list_of_meetings(committee_id):
    list_page = requests.get(MEETING_LIST_PAGE.format(committee_id))
    time.sleep(DOS_DELAY)

    if list_page.status_code != 200:  # pragma: no cover
        raise CouncilHttpError("Unable to load the meeting list page.")

    meeting_re = re.compile("ieListDocuments\.aspx\?" +
                            "CId=(\d+)&amp;" +
                            "MId=(\d+)&amp;" +
                            "Ver=(\d+).*>" +
                            "(.*)</a>")

    meetings = meeting_re.findall(list_page.text)

    meetings = [(int(comm_id),
                 int(meet_id),
                 int(ver),
                 html.unescape(meet_time))
                for comm_id, meet_id, ver, meet_time
                in meetings]

    return meetings
