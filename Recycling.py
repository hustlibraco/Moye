#coding=utf-8
"""
查看被所有用户删除的文件

需要用管理员权限运行
"""
import os
import _winreg as wr

def get_recycle_dir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for _dir in dirs:
        if os.path.isdir(_dir):
            return _dir
    return False

def sid2user(sid):
    try:
        keyname = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\{0}'.format(sid)
        key = wr.OpenKeyEx(wr.HKEY_LOCAL_MACHINE, keyname)
        value, _ = wr.QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid

def main():
    rdir = get_recycle_dir()
    for sid in os.listdir(rdir):
        print sid2user(sid), os.listdir(os.path.join(rdir, sid))

if __name__ == '__main__':
    main()