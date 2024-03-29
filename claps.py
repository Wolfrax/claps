#!/usr/bin/python

import os
import requests
from flask import Flask, render_template


__author__ = 'Wolfrax'

app = Flask(__name__)

# traverse root directory, and list directories as dirs and files as files
father_root = "/home/pi/app/wlog/"
http_root = "wlog.viltstigen.se/"


@app.route("/claps")
def get_claps():
    #  Note, applause-button api allows maximum 100 items in once call to get-multiple
    pages = []
    data = [http_root]
    #  data = ["google.com"] * 101  # For testing
    for root, dirs, files in os.walk(father_root + "articles"):
        if not dirs:
            if len(data) < 100:
                data.append(str(http_root + root[len(father_root):] + "/"))
            else:
                pages.append(data)
                data = [str(http_root + root[len(father_root):] + "/")]
    if data:
        pages.append(data)

    res = []
    if pages:
        for item in pages:
            r = requests.post('https://api.applause-button.com/get-multiple', json=item)
            if r.status_code == requests.codes.ok:
                res += r.json()

    result = []
    no_claps = 0
    for item in res:
        url = item['url'].split("/")[-2] if "/" in item['url'] else item['url']
        result.append({'url': url, 'claps': item['claps']})
        no_claps += int(item['claps'])

    result = sorted(result, key=lambda i: i['claps'])
    result.append({'url': 'Total', 'claps': str(no_claps)})
    return render_template("claps.html", result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
