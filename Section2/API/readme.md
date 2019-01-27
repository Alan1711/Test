## The Tools You Need

### Newman Postman

npm install -g newman

Guide here: https://www.npmjs.com/package/newman

## Create Gist

Replace {{userToken}} with a user token obtained from GitHub
navigate to Section2/API/ and run from Terminal 'newman run CreateGist.json'

## List User Gists

Replace {{userToken}} with a user token obtained from GitHub
Replace {{userName}} with the associated GitHub user name
navigate to Section2/API/ and run from Terminal 'newman run ListUserGist.json'

## Delete User Gists

Replace {{userToken}} with a user token obtained from GitHub
Replace {{gistId}} with the ID of the gist you wish to delete
navigate to Section2/API/ and run from Terminal 'newman run DeleteGist.json'
