# import requests
# # r = requests.post("https://login.vk.com/?act=login", data={'act':'login', 'role':'al_frame', 'expire':'','_origin':'https://vk.com','ip_h':'b5c895052695bdcb15', 'lg_h': 'b0c7b2dc22b982dd72', 'email': 'berserk@mail.ru', 'pass': 'uniiiispanec'})
# r = requests.post("https://www.facebook.com/login/", {"email":"+79501111111", "pass":"pass"})
# print(r.status_code, r.reason)
# # print(r.text)




# import requests
# r = requests.post("https://auth.mail.ru/cgi-bin/auth", {"Login":"mmmail@bk.ru", "Password":"pass"})
# print(r.status_code, r.reason)
# print(r.text)

# from twill.commands import *

# go('https://auth.mail.ru/cgi-bin/auth')
# fv("1", "Login", "mmmail@bk.ru")
# fv("1", "Password", "pass")
# submit('0')
# showhistory()

# # import io
# # with io.open("html.html", "w", encoding="utf-8") as f:
# #     f.write()





# from twill.commands import *

# go('https://www.facebook.com/login/')
# fv("1", "email", "+79501111111")
# fv("1", "pass", "pass")
# submit('0')


# from twill.commands import *

# go('https://www.facebook.com/checkpoint/?next')
# # fv("1", "jazoest", "21014")
# # fv("1", "fb_dtsg", "RKljTXeTvc0=")
# # fv("1", "nh", "e5be4d1e9e34e185427dd31f4b26e8d2ab67bcf1")
# # fv("1", "approvals_code", "246202")
# fv("1", "email", "+79501111111")
# fv("1", "pass", "pass")
# showforms()
# # show()
# # submit('0')


# import io
# with io.open("html.html", "w", encoding="utf-8") as f:
#     f.write(show())



# from twill.commands import *

# go('https://auth.mail.ru/cgi-bin/secstep')
# fv("1", "Login", "mmmail@bk.ru")
# fv("1", "AuthCode", "lkknll")
# show()
# showforms()
# submit('0')
 
# import io
# with io.open("html.html", "w", encoding="utf-8") as f:
#     f.write(show())








# import requests

# URL = "https://www.facebook.com/login/"
# payload = {"email":"+79501111111", "pass":"pass"}

# session = requests.Session()
# session.headers = {"User-Agent":"Mozilla/5.0"}

# req = session.post(URL, data=payload)
# cook = req.cookies

# URL = "https://www.facebook.com/checkpoint/?next"
# payload = {"approvals_code":"686472"}

# req2 = session.post(URL, data=payload)
# print(req2.result_code)





# from twill.commands import *

# go('https://www.facebook.com/login/')
# fv("1", "email", "+79501111111")
# fv("1", "pass", "pass")
# submit('0')
# showhistory()








# import mechanize

# url = "https://www.facebook.com/login"
# br = mechanize.Browser()
# br.set_handle_robots(False) # ignore robots
# br.open(url)
# br.select_form(id="login_form")
# br["email"] = "+79501111111"
# br["pass"] = "pass"
# res = br.submit()

# url = "https://www.facebook.com/checkpoint/?next"
# br.open(url)
# br.select_form(id="u_0_a")
# br["approvals_code"] = "514331"
# res = br.submit()

# content = res.read()
# with open("mechanize_results.html", "wb") as f:
#     f.write(content)


# for form in br.forms():
	# print(form)














# import mechanize

# url = "https://mail.ru/"
# br = mechanize.Browser()
# br.set_handle_robots(False) # ignore robots
# br.open(url)

# br.select_form(name="Auth")
# br["Login"] = "mmmail@bk.ru"
# br["Password"] = "pass"
# res = br.submit()
# print(res.cookies)
# url = "https://auth.mail.ru/cgi-bin/secstep"
# br.open(url)
# # br.select_form(nr=0)
# for form in br.forms():
# 	print(form)
# # br.submit()
# # br.select_form(id="u_0_a")
# # br["approvals_code"] = "514331"
# # res = br.submit()

# content = res.read()
# # with open("mechanize_results.html", "wb") as f:
# #     f.write(content)






















# import mechanize, urllib

# url = "https://mail.ru"
# br = mechanize.Browser()
# br.set_handle_robots(False)
# br.open(url)
# br.select_form(nr=0)
# br["Login"] = "mmmail@bk.ru"
# br["Password"] = "pass"
# res1 = br.submit()

# # br.open('https://auth.mail.ru/cgi-bin/secstep?FromAccount=1&send_sms=1')
# # br.open('https://auth.mail.ru/cgi-bin/secstep?FromAccount=1')
# print(br.forms())

# code = str(input('input code: '))
# params = {u'AuthCode':code, u'Login':'mmmail@bk.ru', u'Password':'pass'}
# data = urllib.parse.urlencode(params)
# request = mechanize.Request('https://auth.mail.ru/cgi-bin/secstep')
# # response = mechanize.urlopen(request, data=data)
# req = br.open(request, data=data)
# input('just tap ok')



# f = open('secstep.txt', 'wb')
# f.write(r.read())
# f.close()


# url = "https://auth.mail.ru/cgi-bin/secstep"


# url = "https://auth.mail.ru/cgi-bin/secstep"
# br.open(url)
# # br.select_form('')

# br.submit()
# br.select_form(id="u_0_a")
# br["approvals_code"] = "514331"
# res = br.submit()