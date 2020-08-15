
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['get_test_result', 'cancel_test_run']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# TestResults, Get Test Result
def get_test_result(resultId):
    """
    example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b7133854c611834aa6ceb",
    "autoRetry": false,
    "autoRetryTriggered": false,
    "browser": "chrome-79",
    "commentCount": 0,
    "comments": [],
    "console": [
      {
        "_id": "5e2b714065c1671520bc20e6",
        "dateExecuted": "2020-01-24T22:35:38.468Z",
        "error": false,
        "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
        "url": "https://ghostinspector.com/"
      }
    ],
    "dateCreated": "2020-01-24T22:35:31.256Z",
    "dateExecutionFinished": "2020-01-24T22:35:44.348Z",
    "dateExecutionStarted": "2020-01-24T22:35:36.451Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "endUrl": "https://ghostinspector.com/docs/",
    "executionHost": "test001.ghostinspector.net",
    "executionTime": 7897,
    "failOnJavaScriptError": false,
    "filters": [],
    "finalDelay": 0,
    "globalStepDelay": 250,
    "language": null,
    "maxAjaxDelay": 10000,
    "maxWaitDelay": 15000,
    "name": "Login and Check Dashboard",
    "organization": "5a1b419ae40144279f9ac680",
    "passing": true,
    "region": "us-east-1",
    "screenshot": {
      "original": {
        "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/f4357288-944a-4acd-97a0-c8a9b617dd54-original.png",
        "dims": {
          "h": 2708,
          "w": 1024
        },
        "path": "screenshots/f4357288-944a-4acd-97a0-c8a9b617dd54-original.png",
        "size": 221486
      },
      "small": {
        "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/f4357288-944a-4acd-97a0-c8a9b617dd54-small.png",
        "dims": {
          "h": 846,
          "w": 320
        },
        "path": "screenshots/f4357288-944a-4acd-97a0-c8a9b617dd54-small.png",
        "size": 70909
      }
    },
    "screenshotCompareBaselineResult": "5e2b6344854c611834aa6ce5",
    "screenshotCompareDifference": 0,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b714165c1671520bc20eb",
        "command": "click",
        "condition": null,
        "dateExecuted": "2020-01-24T22:35:40.954Z",
        "extra": {
          "source": {
            "sequence": 0,
            "test": "5e2a0b342d0f5947444c31fc"
          }
        },
        "notes": "",
        "optional": false,
        "passing": true,
        "private": false,
        "sequence": 0,
        "target": ".site-logo a",
        "url": "https://ghostinspector.com/",
        "value": "",
        "variableName": ""
      },
      {
        "_id": "5e2b714165c1671520bc20ec",
        "command": "open",
        "condition": null,
        "dateExecuted": "2020-01-24T22:35:42.754Z",
        "extra": {
          "source": {
            "sequence": 1,
            "test": "5e2a0b342d0f5947444c31fc"
          }
        },
        "notes": "",
        "optional": false,
        "passing": true,
        "private": false,
        "sequence": 1,
        "target": "",
        "url": "https://ghostinspector.com/",
        "value": "/docs/",
        "variableName": ""
      }
    ],
    "suiteResult": null,
    "test": {
      "_id": "5e2a0b342d0f5947444c31fc",
      "name": "Login and Check Dashboard",
      "organization": "5a1b419ae40144279f9ac680",
      "suite": "5a1e1b90154014760af39ef5"
    },
    "urls": [
      "https://ghostinspector.com",
      "https://ghostinspector.com/",
      "https://ghostinspector.com/docs/"
    ],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "name": "Justin Klemm"
    },
    "uuid": "f4357288-944a-4acd-97a0-c8a9b617dd54",
    "variables": {
      "orgVar": "foo"
    },
    "video": {
      "dims": {
        "h": 768,
        "w": 1024
      },
      "path": "videos/f4357288-944a-4acd-97a0-c8a9b617dd54.mp4",
      "url": "https://ghostinspector-example.s3.amazonaws.com/videos/f4357288-944a-4acd-97a0-c8a9b617dd54.mp4"
    },
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/results/'+resultId+'/?apiKey='+apiKey)
    return res


# TestResults, Cancel Test Run
def cancel_test_run(resultId):
    """
    Cancel an active test run
    """
    res = requests.post('https://api.ghostinspector.com/v1/results/'+resultId+'/cancel/?apiKey='+apiKey)
    return res

