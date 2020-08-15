
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['get_suite_result', 'cancel_suite_run', 'list_test_results', 'get_xunit_xml_report']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# SuiteResults, Get Suite Result
def get_suite_result(suiteResultId):
    """
    apiKey: Your API key provided in your account
suiteResultId: The ID of the suite result to fetch

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b7924854c611834aa6cf6",
    "commentCount": 0,
    "comments": [],
    "countFailing": 0,
    "countPassing": 1,
    "countScreenshotCompareFailing": 0,
    "countScreenshotComparePassing": 1,
    "countScreenshotCompareUnknown": 0,
    "countUnknown": 0,
    "dateCreated": "2020-01-24T23:09:24.477Z",
    "dateExecutionFinished": "2020-01-24T23:11:39.548Z",
    "dateExecutionStarted": "2020-01-24T23:09:24.477Z",
    "executionTime": 135071,
    "name": "Smoke Tests",
    "passing": true,
    "screenshotComparePassing": true,
    "startUrl": "",
    "suite": {
      "_id": "5a1e1b90154014760af39ef5",
      "name": "Smoke Tests",
      "organization": "5a1b419ae40144279f9ac680"
    },
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "name": "Justin Klemm"
    }
  }
}

    """
    res = requests.get('https://api.ghostinspector.com/v1/suite-results/'+suiteResultId+'/?apiKey='+apiKey)
    return res


# SuiteResults, Cancel Suite Run
def cancel_suite_run(suiteResultId):
    """
    example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b7924854c611834aa6cf6",
    "commentCount": 0,
    "comments": [],
    "countFailing": 0,
    "countPassing": 1,
    "countScreenshotCompareFailing": 0,
    "countScreenshotComparePassing": 1,
    "countScreenshotCompareUnknown": 0,
    "countUnknown": 0,
    "dateCreated": "2020-01-24T23:09:24.477Z",
    "dateExecutionFinished": "2020-01-24T23:11:39.548Z",
    "dateExecutionStarted": "2020-01-24T23:09:24.477Z",
    "executionTime": 135071,
    "name": "Smoke Tests",
    "passing": null,
    "screenshotComparePassing": null,
    "startUrl": "",
    "suite": {
      "_id": "5a1e1b90154014760af39ef5",
      "name": "Smoke Tests",
      "organization": "5a1b419ae40144279f9ac680"
    },
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "name": "Justin Klemm"
    }
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suite-results/'+suiteResultId+'/cancel/?apiKey='+apiKey)
    return res


# SuiteResults, List Test Results
def list_test_results(suiteResultId):
    """
    Fetch an array containing the test results in a suite result. Results are returned in the order they were created when the suite was triggered (typically alphabetical order by test name)

apiKey
Your API key provided in your account
suiteResultId
The ID of the suite result containing the test results
count
The number of results to return (default 10, maximum 50)
offset
The number of results to offset the returned set by (default 0)

example Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2b7924854c611834aa6cf7",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome-79",
      "commentCount": 0,
      "comments": [],
      "console": [
        {
          "_id": "5e2b79a665c1671520bc20f1",
          "dateExecuted": "2020-01-24T23:09:28.104Z",
          "error": false,
          "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
          "url": "https://ghostinspector.com/"
        }
      ],
      "dateCreated": "2020-01-24T23:09:24.498Z",
      "dateExecutionFinished": "2020-01-24T23:11:34.886Z",
      "dateExecutionStarted": "2020-01-24T23:09:26.088Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "https://ghostinspector.com/docs/",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": 128798,
      "extractions": {},
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
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b354de4b-eca1-40bd-9f81-8e550642f1a4-original.png",
          "dims": {
            "h": 2708,
            "w": 1024
          },
          "path": "screenshots/b354de4b-eca1-40bd-9f81-8e550642f1a4-original.png",
          "size": 221486
        },
        "small": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b354de4b-eca1-40bd-9f81-8e550642f1a4-small.png",
          "dims": {
            "h": 846,
            "w": 320
          },
          "path": "screenshots/b354de4b-eca1-40bd-9f81-8e550642f1a4-small.png",
          "size": 70909
        }
      },
      "screenshotCompareBaselineResult": "5e2b7133854c611834aa6ceb",
      "screenshotCompareDifference": 0,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b79a865c1671520bc20f6",
          "command": "click",
          "condition": null,
          "dateExecuted": "2020-01-24T23:09:30.591Z",
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
          "_id": "5e2b79a865c1671520bc20f8",
          "command": "open",
          "condition": null,
          "dateExecuted": "2020-01-24T23:11:33.303Z",
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
      "suiteResult": "5e2b7924854c611834aa6cf6",
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
      "uuid": "b354de4b-eca1-40bd-9f81-8e550642f1a4",
      "variables": {
        "orgVar": "foo"
      },
      "video": {
        "dims": {
          "h": 768,
          "w": 1024
        },
        "path": "videos/b354de4b-eca1-40bd-9f81-8e550642f1a4.mp4",
        "url": "https://ghostinspector-example.s3.amazonaws.com/videos/b354de4b-eca1-40bd-9f81-8e550642f1a4.mp4"
      },
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suite-results/'+suiteResultId+'/results/?apiKey='+apiKey)
    return res


# SuiteResults, Get XUnit XML Report
def get_xunit_xml_report(suiteResultId):
    """
    Fetch an XML report (XUnit v2) for a suite result.


Response
<assemblies>
  <assembly test-framework="Ghost Inspector" name="Ghost Inspector Suites" run-date="2018-10-03" run-time="17:17:24" time="45.071" passed="2" failed="0" skipped="0" total="2" config-file="/no-config-file" environment="browser">
    <collection name="Promises - Chrome" time="45.071" passed="2" failed="0" skipped="0" total="2">
      <test name="Promises - Chrome" type="browser" method="Promises - Chrome" time="26.205" result="Pass">
        <traits>
          <trait/>
        </traits>
      </test>
      <test name="Verify > Promises - Chrome" type="browser" method="Verify > Promises - Chrome" time="10.386" result="Pass">
        <traits>
          <trait/>
        </traits>
      </test>
    </collection>
    <errors/>
  </assembly>
</assemblies>
    """
    res = requests.get('https://api.ghostinspector.com/v1/suite-results/'+suiteResultId+'/xunit/?apiKey='+apiKey)
    return res

