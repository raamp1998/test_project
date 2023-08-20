# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:07:51 2023

@author: Raam
"""
import pickle
from re import match
import pandas as pd
from datetime import date
import time
from folder import folder
from file import file
class directory_system:
    
    def __init__(self):
        self.head=folder("root")
        self.commands=["mkdir","mkfile","ll","exit","cd","rm","pwd","append","cat","grep","save","load","diff","find"]
        self.curr=None
        
    def log(self,type_of_command,error):
        datee = str(date.today())
        hour=time.strftime("%H:%M:%S", time.localtime())
        df_old=pd.read_pickle("test.pkl")
        df_new=pd.DataFrame({"date":[],"hour":[],"type_of_command":[],"error":[]})
        df_new.loc[0,"date"]=datee
        df_new.loc[0,"hour"]=hour
        df_new.loc[0,"type_of_command"]=type_of_command
        df_new.loc[0,"error"]=error
        df_total=pd.concat([df_old, df_new], axis=0).reset_index().drop(columns=['index'])
        df_total.to_pickle("test.pkl")
    
    #printing the possiable commands
    def mann(self):
        print("\n".join(self.commands)) 
        
    #making new folder in the route
    def mkdir(self,folder_name):
        f=folder(folder_name)
        if self.curr:
            if folder_name in self.curr.files_names:
                print ("folder's name alredy taken")
                self.log("mkdir","folder's name alredy taken")
                return 
            else:
                f.father=self.curr
                f.route=self.curr.route+"/"+f.folder_name
                self.curr.files.append(f)
                self.curr.files_names.append(folder_name)
        else:
            f.father=self.head
            f.route="root/"+f.folder_name
            self.head.files.append(f)
            self.head.files_names.append(folder_name)
            self.curr=self.head
        
    
    #making new file in the route        
    def mkfile(self,file_name):
        f=file(file_name)
        if self.curr:
            if file_name in self.curr.files_names:
                print ("file's name alredy taken")
                self.log("mkfile","file's name alredy taken")
                return 
            else:
                f.route=self.curr.route+"/"+f.file_name
                self.curr.files.append(f)
                self.curr.files_names.append(file_name)
        else:
            f.route="root/"+f.folder_name
            self.head.files.append(f)
            self.head.files_names.append(file_name)
            self.curr=self.head
        
    #printing all the files and folders in the route, can except argumnets
    def printt(self,argument=""):
        try:
            files="Files: ["
            directories="Directories: ["
            if argument=="":
                index=0
                for obj in self.curr.files_names:
                    if type(self.curr.files[index])==folder:
                        directories=directories+obj+","
                    if type(self.curr.files[index])==file:
                        files=files+obj+","
                    index+=1
                directories=directories.strip(",")+"]"
                files=files.strip(",")+"]"
                print(files+", "+directories)
                
                # print("\n".join(self.curr.files_names))
            elif argument=="l":
                index=0
                files_names_lst, files_lst = zip(*sorted(zip(self.curr.files_names, self.curr.files)))
                files_names_lst=list(files_names_lst)
                files_lst=list(files_lst)
                for obj in files_names_lst:
                    if type(files_lst[index])==folder:
                        directories=directories+obj+","
                    if type(files_lst[index])==file:
                        files=files+obj+","
                    index+=1
                directories=directories.strip(",")+"]"
                files=files.strip(",")+"]"
                print(files+", "+directories)
                # print("\n".join(sorted(self.curr.files_names)))
            
            elif argument=="s":
                index=0
                files_names_lst, files_lst = zip(*sorted(zip(self.curr.files_names, self.curr.files),reverse=True))
                files_names_lst=list(files_names_lst)
                files_lst=list(files_lst)
                for obj in files_names_lst:
                    if type(files_lst[index])==folder:
                        directories=directories+obj+","
                    if type(files_lst[index])==file:
                        files=files+obj+","
                    index+=1
                directories=directories.strip(",")+"]"
                files=files.strip(",")+"]"
                print(files+", "+directories)
                # print("\n".join(sorted(self.curr.files_names, reverse=True)))
            else:
                self.log("ll","wrong command")
                print("wrong command")
        except:
            self.log("ll","file/folder doesn't exist")
            print("file/folder doesn't exist")
    #direct to route
    ##################################
    def auto_complete(self,start):
        filtered_files = list(filter(lambda x: x.startswith(start), self.curr.files_names))
        strr=""
        if len(filtered_files)==1:
            strr=filtered_files[0]
        return strr
    ################################
    #instead of tab the autofill work with ~
    def cdd(self,rout):
        if len(self.head.files) != 0:
            if(rout=="cd .."):
                try:
                    self.curr=self.curr.father
                except:
                    print ("file or directory doesnt exist")
                    return
            else:  
                pointer=self.head
                for obj in rout.split(" ")[1].split("/"):
                    if obj not in pointer.files_names:
                        self.log("cd","file or directory doesnt exist")
                        print ("file or directory doesnt exist")
                        return
                    else:
                        pointer=pointer.files[pointer.files_names.index(obj)]
                self.curr=pointer
        else:
            self.log("cd","file system empty")
            print ("file system empty")
            
    #deleting folder/file
    #I didn't really delete all the route of folders and files that 
    #start from the one I asked to delete, I just denied access to them.
    #I can do it if I asked for 
    def rmm(self,obj_name):
        if len(self.head.files) != 0:
            if obj_name in self.curr.files_names:
                remove_index=self.curr.files_names.index(obj_name)
                self.curr.files[remove_index].father=None
                self.curr.files_names.remove(obj_name)
                del self.curr.files[remove_index]
            else:
                self.log("rmm","file/folder doesn't exist")
                print ("file/folder doesn't exist")
        else:
            self.log("rmm","file system empty")
            print ("file system empty")
    
    #printint current route
    def pwd(self):
        try:
            print (self.curr.route) 
        except:
            print("root/")
    
    def appendd(self,file_name,text):
        try:
            file_index=self.curr.files_names.index(file_name)
            pointer=self.curr.files[file_index]
            pointer.text=pointer.text+text
        except:
            self.log("append","not a file or file not exists")
            print ("not a file or file not exists")
    def cat(self,file_name):
        try:
            file_index=self.curr.files_names.index(file_name)
            pointer=self.curr.files[file_index]
            strr=""
            for obj in pointer.text.split("\n")[0].split("\\n"):
                strr=strr+obj+"\n"
            print(strr)
        except:
            self.log("cat","not a file or file not exists")
            print ("not a file or file not exists")
            
    #I didnt shore what this command does so i did it like the example
    def grep(self,file_name):
        try:
            file_index=self.curr.files_names.index(file_name)
            pointer=self.curr.files[file_index]
            strr=""
            for obj in pointer.text.split("\n")[0].split("\\n")[3:]:
                strr=strr+"\n"+obj
            print(strr)
        except:
            self.log("grep","not a file or file not exists")
            print ("not a file or file not exists")
    
    def save(self,route):
        try:
            pickle_out = open(route,"wb")
            pickle.dump(self, pickle_out)
            pickle_out.close()
        except:
            self.log("save","wrong commend")
            print("wrong commend")
    def load(self,route):
        try:
            pickle_in = open(route,"rb")
            return pickle.load(pickle_in)
        except:
            self.log("load","wrong commend")
            print("wrong commend")
    
    def diff(self,file_name_1,file_name_2):
        lst_file1=self.curr.files[self.curr.files_names.index(file_name_1)].text.split(" ")
        lst_file2=self.curr.files[self.curr.files_names.index(file_name_2)].text.split(" ")
        diff_lst=list(set(lst_file1) - set(lst_file2))+list(set(lst_file2) - set(lst_file1))
        print(' '.join(diff_lst))
        
    
    def find(self,regex):
        dic_helper = {self.curr.files_names[i]: self.curr.files[i] for i in range(len(self.curr.files_names))}
        find_files = list(filter(lambda x: match(regex, x), self.curr.files_names))
        files="Files: ["
        directories="Directories: ["
        index=0
        for obj in find_files:
            if type(dic_helper[obj])==folder:
                directories=directories+obj+","
            if type(dic_helper[obj])==file:
                files=files+obj+","
            index+=1
        directories=directories.strip(",")+"]"
        files=files.strip(",")+"]"
        print(files+", "+directories)