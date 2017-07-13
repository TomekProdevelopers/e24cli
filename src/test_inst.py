import boto3
boto3.setup_default_session(profile_name= 'e24')
ec2 = boto3.resource('ec2',  endpoint_url ='https://eu-poland-1poznan.api.e24cloud.com')
intsances = ec2.instances.all()
for ins in intsances:
    print("Instance: Id: {0} state: {1} type:{1}  image id:{2} image_id:{3}".format(ins.id, ins.state, ins.instance_type, ins.image_id))



import boto3
ec2 = boto3.resource('ec2',
                    aws_access_key_id='test_key', 
                    aws_secret_access_key='test_secret', 
                    region_name = 'eu-poland-1poznan',
                    endpoint_url ='https://eu-poland-1poznan.api.e24cloud.com')

ins = ec2.create_instances(ImageId='ami-000008dc', MinCount =  1, MaxCount = 1, InstanceType='m1.small')#m1.small
print("Instance: Id: {0} state: {1} type:{2}  image id:{3}".format(ins.id, ins.state, ins.instance_type, ins.image_id))