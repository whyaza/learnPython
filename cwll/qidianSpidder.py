from selenium import webdriver
import os
import selenium
import time

begin_url = 'https://read.qidian.com/chapter/31x8tOUW-AMsmgY_yC2imA2/zxx5rE6QQyf4p8iEw--PPw2' 
xname = '1950香江大亨'
def get_oneCharpter(browser,xdir):
    try:
        title = browser.find_element_by_class_name('j_chapterName')
        content = browser.find_element_by_class_name('j_readContent')
        titlepath = xdir + '/' + title.text
        with open(titlepath,'w') as f:
            f.write(title.text+'\n')
            f.write(content.text)
        print(title.text+'已写入文件')
        time.sleep(1)
        next_button = browser.find_element_by_css_selector('#j_chapterNext')
        next_button.click()
        get_oneCharpter(browser,xdir)
    except selenium.common.exceptions.NoSuchElementException:
        print('一个小说爬取完毕')
        return None 

def main():
    browser = webdriver.Chrome()
    browser.get(begin_url)
    filedir = '/home/wuhongyu/Desktop/qidian'
    xdir = filedir +'/' +xname
    if not os.path.exists(xdir):
        os.makedirs(xdir)
        #下面做一个第一次进入本小说页面的初始化操作
        browser.implicitly_wait(10)
        try:
            close_lbf_button = browser.find_element_by_class_name('lbf-panel-close')
            close_lbf_button.click()
            print('关闭悬浮标签页面')
        except Exception:
            print('no lbf.')
        get_oneCharpter(browser,xdir)
        

if __name__ == '__main__':
    main()
