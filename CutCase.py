import os,shutil

def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):          #判断srcfile所对应是否为已经存在的文件
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)   #分离文件名和路径，将文件名和路径分割开，'C:/soft/test.py'->'C:/soft/','test.py'
        if not os.path.exists(fpath):        #判断fpath所对应的是否为已经存在，返回True或者False
            os.makedirs(fpath)               #创建路径，递归创建目录。
        shutil.move(srcfile, dstfile)        #移动文件，将文件或整个文件目录srcfile移动到dstfile，移动成功后返回目标文件路径；若dstfile不存在时自动创建
        print ("move %s -> %s"%( srcfile, dstfile))

def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile, dstfile)     #复制文件。将文件srcfile复制到文件dstfile中，复制成功后返回dstfile完整路径，srcfile，dstfile需是文件路径而非文件目录
        print ("copy %s -> %s"%( srcfile, dstfile))

def findAllFile(base):#返回当前目录下的所有子文件的绝对路径，或者文件名。返回值，生成器
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = 'D:/Judy/0820自动化用例分析/'
    for i in findAllFile(base):
        print(i)

    print("=======================================================================================================")
    print("=======================================================================================================")
    print("=======================================================================================================")
    print("=======================================================================================================")
    print("=======================================================================================================")

    tf = open("1.txt","rt")
    for i in range(1,137):
        # 逐行读取，去掉前后字符串，去掉特殊字符串"failed0930"，并加上.java后缀
        AutomatedCaseName = tf.readline().strip().strip("failed0930").strip()+".java"
        print(AutomatedCaseName)

        srcfile = 'D:/Judy/0820自动化用例分析/'+AutomatedCaseName
        dstfile = 'D:/Judy/0820自动化用例分析/failed0930/'+AutomatedCaseName
        mymovefile(srcfile, dstfile)
    tf.close()#关闭1.txt文件

if __name__ == '__main__':
    main()
