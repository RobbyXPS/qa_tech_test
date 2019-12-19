# **QA Candidate Test**

- Each test section has it's own folder (command shell, databases, browser testing, test authoring, exploratory, rest api).
- Each folder contains relevant screenshots and other reference material. 
- The test also mentioned to write out my thought process as I worked so I tried to capture some of that in the my_thoughts.txt file.



## **Status:**

All test sections except 'command shell' have been completed. 


## **Answers:**

### **Command Shell:**
*A.* Terminal Script that updates strings in a file.

*Answer:* Meets simple requirement but could use more updates.
- https://github.com/RobbyXPS/qa_tech_test/tree/master/01_command_shell

*B.* Terminal script that copies and moves files.
Answer: Have not started.

### **Databases**
*A.* Write a query to list all of the large (L) clients
*Answer:*
```
SELECT * FROM jama_test01.clients
WHERE size='L';
```
- Screenshots: https://github.com/RobbyXPS/qa_tech_test/tree/master/02_databases

*B.* Write a query to enable a feature called “SpaceshipPlugin”
*Answer:* 
```
UPDATE jama_test01.features
SET enabled = ’T’
WHERE name = 'SpaceshipPlugin';
```

*C.* Write a query to list all of the features that were added in 2017
*Answer:*
```
SELECT *
FROM jama_test01.features 
WHERE 
    addeddate >= '2017-01-01T00:00:00.000' AND 
    addeddate <= '2017-12-31T23:59:59.599'
```

### **Browser Testing**
*A.* Jama logo image id
*Answer:* "j-homescreen-logo"

*B.* Full Jama version
*Answer:* "v. 8.44.0 sha-234ac17"

### **Test Authoring***
*Answer:* Test plan and verify of cases can be found here https://github.com/RobbyXPS/qa_tech_test/tree/master/04_test_authoring

### **Exploratory Testing**
*Answer:* Testing doc and screenshots can be found here https://github.com/RobbyXPS/qa_tech_test/tree/master/05_exploratory

### **REST API**
*A.* GET Single comment
*Answer:*
```
curl -X GET "https://qaexercise.jamacloud.com/rest/v1/comments/107" -H "accept: application/json" -H "jama-csrf-token: 95e24cef-176a-4d68-b90c-9b24cd14fb9f"
```

*B.* POST new comment
*Answer:*
```
curl -X POST "https://qaexercise.jamacloud.com/rest/v1/comments" -H "accept: application/json" -H "Content-Type: application/json" -H "jama-csrf-token: 95e24cef-176a-4d68-b90c-9b24cd14fb9f" -d "{ \"body\": { \"text\": \"HEYOH\" }, \"commentType\": \"GENERAL\"}"
```

*C.* GET current user
*Answer:*
```
{
  "meta": {
    "status": "OK",
    "timestamp": "2019-12-17T22:36:54.972+0000"
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
*D.* Explore API
*Answer:* See https://github.com/RobbyXPS/qa_tech_test/blob/master/06_rest_api/rest_api_D_explore.txt
