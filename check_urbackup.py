
#!/usr/bin/env python3
# Written By:Tal Bar-Or'
# Created - 21/12/2016
# check_urbackup for backup status
#Ver 0.3import urbackup_api
#simple script to check Urbackup backup status used by https://github.com/uroni/urbackup-server-python-web-api-wrapper
#source code found at https://bitbucket.org/tal_bar_or/check_urbackup
import urbackup_api
import datetime,sys
import time,argparse






ClientPrint = ""
GlobalStatus = []
Globelstat = ""



def Statuscheck(client):
    global ClientPrint
    ClientStatus = ""
    if client["delete_pending"] != 0 and client["file_ok"] == True and client["online"] == True:
        ClientStatus = "OK"
        ClientPrint +="HostName:"+client["name"] +", ClintStatus:Online" +", LastBackup:"+ datetime.datetime.fromtimestamp(client["lastbackup"]).strftime("%x %X") \
              +", File_back_statusclient:OK"+", Status:OK" +'\n'

        return ClientStatus

    elif client["delete_pending"] != 0 and client["file_ok"] != True and client["online"] == True:
        ClientStatus = "Critical"

        ClientPrint += "HostName:" + client["name"] + ", ClintStatus:Online" + ", LastBackup:" + datetime.datetime.fromtimestamp(client["lastbackup"]).strftime("%x %X") \
                       + ", File_back_statusclient:Critical"+", Status:Critical" + '\n'
        return ClientStatus

    elif client["delete_pending"] != 0 and client["file_ok"] != True and client["online"] != True:
        ClientStatus = "Critical"
        ClientPrint += "HostName:" + client["name"] + ", ClintStatus:Down" + ", LastBackup:" + datetime.datetime.fromtimestamp(client["lastbackup"]).strftime("%x %X") \
                       + ", File_back_statusclient:Critical" +", Status:Critical"+ '\n'

        return ClientStatus

    elif client["delete_pending"] != 0 and client["file_ok"] == True and client["online"] != True:
        ClientStatus = "Warning"
        ClientPrint += "HostName:" + client["name"] + ", ClintStatus:Down" + ", LastBackup:" + datetime.datetime.fromtimestamp(client["lastbackup"]).strftime("%x %X") \
                       + ", File_back_statusclient:OK" +", Status:Warning" + '\n'

        return ClientStatus




parser = argparse.ArgumentParser()
parser.add_argument('--version','-v',action="store_true",help='show agent version')
parser.add_argument('--host','-ho',action="append",help='host name or IP')
parser.add_argument('--user','-u',action="append",help='User name for Urbackup server')
parser.add_argument('--password','-p',action="append",help='user password for Urbackup server')
args = parser.parse_args()

if args.host or args.user or args.password:
    try:
        server = urbackup_api.urbackup_server("http://"+ args.host[0] +":55414/x", args.user[0], args.password[0])
        clients = server.get_status()
        for client in clients:
            GlobalStatus.append(Statuscheck(client))
            Globelstat = set(GlobalStatus)
        while True:
            if "Critical" in Globelstat:
                #print(Globelstat)
                print("CRITICAL")
                break
            elif "Warning" in Globelstat:
                #print(Globelstat)
                print("WARNING")
                break
            elif "OK" in Globelstat:
                #print(Globelstat)
                print("OK")
                break
            else:
                print("UNKOWN")
                break
        print(ClientPrint)

    except Exception as e:

        print("Error Occured: ",e)


elif args.version:
    print('1.0 Urback Check ,Written By:Tal Bar-Or')
    sys.exit()
else:
    print("please run check --host <IP OR HOSTNAME> --user <username> --password <password>"+ '\n or use --help')
    sys.exit()
