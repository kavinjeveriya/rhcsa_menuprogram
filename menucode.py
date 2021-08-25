#!/usr/python3

import os
import subprocess as sp
import getpass


def MENU():
    sp.getoutput('clear')
    print('---------------Services--------------')
    print('1. AWS')
    print('2. Docker')
    print('3. Hadoop')
    print('4. lvm')
    print('5. Webserver')
    print('6. Quit the program')
    service = input('Service you want - ')
    if service == '1':
        awsconf()
    elif service == '2':
        dockerconf()
    elif service == '3':
        cluster()
    elif service == '4':
        lvm()
    elif service == '5':
        webser_conf()
    elif service == '6':
        exit()
    else :
        print('unsupported input')


def dockerconf():
    status = sp.getstatusoutput('docker --version | echo $?')
    if status == 0 :
        print("Hello sir DOCKER is not installed on your machine")
        ch = input('''
        press y/n for installing or not installing respectivly - ''')
        if ch == y :
            os.system('yum install yum-utils -y')
            os.system('yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
            os.system('yum install docker-ce --nobest -y')
        else :
            print("Try again,Thank you!!!")
    else :
        sp.getoutput('clear')
        print("\n---------------DOCKER--------------\n")
        print("1. Docker daemon start/stop/status services")
        print("2. Show docker process")
        print("3. Show docker images")
        print("4. Search images on docker hub")
        print("5. Download docker image from docker hub")
        print("6. Run a docker image")
        print("7. Stop docker container")
        print("8. Delete docker image")
        print("9. Configure webserver(httpd) in docker container")
        command = int(input('\nEnter your choice - '))
        if command == 1:
            op = int(input('1.start  2.stop  3.status'))
            if op == 1: print(sp.getoutput('systemctl start docker'))
            elif op == 2: print(sp.getoutput('sytemctl stop docker'))
            elif op == 3: print(sp.getoutput('systemctl status docker'))
            else: print('unsupported input')
        elif command == 2:
            op = int(input('1.Recent process  2.All process'))
            if op == 1: print(sp.getoutput('docker ps'))
            elif op == 2: print(sp.getoutput('docker ps -a'))
            else: print('unsupported input')
        elif command == 3: print(sp.getoutput('docker images'))
        elif command == 4:
            im = input('image name - ')
            print(sp.getoutput('docker search {}'.format(im)))
        elif command == 5:
            im = input('image name - ')
            print(sp.getoutput('docker pull {}'.format(im)))
        elif command == 6:
            im = input('image name - ')
            sp.getoutput('docker run -it {} &'.format(im))
        elif command == 7:
            im = input('OS name - ')
            sp.getoutput('docker stop {}'.format(im))
        elif command == 8:
            im = input('image name - ')
            sp.getoutput('docker rmi {}'.format(im))
        elif command == 9:
            httpdconf()
        else: print('Error')

def httpdconf():
    check = sp.getoutput('docker ps --format "{{.Status}}" | grep Exited | echo $?')
    if check == '0' :
        print('No container is not running, run a container first')
    else :
        c1 = sp.getoutput('docker exec -it `docker ps --format "{{.Names}}"` yum install httpd | echo $?')
        c2 = sp.getoutput('docker exec -it `docker ps --format "{{.Names}}"` /usr/sbin/httpd | echo $?')
        if c1 and c2 == 0:
            print('\nWebserver configured successfully!\n')

def awsconf():
        sp.getoutput('clear')
        print('\n---------------Services--------------\n')
        print(' EC2')
        print(' EBS')
        print(' S3 ')
        aws_ser = input('Enter here : ')
        if aws_ser == 'EC2' or aws_ser == 'ec2' :
                ec2conf()
        elif aws_ser == 'EBS' or aws_ser == 'ebs':
                ebsconf()
        elif aws_ser == 'S3' or aws_ser == 's3':
                s3conf()
        else :
                print('unsupported input')

def ec2conf():
    sp.getoutput('clear')
    print("\n----------------EC2---------------\n")
    print("1. Create/Delete Key Pair")
    print("2. Create/Delete Security group")
    print("3. EC2 instance start/stop/terminate")
    print("4. Show all instances ")
    print("5. Create new Instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        kp = int(input('1.Create  2.Delete '))
        if kp == 1:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 create-key-pair --key-name {0}'.format(key_name))
        elif kp == 2:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 delete-key-pair --key-name {0}'.format(key_name))
        else :
            print('unsupported input')
    elif command ==2:
        sg = int(input('1.Create  2.Delete '))
        if sg == 1:
            se_group_name = input("Enter name for security group : ")
            se_disc = input("Enter description for security group : ")
            sp.getoutput('aws ec2 create-security-group --group-name {0} --description {1}'.format(se_group_name, se_disc))
        elif sg == 2:
            se_grp_id = input("Enter id of security group :")
            sp.getoutput('aws ec2 delete-security-group --group-id{0}'.format(se_grp_id))
        else :
            print('unsupported input')
    elif command == 3:
        ins_id = input(" Enter Instance ID : ")
        op = int(input('1.start  2.stop  3.terminate'))
        if op == 1:
            sp.getoutput('aws ec2 start-instances --instance-ids {0}'.format(ins_id))
        elif op == 2:
            sp.getoutput('aws ec2 stop-instances --instance-ids {0}'.format(ins_id))
        elif op == 3:
            sp.getoutput('aws ec2 terminate-instances --instance-ids {0}'.format(ins_id))
        else:
            print('unsupported input')
    elif command == 4:
        l= sp.getoutput('aws ec2 describe-instances')
        print(l)
    elif command == 5:
        img_id = input("Enter image id : ")
        img_type = input("Enter image type : ")
        subnet_id = input("Enter subnetId : ")
        se_id = input("Enter security group id : ")
        key_name = input("Enter created  key name : ")
        sp.getoutput('aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}'.format(
                img_id, img_type, subnet_id, se_id, key_name))
    else :
        print('unsupported input')

def ebsconf():
    sp.getoutput('clear')
    print("\n--------------EBS-------------\n")
    print("1. Create EBS volume")
    print("2. Attach EBS volume to EC2 instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        vt = input("Enter the type of volume : ")
        size = input("Enter the size of volume :")
        zone = input("Enter the name of avaiability zone :")
        sp.getoutput('aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}'.format(vt, size, zone))
    elif command ==2:
        vol_id = input("Enter volume id: ")
        instance_id = input("Enter instance id : ")
        dev_name = input("Enter device name or drive name : ")
        sp.getoutput('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}'.format(vol_id, instance_id, dev_name))
    else :
        print('unsupported input')


def s3conf():
    sp.getoutput('clear')
    print("\n--------------S3-------------\n")
    print("1. Create Bucket")
    print("2. List buckets and objects")
    print("3. Create Object")
    print("4. Delete Bucket")
    print("5. Delete Object")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        buck_name = input("Enter unique bucket name : ")
        region_name = input("Enter region name :")
        s = sp.getoutput('aws s3 mb s3://{0} --region {1}'.format(buck_name,region_name))
        print(s)
    elif command ==2 :
        s = sp.getoutput('aws s3 ls')
        print(s)
    elif command ==3 :
        s = sp.getoutput('aws s3 sync')
        print(s)
    elif command ==4 :
        buck_name = input("Enter bucket name : ")
        s = sp.getoutput('aws s3 rb s3://{}'.format(buck_name))
        print(s)
    elif command ==5 :
        buck_name = input("Enter bucket name : ")
        obj_name = input("Enter object name : ")
        s = sp.getoutput('aws s3 rm s3://{0}/{1}'.format(buck_name,obj_name))
        print(s)

def cluster():
        status = sp.getstatusoutput("rpm -q hadoop")
        print(status[0])
        print(status[1])
        if status[0] != 0 :
            os.system("yum install python3-pip -y")
            os.system("pip2 install gdown")
            os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
            os.system("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz")
            os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
            os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
        else:

            print("-----hadoop services-----")
            print("tell your requirements whatever you want please")
            inp1 = input("what you want: ")
            if "namenode" in inp1 or "datanode" in inp1 or "client" in inp1:
                hadoopconf()


def hadoopconf():
        inp = input("what do you want tell your requirements:\n")
        if "configure namenode" in inp or "make a hadoop master" in inp:
            print("---------master node configuration------------")
            ip=input("\nenter machine IP\n")

            namenode_folder = input("\t\t\tFolder name for namenode:")
            os.system("rm -rf {}".format(namenode_folder))
            os.system("mkdir {}".format(namenode_folder))
            namenode_port = input("\t\t\tGive Port Number at which you want to run namenode service:")

            file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
            hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
            file_hdfs.write(hdfs_data)

            file_core = open("/etc/hadoop/core-site.xml", "w")
            core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(ip , namenode_port)
            file_core.write(core_data)
            print("now you have setup ready")
            print("1. format")
            print("2. start namenode")
            print("3. show report")
            command == int(input("enter your choice"))
            if command == 1:
                os.system("hadoop namenode -format")
            elif command == 2:
                os.system("hadoop-daemon.sh start namenode")
            elif command == 3:
                os.system("hadoop dfsadmin -report")



        elif inp  in "configure datanode" or inp in "make a hadoop slave":
            print("---------data node configuration------------")
            datanode_folder = input("\t\t\tFolder name for datanode:")
            os.system("rm -rf {}".format(datanode_folder))
            os.system("mkdir {}".format(datanode_folder))
            namenode_IP = input("\t\t\tEnter namenode IP: ")
            namenode_port = input("\t\t\tEnter port number of namenode: ")
            file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
            hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(datanode_folder)
            file_hdfs.write(hdfs_data)

            file_core = open("/etc/hadoop/core-site.xml", "w")
            core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
            file_core.write(core_data)
            print("now have datanode setup ready")
            print("1. start datanode")
            print("2. show report")
            command = int(input("select choice"))
            if command == 1:
                os.system("hadoop-daemon.sh start datanode")
            elif command == 2:
                os.system("hadoop dfsadmin -report")


        elif inp in "configure client" or inp in "make a hadoop client":
            print("---------master node configuration------------")
            namenode_IP = input("\t\t\tEnter namenode IP: ")
            namenode_port = input("\t\t\tEnter port number of namenode: ")
            file_core = open("/etc/hadoop/core-site.xml", "w")
            core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
            file_core.write(core_data)
            print("now you have client setup ready")
            print("options are :")
            print("1. add files into cluster")
            print("2. delete files from cluster")
            print("3. Listing the file of cluster")
            print("4. read a file")
            print("5. change block size ")
            print("6. change replication factor")
            print("7. change replication factor and block size both")
            command = int(input("\nEnter your choice--"))
            if command == 1:
                filename = input("enter your file name")
                os.system("hadoop fs -put {} /".format(filename))
            elif command == 2:
                filename = input("enter your file name")
                os.system("hadoop fs -rm {} /".format(filename))
            elif command == 3:
                os.system("hadoop fs -ls /")
            elif command == 4:
                filename = input("enter filename which you want to read")
                os.system("hadoop fs -cat / {}".format(filename))
            elif command == 5:
                filename = input("enter your file name")
                size = input("enter size in bytes")
                os.system("hadoop fs -Ddfs.block.size = {} -put {} /".format(size , filename))
            elif command == 6:
                filename = input("enter filename")
                factor = int(input("enter your replication factor"))
                os.system("hadoop fs -setrep -w {} {}".format(factor , filename))
            elif command == 7:
                filename = input("enter filename")
                factor = input("enter factor")
                size = input("enter block size")
                os.system("hadoop -fs -setrep -w {} -Ddfs.block.size = {} -put {} /".format(factor , size , filename))

def webser_conf():
    os.system("tput setaf 7")
    print("\t\t\t==============================================")
    os.system("tput setaf 2")
    print("\t\t\t| YOU CAN CONFIGURE WEBSERVER EASILY USING CLI |")
    os.system("tput setaf 7")
    print("\t\t\t==============================================")
    print("\t\t\tTo configure webserver following steps are must")
    print("\t\t\t install httpd ")
    print("\t\t\t start the service of httpd")
    print("\t\t\t===============================================")

    name=input("Enter install to install the httpd :")
    q = os.system("yum install httpd".format(name))
    print(q)
    os.system("tput setaf 2")
    print("Done.")
    print("\t\t\t===============================================")
    os.system("tput setaf 7")
    state = input("Enter start to start the service:")
    r = os.system("systemctl {0} httpd".format(state))
    print("Configuration done !")

def lvm():
  while (True):
                        os.system("tput setaf 7")
                        print("\t\t\t==============================================")
                        os.system("tput setaf 2")
                        print("\t\t\t| LVM Partition |")
                        os.system("tput setaf 7")
                        print("\t\t\t==============================================")
                        print()
                        print("1. for see the all disks")
                        print("2. (create/delete) a physical volume")
                        print("3. display the physical volume")
                        print("4. (create/delete) the volume group")
                        print("5. display the volume group")
                        print("6. (create/delete) the logical volume")
                        print("7. display the logical volume")
                        print("8. extend the logical volume")
                        print("9. (format/continue-format) the logical volume")
                        print("10. display the filesystem")
                        print("11. (mount/umount) the logical volume to that particular folder")
                        print("12. exit the program")
                        c = int(input("Enter your choice: "))
                        if c == 1:
                            os.system("fdisk -l")
                        elif c == 2:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                physical = input("Enter your disk name: ")
                                os.system(" pvcreate {}".format(physical))
                            elif disk == "delete":
                                physical = input("Enter your disk name: ")
                                os.system(" pvremove {}".format(physical))
                            else:
                                print("Not Found")
                        elif c == 3:
                            physical = input("Enter your disk name: ")
                            os.system("pvdisplay {}".format(physical))
                        elif c == 4:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                volume = input("Enter your volume group name: ")
                                physical1 = input("Enter your 1st physical disk name: ")
                                physical2 = input("Enter your 2nd physical disk name: ")
                                os.system(" vgcreate {} {} {}".format(volume,physical1,physical2))
                            elif disk == "delete":
                                volume = input("Enter your volume group name: ")
                                os.system(" vgchange -an {}".format(volume))
                                os.system(" vgremove {}".format(volume))
                            else:
                                print("Not Found")
                        elif c == 5:
                            volume = input("Enter your volume group name: ")
                            os.system(" vgdisplay {}".format(volume))
                        elif c == 6:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                logical = input("Enter your logical volume name: ")
                                volume = input("Enter your volume group name: ")
                                size = input("Enter the size of logical volume (in G): ")
                                os.system(" lvcreate --size {} --name {} {}".format(size,logical,volume))
                            elif disk == "delete":
                                logical = input("Enter your logical volume name: ")
                                volume = input("Enter your volume group name: ")
                                os.system(" lvchange -an /dev/{}/{}".format(volume,logical))
                            else:
                                print("Not Found")
                        elif c == 7:
                            logical = input("Enter your volume group name: ")
                            os.system(" lvdisplay {}".format(logical))
                        elif c == 8:
                            volume = input("Enter your volume group name: ")
                            logical = input("Enter your logical volume name: ")
                            size = input("Enter the size of logical volume (in G): ")
                            os.system(" lvextend --size +{} /dev/{}/{}".format(size,volume,logical))
                        elif c == 9:
                            disk = input("What do you want (format/continue-format): ")
                            if disk == "format":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                os.system(" mkfs.ext4 /dev/{}/{}".format(volume,logical))
                            elif disk == "continue-format":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                os.system(" resize2fs /dev/{}/{}".format(volume,logical))
                            else:
                                print("Not Found")
                        elif c == 10:
                            os.system("df -h")
                        elif c == 11:
                            disk = input("What do you want (mount/umount): ")
                            if disk == "mount":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                folder = input("Enter your folder name: ")
                                os.system(" mount /{}".format(folder))
                                os.system(" mount /dev/{}/{}  /{}".format(volume,logical,folder))
                                print("Mounted Successfully")
                            elif disk == "umount":
                                folder = input("Enter your folder name: ")
                                os.system("umount /{}".format(folder))
                                print("Umounted Successfuly")
                            else:
                                print("Not Found")
                        elif c == 12:
                            break
                        else:
                             print("this service is not valid")


os.system("clear")
os.system("tput setaf 7")
print("\t\t\t==============================================")
os.system("tput setaf 2")
print("\t\t\t|Hey Welcome to Automation world !!!|")
os.system("tput setaf 7")
print("\t\t\t==============================================")

while(True):
        MENU()
