import os
import requests

from yandex_tracker_client import TrackerClient

file = open("config.txt")
token = file.readline().strip()
org_id = file.readline().strip()

 headers = {
    "Host": "https://api.tracker.yandex.net",
    "Authorization": f"OAuth {token}",
    "X-Cloud-Org-ID": f"{org_id}"
 }

client = TrackerClient(token=token,
                       cloud_org_id=org_id)

queue = client.queues['TEAMCITYBUILDFA']
issues = client.issues.get_all()
last_issue = str(issues[0])
try:
    client.issues.create(queue='TEAMCITYBUILDFA', summary=f"Issue № {last_issue[len(last_issue) - 2]}",
                         type={'name': 'Bug'})
except Exception as ex:
    print("exception:\n", ex)
 data = {
     "queue": "TEAMCITYBUILDFA",
     "summary": f"Issue № {last_issue[len(last_issue) - 2]}",
     "type": "bug",
 }

 //print(issues)
 print(queue)

 try:
    r = requests.post(headers=headers, data=data, url="https://api.tracker.yandex.net/v2/issues/")
     print("Успешно")
 except Exception as ex:
     print("exception", ex)
 r = requests.post(headers=headers, data=data,url="https://api.tracker.yandex.net/v2/issues/")