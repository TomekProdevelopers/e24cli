import boto3
import argparse
import commands
import func
ec2 = None

cmds = commands.get_commands() 
while True:
   # func.print_ec2()
    args = input(">")
    args_list = args.split()
    if(len(args_list) < 1):
        print("Incorect command")
        continue
    if(args_list[0]=="exit"):
        quit()
    if(args_list[0] not in cmds.keys()):
        print("Incorect command:{0}".format(cmds.keys()))
        continue
    cmd = cmds.get(args_list[0])
    cmd_func = cmd[1]
    parser = cmd[0]
    try:
        parse_args = parser.parse_args(args_list[1:])
    except SystemExit:
        continue
    cmd_func(parse_args)
   