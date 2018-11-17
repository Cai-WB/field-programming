import  itchat
itchat.auto_login(hotReload=True)   #热启动你的微信

friends=itchat.get_chatrooms(update=True)
for i in range(len(friends)):
    print(friends[i])   #查看你多有的群
f="C:/Users/cwb/Desktop/yedo.jpg"  #图片地址
userName = friends[0]['UserName']
try:
    itchat.send_image(f,toUserName=userName)  
    # 如果是其他文件可以直接send_file
    print("success")
except:
    print("fail")
