import pandas as pd
from time import gmtime, strftime
from d3blocks import D3Blocks

def convert_time(minute):
    return strftime("%d-%m-%Y %H:%M:%S", gmtime(int(minute)*60))

def get_activity(code):
    code = int(code)
    if code in [101, 102, 199, 201, 202, 299, 301, 302, 399, 401, 402, 405, 499, 502]:
        return "Work"
    if code in [198, 298, 398, 507, 598, 698, 798, 898, 998, 1098, 1198, 1298, 1398, 1498, 1598]:
        return "Travelling"
    if code in [501]:
        return "Sell food"
    if code in [504, 505, 506, 508]:
        return "Provide services"
    if code in [104, 205, 305, 405, 510]:
        return "Looking for jobs"
    if code in [103, 203, 303, 403, 503, 509 ,804]:
        return "Meetings"
    if code in [204, 304, 404, 602]:
        return "Shopping"
    if code in [701, 702]:
        return "Caring"
    if code in [901, 902, 903, 904, 905, 999, 1405]:
        return "Education"
    if code in [1001, 1002, 1003, 1004]:
        return "Socializing and community"
    if code in [1201, 1202, 1203, 1299, 1101, 1102, 1103, 1199]:
        return "Hobbies"
    if code in [1301, 1302, 1309]:
        return "Exercise"
    if code in [1401]:
        return "Reading"
    if code in [1402, 1403]:
        return "TV/Youtube"
    if code in [1404]:
        return "Surf web"
    if code in [1501]:
        return "Sleep"
    if code in [1502]:
        return "Eating"
    if code in [1503]:
        return "Personal hygience"
    if code in [1506]:
        return "Relax"
    else:
        return "Othes"





ds = pd.read_csv("4_diary_main.csv",usecols=["ID", "BEGIN", "Q401"], encoding="latin-1",  converters={"Q401":get_activity, "BEGIN": convert_time})
ds = ds.sort_values(["ID", "BEGIN"])
ds = ds.rename(columns={"ID": "sample_id", "BEGIN": "datetime", "Q401":"state"})
ds = ds.iloc[:int(len(ds)/4)]
d3 = D3Blocks()
d3.movingbubbles(ds, datetime="datetime", sample_id="sample_id", state="state", filepath="./moving_point.html",
                 note="Thời gian biểu của người Việt Nam", cmap="hsv", center="Travelling", figsize=(780, 800), size=2)


