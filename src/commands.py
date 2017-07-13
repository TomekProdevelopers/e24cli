import func
import argparse
# pars_set_profile = argparse.ArgumentParser(prog= "set_profile")
# #pars_set_profile.add_argument("profile",nargs= 1, type = str,  choices=['e24','aws'])
# args= {'nargs': 1, 'type':str, 'choices':['e24','aws'] } 
# pars_set_profile.add_argument("profile", **args)
# commands = {"set_profile": pars_set_profile}
# commands["exit"] = pars_set_profile

cmd_def= {"set_profile": [{"profile":{'nargs': 1, 'type':str, 'choices':['e24','aws'] }} , func.set_default_profile] }
cmd_def["get_images"] = [{"filter":{'nargs':'?','type':str}} , func.get_images_list] 
cmd_def["get_instances"] = [{"filter":{'nargs':'?','type':str}} , func.get_instances_list] 
cmd_def["create_instance"] = [{"image_id":{'nargs':1,'type':str},"instance_type":{'nargs':1,'type':str}  } , func.create_instance] 


def get_commands():
    commands = {}
    for cmd in cmd_def.keys():
        parser = argparse.ArgumentParser(prog= cmd)
        params = cmd_def.get(cmd)[0]
        func = cmd_def.get(cmd)[1]
        for param in params.keys():
            parser.add_argument(param, **params.get(param))
        commands[cmd] =[parser, func]
    return commands