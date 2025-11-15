import boto3
region = 'ap-south-1'
instances = ['i-0b0bbc32e2353c00']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('Stopped your instance(s): ' + str(instances))
