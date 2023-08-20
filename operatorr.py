
import pickle
from re import match
import pandas as pd
from datetime import date
import time
from folder import folder
from file import file
from directory_system import directory_system
def operatorr():   
    ds=directory_system()
    command=input()
    while (command!="exit"):
        if command=="man":
            ds.mann()
        ###############################
        elif "mkdir" in command:
            try:
                folder_strr=command.split(" ")[1]
                ds.mkdir(folder_strr)
            except:
                ds.log("mkdir","wrong command")
                print ("wrong command")
        ###############################
        elif "mkfile" in command:
            try:
                file_strr=command.split(" ")[1]
                ds.mkfile(file_strr)
            except:
                ds.log("mkfile","wrong command")
                print ("wrong command")
        ##############################
        elif "ll"==command:
            ds.printt()
        ################################
        elif ("cd" in command) and ("~" not in command):
            try:
                cd_strr=command
                ds.cdd(cd_strr)
            except:
                ds.log("cd","wrong command")
                print ("wrong command")
        elif ("cd" in command) and ("~"  in command):
            try:
                
                strr_file=ds.auto_complete(command.strip("~").split("/")[-1])
                cd_strr=command.strip(strr_file+"~")+strr_file
                print(cd_strr)
                ds.cdd(cd_strr)
            except:
                ds.log("cd","wrong command")
                print ("wrong command")   
        ################################
        elif "rm" in command:
            try:
                file_strr=command.split(" ")[1]
                ds.rmm(file_strr)
            except:
                ds.log("rm","wrong command")
                print ("wrong command")
       ################################  
        elif "pwd" ==command:
            try:
                ds.pwd()
            except:
                print("root/")
        ################################
        elif "append" in command:
            try:
                strr_text=command.split("append")[1].strip(" ")
                file_name=strr_text.split(" ")[0]
                text=strr_text.strip(file_name).strip(" ")
                ds.appendd(file_name,text)
            except:
                ds.log("append","wrong command")
                print ("wrong command")
        ################################
        elif "cat" in command and "grep" not in command:
            try:
                file_name=command.split(" ")[1]
                ds.cat(file_name)
            except:
                print("1")
                ds.log("cat","wrong command")
                print ("wrong command")
        ################################
        elif "cat" in command and "grep e"  in command:
            try:
                file_name=command.split(" ")[1]
                ds.grep(file_name)
            except:
                ds.log("grep","wrong command")
                print ("wrong command")
       ################################
        elif ("ll" in command) and (len(command)>=5):
            lst_arguments=["l","s"]  
            if command[4] in lst_arguments:
                ds.printt(command[4])
            else:
                print ("wrong command")
        ################################
        elif "save" in command:
            try:
                route=command.split(" ")[1]
                ds.save(route)
            except:
                ds.log("save","wrong command")
                print ("wrong command")
        ################################
        elif "load" in command:
            try:
                route=command.split(" ")[1]
                ds=ds.load(route)
            except:
                ds.log("load","wrong command")
                print ("wrong command")
        ################################
        elif "diff" in command:
            try:
                lst_helper=command.split(" ")
                file1=lst_helper[1]
                file2=lst_helper[2]
                ds.diff(file1,file2)
            except:
                ds.log("diff","wrong command")
                print ("wrong command")
        ################################
        elif "find" in command:
            try:
                regex=command.split('"')[1]
                ds.find(regex)
            except:
                ds.log("find","wrong command")
                print ("wrong command")
        ################################
        elif "log"==command:
            df=pd.read_pickle("test.pkl")
            print(df)
        ################################
        else:
            ds.log("general error","wrong command")
            print("wrong command")
        command=input()
