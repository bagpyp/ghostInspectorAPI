
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['list_suites', 'get_suite', 'execute_suite', 'execute_suite_post', 'create_suite', 'update_suite', 'duplicate_suite', 'duplicate_suite_post', 'import_test', 'list_suite_tests', 'list_suite_results', 'list_suite_results_csv', 'download_suite_tests_json', 'download_suite_tests_side', 'download_suite_tests_html', 'suite_status_badges']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# Suites, List Suites
def list_suites():
    """
    Fetch an array of all the suites in your account.

Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5a1e1b90154014760af39ef5",
      "abortOnTestFailure": false,
      "autoRetry": false,
      "browser": "chrome",
      "dateCreated": "2017-11-29T02:29:36.132Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "failOnJavaScriptError": false,
      "finalDelay": 0,
      "folder": "5af3736b34967c7736a5bd33",
      "globalStepDelay": 250,
      "httpHeaders": [],
      "language": null,
      "maxAjaxDelay": 10000,
      "maxConcurrentTests": 0,
      "maxWaitDelay": 15000,
      "name": "Smoke Tests",
      "notificationsSuite": {},
      "organization": {
        "_id": "5a1b419ae40144279f9ac680",
        "name": "Ghost Inspector",
        "personal": false
      },
      "persistVariables": false,
      "publicStatusEnabled": false,
      "region": "us-east-1",
      "screenshotCompareEnabled": false,
      "screenshotCompareThreshold": 0.1,
      "startUrl": "",
      "testCount": 1,
      "testFrequency": 0,
      "testFrequencyAdvanced": [],
      "variables": [],
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/?apiKey='+apiKey)
    return res


# Suites, Get Suite
def get_suite(suiteId):
    """
    Fetch a single suite

Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5a1e1b90154014760af39ef5",
    "abortOnTestFailure": false,
    "autoRetry": false,
    "browser": "chrome",
    "dataSource": null,
    "dateCreated": "2017-11-29T02:29:36.132Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "failOnJavaScriptError": false,
    "finalDelay": 0,
    "folder": "5af3736b34967c7736a5bd33",
    "globalStepDelay": 250,
    "httpHeaders": [],
    "language": null,
    "maxAjaxDelay": 10000,
    "maxConcurrentTests": 0,
    "maxWaitDelay": 15000,
    "name": "Smoke Tests",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "persistVariables": false,
    "publicStatusEnabled": false,
    "region": "us-east-1",
    "screenshotCompareEnabled": false,
    "screenshotCompareThreshold": 0.1,
    "startUrl": "",
    "testCount": 1,
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "variables": [],
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/?apiKey='+apiKey)
    return res


# Suites, Execute Suite
def execute_suite(suiteId, startUrl):
    """
    

---NOTE---
Note: We execute tests concurrently, however this request can still take some time to return. In general, it will return in the time that it takes to run your longest test; however, this can vary depending on the load on our system and the number of tests being run. We’d suggest programming your request to deal with response times up to 20 minutes. If all the suite's tests are not completed within 20 minutes, the API will send a timeout error (although your tests will still be triggered).



---PARAMS---

apiKey
Your API key provided in your account
suiteId
The ID of the suite to execute
startUrl
(Optional) Alternate start URL to use for all tests in this execution only
browser
(Optional) Alternate browser to use for this execution. The following options are available: chrome (Latest version), chrome-<version> (Specific version of Chrome, for example chrome-83), firefox (Latest version), firefox-<version> (Specific version of Firefox, for example firefox-77).
userAgent
(Optional) Alternate user agent to use for all tests in this execution only
region
(Optional) Geo-location for test execution. The following options are available: us-east-1 (default), us-west-1, ca-central-1, eu-central-1, eu-west-1, eu-west-2, eu-west-3, eu-north-1, me-south-1, ap-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, sa-east-1
httpAuthUsername
(Optional) Alternate HTTP authentication username to use for this execution only
httpAuthPassword
(Optional) Alternate HTTP authentication password to use for this execution only
disableNotifications
(Optional) Use 1 to disable (or 0 to enable) all notifications for this execution only
immediate
(Optional) Use 1 to initiate the execution, then immediate return a response (without results)
dataFile
(Optional) A CSV file containing a row of variable values for each suite run as outlined in our data-driven testing section. A POST request must be used when sending this file. When included, an array of suite results will be returned instead of an array of test result.
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
(Optional) Alternate screen size to use for all tests in this execution only. This should be a string formatted as {width}x{height}, for example 1024x768.
slackChannel
(Optional) Specify the Slack channel to notify for this suite run. Note that the value must be myChannel or %23myChannel and not #myChannel.
[varName]
(Optional) Pass in custom variables for the suite run that are accessible in your steps via {{varName}}. For example, including &firstName=Justin in the API call will create a {{firstName}} variable with the value Justin in each test run



---cURL EXAMPLES---
Request Examples using cURL
Note: In all cases POST variables will override GET parameters.
GET Request with Parameters:
curl "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/?apiKey=<key>&startUrl=<url>"

POST Request with Parameters:
curl -d "apiKey=<key>" -d "startUrl=<url>" "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/"

POST Request with JSON body:
curl -H 'Content-Type: application/json' -d '{"apiKey": "<key>", "startUrl": "url", "myVar": 99}' 'https://api.ghostinspector.com/v1/suites/<suiteId>/execute/'

POST Multipart Form Request with CSV File:
curl -F "apiKey=<key>" -F "dataFile=@vars.csv" "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/"






--- EXAMPLE Response ---
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2b8538d4c4051afbd22493",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome-79",
      "commentCount": 0,
      "comments": [],
      "console": [
        {
          "_id": "5e2b854365c1671520bc20f9",
          "dateExecuted": "2020-01-25T00:01:01.649Z",
          "error": false,
          "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
          "url": "https://ghostinspector.com/"
        }
      ],
      "dateCreated": "2020-01-25T00:00:56.897Z",
      "dateExecutionFinished": "2020-01-25T00:01:07.629Z",
      "dateExecutionStarted": "2020-01-25T00:00:59.598Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "https://ghostinspector.com/docs/",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": 8031,
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
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-original.png",
          "dims": {
            "h": 2708,
            "w": 1024
          },
          "path": "screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-original.png",
          "size": 221486
        },
        "small": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-small.png",
          "dims": {
            "h": 846,
            "w": 320
          },
          "path": "screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-small.png",
          "size": 70909
        }
      },
      "screenshotCompareBaselineResult": "5e2b7924854c611834aa6cf7",
      "screenshotCompareDifference": 0,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b854565c1671520bc20fe",
          "command": "click",
          "condition": null,
          "dateExecuted": "2020-01-25T00:01:04.221Z",
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
          "_id": "5e2b854565c1671520bc20ff",
          "command": "open",
          "condition": null,
          "dateExecuted": "2020-01-25T00:01:06.030Z",
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
      "suiteResult": "5e2b8538d4c4051afbd22492",
      "test": "5e2a0b342d0f5947444c31fc",
      "testName": "Login and Check Dashboard",
      "urls": [
        "https://ghostinspector.com",
        "https://ghostinspector.com/",
        "https://ghostinspector.com/docs/"
      ],
      "user": {
        "_id": "55b2accc4f66690c07294201",
        "name": "Justin Klemm"
      },
      "uuid": "453ca18c-b21e-4eac-9fc7-ab05b1f4d296",
      "variables": {
        "orgVar": "foo"
      },
      "video": {
        "dims": {
          "h": 768,
          "w": 1024
        },
        "path": "videos/453ca18c-b21e-4eac-9fc7-ab05b1f4d296.mp4",
        "url": "https://ghostinspector-example.s3.amazonaws.com/videos/453ca18c-b21e-4eac-9fc7-ab05b1f4d296.mp4"
      },
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/execute/?apiKey='+apiKey+'&startUrl='+startUrl)
    return res


# Suites, Execute Suite Post
def execute_suite_post(suiteId, startUrl):
    """
    ---POSTIT NOTE---
Note: In all cases POST variables will override GET parameters.





---NOTE---
Note: We execute tests concurrently, however this request can still take some time to return. In general, it will return in the time that it takes to run your longest test; however, this can vary depending on the load on our system and the number of tests being run. We’d suggest programming your request to deal with response times up to 20 minutes. If all the suite's tests are not completed within 20 minutes, the API will send a timeout error (although your tests will still be triggered).



---PARAMS---

apiKey
Your API key provided in your account
suiteId
The ID of the suite to execute
startUrl
(Optional) Alternate start URL to use for all tests in this execution only
browser
(Optional) Alternate browser to use for this execution. The following options are available: chrome (Latest version), chrome-<version> (Specific version of Chrome, for example chrome-83), firefox (Latest version), firefox-<version> (Specific version of Firefox, for example firefox-77).
userAgent
(Optional) Alternate user agent to use for all tests in this execution only
region
(Optional) Geo-location for test execution. The following options are available: us-east-1 (default), us-west-1, ca-central-1, eu-central-1, eu-west-1, eu-west-2, eu-west-3, eu-north-1, me-south-1, ap-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, sa-east-1
httpAuthUsername
(Optional) Alternate HTTP authentication username to use for this execution only
httpAuthPassword
(Optional) Alternate HTTP authentication password to use for this execution only
disableNotifications
(Optional) Use 1 to disable (or 0 to enable) all notifications for this execution only
immediate
(Optional) Use 1 to initiate the execution, then immediate return a response (without results)
dataFile
(Optional) A CSV file containing a row of variable values for each suite run as outlined in our data-driven testing section. A POST request must be used when sending this file. When included, an array of suite results will be returned instead of an array of test result.
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
(Optional) Alternate screen size to use for all tests in this execution only. This should be a string formatted as {width}x{height}, for example 1024x768.
slackChannel
(Optional) Specify the Slack channel to notify for this suite run. Note that the value must be myChannel or %23myChannel and not #myChannel.
[varName]
(Optional) Pass in custom variables for the suite run that are accessible in your steps via {{varName}}. For example, including &firstName=Justin in the API call will create a {{firstName}} variable with the value Justin in each test run



---cURL EXAMPLES---
Request Examples using cURL
Note: In all cases POST variables will override GET parameters.
GET Request with Parameters:
curl "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/?apiKey=<key>&startUrl=<url>"

POST Request with Parameters:
curl -d "apiKey=<key>" -d "startUrl=<url>" "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/"

POST Request with JSON body:
curl -H 'Content-Type: application/json' -d '{"apiKey": "<key>", "startUrl": "url", "myVar": 99}' 'https://api.ghostinspector.com/v1/suites/<suiteId>/execute/'

POST Multipart Form Request with CSV File:
curl -F "apiKey=<key>" -F "dataFile=@vars.csv" "https://api.ghostinspector.com/v1/suites/<suiteId>/execute/"






--- EXAMPLE Response ---
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2b8538d4c4051afbd22493",
      "autoRetry": false,
      "autoRetryTriggered": false,
      "browser": "chrome-79",
      "commentCount": 0,
      "comments": [],
      "console": [
        {
          "_id": "5e2b854365c1671520bc20f9",
          "dateExecuted": "2020-01-25T00:01:01.649Z",
          "error": false,
          "output": "An  element was lazyloaded with loading=lazy, but had no dimensions specified. Specifying dimensions improves performance. See https://crbug.com/954323",
          "url": "https://ghostinspector.com/"
        }
      ],
      "dateCreated": "2020-01-25T00:00:56.897Z",
      "dateExecutionFinished": "2020-01-25T00:01:07.629Z",
      "dateExecutionStarted": "2020-01-25T00:00:59.598Z",
      "disableVisuals": false,
      "disallowInsecureCertificates": false,
      "endUrl": "https://ghostinspector.com/docs/",
      "executionHost": "test001.ghostinspector.net",
      "executionTime": 8031,
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
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-original.png",
          "dims": {
            "h": 2708,
            "w": 1024
          },
          "path": "screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-original.png",
          "size": 221486
        },
        "small": {
          "defaultUrl": "https://ghostinspector-example.s3.amazonaws.com/screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-small.png",
          "dims": {
            "h": 846,
            "w": 320
          },
          "path": "screenshots/453ca18c-b21e-4eac-9fc7-ab05b1f4d296-small.png",
          "size": 70909
        }
      },
      "screenshotCompareBaselineResult": "5e2b7924854c611834aa6cf7",
      "screenshotCompareDifference": 0,
      "screenshotCompareEnabled": true,
      "screenshotComparePassing": true,
      "screenshotCompareThreshold": 0.01,
      "startUrl": "https://ghostinspector.com",
      "steps": [
        {
          "_id": "5e2b854565c1671520bc20fe",
          "command": "click",
          "condition": null,
          "dateExecuted": "2020-01-25T00:01:04.221Z",
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
          "_id": "5e2b854565c1671520bc20ff",
          "command": "open",
          "condition": null,
          "dateExecuted": "2020-01-25T00:01:06.030Z",
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
      "suiteResult": "5e2b8538d4c4051afbd22492",
      "test": "5e2a0b342d0f5947444c31fc",
      "testName": "Login and Check Dashboard",
      "urls": [
        "https://ghostinspector.com",
        "https://ghostinspector.com/",
        "https://ghostinspector.com/docs/"
      ],
      "user": {
        "_id": "55b2accc4f66690c07294201",
        "name": "Justin Klemm"
      },
      "uuid": "453ca18c-b21e-4eac-9fc7-ab05b1f4d296",
      "variables": {
        "orgVar": "foo"
      },
      "video": {
        "dims": {
          "h": 768,
          "w": 1024
        },
        "path": "videos/453ca18c-b21e-4eac-9fc7-ab05b1f4d296.mp4",
        "url": "https://ghostinspector-example.s3.amazonaws.com/videos/453ca18c-b21e-4eac-9fc7-ab05b1f4d296.mp4"
      },
      "viewportSize": {
        "height": 768,
        "width": 1024
      }
    }
  ]
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suites/'+suiteId+'/execute/?apiKey='+apiKey+'&startUrl='+startUrl)
    return res


# Suites, Create Suite
def create_suite():
    """
    Create a suite and return the new suite.

JSON Body
name
Name for the new suite
organization
The ID of the organization this suite should be within

Request Example using cURL

POST Request with JSON body:
curl -H 'Content-Type: application/json' -X POST -d "{"name":"Sweet New Suite", organization: "5a1b419ae40144279f9ac680"}" 'https://api.ghostinspector.com/v1/suites/?apiKey=<apiKey>"'

Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5a1e1b90154014760af39ef5",
    "abortOnTestFailure": false,
    "autoRetry": false,
    "browser": "chrome",
    "dataSource": null,
    "dateCreated": "2017-11-29T02:29:36.132Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "failOnJavaScriptError": false,
    "finalDelay": 0,
    "folder": null,
    "globalStepDelay": 250,
    "httpHeaders": [],
    "language": null,
    "maxAjaxDelay": 10000,
    "maxConcurrentTests": 0,
    "maxWaitDelay": 15000,
    "name": "Sweet New Suite",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "persistVariables": false,
    "publicStatusEnabled": false,
    "region": "us-east-1",
    "screenshotCompareEnabled": false,
    "screenshotCompareThreshold": 0.1,
    "startUrl": "",
    "testCount": 0,
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "variables": [],
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suites/?apiKey='+apiKey)
    return res


# Suites, Update Suite
def update_suite(suiteId):
    """
    Update a suite and return the updated suite.

Request Example using cURL

POST Request with JSON body:
curl -H 'Content-Type: application/json' -X POST -d "{"_id":"<suiteId>", name: "Sweet New Suite (updated)"}" 'https://api.ghostinspector.com/v1/suites/<suiteId>/?apiKey=<apiKey>"'

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5a1e1b90154014760af39ef5",
    "abortOnTestFailure": false,
    "autoRetry": false,
    "browser": "chrome",
    "dataSource": null,
    "dateCreated": "2017-11-29T02:29:36.132Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "failOnJavaScriptError": false,
    "finalDelay": 0,
    "folder": null,
    "globalStepDelay": 250,
    "httpHeaders": [],
    "language": null,
    "maxAjaxDelay": 10000,
    "maxConcurrentTests": 0,
    "maxWaitDelay": 15000,
    "name": "Sweet New Suite (updated)",
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "persistVariables": false,
    "publicStatusEnabled": false,
    "region": "us-east-1",
    "screenshotCompareEnabled": false,
    "screenshotCompareThreshold": 0.1,
    "startUrl": "",
    "testCount": 0,
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "variables": [],
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suites/'+suiteId+'/?apiKey='+apiKey)
    return res


# Suites, Duplicate Suite
def duplicate_suite(suiteId):
    """
    Duplicate a suite and return the new suite.

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b860ed4c4051afbd22496",
    "abortOnTestFailure": false,
    "autoRetry": false,
    "browser": "chrome",
    "dateCreated": "2020-01-25T00:04:30.303Z",
    "dateExecutionTriggered": "1970-01-01T00:00:00.000Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "failOnJavaScriptError": false,
    "finalDelay": 0,
    "folder": "5af3736b34967c7736a5bd33",
    "globalStepDelay": 250,
    "httpHeaders": [],
    "language": null,
    "maxAjaxDelay": 10000,
    "maxConcurrentTests": 0,
    "maxWaitDelay": 15000,
    "name": "Smoke Tests (Copy)",
    "notifications": {},
    "notificationsSuite": {},
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "persistVariables": false,
    "publicStatusEnabled": false,
    "region": "us-east-1",
    "screenshotCompareEnabled": false,
    "screenshotCompareThreshold": 0.1,
    "startUrl": "",
    "testCount": 1,
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "firstName": "Justin",
      "lastName": "Klemm"
    },
    "variables": [],
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/duplicate/?apiKey='+apiKey)
    return res


# Suites, Duplicate Suite Post
def duplicate_suite_post(suiteId):
    """
    Duplicate a suite and return the new suite.

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b860ed4c4051afbd22496",
    "abortOnTestFailure": false,
    "autoRetry": false,
    "browser": "chrome",
    "dateCreated": "2020-01-25T00:04:30.303Z",
    "dateExecutionTriggered": "1970-01-01T00:00:00.000Z",
    "disableVisuals": false,
    "disallowInsecureCertificates": false,
    "failOnJavaScriptError": false,
    "finalDelay": 0,
    "folder": "5af3736b34967c7736a5bd33",
    "globalStepDelay": 250,
    "httpHeaders": [],
    "language": null,
    "maxAjaxDelay": 10000,
    "maxConcurrentTests": 0,
    "maxWaitDelay": 15000,
    "name": "Smoke Tests (Copy)",
    "notifications": {},
    "notificationsSuite": {},
    "organization": {
      "_id": "5a1b419ae40144279f9ac680",
      "name": "Ghost Inspector"
    },
    "persistVariables": false,
    "publicStatusEnabled": false,
    "region": "us-east-1",
    "screenshotCompareEnabled": false,
    "screenshotCompareThreshold": 0.1,
    "startUrl": "",
    "testCount": 1,
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "user": {
      "_id": "55b2accc4f66690c07294201",
      "firstName": "Justin",
      "lastName": "Klemm"
    },
    "variables": [],
    "viewportSize": {
      "height": 768,
      "width": 1024
    }
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suites/'+suiteId+'/duplicate/?apiKey='+apiKey)
    return res


# Suites, Import Test
def import_test(suiteId):
    """
    Import a test in Ghost Inspector JSON or Selenium HTML format and return the new test.

Request Example using cURL

POST with JSON file:
curl -X POST -H "Content-Type: application/json" -d @test.json "https://api.ghostinspector.com/v1/suites/<suiteId>/import-test/?apiKey=<apiKey>"

POST with HTML file:
curl -F "apiKey=<key>" -F "dataFile=@test.html" https://api.ghostinspector.com/v1/suites/<suiteId>/import-test/

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5e2b889bd4c4051afbd2249b",
    "autoRetry": null,
    "browser": null,
    "dateCreated": "1970-01-01T00:00:00.000Z",
    "dateExecutionFinished": "1970-01-01T00:00:00.000Z",
    "dateExecutionStarted": "1970-01-01T00:00:00.000Z",
    "dateExecutionTriggered": "1970-01-01T00:00:00.000Z",
    "dateUpdated": "2020-01-25T00:15:23.670Z",
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
        "enabled": true,
        "options": {
          "urls": [
            {
              "condition": null,
              "url": "http://requestbin.net/r/19hsp471"
            }
          ]
        }
      }
    },
    "organization": {},
    "passing": null,
    "publicStatusEnabled": true,
    "region": null,
    "screenshotCompareEnabled": true,
    "screenshotComparePassing": null,
    "screenshotCompareThreshold": 0.01,
    "startUrl": "https://ghostinspector.com",
    "steps": [
      {
        "command": "click",
        "condition": null,
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
    "suite": {},
    "testFrequency": 0,
    "testFrequencyAdvanced": [],
    "user": "55b2accc4f66690c07294201",
    "viewportSize": null
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/suites/'+suiteId+'/import-test/?apiKey='+apiKey)
    return res


# Suites, List Suite Tests
def list_suite_tests(suiteId):
    """
    Fetch an array of all the tests in a suite.



example Response
{
  "code": "SUCCESS",
  "data": [
    {
      "_id": "5e2a0b342d0f5947444c31fc",
      "autoRetry": null,
      "browser": null,
      "dataSource": null,
      "dateCreated": "2020-01-23T21:08:04.664Z",
      "dateExecutionFinished": "2020-01-25T00:01:07.629Z",
      "dateExecutionStarted": "2020-01-25T00:00:59.598Z",
      "dateUpdated": "2020-01-25T00:00:47.041Z",
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
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/tests/?apiKey='+apiKey)
    return res


# Suites, List Suite Results
def list_suite_results(suiteId):
    """
    Fetch an array of suite results for a suite.

Parameters
apiKey
Your API key provided in your account
suiteId
The ID of the suite containing the results
count
The number of results to return (default 10, maximum 50)
offset
The number of results to offset the returned set by (default 0)

example Response {
  "code": "SUCCESS",
  "data": [
    {
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
    },
    {
      "_id": "5e2b8538d4c4051afbd22492",
      "commentCount": 0,
      "comments": [],
      "countFailing": 0,
      "countPassing": 1,
      "countScreenshotCompareFailing": 0,
      "countScreenshotComparePassing": 1,
      "countScreenshotCompareUnknown": 0,
      "countUnknown": 0,
      "dateCreated": "2020-01-25T00:00:56.865Z",
      "dateExecutionFinished": "2020-01-25T00:01:11.958Z",
      "dateExecutionStarted": "2020-01-25T00:00:56.865Z",
      "executionTime": 15093,
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
  ]
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/results/?apiKey='+apiKey)
    return res


# Suites, List Suite Results CSV
def list_suite_results_csv(suiteId):
    """
    Fetch a CSV formatted export of suite results for a suite. Results are returned in reverse chronological order (newest first).

Parameters
apiKey
Your API key provided in your account
suiteId
The ID of the suite containing the results
count
The number of results to return (default 10, maximum 50)
offset
The number of results to offset the returned set by (default 0)

example Response
Suite Result ID,Suite Result URL,Name,Start URL,Tests Passed,Screenshots Passed,Tests Passing,Tests Failing,Test Unknown,Screenshots Passing,Screenshots Failing,Screenshots Unknown,Duration,Date Triggered,Date Started,Date Completed
5ec56cab7295aa759378d48f,https://app.ghostinspector.com/suite-results/5ec56cab7295aa759378d48f,Scheduler Testing,undefined,true,false,2,0,0,0,1,1,25.118,2020-05-20T17:45:15.139Z,2020-05-20T17:45:15.152Z,2020-05-20T17:45:40.270Z
5ec56c337295aa759378d48b,https://app.ghostinspector.com/suite-results/5ec56c337295aa759378d48b,Scheduler Testing,undefined,true,false,2,0,0,0,1,1,30.15,2020-05-20T17:43:15.186Z,2020-05-20T17:43:15.210Z,2020-05-20T17:43:45.360Z
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/results/csv/?apiKey='+apiKey)
    return res


# Suites, Download Suite Tests JSON
def download_suite_tests_json(suiteId):
    """
    Download a zip file of all tests in Ghost Inspector format (.json).

Response
[ Zip file containing all tests in Ghost Inspector JSON format will be returned ]
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/export/json/?apiKey='+apiKey)
    return res


# Suites, Download Suite Tests side
def download_suite_tests_side(suiteId):
    """
    Download a JSON file of all tests in Selenium IDE format (.side).

sample Response
{
  "id": "ce572f2a-8e4f-4a1e-8f69-9e3de21d2350",
  "version": "1.1",
  "name": "Sample Suite",
  "url": "",
  "tests": [
      {
      "id": "9b449d9b-28f1-4106-8aae-b1e4c8853626",
      "name": "Test #1",
      "commands": [
          {
          "command": "open",
          "target": "https://ghostinspector.com/",
          "value": ""
          },
          {
          "command": "setWindowSize",
          "target": "1024x768",
          "value": ""
          }
      ]
      },
      {
      "id": "a727f3c0-57a1-4d22-8097-54ab34288249",
      "name": "Test #2",
      "commands": [
          {
          "command": "open",
          "target": "https://ghostinspector.com",
          "value": ""
          },
          {
          "command": "setWindowSize",
          "target": "1024x768",
          "value": ""
          }
      ]
      }
  ],
  "suites": [
      {
      "id": "36f02748-d241-4da4-9382-a8b4a438b262",
      "name": "Sample Suite",
      "persistSession": false,
      "parallel": false,
      "timeout": 600,
      "tests": [
          "9b449d9b-28f1-4106-8aae-b1e4c8853626",
          "a727f3c0-57a1-4d22-8097-54ab34288249"
      ]
      }
  ],
  "plugins": []
}
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/export/selenium-side/?apiKey='+apiKey)
    return res


# Suites, Download Suite Tests HTML
def download_suite_tests_html(suiteId):
    """
    Download a zip file of all tests in Selenium IDE format (.html).

Response
[ Zip file containing all tests in Selenium HTML format will be returned ]
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/export/selenium-html/?apiKey='+apiKey)
    return res


# Suites, Suite Status Badges
def suite_status_badges(suiteId):
    """
    Note: Status badges are disabled by default and can be enabled under Suite Settings > Details > Enable Status Badge.

Real-time embeddable status badges for your suite. Will return the appropriate status badge image based on the current status of your last suite result.


Statuses
Passing
 All tests from the last completed run of this suite passed.
Partially Failing
 The last completed run of this suite had partial test failures.
Failing
 All tests from the last completed run of this suite failed.
Running
 Suite execution is in progress.
Unknown
 The suite has no previous execution or the last execution was cancelled.
Screenshot Compare
 The screenshot comparisons for this suite are passing.


Example usage
<img src="https://api.ghostinspector.com/v1/suites/<suiteId>/status-badge" title="My suite status">
    """
    res = requests.get('https://api.ghostinspector.com/v1/suites/'+suiteId+'/status-badge)
    return res

