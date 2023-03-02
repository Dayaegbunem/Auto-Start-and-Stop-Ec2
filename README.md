# Auto-Start-and-Stop-Ec2
Automation of Ec2 start and stop using Lambda
Abstract:
The need to automate the starting and stopping of ec2 to minimize cost to an organization.

Purpose:
A business starts the day at 7am, closes at 5pm and has no need to run its infrastructure all through the night. This system can help.

Step 1:
Install into the pc , if you do not have already:
Python, aws cli,vscode. 

Step 2:
Create a Lambda function on aws console. You could name it ‘ec2start’, Select python 3.7, attach the appropriate permission, increase the timeout runtime to 15mins and deploy the lambda.

Step 3:
Create a second Lambda function on aws console. You could name it ‘ec2stop’, Select python 3.7, attach the appropriate permission, increase the timeout runtime to 15mins and deploy the lambda.

Step 4:
Paste the Ec2start.py code in the lambda function deployed in step2 and the Ec2stop.py code in the lambda function created in step3.

How to use
===============================
Go to amazon EventBridge on the aws console to set up rules. Create 2 rules that  run on a recurring schedule. First rule is to schedule when the lambda function created in step 2 will start and second rule is when the lambda function created in step3 is going to stop.
