
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['get_running']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# Organizations, Get Running
def get_running(organizationId):
    """
    Fetch a list of all the currently-executing results for the entire organization and return the results

Eexample Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2b6294854c611834aa6cde",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome",
      "commentCount": 0,
      "comments": [],
      "console": [],
      "dateCreated": "2020-01-24T21:33:08.870Z",
      "dateExecutionStarted": "2020-01-24T21:33:09.571Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": null,
      "failOnJavaScriptError": false,
      "filters": [],
      "finalDelay": 0,
      "globalStepDelay": 250,
      "language": null,
      "maxAjaxDelay": 10000,
      "maxWaitDelay": 15000,
      "name": "Login and Check Dashboard",
      "organization": "5a1b419ae40144279f9ac680",
      "passing": null,
      "region": "us-east-1",
      "screenshotCompareBaselineResult": null,
      "screenshotCompareDifference": null,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": null,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b5ce5854c611834aa6cd2",
          "command": "click",
          "condition": null,
          "extra": {
            "source": {
              "sequence": 0,
              "test": "5e2a0b342d0f5947444c31fc"
            }
          },
          "notes": "",
          "optional": false,
          "passing": null,
          "private": false,
          "sequence": 0,
          "target": ".site-logo a",
          "value": "",
          "variableName": ""
        }
        {
          "_id": "5e2b5ce5854c611834aa6cd1",
          "command": "assertTextPresent",
          "condition": null,
          "extra": {
            "source": {
              "sequence": 1,
              "test": "5e2a0b342d0f5947444c31fc"
            }
          },
          "notes": "",
          "optional": false,
          "passing": null,
          "private": false,
          "sequence": 1,
          "target": "h1",
          "value": "Automated",
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
      "urls": [],
      "user": {
        "_id": "55b2accc4f66690c07294201",
        "name": "Justin Klemm"
      },
      "uuid": "6e930f8b-37f4-42e6-a4a1-11d85cf57fd0",
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/organizations/'+organizationId+'/running/?apiKey='+apiKey)
    return res

