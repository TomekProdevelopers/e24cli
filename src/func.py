import boto3
class Cfg:
    ec2 = None
cfg = Cfg()

class check_profile(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):    
        if cfg.ec2 is None:
            print("Please set up profile: e24 or aws")
            return
        self.f(*args)    


def set_default_profile(params_args):
    profile = params_args.profile[0]
    boto3.setup_default_session(profile_name= profile)
    if profile == 'e24':
        ec2 = boto3.resource('ec2',  endpoint_url ='https://eu-poland-1poznan.api.e24cloud.com')
    else:
        ec2 = boto3.resource('ec2')
    cfg.ec2 = ec2
    #print("EC2 set_default_profile: " + str(ec2))
    #print("EC2 cfg set_default_profile: " + str(cfg.ec2 ))


# def print_ec2():
#     print("EC2: " + str(cfg.ec2))

@check_profile
def get_images_list(pattern):
    ids = pattern.filter
    print("id " + str(ids) )
    if ids == None or len(ids) == 0:
        images = cfg.ec2.images.all()
    else:
        images = cfg.ec2.images.filter( ImageIds=[ids])   
    for img in images:
        print('Image: id:{0}, architecture:{1}, description:{2}, platform:{3}'.format(img.id,img.architecture,img.description, img.platform ))

@check_profile
def get_instances_list(pattern):
    intsances = cfg.ec2.instances.all()
    for ins in intsances:
        print("Instance: Id: {0} state: {1} type:{1}  image id:{2} image_id:{3}".format(ins.id, ins.state, ins.instance_type, ins.image_id))

@check_profile
def create_instance(pattern):
    image_id = pattern.image_id[0]
    instance_type = pattern.instance_type[0]
    instances = cfg.ec2.create_instances(ImageId=image_id, MinCount =  1, MaxCount = 1, InstanceType=instance_type)#m1.small
    for ins in instances:
        print("Instance: Id: {0} state: {1} type:{2}  image id:{3}".format(ins.id, ins.state, ins.instance_type, ins.image_id))

def terminate_instance(pattern):
    id=pattern.id[0]
    ints = cfg.ec2.Instance(id)
    ints.terminate()
    print("Instance has been terminated: Id: {0} state: {1} type:{2}  image id:{3}".format(ints.id, ints.state, ints.instance_type,ints.image_id))

def stop_instance(pattern):
    id=pattern.id[0]
    ints = cfg.ec2.Instance(id)
    ints.stop()
    print("Instance has been stoped: Id: {0} state: {1} type:{2}  image id:{3}".format(ints.id, ints.state, ints.instance_type,ints.image_id))

def start_instance(pattern):
    id=pattern.id[0]
    ints = cfg.ec2.Instance(id)
    ints.start()
    print("Instance has been started: Id: {0} state: {1} type:{2}  image id:{3}".format(ints.id, ints.state, ints.instance_type,ints.image_id))