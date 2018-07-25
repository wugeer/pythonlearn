import os,shutil
#将一个文件夹下某种类型文件移动到另一个文件夹内
if __name__ == '__main__':
    dir = "D:\\xhwCode\\leetcode\\algorithms\\cpp"
    if os.path.exists(dir):
        print('dir exists:\n')
        for root,dirs,files in os.walk(dir):
            for filename in files:
                if not filename.endswith('main.cpp'):
                    if filename not in os.listdir('D:\\xhwCode\\leetcode\\algorithms\\cpp'):
                        shutil.move(os.path.join(root,filename),'D:\\xhwCode\\leetcode\\algorithms\\cpp')
