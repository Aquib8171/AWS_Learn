import boto3
region = 'ap-south-1'
instances = ['i-0b0bbc32e2353c00']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started your instance(s): ' + str(instances))
