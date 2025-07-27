



# source yadgire build in team arianbot



from arsein import Messenger

from json import *

import os.path

import time

from time import sleep, localtime

import os

import re

import random



# meghdars # version 14



auth = " "



Gap = " "



admin = " "



guid_bot = " "



keyp = " "



app = Messenger(auth, keyp)





limsg, yadDic, readli, messageidjson, GetAdmin, sended, on, removeads, getcheckAds, CHATHISTORY, errorRepleytobot, dastor_bot = [

], [], None, [], [], False, True, False, [], False, False, ['/admin', '/unadmin', 'سکوت']





while 1:

    try:

        se = app.sendMessage(Gap, "با موفقیت فعال شد")["status"]

        if se == 'OK':

            print("starting...")

            if "".join(open("admins.json", "r", encoding="utf-8").read()) == "{}":

                GetAdmin = [admin]

            elif "".join(open("admins.json", "r", encoding="utf-8").read()) != "{}":

                print("starting...")

                GetAdmin = [guie for guie in loads(

                    "".join(open("admins.json", "r", encoding="utf-8").read())).keys()]

                GetAdmin.append(admin)

            break

        else:

            continue

    except FileNotFoundError:

        admins = os.path.exists("admins.json")

        if admins == False:

            open("admins.json", "w").write("{}")

            print("starting building admins.json")

        else:

            ...



while 1:

    try:

        message = app.getChatGroup(Gap)

        for msg in message:

            if msg["type"] == 'Text' and not msg['message_id'] in limsg:

                limsg.append(msg['message_id'])



                if CHATHISTORY == False:

                    his = app.deleteChatHistory(

                        Gap, msg['message_id']).get('status')

                    print('delete chat history' if his ==

                          'OK' else 'error delete chat history')

                    CHATHISTORY = True



                print(f"message = {msg['text']}")



                if msg.get("text").startswith("یاد بگیر ") and msg.get("author_object_guid") in GetAdmin and on != False:

                    try:

                        if "#تبلیغ" in msg.get("text") and not 'reply_to_message_id' in msg.keys():

                            getmatn2 = str(" ".join(msg.get("text").replace(

                                "یاد بگیر اگر #تبلیغ", "").split(" ")[:]))

                            removeads = True

                            check = os.path.exists("yad.json")

                            if check == True:

                                readinfo = open(

                                    "yad.json", "r", encoding="utf-8").read()

                                if readinfo == "":

                                    buildDic = dict(

                                        {"Remove_ads": f"{getmatn2}"})

                                    sleep(3)

                                    wri = open("yad.json", "w").write(

                                        dumps(buildDic))

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    print("Ok write json")

                                    app.sendMessage(

                                        Gap, "یاد گرفتم", message_id=msg['message_id'])

                                    print("Ok yadgire delete message")

                                    sleep(5)

                                elif readinfo != "":

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    readli.update(

                                        dict({"Remove_ads": f"{getmatn2}"}))

                                    print("Ok Update json")

                                    wri = open("yad.json", "w").write(

                                        dumps(readli))

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    app.sendMessage(

                                        Gap, "یاد گرفتم", message_id=msg['message_id'])

                                    print("Ok yadgire delete message")

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("yad.json", "w").write("{}")



                        elif "#بن" in msg.get("text") and not 'reply_to_message_id' in msg.keys():

                            getmatn2 = str(" ".join(msg.get("text").replace(

                                "یاد بگیر اگر #بن", "").split(" ")[:]))

                            removeads = True

                            check = os.path.exists("yad.json")

                            if check == True:

                                readinfo = open(

                                    "yad.json", "r", encoding="utf-8").read()

                                if readinfo == "":

                                    buildDic = dict({"Ban_ads": f"{getmatn2}"})

                                    sleep(3)

                                    wri = open("yad.json", "w").write(

                                        dumps(buildDic))

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    print("Ok write json")

                                    app.sendMessage(

                                        Gap, "یاد گرفتم", message_id=msg['message_id'])

                                    print("Ok yadgire Ban")

                                    sleep(5)

                                elif readinfo != "":

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    readli.update(

                                        dict({"Ban_ads": f"{getmatn2}"}))

                                    print("Ok Update json")

                                    wri = open("yad.json", "w").write(

                                        dumps(readli))

                                    readli = loads(

                                        "".join(open("yad.json", "r", encoding="utf-8").read()))

                                    app.sendMessage(

                                        Gap, "یاد گرفتم", message_id=msg['message_id'])

                                    print("Ok yadgire Ban")

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("yad.json", "w").write("{}")



                        elif 'reply_to_message_id' in msg.keys():

                            msid = msg.get('reply_to_message_id')

                            getType = app.getMessagesInfo(

                                Gap, [msg.get('reply_to_message_id')])["data"]

                            if 'Event' in str(getType['messages'][0]['type']):

                                getmatn1 = str(app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                               "data"]["messages"][0]["event_data"]["type"])

                                getmatn2 = str(" ".join(msg.get("text").replace(

                                    "یاد بگیر ", "").split(" ")[:]))

                            elif 'Text' in str(getType['messages'][0]['type']):

                                getmatn1 = str(app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                               "data"]["messages"][0]["text"])

                                getmatn2 = str(" ".join(msg.get("text").replace(

                                    "یاد بگیر ", "").split(" ")[:]))



                            check = os.path.exists("yad.json")

                            if check == True:

                                if not guid_bot in str(getType['messages'][0]):

                                    if not getmatn1 in dastor_bot:

                                        readinfo = open(

                                            "yad.json", "r", encoding="utf-8").read()

                                        if readinfo == "":

                                            buildDic = dict(

                                                {f"{getmatn1}": f"{getmatn2}"})

                                            sleep(3)

                                            wri = open("yad.json", "w").write(

                                                dumps(buildDic))

                                            readli = loads(

                                                "".join(open("yad.json", "r", encoding="utf-8").read()))

                                            print("Ok write json")

                                            app.sendMessage(

                                                Gap, "یاد گرفتم", message_id=msg['message_id'])

                                            print("Ok yadgire")

                                            sleep(5)

                                        elif readinfo != "":

                                            readli = loads(

                                                "".join(open("yad.json", "r", encoding="utf-8").read()))

                                            readli.update(

                                                dict({f"{getmatn1}": f"{getmatn2}"}))

                                            print("Ok Update json")

                                            wri = open("yad.json", "w").write(

                                                dumps(readli))

                                            readli = loads(

                                                "".join(open("yad.json", "r", encoding="utf-8").read()))

                                            app.sendMessage(

                                                Gap, "یاد گرفتم", message_id=msg['message_id'])

                                            print("Ok yadgire")

                                    else:

                                        app.sendMessage(

                                            Gap, "به دستورات اصلی من نمی توانید کلمه یاد دهید 😛", message_id=msg['message_id'])

                                else:

                                    app.sendMessage(

                                        Gap, "روی من نمیتونی ریپلای بزنی و دستور یاد بدی 😛", message_id=msg['message_id'])

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("yad.json", "w").write("{}")

                        else:

                            app.sendMessage(

                                Gap, "باید رو کلمه ای که میخوایی یاد بگیرم ریپلای کنی", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text") in loads("".join(open("yad.json", "r", encoding="utf-8").read())).keys() and not msg['message_id'] in messageidjson and on != False:

                    try:

                        if "#ادمین" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            print("1")

                            if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                    ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                    family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                    name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                    bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                    mtnesm = str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#ادمین", "").replace("#بیو", bio).replace(

                                        "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                    app.sendMessage(

                                        Gap, mtnesm, message_id=msg['message_id'])

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                                else:

                                    app.sendMessage(

                                        Gap, f"{loads(''.join(open('yad.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}", message_id=msg['message_id'])

                                    messageidjson.append(msg['message_id'])

                                    print("sended")



                        elif "#کاربر" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            print("2")

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                    ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                    family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                    name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                    bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                    mtnesm = str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#کاربر", "").replace("#بیو", bio).replace(

                                        "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                    app.sendMessage(

                                        Gap, mtnesm, message_id=msg['message_id'])

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                                else:

                                    app.sendMessage(

                                        Gap, f"{loads(''.join(open('yad.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}", message_id=msg['message_id'])

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                            else:

                                ...



                        elif "#رندوم" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                mtnesm = str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#کاربر", "").replace("#بیو", bio).replace(

                                    "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                matnrendome = re.sub(r"#رندوم\s*((?:'[^']+'(?:,\s*)?)*)", lambda match: random.choice(

                                    re.findall(r"'(.*?)'", match.group(1))), mtnesm).replace("'", "").replace(",", "")

                                app.sendMessage(

                                    Gap, matnrendome, message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended")

                            else:

                                mtnesm = loads(

                                    ''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))

                                matnrendome = random.choice(

                                    re.findall(r"'(.*?)'", mtnesm))

                                deletematn = ' '.join(re.sub(

                                    r"'.*?'", "", mtnesm).split()).replace("#رندوم", matnrendome).replace(',', '')

                                app.sendMessage(

                                    Gap, deletematn, message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended")



                        else:

                            if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                mtnesm = str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace(

                                    "#ساعت", time.strftime("%H : %M : %S", localtime())).replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family).replace("#بیو", bio)

                                app.sendMessage(

                                    Gap, mtnesm, message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended")

                            else:

                                print(":3")

                                c = app.sendMessage(

                                    Gap, f"{loads(''.join(open('yad.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}", message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print(c)

                                print("sended")

                    except Exception as e:

                        print(e)



                elif msg.get("text").startswith("پیوی بگو ") and msg.get("author_object_guid") in GetAdmin and on != False:

                    try:

                        if 'reply_to_message_id' in msg.keys():

                            msid = msg.get('reply_to_message_id')

                            getType = app.getMessagesInfo(

                                Gap, [msg.get('reply_to_message_id')])["data"]

                            if 'Event' in str(getType['messages'][0]['type']):

                                getmatn1 = str(app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                               "data"]["messages"][0]["event_data"]["type"])

                                getmatn2 = str(

                                    " ".join(msg.get("text").replace("پیوی بگو", "").split(" ")[:]))

                            elif 'Text' in str(getType['messages'][0]['type']):

                                getmatn1 = str(app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                               "data"]["messages"][0]["text"])

                                getmatn2 = str(

                                    " ".join(msg.get("text").replace("پیوی بگو", "").split(" ")[:]))

                                print(getmatn2)



                            check = os.path.exists("pv.json")

                            if check == True:

                                if not guid_bot in str(getType['messages'][0]):

                                    if not getmatn1 in dastor_bot:

                                        readinfo = open(

                                            "pv.json", "r", encoding="utf-8").read()

                                        if readinfo == "":

                                            buildDic = dict(

                                                {f"{getmatn1}": f"{getmatn2}"})

                                            sleep(3)

                                            wri = open("pv.json", "w").write(

                                                dumps(buildDic))

                                            readli = loads(

                                                "".join(open("pv.json", "r", encoding="utf-8").read()))

                                            print("Ok write json")

                                            app.sendMessage(

                                                Gap, "یاد گرفتم", message_id=msg['message_id'])

                                            print("Ok yadgire")

                                            sleep(5)

                                        elif readinfo != "":

                                            readli = loads(

                                                "".join(open("pv.json", "r", encoding="utf-8").read()))

                                            readli.update(

                                                dict({f"{getmatn1}": f"{getmatn2}"}))

                                            print("Ok Update json")

                                            wri = open("pv.json", "w").write(

                                                dumps(readli))

                                            readli = loads(

                                                "".join(open("pv.json", "r", encoding="utf-8").read()))

                                            app.sendMessage(

                                                Gap, "یاد گرفتم", message_id=msg['message_id'])

                                            print("Ok yadgire")

                                    else:

                                        app.sendMessage(

                                            Gap, "به دستورات اصلی من نمی توانید کلمه یاد دهید 😛", message_id=msg['message_id'])

                                else:

                                    app.sendMessage(

                                        Gap, "روی من نمیتونی ریپلای بزنی و دستور یاد بدی 😛", message_id=msg['message_id'])

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("pv.json", "w").write("{}")

                        else:

                            app.sendMessage(

                                Gap, "باید رو کلمه ای که میخوایی یاد بگیرم ریپلای کنی", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text") in loads("".join(open("pv.json", "r", encoding="utf-8").read())).keys() and not msg['message_id'] in messageidjson and on != False:

                    try:

                        pv = msg.get("author_object_guid")

                        if "#ادمین" in str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#ساعت" or "#بیو" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                    ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                    family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                    name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                    bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                    mtnesm = str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#ادمین", "").replace("#بیو", bio).replace(

                                        "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                    app.sendMessage(pv, mtnesm)

                                    app.sendMessage(

                                        Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                                else:

                                    app.sendMessage(

                                        pv, f"{loads(''.join(open('pv.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}")

                                    app.sendMessage(

                                        Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                    messageidjson.append(msg['message_id'])

                                    print("sended")



                        elif "#کاربر" in str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#ساعت" or "#بیو" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                    ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                    family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                    name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                    bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                    ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                    mtnesm = str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#کاربر", "").replace("#بیو", bio).replace(

                                        "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                    app.sendMessage(pv, mtnesm)

                                    app.sendMessage(

                                        Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                                else:

                                    app.sendMessage(

                                        pv, f"{loads(''.join(open('pv.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}")

                                    app.sendMessage(

                                        Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                    messageidjson.append(msg['message_id'])

                                    print("sended")

                            else:

                                ...



                        elif "#رندوم" in str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                            if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                mtnesm = str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#کاربر", "").replace("#بیو", bio).replace(

                                    "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                matnrendome = re.sub(r"#رندوم\s*((?:'[^']+'(?:,\s*)?)*)", lambda match: random.choice(

                                    re.findall(r"'(.*?)'", match.group(1))), mtnesm).replace("'", "").replace(",", "")

                                messageidjson.append(msg['message_id'])

                                print("sended")

                            else:

                                mtnesm = loads(

                                    ''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))

                                matnrendome = random.choice(

                                    re.findall(r"'(.*?)'", mtnesm))

                                deletematn = ' '.join(

                                    re.sub(r"'.*?'", "", mtnesm).split()).replace("#رندوم", matnrendome).strip(',')

                                app.sendMessage(

                                    Gap, deletematn, message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended")

                        else:

                            if "#اسم" or "#ایدی" or "#لینک" or "#گروه" or "#فامیلی" or "#ساعت" or "#بیو" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('text'))):

                                ide = "#not" if not "username" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else f"@{app.getUserInfo(msg['author_object_guid'])['data']['user']['username']}"

                                family = "#not" if not "last_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['last_name']

                                name = "#not" if not "first_name" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['first_name']

                                bio = "#not" if not "bio" in app.getUserInfo(msg["author_object_guid"])["data"]["user"].keys(

                                ) else app.getUserInfo(msg["author_object_guid"])['data']['user']['bio']

                                mtnesm = str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('text'))).replace("#اسم", name).replace("#ایدی", ide).replace("#بیو", bio).replace(

                                    "#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}").replace("#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family)

                                app.sendMessage(pv, mtnesm)

                                app.sendMessage(

                                    Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                messageidjson.append(msg['message_id'])

                                print("sended")

                            else:

                                app.sendMessage(

                                    pv, f"{loads(''.join(open('pv.json','r',encoding = 'utf-8').read())).get(msg.get('text'))}", message_id=msg['message_id'])

                                app.sendMessage(

                                    Gap, "پیوی خود را چک کنید", message_id=msg.get('message_id'))

                                messageidjson.append(msg['message_id'])

                                print("sended")

                    except Exception as e:

                        print(e)



                if "Remove_ads" in loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).keys() and "true" in ['true' if text in msg.get("text") else 'false' for text in re.findall(r"'(.*?)'", str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get("Remove_ads")))] and on != False:

                    print('get ads')

                    getdataVLUE = str(

                        loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get("Remove_ads"))

                    if '~ادمین بود ' in getdataVLUE.split('_')[0]:

                        if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                            if "حذف نکن" in getdataVLUE.split('_')[1]:

                                print('1 it is Admin no delete')

                                pass



                            elif "حذف کن" in getdataVLUE.split('_')[1]:

                                print('1 it is Admin yes delete')

                                DELETE_ADS = app.deleteMessages(

                                    Gap, message_ids=[msg.get('message_id')], All=True).get('status')

                                print(DELETE_ADS)

                                Matnads = "ok delete ADS" if DELETE_ADS == 'OK' else "error delete ADS"

                                if DELETE_ADS == 'OK':

                                    app.sendMessage(

                                        Gap, "پیام با موفقیت حذف شد", message_id=msg.get('message_id'))

                                print(Matnads)



                        elif "وگرنه " in getdataVLUE.split('_')[1]:

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "حذف نکن" in getdataVLUE.split('_')[2]:

                                    print('2 it is User no delete')

                                    pass



                                elif "حذف کن" in getdataVLUE.split('_')[2]:

                                    print('2 it is User yes delete')

                                    DELETE_ADS = app.deleteMessages(

                                        Gap, message_ids=[msg.get('message_id')], All=True).get('status')

                                    Matnads = "ok delete ADS" if DELETE_ADS == 'OK' else "error delete ADS"

                                    if DELETE_ADS == 'OK':

                                        app.sendMessage(

                                            Gap, "پیام با موفقیت حذف شد", message_id=msg.get('message_id'))

                                    print(Matnads)



                        elif '~ادمین نبود ' in getdataVLUE.split('_')[0]:

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "حذف نکن" in getdataVLUE.split('_')[1]:

                                    print('it is User')

                                    pass



                                elif "حذف کن" in getdataVLUE.split('_')[1]:

                                    print('it is User')

                                    DELETE_ADS = app.deleteMessages(

                                        Gap, message_ids=[msg.get('message_id')], All=True).get('status')

                                    Matnads = "ok delete ADS" if DELETE_ADS == 'OK' else "error delete ADS"

                                    if DELETE_ADS == 'OK':

                                        app.sendMessage(

                                            Gap, "پیام با موفقیت حذف شد", message_id=msg.get('message_id'))

                                    print(Matnads)



                            elif "وگرنه " in getdataVLUE.split('_')[1]:

                                if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                    if "حذف نکن" in getdataVLUE.split('_')[2]:

                                        print('it is User')

                                        pass



                                    elif "حذف کن" in getdataVLUE.split('_')[2]:

                                        print('it is User')

                                        DELETE_ADS = app.deleteMessages(

                                            Gap, message_ids=[msg.get('message_id')], All=True).get('status')

                                        Matnads = "ok delete ADS" if DELETE_ADS == 'OK' else "error delete ADS"

                                        if DELETE_ADS == 'OK':

                                            app.sendMessage(

                                                Gap, "پیام با موفقیت حذف شد", message_id=msg.get('message_id'))

                                        print(Matnads)



                if "Ban_ads" in loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).keys() and "true" in ['true' if text in msg.get("text") else 'false' for text in re.findall(r"'(.*?)'", str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get("Remove_ads")))] and on != False:

                    print('get ads and ban User')

                    getdataVLUE = str(

                        loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get("Ban_ads"))

                    if '~ادمین بود ' in getdataVLUE.split('_')[0]:

                        if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                            if "بن نکن" in getdataVLUE.split('_')[1]:

                                print('1 it is Admin no ban')

                                pass



                            elif "بن کن" in getdataVLUE.split('_')[1]:

                                print('1 it is Admin yes ban')

                                BAN_ADS = app.banGroupMember(Gap, msg.get(

                                    "author_object_guid")).get('status')

                                Matnads = "ok ban ADS" if BAN_ADS == 'OK' else "error ban ADS"

                                if BAN_ADS == 'OK':

                                    app.sendMessage(

                                        Gap, "با موفقیت بن شد", message_id=msg.get('message_id'))

                                print(Matnads)



                        elif "وگرنه " in getdataVLUE.split('_')[1]:

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "بن نکن" in getdataVLUE.split('_')[2]:

                                    print('2 it is User no ban')

                                    pass



                                elif "بن کن" in getdataVLUE.split('_')[2]:

                                    print('2 it is User yes ban')

                                    BAN_ADS = app.banGroupMember(Gap, msg.get(

                                        "author_object_guid")).get('status')

                                    Matnads = "ok ban ADS" if BAN_ADS == 'OK' else "error ban ADS"

                                    if BAN_ADS == 'OK':

                                        app.sendMessage(

                                            Gap, "با موفقیت بن شد", message_id=msg.get('message_id'))

                                    print(Matnads)



                        elif '~ادمین نبود ' in getdataVLUE.split('_')[0]:

                            if not msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                if "بن نکن" in getdataVLUE.split('_')[1]:

                                    print('it is User')

                                    pass



                                elif "بن کن" in getdataVLUE.split('_')[1]:

                                    print('it is User')

                                    BAN_ADS = app.banGroupMember(Gap, msg.get(

                                        "author_object_guid")).get('status')

                                    Matnads = "ok ban ADS" if BAN_ADS == 'OK' else "error ban ADS"

                                    if BAN_ADS == 'OK':

                                        app.sendMessage(

                                            Gap, "با موفقیت بن شد", message_id=msg.get('message_id'))

                                    print(Matnads)



                            elif "وگرنه " in getdataVLUE.split('_')[1]:

                                if msg.get("author_object_guid") in [js["member_guid"] for js in app.getGroupAdmins(Gap)["data"]["in_chat_members"]]:

                                    if "بن نکن" in getdataVLUE.split('_')[2]:

                                        print('it is User')

                                        pass



                                    elif "بن کن" in getdataVLUE.split('_')[2]:

                                        print('it is User')

                                        BAN_ADS = app.banGroupMember(Gap, msg.get(

                                            "author_object_guid")).get('status')

                                        Matnads = "ok ban ADS" if BAN_ADS == 'OK' else "error ban ADS"

                                        if BAN_ADS == 'OK':

                                            app.sendMessage(

                                                Gap, "با موفقیت بن شد", message_id=msg.get('message_id'))

                                        print(Matnads)



                elif msg.get("text") == "سکوت" and msg.get("author_object_guid") in GetAdmin and on != False:

                    try:

                        if 'reply_to_message_id' in msg.keys():

                            typesend = app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                "data"]["messages"][0]["type"]

                            if 'Event' in typesend:

                                getkey = app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                    "data"]["messages"][0]["event_data"]["type"]

                            elif "Text" in typesend:

                                getkey = app.getMessagesInfo(Gap, [msg.get('reply_to_message_id')])[

                                    "data"]["messages"][0]["text"]

                            if getkey in loads("".join(open("pv.json", "r", encoding="utf-8").read())).keys():

                                readJson = loads(

                                    "".join(open("pv.json", "r", encoding="utf-8").read()))

                                readJson.pop(getkey)

                                open("pv.json", "w").write(dumps(readJson))

                                sleep(3)

                                app.sendMessage(Gap, "این دستور در حالت سکوت قرار گرفت", message_id=msg.get(

                                    "reply_to_message_id"))

                                print("sended sokot pv")

                            elif getkey in loads("".join(open("yad.json", "r", encoding="utf-8").read())).keys():

                                readJson = loads(

                                    "".join(open("yad.json", "r", encoding="utf-8").read()))

                                readJson.pop(getkey)

                                open("yad.json", "w").write(dumps(readJson))

                                sleep(3)

                                app.sendMessage(Gap, "این دستور در حالت سکوت قرار گرفت", message_id=msg.get(

                                    "reply_to_message_id"))

                                print(f"sended sokot {getkey}")

                            else:

                                app.sendMessage(Gap, "خطا: من چنین دستوری یاد نگرفتم", message_id=msg.get(

                                    "reply_to_message_id"))

                        else:

                            app.sendMessage(

                                Gap, "شما ریپ نزده اید", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text") == "/list" and on != False:

                    try:

                        gad = ""

                        addad = 0

                        for g in GetAdmin:

                            addad += 1

                            nameadmin = app.getUserInfo(

                                g)['data']['user']['first_name']

                            gad += f"{addad}: {nameadmin}\n"

                        app.sendMessage(

                            Gap, f"{gad}\n\nتعداد آدمین ها : {addad} نفر", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text") == "حالت روشن" and msg.get("author_object_guid") in GetAdmin:

                    try:

                        if on == False:

                            on = True

                            app.sendMessage(

                                Gap, "با موفقیت فعال شد", message_id=msg['message_id'])

                        else:

                            app.sendMessage(

                                Gap, "قبلا روشن شده است", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text") == "حالت خاموش" and msg.get("author_object_guid") in GetAdmin:

                    try:

                        if on == True:

                            on = False

                            app.sendMessage(

                                Gap, "با موفقیت غیرفعال شد", message_id=msg['message_id'])

                        else:

                            app.sendMessage(

                                Gap, "قبلا خاموش شده است", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text").startswith("/admin") and msg.get("author_object_guid") == admin and on != False:

                    try:

                        if 'reply_to_message_id' in msg.keys() and msg.get("text") == "/admin":

                            getguiduser = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])[

                                "data"]["messages"][0]["author_object_guid"]

                            check = os.path.exists("admins.json")

                            if check == True:

                                read = open("admins.json", "r",

                                            encoding="utf-8").read()

                                if read == "":

                                    buidadmin = {f"{getguiduser}": "Ok"}

                                    write = open("admins.json", "w").write(

                                        dumps(buidadmin))

                                    app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                        "reply_to_message_id"))

                                elif read != "":

                                    if read == "{}":

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r").read()))

                                        getguiduser = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])[

                                            "data"]["messages"][0]["author_object_guid"]

                                        getjsadmins.update(

                                            {f"{getguiduser}": "Ok"})

                                        write = open("admins.json", "w").write(

                                            dumps(getjsadmins))

                                        app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                            "reply_to_message_id"))

                                        getkeys = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        GetAdmin.append(getguiduser)

                                    else:

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        getguiduser = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])[

                                            "data"]["messages"][0]["author_object_guid"]

                                        if not getguiduser in getjsadmins.keys():

                                            getjsadmins.update(

                                                {f"{getguiduser}": "Ok"})

                                            write = open("admins.json", "w").write(

                                                dumps(getjsadmins))

                                            app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                                "reply_to_message_id"))

                                            getkeys = loads(

                                                "".join(open("admins.json", "r", encoding="utf-8").read()))

                                            GetAdmin.append(getguiduser)

                                        else:

                                            app.sendMessage(Gap, "این کاربر قبلا آدمین شده است", message_id=msg.get(

                                                "reply_to_message_id"))

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("admins.json", "w").write("{}")



                        elif "@" in msg.get("text").replace("/admin", "").split(" ")[-1]:

                            getguiduser = app.getInfoByUsername(msg.get("text").replace(

                                "/admin", "").split(" ")[-1])["data"]["user"]["user_guid"]

                            check = os.path.exists("admins.json")

                            if check == True:

                                read = open("admins.json", "r",

                                            encoding="utf-8").read()

                                if read == "":

                                    buidadmin = {f"{getguiduser}": "Ok"}

                                    write = open("admins.json", "w").write(

                                        dumps(buidadmin))

                                    app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                        "reply_to_message_id"))

                                elif read != "":

                                    if read == "{}":

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r").read()))

                                        getguiduser = app.getInfoByUsername(msg.get("text").replace(

                                            "/admin", "").split(" ")[-1])["data"]["user"]["user_guid"]

                                        getjsadmins.update(

                                            {f"{getguiduser}": "Ok"})

                                        write = open("admins.json", "w").write(

                                            dumps(getjsadmins))

                                        app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                            "reply_to_message_id"))

                                        getkeys = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        GetAdmin.append(getguiduser)

                                    else:

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        getguiduser = app.getInfoByUsername(msg.get("text").replace(

                                            "/admin", "").split(" ")[-1])["data"]["user"]["user_guid"]

                                        if not getguiduser in getjsadmins.keys():

                                            getjsadmins.update(

                                                {f"{getguiduser}": "Ok"})

                                            write = open("admins.json", "w").write(

                                                dumps(getjsadmins))

                                            app.sendMessage(Gap, "شما با موفقیت آدمین شده اید\n\nهم اکنون می توانید به من کلمه یاد دهید", message_id=msg.get(

                                                "reply_to_message_id"))

                                            getkeys = loads(

                                                "".join(open("admins.json", "r", encoding="utf-8").read()))

                                            GetAdmin.append(getguiduser)

                                        else:

                                            app.sendMessage(Gap, "این کاربر قبلا آدمین شده است", message_id=msg.get(

                                                "reply_to_message_id"))

                        else:

                            app.sendMessage(

                                Gap, "آیدی کاربری که میخوایی آدمین بشه رو به من ندادی 😐", message_id=msg['message_id'])

                    except:

                        continue



                elif msg.get("text").startswith("/unadmin") and msg.get("author_object_guid") == admin and on != False:

                    try:

                        if 'reply_to_message_id' in msg.keys() and msg.get("text") == "/unadmin":

                            getguiduser = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])[

                                "data"]["messages"][0]["author_object_guid"]

                            check = os.path.exists("admins.json")

                            if check == True:

                                read = open("admins.json", "r",

                                            encoding="utf-8").read()

                                if read == "":

                                    app.sendMessage(Gap, "فعلا بجز آدمین اصلی هیچ فرد دیگری آدمین نمی باشد", message_id=msg.get(

                                        "reply_to_message_id"))

                                elif read != "":

                                    if read == "{}":

                                        app.sendMessage(Gap, "فعلا بجز آدمین اصلی هیچ فرد دیگری آدمین نمی باشد", message_id=msg.get(

                                            "reply_to_message_id"))

                                    else:

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        getguiduser = app.getMessagesInfo(Gap, [msg.get("reply_to_message_id")])[

                                            "data"]["messages"][0]["author_object_guid"]

                                        if getguiduser in getjsadmins.keys():

                                            getjsadmins.pop(getguiduser)

                                            write = open("admins.json", "w").write(

                                                dumps(getjsadmins))

                                            app.sendMessage(Gap, "این کاربر از ادمینی برداشته شد", message_id=msg.get(

                                                "reply_to_message_id"))

                                            GetAdmin.remove(getguiduser)

                                        else:

                                            app.sendMessage(Gap, "این کاربر قبلا از ادمینی برداشته شده است", message_id=msg.get(

                                                "reply_to_message_id"))

                            else:

                                app.sendMessage(

                                    Gap, "در حال ساخت فایل بعد از 5 ثانیه دوباره دستور دهید", message_id=msg['message_id'])

                                open("admins.json", "w").write("{}")



                        elif "@" in msg.get("text").replace("/unadmin", "").split(" ")[-1]:

                            getguiduser = app.getInfoByUsername(msg.get("text").replace(

                                "/unadmin", "").split(" ")[-1])["data"]["user"]["user_guid"]

                            check = os.path.exists("admins.json")

                            if check == True:

                                read = open("admins.json", "r",

                                            encoding="utf-8").read()

                                if read == "":

                                    app.sendMessage(Gap, "فعلا بجز آدمین اصلی هیچ فرد دیگری آدمین نمی باشد", message_id=msg.get(

                                        "reply_to_message_id"))

                                elif read != "":

                                    if read == "{}":

                                        app.sendMessage(Gap, "فعلا بجز آدمین اصلی هیچ فرد دیگری آدمین نمی باشد", message_id=msg.get(

                                            "reply_to_message_id"))

                                    else:

                                        getjsadmins = loads(

                                            "".join(open("admins.json", "r", encoding="utf-8").read()))

                                        getguiduser = app.getInfoByUsername(msg.get("text").replace(

                                            "/unadmin", "").split(" ")[-1])["data"]["user"]["user_guid"]

                                        if getguiduser in getjsadmins.keys():

                                            getjsadmins.pop(getguiduser)

                                            write = open("admins.json", "w").write(

                                                dumps(getjsadmins))

                                            app.sendMessage(Gap, "این کاربر از ادمینی برداشته شد", message_id=msg.get(

                                                "reply_to_message_id"))

                                            GetAdmin.remove(getguiduser)

                                        else:

                                            app.sendMessage(Gap, "این کاربر قبلا از ادمینی برداشته شده است", message_id=msg.get(

                                                "reply_to_message_id"))

                        else:

                            app.sendMessage(

                                Gap, "آیدی کاربری که میخوایی از آدمینی برداشته بشه رو به من ندادی 😐", message_id=msg['message_id'])

                    except:

                        continue



            elif msg.get("type") == "Event" and not msg['message_id'] in limsg and on != False:

                try:

                    print("message glass")

                    limsg.append(msg['message_id'])

                    GetGuid_Glass = msg['event_data']['peer_objects'][0]['object_guid'] if 'peer_objects' in msg['event_data'].keys(

                    ) else msg['event_data']['performer_object']['object_guid']

                    if msg.get("event_data").get("type") in loads("".join(open("yad.json", "r", encoding="utf-8").read())).keys() and not msg['message_id'] in messageidjson:

                        if "#اسم" or "#ایدی" or "#گروه" or "#فامیلی" or "#لینک" or "#بیو" or "#ساعت" in str(loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('event_data').get('type'))):

                            ide = "#not" if not "username" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                            ) else f"@{app.getUserInfo(GetGuid_Glass)['data']['user']['username']}"

                            family = "#not" if not "last_name" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                            ) else app.getUserInfo(GetGuid_Glass)['data']['user']['last_name']

                            name = "#not" if not "first_name" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                            ) else app.getUserInfo(GetGuid_Glass)['data']['user']['first_name']

                            bio = "#not" if not "bio" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                            ) else app.getUserInfo(GetGuid_Glass)['data']['user']['bio']

                            sendmatn = loads(''.join(open('yad.json', 'r', encoding='utf-8').read())).get(msg.get('event_data').get('type')).replace("#اسم", name).replace("#ایدی", ide).replace("#بیو", bio).replace(

                                "#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family).replace("#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}")

                            app.sendMessage(

                                Gap, sendmatn, message_id=msg['message_id'])

                            messageidjson.append(msg['message_id'])

                            print("sended glass Gap")

                        else:

                            app.sendMessage(

                                Gap, f"{loads(''.join(open('yad.json','r',encoding = 'utf-8').read())).get(msg.get('event_data').get('type'))}", message_id=msg['message_id'])

                            messageidjson.append(msg['message_id'])

                            print("sended glass Gap")



                    else:

                        if msg.get("event_data").get("type") in loads("".join(open("pv.json", "r", encoding="utf-8").read())).keys() and not msg['message_id'] in messageidjson:

                            pv = msg['event_data']['performer_object']['object_guid']

                            if "#اسم" or "#ایدی" or "#گروه" or "#فامیلی" or "#لینک" or "#بیو" or "#ساعت" in str(loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('event_data').get('type'))):

                                ide = "#not" if not "username" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                                ) else f"@{app.getUserInfo(GetGuid_Glass)['data']['user']['username']}"

                                family = "#not" if not "last_name" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                                ) else app.getUserInfo(GetGuid_Glass)['data']['user']['last_name']

                                name = "#not" if not "first_name" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                                ) else app.getUserInfo(GetGuid_Glass)['data']['user']['first_name']

                                bio = "#not" if not "bio" in app.getUserInfo(GetGuid_Glass)['data']['user'].keys(

                                ) else app.getUserInfo(GetGuid_Glass)['data']['user']['bio']

                                sendmatn = loads(''.join(open('pv.json', 'r', encoding='utf-8').read())).get(msg.get('event_data').get('type')).replace("#اسم", name).replace("#ایدی", ide).replace("#بیو", bio).replace(

                                    "#گروه", app.getGroupInfo(Gap)["data"]["group"]["group_title"]).replace("#فامیلی", family).replace("#ساعت", f"{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}")

                                app.sendMessage(

                                    pv, sendmatn, message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended glass pv")

                            else:

                                app.sendMessage(

                                    pv, f"{loads(''.join(open('pv.json','r',encoding = 'utf-8').read())).get(msg.get('event_data').get('type'))}", message_id=msg['message_id'])

                                messageidjson.append(msg['message_id'])

                                print("sended glass pv")

                except Exception as error:

                    print(error)



    except FileNotFoundError:

        if sended == False:

            app.sendMessage(

                Gap, "در حال ساخت فایل مورد نظر بعد از چند ثانیه دوباره دستور دهید")

            sended = True

        else:

            ...

        yad = os.path.exists("yad.json")

        admins = os.path.exists("admins.json")

        pve = os.path.exists("pv.json")

        if admins == False:

            open("admins.json", "w").write("{}")

            print("starting building admins.json")

        elif yad == False:

            open("yad.json", "w").write("{}")

            print("starting building yad.json")

        elif pve == False:

            open("pv.json", "w").write("{}")

            print("starting building pv.json")

    except Exception as s:

        print(s)
