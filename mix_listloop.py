#!/usr/bin/python3

def main():

    networklists = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['ios-xr', '10.0.3.1'], ['junos', '10.0.10.1'], ['eos', '10.0.14.1']]
    for driveandip in networklists:
         print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])
main()
