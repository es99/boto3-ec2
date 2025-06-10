import boto3
import json

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
            print("Private Ip: ", instance["PrivateIpAddress"])
            print("Status: ", instance["State"]["Name"])
            print("InstanceType: ", instance["InstanceType"])
            print("Keyname: ", instance["KeyName"])
            print("Security Group Id: ", instance["SecurityGroups"][0]["GroupId"])
            print('-' * 30)