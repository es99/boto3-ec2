import boto3
import json
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def mostraInstancias():
    response = ec2.describe_instances()

    for instances in response['Reservations']:
        for instance in instances['Instances']:
            print("Name: ", instance["Tags"][0]["Value"])
            print("InstanceId: ", instance["InstanceId"])
            print("ImageId: ", instance["ImageId"])
            print("VpcId: ", instance["VpcId"])
            print("SubnetId: ", instance["SubnetId"])
            print("Public ip: ", instance.get("PublicIpAddress", "não possui"))
            print("Private Ip: ", instance["PrivateIpAddress"])
            print("Status: ", instance["State"]["Name"])
            print("InstanceType: ", instance["InstanceType"])
            print("Keyname: ", instance["KeyName"])
            print("Security Group Id: ", instance["SecurityGroups"][0]["GroupId"])
            print('-' * 30)

def iniciarInstancia(instanceId):
    try:
        ec2.start_instances(
            InstanceIds=[instanceId], DryRun=True
        )
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    try:
        response = ec2.start_instances(
            InstanceIds=[instanceId], DryRun=False
        )
    except ClientError as e:
        print(e)
    print(json.dumps(response.get('StartingInstances'), indent=4, default=str))
    return True

def pararInstancia(instancia):
    try:
        ec2.stop_instances(
            InstanceIds = [instancia],
            Hibernate=False,
            DryRun=True,
            Force=False
        )
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    
    try:
        response = ec2.stop_instances(
            InstanceIds = [instancia],
            Hibernate=False,
            DryRun=False,
            Force=False
        )
    except ClientError as e:
        print(e)
    print(json.dumps(response.get('StoppingInstances'), indent=4, default=str))
    return True