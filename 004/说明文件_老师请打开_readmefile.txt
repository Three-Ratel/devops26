python周末26期吴兴普
作业位于homework   第一次提交0423

作业目录说明
blogger.py作业主函数文件
homework4登录注册 (已导入第一个)
news.db 文档  olddairy 日志  user.txt用户   


if __name__ == '__main__':
    while True:
        dic = {1: 'login', 2: 'reg', 3: 'explor_blogs', 4: 'dairy', 5: 'reply_blogs', 6: 'like_blogs'}
        print('''欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序''')
        s = int(input('请选择功能: '))
#===================================================
#===================简要程序结构函数名说明================================
        if s == 1:
            login()				#导入自homework4
        elif s == 2:
            reg()				#导入自homework4
        elif s == 3:
            explor_blogs()			#读取json文件
        elif s == 4:
            dairy()				#读取dairy文件
        elif s == 5:
            reply_blogs()			#追加到字典里的列表,写入文件
        elif s == 6:
            like_blogs()			#找到对应的字典star+1
        elif s == 7:
            logout()				#退出 恢复全局用户名为None
        elif s == 8:
            exit()				#退出程序



