
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['list_tests', 'get_test', 'update_test', 'delete_a_test', 'execute_test', 'execute_test_post', 'get_running', 'get_running_post', 'accept_screenshot', 'accept_screenshot_post', 'duplicate_test', 'list_test_results', 'list_test_results_csv', 'download_gi_format_json', 'download_in_selenium_format_side', 'download_in_selenium_html', 'test_status_badges', 'execute_on_demand_tests']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# Tests, List Tests
def list_tests():
    """
    Fetch an array of all the tests in your account.

example Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5db700c6881b5f7978697da9",
      "autoRetry": null,
      "browser": null,
      "dateCreated": "2019-10-28T14:52:54.363Z",
      "dateExecutionFinished": "2020-01-24T20:06:28.041Z",
      "dateExecutionStarted": "2020-01-24T20:06:10.831Z",
      "dateUpdated": "2019-10-28T18:02:43.940Z",
      "disableVisuals": true,
      "failOnJavaScriptError": null,
      "finalDelay": null,
      "globalStepDelay": null,
      "httpHeaders": [],
      "links": [],
      "maxAjaxDelay": null,
      "maxWaitDelay": 5000,
      "name": "Multiple Targets",
      "organization": {
        "_id": "5a1b419ae40144279f9ac680",
        "name": "Ghost Inspector"
      },
      "passing": true,
      "publicStatusEnabled": false,
      "region": null,
      "screenshotCompareEnabled": null,
      "screenshotComparePassing": null,
      "screenshotCompareThreshold": 0.1,
      "startUrl": "https://ghostinspector.com/demo/",
      "suite": {
        "_id": "5a1e1b90154014760af39ef5",
        "name": "Smoke Tests"
      },
      "testFrequency": 0,
      "testFrequencyAdvanced": [],
      "viewportSize": null
    },
    {
      "_id": "5e2a0b342d0f5947444c31fc",
      "autoRetry": null,
      "browser": null,
      "dataSource": null,
      "dateCreated": "2020-01-23T21:08:04.664Z",
      "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
      "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
      "dateUpdated": "2020-01-24T21:09:24.948Z",
      "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
      "disableVisuals": null,
      "disallowInsecureCertificates": null,
      "failOnJavaScriptError": null,
      "finalDelay": null,
      "globalStepDelay": null,
      "httpHeaders": [],
      "language": null,
      "links": [],
      "maxAjaxDelay": null,
      "maxWaitDelay": null,
      "name": "Login and Check Dashboard",
      "organization": {
        "_id": "5a1b419ae40144279f9ac680",
        "name": "Ghost Inspector"
      },
      "passing": true,
      "publicStatusEnabled": true,
      "region": null,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "suite": {
        "_id": "5a1e1b90154014760af39ef5",
        "name": "Smoke Tests"
      },
      "testFrequency": 0,
      "testFrequencyAdvanced": [],
      "viewportSize": null
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/?apiKey='+apiKey)
    return res


# Tests, Get Test
def get_test(testId):
    """
    Fetch a single test

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2a0b342d0f5947444c31fc",
    "autoRetry": null,
    "browser": null,
    "dataSource": null,
    "dateCreated": "2020-01-23T21:08:04.664Z",
    "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
    "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
    "dateUpdated": "2020-01-24T21:09:24.948Z",
    "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
    "disableVisuals": null,
    "disallowInsecureCertificates": null,
    "failOnJavaScriptError": null,
    "filters": [],
    "finalDelay": null,
    "globalStepDelay": null,
    "httpHeaders": [],
    "language": null,
    "links": [],
    "maxAjaxDelay": null,
    "maxWaitDelay": null,
    "name": "Login and Check Dashboard",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "passing": true,
    "publicStatusEnabled": true,
    "region": null,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b5ce5854c611834aa6cd2",
        "command": "click",
        "condition": {
          "statement": "return 2 + 2 === 4;"
        },
        "optional": false,
        "private": false,
        "sequence": 0,
        "target": ".site-logo a",
        "value": "",
        "variableName": ""
      },
      {
        "_id": "5e2b5ce5854c611834aa6cd1",
        "command": "assertTextPresent",
        "condition": null,
        "optional": false,
        "private": false,
        "sequence": 1,
        "target": [
          {
            "selector": "h1"
          },
          {
            "selector": ".subhead"
          }
        ],
        "value": "Automated",
        "variableName": ""
      }
    ],
    "suite": {
      "_id": "5a1e1b90154014760af39ef5",
      "name": "Smoke Tests"
    },
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "viewportSize": null
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/?apiKey='+apiKey)
    return res


# Tests, Update Test
def update_test(testId):
    """
    Update a test and return the updated test.


Request Example using cURL

POST Request with JSON body:
curl -H 'Content-Type: application/json' -X POST -d '{"name": "Login and Check Dashboard (updated)"}' 'https://api.ghostinspector.com/v1/tests/<testId>/?apiKey=<apiKey>'


example Response
{
    "code": "SUCCESS",
    "data": {
      "_id": "5e2a0b342d0f5947444c31fc",
      "autoRetry": null,
      "browser": null,
      "dataSource": null,
      "dateCreated": "2020-01-23T21:08:04.664Z",
      "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
      "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
      "dateUpdated": "2020-05-06T21:09:24.948Z",
      "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
      "disableVisuals": null,
      "disallowInsecureCertificates": null,
      "failOnJavaScriptError": null,
      "filters": [],
      "finalDelay": null,
      "globalStepDelay": null,
      "httpHeaders": [],
      "language": null,
      "links": [],
      "maxAjaxDelay": null,
      "maxWaitDelay": null,
      "name": "Login and Check Dashboard (updated)",
      "organization": {
        "_id": "5a1b419ae40144279f9ac680",
        "name": "Ghost Inspector"
      },
      "passing": true,
      "publicStatusEnabled": true,
      "region": null,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b5ce5854c611834aa6cd2",
          "command": "click",
          "condition": {
            "statement": "return 2 + 2 === 4;"
          },
          "optional": false,
          "private": false,
          "sequence": 0,
          "target": ".site-logo a",
          "value": "",
          "variableName": ""
        },
        {
          "_id": "5e2b5ce5854c611834aa6cd1",
          "command": "assertTextPresent",
          "condition": null,
          "optional": false,
          "private": false,
          "sequence": 1,
          "target": [
          {
            "selector": "h1"
          },
          {
            "selector": ".subhead"
          }
        ],
          "value": "Automated",
          "variableName": ""
        }
      ],
      "suite": {
        "_id": "5a1e1b90154014760af39ef5",
        "name": "Smoke Tests"
      },
      "testFrequency": 0,
      "testFrequencyAdvanced": [],
      "viewportSize": null
    }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/tests/'+testId+'/?apiKey='+apiKey)
    return res


# Tests, Delete a Test
def delete_a_test(testId):
    """
    Delete a test.

Response
{
    "code": "SUCCESS",
    "data": true
}
    """
    res = requests.delete('https://api.ghostinspector.com/v1/tests/'+testId+'/?apiKey='+apiKey)
    return res


# Tests, Execute Test
def execute_test(testId, startUrl):
    """
    Note: Test are executed in real time so this request can take some time to return. We’d suggest programming your request to deal with response times of up to 11 minutes. Tests are currently limited to 10 minutes of run time.

Parameters

apiKey
Your API key provided in your account
testId
The ID of the test to execute
startUrl
(Optional) Alternate start URL to use for this execution only
browser
(Optional) Alternate browser to use for this execution. The following options are available: chrome (Latest version), chrome-<version> (Specific version of Chrome, for example chrome-83), firefox (Latest version), firefox-<version> (Specific version of Firefox, for example firefox-77).
userAgent
(Optional) Alternate user agent to use for this execution only
region
(Optional) Geo-location for test execution. The following options are available: us-east-1 (default), us-west-1, ca-central-1, eu-central-1, eu-west-1, eu-west-2, eu-west-3, eu-north-1, me-south-1, ap-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, sa-east-1
httpAuthUsername
(Optional) Alternate HTTP authentication username to use for this execution only
httpAuthPassword
(Optional) Alternate HTTP authentication password to use for this execution only
webhook
(Optional) An escaped URL (or array of URLs) added to the webhooks list for this execution only
disableNotifications
(Optional) Use 1 to disable (or 0 to enable) all notifications for this execution only
immediate
(Optional) Use 1 to initiate the execution, then immediate return a response (without results)
dataFile
(Optional) A CSV file containing a row of variable values for each test run as outlined in our data-driven testing section. A POST request must be used when sending this file. When included, an array of test results will be returned, instead of a single result.
disableVisuals
(Optional) Use 1 to disable (or 0 to enable) capturing screenshots and videos for this execution only
screenshotCompareEnabled
(Optional) Use 1 to enable (or 0 to disable) screenshot comparison for this execution only
screenshotCompareThreshold
(Optional) Use a number between 0.0 and 1.0 to set the tolerance when comparing screenshots (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
screenshotExclusions
(Optional) Use comma-separated CSS selectors. Elements matched by this CSS will be hidden before the screenshot is taken (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
screenshotTarget
(Optional) Use a CSS or XPath selector. Screenshot will be taken of the element specified instead of the whole page (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
viewport
(Optional) Alternate screen size to use for this execution only. This should be a string formatted as {width}x{height}, for example 1024x768. Will be ignored if screenshot comparison or visual capture is disabled.
slackChannel
(Optional) Specify the Slack channel to notify for this test run. Note that the value must be myChannel or %23myChannel and not #myChannel.
[varName]
(Optional) Pass in custom variables for the test run that are accessible in your steps via {{varName}}. For example, including &firstName=Justin in the API call will create a {{firstName}} variable with the value Justin.

Request Examples using cURL
Note: In all cases POST variables will override GET parameters.
GET Request with Parameters:
curl "https://api.ghostinspector.com/v1/tests/<testId>/execute/?apiKey=<key>&startUrl=<url>"

POST Request with Parameters:
curl -d "apiKey=<key>" -d "startUrl=<url>" "https://api.ghostinspector.com/v1/tests/<testId>/execute/"

POST Request with JSON body:
curl -H 'Content-Type: application/json' -d '{"apiKey": "<key>", "startUrl": "https://ghostinspector.com", "myVar": 99}' 'https://api.ghostinspector.com/v1/tests/<testId>/execute/'

POST Multipart Form Request with CSV File:
curl -F "apiKey=<key>" -F "dataFile=@vars.csv" "https://api.ghostinspector.com/v1/tests/<testId>/execute/"


example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b5d5dd4c4051afbd2248c",
    "autoRetry": false,
    "autoRetryTriggered": false,
    "browser": "chrome-79",
    "commentCount": 0,
    "comments": [],
    "console": [
      {
        "_id": "5e2b5d6765c1671520bc20d2",
        "dateExecuted": "2020-01-24T21:10:58.098Z",
        "error": false,
        "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
        "url": "https://ghostinspector.com/"
      }
    ],
    "dateCreated": "2020-01-24T21:10:53.194Z",
    "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
    "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "endUrl": "https://ghostinspector.com/",
    "error": {},
    "executionHost": "test001.ghostinspector.net",
    "executionTime": 7086,
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
        "defaultUrl": "https://ghostinspector-prod.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
        "dims": {
          "h": 3315,
          "w": 1024
        },
        "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
        "size": 508453
      },
      "small": {
        "defaultUrl": "https://ghostinspector-prod.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
        "dims": {
          "h": 1036,
          "w": 320
        },
        "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
        "size": 159382
      }
    },
    "screenshotCompareBaselineResult": "5e2b5d06854c611834aa6cd7",
    "screenshotCompareDifference": 0,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b5d6965c1671520bc20d6",
        "command": "click",
        "condition": {
          "statement": "return 2 + 2 === 4;",
          "result": true
        },
        "dateExecuted": "2020-01-24T21:11:00.606Z",
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
        "_id": "5e2b5d6965c1671520bc20d7",
        "command": "assertTextPresent",
        "condition": null,
        "dateExecuted": "2020-01-24T21:11:01.343Z",
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
        "target": "h1",
        "url": "https://ghostinspector.com/",
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
    "urls": [
      "https://ghostinspector.com",
      "https://ghostinspector.com/"
    ],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "name": "Justin Klemm"
    },
    "uuid": "4b362e32-0bae-44b5-a482-387f3a882ebf",
    "variables": {
      "orgVar": "foo"
    },
    "video": {
      "dims": {
        "h": 768,
        "w": 1024
      },
      "path": "videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4",
      "url": "https://ghostinspector-prod.s3.amazonaws.com/videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4"
    },
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/execute/?apiKey='+apiKey+'&startUrl='+startUrl)
    return res


# Tests, Execute Test Post
def execute_test_post(testId, startUrl):
    """
    Note: Test are executed in real time so this request can take some time to return. We’d suggest programming your request to deal with response times of up to 11 minutes. Tests are currently limited to 10 minutes of run time.

Parameters

apiKey
Your API key provided in your account
testId
The ID of the test to execute
startUrl
(Optional) Alternate start URL to use for this execution only
browser
(Optional) Alternate browser to use for this execution. The following options are available: chrome (Latest version), chrome-<version> (Specific version of Chrome, for example chrome-83), firefox (Latest version), firefox-<version> (Specific version of Firefox, for example firefox-77).
userAgent
(Optional) Alternate user agent to use for this execution only
region
(Optional) Geo-location for test execution. The following options are available: us-east-1 (default), us-west-1, ca-central-1, eu-central-1, eu-west-1, eu-west-2, eu-west-3, eu-north-1, me-south-1, ap-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, sa-east-1
httpAuthUsername
(Optional) Alternate HTTP authentication username to use for this execution only
httpAuthPassword
(Optional) Alternate HTTP authentication password to use for this execution only
webhook
(Optional) An escaped URL (or array of URLs) added to the webhooks list for this execution only
disableNotifications
(Optional) Use 1 to disable (or 0 to enable) all notifications for this execution only
immediate
(Optional) Use 1 to initiate the execution, then immediate return a response (without results)
dataFile
(Optional) A CSV file containing a row of variable values for each test run as outlined in our data-driven testing section. A POST request must be used when sending this file. When included, an array of test results will be returned, instead of a single result.
disableVisuals
(Optional) Use 1 to disable (or 0 to enable) capturing screenshots and videos for this execution only
screenshotCompareEnabled
(Optional) Use 1 to enable (or 0 to disable) screenshot comparison for this execution only
screenshotCompareThreshold
(Optional) Use a number between 0.0 and 1.0 to set the tolerance when comparing screenshots (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
screenshotExclusions
(Optional) Use comma-separated CSS selectors. Elements matched by this CSS will be hidden before the screenshot is taken (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
screenshotTarget
(Optional) Use a CSS or XPath selector. Screenshot will be taken of the element specified instead of the whole page (for this execution only). Will be ignored if screenshot comparison or visual capture is disabled.
viewport
(Optional) Alternate screen size to use for this execution only. This should be a string formatted as {width}x{height}, for example 1024x768. Will be ignored if screenshot comparison or visual capture is disabled.
slackChannel
(Optional) Specify the Slack channel to notify for this test run. Note that the value must be myChannel or %23myChannel and not #myChannel.
[varName]
(Optional) Pass in custom variables for the test run that are accessible in your steps via {{varName}}. For example, including &firstName=Justin in the API call will create a {{firstName}} variable with the value Justin.

Request Examples using cURL
Note: In all cases POST variables will override GET parameters.
GET Request with Parameters:
curl "https://api.ghostinspector.com/v1/tests/<testId>/execute/?apiKey=<key>&startUrl=<url>"

POST Request with Parameters:
curl -d "apiKey=<key>" -d "startUrl=<url>" "https://api.ghostinspector.com/v1/tests/<testId>/execute/"

POST Request with JSON body:
curl -H 'Content-Type: application/json' -d '{"apiKey": "<key>", "startUrl": "https://ghostinspector.com", "myVar": 99}' 'https://api.ghostinspector.com/v1/tests/<testId>/execute/'

POST Multipart Form Request with CSV File:
curl -F "apiKey=<key>" -F "dataFile=@vars.csv" "https://api.ghostinspector.com/v1/tests/<testId>/execute/"


example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b5d5dd4c4051afbd2248c",
    "autoRetry": false,
    "autoRetryTriggered": false,
    "browser": "chrome-79",
    "commentCount": 0,
    "comments": [],
    "console": [
      {
        "_id": "5e2b5d6765c1671520bc20d2",
        "dateExecuted": "2020-01-24T21:10:58.098Z",
        "error": false,
        "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
        "url": "https://ghostinspector.com/"
      }
    ],
    "dateCreated": "2020-01-24T21:10:53.194Z",
    "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
    "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "endUrl": "https://ghostinspector.com/",
    "error": {},
    "executionHost": "test001.ghostinspector.net",
    "executionTime": 7086,
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
        "defaultUrl": "https://ghostinspector-prod.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
        "dims": {
          "h": 3315,
          "w": 1024
        },
        "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
        "size": 508453
      },
      "small": {
        "defaultUrl": "https://ghostinspector-prod.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
        "dims": {
          "h": 1036,
          "w": 320
        },
        "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
        "size": 159382
      }
    },
    "screenshotCompareBaselineResult": "5e2b5d06854c611834aa6cd7",
    "screenshotCompareDifference": 0,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b5d6965c1671520bc20d6",
        "command": "click",
        "condition": {
          "statement": "return 2 + 2 === 4;",
          "result": true
        },
        "dateExecuted": "2020-01-24T21:11:00.606Z",
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
        "_id": "5e2b5d6965c1671520bc20d7",
        "command": "assertTextPresent",
        "condition": null,
        "dateExecuted": "2020-01-24T21:11:01.343Z",
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
        "target": "h1",
        "url": "https://ghostinspector.com/",
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
    "urls": [
      "https://ghostinspector.com",
      "https://ghostinspector.com/"
    ],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "name": "Justin Klemm"
    },
    "uuid": "4b362e32-0bae-44b5-a482-387f3a882ebf",
    "variables": {
      "orgVar": "foo"
    },
    "video": {
      "dims": {
        "h": 768,
        "w": 1024
      },
      "path": "videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4",
      "url": "https://ghostinspector-prod.s3.amazonaws.com/videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4"
    },
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/tests/'+testId+'/execute/?apiKey='+apiKey+'&startUrl='+startUrl)
    return res


# Tests, Get Running
def get_running(testId):
    """
    Fetch a list of the currently-executing results for this test and return the result.

example Response
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
          "condition": {
            "statement": "return 2 + 2 === 4;"
          },
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
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/running/?apiKey='+apiKey)
    return res


# Tests, Get Running Post
def get_running_post(testId):
    """
    Fetch a list of the currently-executing results for this test and return the result.

example Response
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
          "condition": {
            "statement": "return 2 + 2 === 4;"
          },
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
    res = requests.post('https://api.ghostinspector.com/v1/tests/'+testId+'/running/?apiKey='+apiKey)
    return res


# Tests, Accept Screenshot
def accept_screenshot(testId):
    """
    Accept the current screenshot as the new baseline for this test.

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2a0b342d0f5947444c31fc",
    "autoRetry": null,
    "browser": null,
    "dateCreated": "2020-01-23T21:08:04.664Z",
    "dateExecutionFinished": "2020-01-24T21:36:14.674Z",
    "dateExecutionStarted": "2020-01-24T21:36:06.839Z",
    "dateExecutionTriggered": "2020-01-24T21:36:04.072Z",
    "dateUpdated": "2020-01-24T21:35:30.841Z",
    "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
    "disableVisuals": null,
    "disallowInsecureCertificates": null,
    "failOnJavaScriptError": null,
    "filters": [],
    "finalDelay": null,
    "globalStepDelay": null,
    "httpHeaders": [],
    "language": null,
    "links": [],
    "maxAjaxDelay": null,
    "maxWaitDelay": null,
    "name": "Login and Check Dashboard",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "passing": true,
    "publicStatusEnabled": true,
    "region": null,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b5ce5854c611834aa6cd2",
        "command": "click",
        "condition": {
          "statement": "return 2 + 2 === 4;"
        },
        "optional": false,
        "private": false,
        "sequence": 0,
        "target": ".site-logo a",
        "value": "",
        "variableName": ""
      },
      {
        "_id": "5e2b5ce5854c611834aa6cd1",
        "command": "open",
        "condition": null,
        "optional": false,
        "private": false,
        "sequence": 1,
        "target": "",
        "value": "/docs/",
        "variableName": ""
      }
    ],
    "suite": {
      "_id": "5a1e1b90154014760af39ef5",
      "name": "Smoke Tests"
    },
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "firstName": "Justin",
      "lastName": "Klemm"
    },
    "viewportSize": null
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/accept-screenshot/?apiKey='+apiKey)
    return res


# Tests, Accept Screenshot Post
def accept_screenshot_post(testId):
    """
    Accept the current screenshot as the new baseline for this test.

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2a0b342d0f5947444c31fc",
    "autoRetry": null,
    "browser": null,
    "dateCreated": "2020-01-23T21:08:04.664Z",
    "dateExecutionFinished": "2020-01-24T21:36:14.674Z",
    "dateExecutionStarted": "2020-01-24T21:36:06.839Z",
    "dateExecutionTriggered": "2020-01-24T21:36:04.072Z",
    "dateUpdated": "2020-01-24T21:35:30.841Z",
    "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
    "disableVisuals": null,
    "disallowInsecureCertificates": null,
    "failOnJavaScriptError": null,
    "filters": [],
    "finalDelay": null,
    "globalStepDelay": null,
    "httpHeaders": [],
    "language": null,
    "links": [],
    "maxAjaxDelay": null,
    "maxWaitDelay": null,
    "name": "Login and Check Dashboard",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "passing": true,
    "publicStatusEnabled": true,
    "region": null,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": true,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "_id": "5e2b5ce5854c611834aa6cd2",
        "command": "click",
        "condition": {
          "statement": "return 2 + 2 === 4;"
        },
        "optional": false,
        "private": false,
        "sequence": 0,
        "target": ".site-logo a",
        "value": "",
        "variableName": ""
      },
      {
        "_id": "5e2b5ce5854c611834aa6cd1",
        "command": "open",
        "condition": null,
        "optional": false,
        "private": false,
        "sequence": 1,
        "target": "",
        "value": "/docs/",
        "variableName": ""
      }
    ],
    "suite": {
      "_id": "5a1e1b90154014760af39ef5",
      "name": "Smoke Tests"
    },
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "firstName": "Justin",
      "lastName": "Klemm"
    },
    "viewportSize": null
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/tests/'+testId+'/accept-screenshot/?apiKey='+apiKey)
    return res


# Tests, Duplicate Test
def duplicate_test(testId):
    """
    Duplicate a test within your account, return the new test. The new test will be duplicated within the same Suite as the original.

{
      "code": "SUCCESS",
      "data": {
        "_id": "5e2b69f3d4c4051afbd2248f",
        "autoRetry": null,
        "browser": null,
        "dateCreated": "2020-01-23T21:08:04.664Z",
        "dateExecutionFinished": "1970-01-01T00:00:00.000Z",
        "dateExecutionStarted": "1970-01-01T00:00:00.000Z",
        "dateExecutionTriggered": "1970-01-01T00:00:00.000Z",
        "dateUpdated": "2020-01-24T21:35:30.841Z",
        "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
        "disableVisuals": null,
        "disallowInsecureCertificates": null,
        "failOnJavaScriptError": null,
        "filters": [],
        "finalDelay": null,
        "globalStepDelay": null,
        "httpHeaders": [],
        "language": null,
        "links": [],
        "maxAjaxDelay": null,
        "maxWaitDelay": null,
        "name": "Login and Check Dashboard (Copy)",
        "organization": {
          "_id": "5a1b419ae40144279f9ac680",
          "name": "Ghost Inspector"
        },
        "passing": null,
        "publicStatusEnabled": true,
        "region": null,
        "screenshotCompareEnabled": true,
        "screenshotComparePassing": null,
        "screenshotCompareThreshold": 0.01,
        "startUrl": "https://ghostinspector.com",
        "steps": [
          {
            "_id": "5e2b5ce5854c611834aa6cd2",
            "command": "click",
            "condition": {
              "statement": "return 2 + 2 === 4;"
            },
            "optional": false,
            "private": false,
            "sequence": 0,
            "target": ".site-logo a",
            "value": "",
            "variableName": ""
          },
          {
            "_id": "5e2b5ce5854c611834aa6cd1",
            "command": "open",
            "condition": null,
            "optional": false,
            "private": false,
            "sequence": 1,
            "target": "",
            "value": "/docs/",
            "variableName": ""
          }
        ],
        "suite": {
          "_id": "5a1e1b90154014760af39ef5",
          "name": "Smoke Tests"
        },
        "testFrequency": 0,
        "testFrequencyAdvanced": [],
        "user": "55b2accc4f66690c07294201",
        "viewportSize": null
      }
    }
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/duplicate/?apiKey='+apiKey)
    return res


# Tests, List Test Results
def list_test_results(testId):
    """
    Fetch an array containing the results for a test. Results are returned in reverse chronological order (newest first).

Parameters
apiKey
Your API key provided in your account
testId
The ID of the test containing the results
count
The number of results to return (default 10, maximum 50)
offset
The number of results to offset the returned set by (default 0)

exampe Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2b5d5dd4c4051afbd2248c",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome-79",
      "commentCount": 0,
      "comments": [],
      "console": [
        {
          "_id": "5e2b5d6765c1671520bc20d2",
          "dateExecuted": "2020-01-24T21:10:58.098Z",
          "error": false,
          "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
          "url": "https://ghostinspector.com/"
        }
      ],
      "dateCreated": "2020-01-24T21:10:53.194Z",
      "dateExecutionFinished": "2020-01-24T21:11:03.194Z",
      "dateExecutionStarted": "2020-01-24T21:10:56.108Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "https://ghostinspector.com/",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": 7086,
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
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
          "dims": {
            "h": 3315,
            "w": 1024
          },
          "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-original.png",
          "size": 508453
        },
        "small": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
          "dims": {
            "h": 1036,
            "w": 320
          },
          "path": "screenshots/4b362e32-0bae-44b5-a482-387f3a882ebf-small.png",
          "size": 159382
        }
      },
      "screenshotCompareBaselineResult": "5e2b5d06854c611834aa6cd7",
      "screenshotCompareDifference": 0,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b5d6965c1671520bc20d6",
          "command": "click",
          "condition": {
            "statement": "return 2 + 2 === 4;",
            "result": true
          },
          "dateExecuted": "2020-01-24T21:11:00.606Z",
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
          "_id": "5e2b5d6965c1671520bc20d7",
          "command": "assertTextPresent",
          "condition": null,
          "dateExecuted": "2020-01-24T21:11:01.343Z",
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
          "target": "h1",
          "url": "https://ghostinspector.com/",
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
      "urls": [
        "https://ghostinspector.com",
        "https://ghostinspector.com/"
      ],
      "user": {
        "_id": "55b2accc4f66690c07294201",
        "name": "Justin Klemm"
      },
      "uuid": "4b362e32-0bae-44b5-a482-387f3a882ebf",
      "variables": {
        "orgVar": "foo"
      },
      "video": {
        "dims": {
          "h": 768,
          "w": 1024
        },
        "path": "videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4",
        "url": "https://ghostinspector-example.s3.amazonaws.com/videos/4b362e32-0bae-44b5-a482-387f3a882ebf.mp4"
      },
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    },
    {
      "_id": "5e2b6344854c611834aa6ce5",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome-79",
      "commentCount": 0,
      "comments": [],
      "console": [
        {
          "_id": "5e2b634e65c1671520bc20df",
          "dateExecuted": "2020-01-24T21:36:08.818Z",
          "error": false,
          "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
          "url": "https://ghostinspector.com/"
        }
      ],
      "dateCreated": "2020-01-24T21:36:04.013Z",
      "dateExecutionFinished": "2020-01-24T21:36:14.674Z",
      "dateExecutionStarted": "2020-01-24T21:36:06.839Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "https://ghostinspector.com/docs/",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": 7835,
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
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-original.png",
          "dims": {
            "h": 2708,
            "w": 1024
          },
          "path": "screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-original.png",
          "size": 221486
        },
        "small": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-small.png",
          "dims": {
            "h": 846,
            "w": 320
          },
          "path": "screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-small.png",
          "size": 70909
        }
      },
      "screenshotCompare": {
        "compareOriginal": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-compareOriginal.png",
          "dims": {
            "h": 2708,
            "w": 1024
          },
          "path": "screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-compareOriginal.png",
          "size": 197958
        },
        "compareSmall": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-compareSmall.png",
          "dims": {
            "h": 846,
            "w": 320
          },
          "path": "screenshots/b21ca485-c15b-40bd-9a5c-d9251f1948ef-compareSmall.png",
          "size": 91638
        }
      },
      "screenshotCompareBaselineResult": "5e2b5d5dd4c4051afbd2248c",
      "screenshotCompareDifference": 0.47,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b635165c1671520bc20e4",
          "command": "click",
          "condition": {
            "statement": "return 2 + 2 === 4;",
            "result": true
          },
          "dateExecuted": "2020-01-24T21:36:11.299Z",
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
          "_id": "5e2b635165c1671520bc20e5",
          "command": "open",
          "condition": null,
          "dateExecuted": "2020-01-24T21:36:13.104Z",
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
      "uuid": "b21ca485-c15b-40bd-9a5c-d9251f1948ef",
      "variables": {
        "orgVar": "foo"
      },
      "video": {
        "dims": {
          "h": 768,
          "w": 1024
        },
        "path": "videos/b21ca485-c15b-40bd-9a5c-d9251f1948ef.mp4",
        "url": "https://ghostinspector-example.s3.amazonaws.com/videos/b21ca485-c15b-40bd-9a5c-d9251f1948ef.mp4"
      },
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/results/?apiKey='+apiKey)
    return res


# Tests, List Test Results CSV
def list_test_results_csv(testId):
    """
    Fetch a CSV formatted export of test results for a test. Results are returned in reverse chronological order (newest first).

Parameters
apiKey
Your API key provided in your account
testId
The ID of the test containing the results
count
The number of results to return (default 10, maximum 50)
offset
The number of results to offset the returned set by (default 0)
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/results/csv/?apiKey='+apiKey)
    return res


# Tests, Download GI Format JSON
def download_gi_format_json(testId):
    """
    Download a single test in Ghost Inspector format (.json).

example Response
{
  "autoRetry": null,
  "browser": null,
  "details": "This is a simple test that will log into the dashboard and assert that the widgets are showing up properly.",
  "disableVisuals": null,
  "disallowInsecureCertificates": null,
  "failOnJavaScriptError": null,
  "filters": [],
  "finalDelay": null,
  "globalStepDelay": null,
  "httpHeaders": [],
  "language": null,
  "links": [],
  "maxAjaxDelay": null,
  "maxWaitDelay": null,
  "name": "Login and Check Dashboard",
  "notifications": {
    "5b1e914a3bad610fa4a8fa8b": {
      "enabled": false
    },
    "email": {
      "enabled": false
    },
    "webhooks": {
      "enabled": false
    }
  },
  "publicStatusEnabled": true,
  "region": null,
  "screenshotCompareEnabled": true,
  "screenshotCompareThreshold": 0.01,
  "startUrl": "https://ghostinspector.com",
  "steps": [
    {
      "command": "click",
      "condition": {
        "statement": "return 2 + 2 === 4;"
      },
      "optional": false,
      "private": false,
      "sequence": 0,
      "target": ".site-logo a",
      "value": "",
      "variableName": ""
    },
    {
      "command": "open",
      "condition": null,
      "optional": false,
      "private": false,
      "sequence": 1,
      "target": "",
      "value": "/docs/",
      "variableName": ""
    }
  ],
  "testFrequency": 0,
  "testFrequencyAdvanced": [],
  "viewportSize": null
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/export/json/?apiKey='+apiKey)
    return res


# Tests, Download in Selenium Format side
def download_in_selenium_format_side(testId):
    """
    Download a single test in Selenium IDE format (.side).

example Response
Response
{
  "id": "2c181a11-c461-4bf3-8df2-7189434804a1",
  "version": "1.1",
  "name": "Sample Test",
  "url": "http://sampledomain.com/",
  "tests": [
    {
      "id": "9e7ea88a-8780-488a-9880-0396d8e341a2",
      "name": "Sample Test",
      "commands": [
        {
          "command": "open",
          "target": "http://sampledomain.com/",
          "value": ""
        },
        {
          "command": "setWindowSize",
          "target": "1024x768",
          "value": ""
        },
        {
          "comment": "",
          "command": "type",
          "target": "xpath=//input[@id=\"username\"]",
          "value": "sample"
        }
      ]
    }
  ],
  "suites": [
    {
      "id": "c7a3f198-7793-4231-817e-05427eca6be9",
      "name": "Sample Test",
      "persistSession": false,
      "parallel": true,
      "timeout": 600,
      "tests": [
        "9e7ea88a-8780-488a-9880-0396d8e341a2"
      ]
    }
  ],
  "plugins": []
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/export/selenium-side/?apiKey='+apiKey)
    return res


# Tests, Download in Selenium HTML
def download_in_selenium_html(testId):
    """
    Download a single test in Selenium IDE format (.html).

example Response
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://ghostinspector.com" />
<title>Sample Test</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr>
<td rowspan="1" colspan="3">Sample Test</td>
</tr>
</thead>
<tbody>
<tr>
<td>open</td>
<td>/</td>
<td></td>
</tr>
<tr>
<td>waitForPageToLoad</td>
<td></td>
<td></td>
</tr>
<tr>
<td>waitForElementPresent</td>
<td>css=#username</td>
<td></td>
</tr>
<tr>
<td>type</td>
<td>css=#username</td>
<td>test</td>
</tr>
<tr>
<td>waitForPageToLoad</td>
<td></td>
<td></td>
</tr>
<tr>
<td>waitForElementPresent</td>
<td>css=#submit</td>
<td></td>
</tr>
<tr>
<td>click</td>
<td>css=#submit</td>
<td></td>
</tr>
</tbody>
</table>
</body>
</html>
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/export/selenium-html/?apiKey='+apiKey)
    return res


# Tests, Test Status Badges
def test_status_badges(testId):
    """
    Note: Status badges are disabled by default and can be enabled under Test Settings > Details > Enable Status Badge.

Real-time embeddable status badges for your test. Will return the appropriate status badge image based on the current status of your test.

Parameters
screenshot
Show the status of screenshotComparePassing for this test.

Statuses
Passing
 The last completed run of this test passed.
Failing
 The last completed run of this test failed.
Running
 Test execution is in progress.
Unknown
 The test has no previous execution or the last execution was cancelled.
Screenshot Compare
 The screenshot comparison for this test is passing.


Example usage
<img src="https://api.ghostinspector.com/v1/tests/<testId>/status-badge" title="My test status">
    """
    res = requests.get('https://api.ghostinspector.com/v1/tests/'+testId+'/status-badge)
    return res


# Tests, Execute On Demand Tests
def execute_on_demand_tests(organizationId):
    """
    Execute an on-demand test using JSON from your file system or repository. This endpoint will trigger a test run created out of the JSON definition provided and immediately return a result ID. On-demand test results are associated with your organization, but are not tied to existing tests or suites within the system. Results must be retrieved using the result ID in the response and the Get Test Result endpoint.

Request Example using cURL

POST Request with JSON body:
curl -H 'Content-Type: application/json' -X POST -d "@test.json" 'https://api.ghostinspector.com/v1/organizations/<my-org-id>/on-demand/execute/'

Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5dbc760c185e8911cfd6f2a0",
    "user": {
      "name": "Ghost User",
      "_id": "59f35ea3ae726358914cc184"
    },
    "viewportSize": {
      "width": 1024,
      "height": 768
    },
    "commentCount": 0,
    "disableVisuals": false,
    "disallowInsecureCertificates": null,
    "passing": null,
    "screenshotCompareDifference": null,
    "screenshotComparePassing": null,
    "urls": [],
    "autoRetry": true,
    "browser": "chrome",
    "comments": [],
    "console": [],
    "dateCreated": "2019-11-01T18:14:36.203Z",
    "endUrl": "",
    "executionHost": "test-runner-916cf2.ghostinspector.net",
    "executionTime": null,
    "failOnJavaScriptError": false,
    "filters": [],
    "finalDelay": 5000,
    "globalStepDelay": 250,
    "language": null,
    "maxAjaxDelay": 10000,
    "maxWaitDelay": 15000,
    "name": "Assertions",
    "organization": "5a0604918ee170435385d4a7",
    "region": "us-east-1",
    "screenshotCompareBaselineResult": null,
    "screenshotCompareEnabled": true,
    "screenshotCompareThreshold": 0.1,
    "screenshotExclusions": "",
    "screenshotTarget": "",
    "startUrl": "https://www.onlineconstructioninc.com/",
    "steps": [
      {
        "sequence": 0,
        "condition": null,
        "private": false,
        "optional": false,
        "passing": null,
        "_id": "5dbc760c185e8911cfd6f2c2",
        "command": "assign",
        "target": "#username",
        "value": "Decimal",
        "variableName": "",
        "notes": "Assign a \"Special\" string to make sure if doesn't get converted to the character"
      },
      {
        "sequence": 1,
        "condition": null,
        "private": false,
        "optional": false,
        "passing": null,
        "_id": "5dbc760c185e8911cfd6f2c1",
        "command": "assertText",
        "target": "#username",
        "value": "Decimal",
        "variableName": ""
      },
      {
        "sequence": 2,
        "condition": {
          "statement": "return 2 + 2 === 4;"
        },
        "private": false,
        "optional": false,
        "passing": null,
        "_id": "5dbc760c185e8911cfd6f2c0",
        "command": "assign",
        "target": "#username",
        "value": "Escape",
        "variableName": "",
        "notes": "Assign a \"Special\" string to make sure if doesn't get converted to the character"
      }
    ],
    "suiteResult": null,
    "test": null,
    "userAgent": "",
    "uuid": "513e2f78-ad93-4158-a15e-a4f9e50e6322",
    "dateExecutionStarted": "2019-11-01T18:14:36.287Z"
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/organizations/'+organizationId+'/on-demand/execute?apiKey='+apiKey)
    return res

