# Setup
To run the project on your machine you need to have docker and docker-compose installed on your machine. 
Also you need to add a <code><b>.env</b></code> file to the project base directory.<br/>
Example of a <code><b>.env</b></code> file:<br/>
<code><b>FLASK_APP=main<br/>
DEBUG=False<br/>
SECRET_KEY=key # a specific secret key<br/>

API_ID=id # the id of the app owner<br/>
API_HASH=hash # the hash of the app owner<br/>
OWNER_CREDS=+380xxxxxxxxx # the number of the account owner<br/>
</b>
</code>
# Run
To run project you need to execute following commands:<br/>
1. The first command creates a docker container:<br/>
<code><b>docker-compose build</b></code>
2. The second command run created by the previous command container:<br/>
<code><b>docker-compose up</b></code>
