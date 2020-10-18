#!/usr/bin/env python3

import os
import sys
import glob
import json
import base64
import argparse
import requests
from argparse import RawTextHelpFormatter


def get_parkings_info(dir_path):
    records = []

    metas = glob.glob(str(os.path.join(dir_path, '*.meta')))

    limit = len(metas)

    for i, meta_path in enumerate(metas):
        try:
            if i >= limit:
                break

            png_path = meta_path[:meta_path.rfind('.')] + ".png"
        
            with open(png_path, "rb") as f:
                photo = base64.b64encode(f.read())

            print(type(photo))

            meta  = json.loads(open(meta_path, "rb").read())

            print(meta_path)
            print(meta)
            print(len(photo))

            # meta.update({"photo": "string"})
            meta.update({"photo": str(photo)})
            records.append(meta)

        except Exception as e:
            print("Error: ", str(e))

    return records

def send_parkings_info(endpoint, dir_path):
    url = endpoint + "/v1/parkings/save"

    headers = {
        'Content-Type': 'application/json'
    }

    records = get_parkings_info(dir_path)

    for record in records:
        response = requests.request('POST', url, headers=headers, json=record, allow_redirects=False)

        if response.status_code != 200:
            raise Exception("Parkings info wasn't saved")

        if "json" in response.headers.get('content-type'):
            print("Json: %s" % json.dumps(response.json(), indent=4))
        else:
            print("Text: %s" % response.text)


# time python3.6 send_parkings_info.py -e http://127.0.0.1/api/rospark -d ./data | tee output.out
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Test Rostelecom.Parking API.\n"
        "Example: time python3.6 %s -e http://167.99.136.99/api/rospark " \
        "-d ./data | tee output.out" % sys.argv[0],
        formatter_class=RawTextHelpFormatter)

    ap.add_argument('-e', '--endpoint', required=True, type=str, help="endpoint for ids")
    ap.add_argument('-d', '--dir_path', required=True, type=str, help="directory path with parkings info")
    args = vars(ap.parse_args())

    # Init parameters
    endpoint = args["endpoint"]
    dir_path = args["dir_path"]

    # Debug print
    print("endpoint: %s" % endpoint)
    print("input_file: %s" % dir_path)
    
    
    send_parkings_info(endpoint, dir_path)    

    print("Well done!")
