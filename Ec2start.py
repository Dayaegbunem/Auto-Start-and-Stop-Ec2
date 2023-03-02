import boto3
client=boto3.client('ec2')
data=client.describe_instances()
minidata=data['Reservations']
for info in minidata:
    instanceid=info['Instances']
    for instanceids in instanceid:
        Instance_id=instanceids['InstanceId']
        id_state=instanceids['State']['Name']
        if id_state=='stopped':
            client.start_instances(InstanceIds=[Instance_id])