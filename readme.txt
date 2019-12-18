Lipsum file notes:
- generated with http://generator.lorem-ipsum.info/_latin

File 01 (normal lorem Epsom large): 15 occurrences 
File 02 (normal lorem Epsom + old English + !?): 7 occurrences 
File 03 (normal lorem Epsom small): 3 occurrences
File 04 (different versions of 'contour'): 4 occurrences
File 05 (empty file): 0 occurrences


- todos:
- test with empty line at end of file





Objective:


Notes:
- make sure to test with different versions of countour (regex)
- mySQL + Workbench resources
	- https://www.youtube.com/watch?v=ltYNt44c2xo


Ref:
-simple example: https://pythonexamples.org/python-replace-string-in-file/










Browser Testing

IMPORTANT: Please avoid the use of any personally identifying information (real name, email address, etc) in the test system.

For this portion, you will need to navigate to the Jama URL you were given along with this test.

A. Find the id of the Jama logo image on the Jama login page
	Answer: j-homescreen-logo


B. Find the full version of Jama. Hint: it’s hidden in the DOM. What is the element’s class name it is hidden under?
	Answer: Version = 8.44.0 Class = j-login-version-number


Test Authoring

Write some test cases for the following story:

As a user of Jama, I would like to log in to Jama using SSO/Active Directory authentication, instead of Jama authentication, so that logging into Jama is simpler.


Exploratory

Spend 30-60 minutes performing exploratory testing on the Jama application. Find, write down, and/or take screenshots of all of the quirks and possible bugs you can find. Are there any features you would change? Write that down, too! We want to see your tester mind at work!

	Answer: Session based testing document and images of issues can be found in ~/qa_tech_test/05_exploratory directory


REST API

Now that you have some familiarity with Jama, navigate to the java url + /api-docs/, ex https://
candidate.jamacloud.com/api-docs You will need to log in to access the API reference documentation, which you should use to answer the following questions.

A. How would you get a single comment using the REST API? The answer should be a single request URL
	Answer:
```
curl -X GET "https://qaexercise.jamacloud.com/rest/v1/comments/107" -H "accept: application/json" -H "jama-csrf-token: 95e24cef-176a-4d68-b90c-9b24cd14fb9f"
```

B. How would you post a new comment using the REST API? The answer should be a request URL plus a JSON object. Hint: you only need to specify the “body” and “commentType” objects.
	Answer:
```
curl -X POST "https://qaexercise.jamacloud.com/rest/v1/comments" -H "accept: application/json" -H "Content-Type: application/json" -H "jama-csrf-token: 95e24cef-176a-4d68-b90c-9b24cd14fb9f" -d "{ \"body\": { \"text\": \"HEYOH\" }, \"commentType\": \"GENERAL\"}"
```

C. Use the API to get the current user (you). The answer should be the JSON response body that is returned
	Answer:
```
{
  "meta": {
    "status": "OK",
    "timestamp": "2019-12-17T21:54:13.802+0000"
  },
  "links": {},
  "data": {
    "id": 28,
    "username": "candidate-75730",
    "firstName": "Candidate",
    "lastName": "Candidate 75730",
    "email": "no@no.no",
    "title": "75730",
    "licenseType": "FLOATING",
    "active": true,
    "type": "users"
  }
}
```

D. Bonus: Do some exploratory testing around the REST API documentation and write down any thoughts or suggestions you might have

- I wasn't able to get the suggested curl request working in my console. There might be some more info we can pass to users around how to better handle that issue. I think I am running into a `CSRF Exception` but I'm not sure what I am doing incorrectly. See ~/qa_tech_test/06_rest_api/csrf_exception_notes.txt for more info.

- Bug: API for comment POST returns a 500 error if sent in the format suggested by the documentation. See ~/qa_tech_test/06_rest_api/potential_issues_images/unsuccessful_post_comment.png for more info.
