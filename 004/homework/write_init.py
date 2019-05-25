#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

dic = {"1": {"1": "python模块详解", "star": "1", "reply": []},
       "2": {"2": "django框架", "star": "1", "reply": []},
       "3": {"3": "前端基础", "star": "1", "reply": []}}

with open('news.db', mode='w', encoding='utf8') as f:
    info = json.dumps(dic, ensure_ascii=False)
    f.write(info)
