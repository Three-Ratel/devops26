python��ĩ26��������
��ҵλ��homework   ��һ���ύ0423

��ҵĿ¼˵��
blogger.py��ҵ�������ļ�
homework4��¼ע�� (�ѵ����һ��)
news.db �ĵ�  olddairy ��־  user.txt�û�   


if __name__ == '__main__':
    while True:
        dic = {1: 'login', 2: 'reg', 3: 'explor_blogs', 4: 'dairy', 5: 'reply_blogs', 6: 'like_blogs'}
        print('''��ӭ��������԰��ҳ
        1:���¼
        2:��ע��
        3:����ҳ��
        4:�ռ�ҳ��
        5:����ҳ��
        6:�ղ�ҳ��
        7:ע��
        8:�˳�����''')
        s = int(input('��ѡ����: '))
#===================================================
#===================��Ҫ����ṹ������˵��================================
        if s == 1:
            login()				#������homework4
        elif s == 2:
            reg()				#������homework4
        elif s == 3:
            explor_blogs()			#��ȡjson�ļ�
        elif s == 4:
            dairy()				#��ȡdairy�ļ�
        elif s == 5:
            reply_blogs()			#׷�ӵ��ֵ�����б�,д���ļ�
        elif s == 6:
            like_blogs()			#�ҵ���Ӧ���ֵ�star+1
        elif s == 7:
            logout()				#�˳� �ָ�ȫ���û���ΪNone
        elif s == 8:
            exit()				#�˳�����



