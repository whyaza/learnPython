from selenium import webdriver
from selenium.webdriver import ActionChains
import time 

# browser = webdriver.Chrome()
# try:
    # browser.get('http://www.baidu.com')
    # print(browser.page_source)
    # input_k = browser.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]')
    # input_k.send_keys('美女')
    # print(input_k)
    # time.sleep(1)
    # input_k.clear()
    # input_k.send_keys('sb')
    # print(input_k)
    # time.sleep(1)
    # input_k.clear()
# finally:
#     browser.close()

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_elements_by_css_selector('#draggable')
# target = browser.find_elements_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("TO BOTTOM")')

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)

# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# print(browser.get_cookie)

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('http://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')




