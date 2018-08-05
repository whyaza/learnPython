import pymongo 
from pypinyin import pinyin, lazy_pinyin, Style
from selenium import webdriver
import selenium

def get_all_name():
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.HEUteacher
    namecollentions = db.CN
    all_ = namecollentions.find()
    names = []
    for item in all_:
        pinlist = lazy_pinyin(item.get('name'))
        name = ''
        for pl in pinlist:
            name += pl
        names.append(name)

    return names #返回所有教师的名字拼音

def get_one_page(browser,url):
    print('正在爬取',url)
    browser.get(url)
    
    try:
        name = browser.find_element_by_css_selector('.h_left h1').text
        depart = browser.find_elements_by_css_selector('.h_left p font')[0].text
        science = browser.find_elements_by_css_selector('.h_left p font')[1].text
        localed = browser.find_elements_by_css_selector('.h_left p font')[2].text
        localed_c = browser.find_elements_by_css_selector('.h_left p font')[3].text
        guider = browser.find_elements_by_css_selector('.h_left p font')[4].text
        telephone =  browser.find_elements_by_css_selector('.h_left p font')[5].text
        email =  browser.find_elements_by_css_selector('.h_left p font')[7].text
        yb =  browser.find_elements_by_css_selector('.h_left p font')[8].text
        address =  browser.find_elements_by_css_selector('.h_left p font')[9].text

        def list_to_allstring(list1):
            allstring = ''
            for l in list1:
                allstring += l.text 
            return allstring 

        profile_list = browser.find_elements_by_css_selector('.mlr40') 
        profile = list_to_allstring(profile_list)
        
        button_sci_study = browser.find_element_by_css_selector('#tab3 a label')
        button_sci_study.click()
        sci_study_list =  browser.find_elements_by_css_selector('.mlr40') 
        sci_study = list_to_allstring(sci_study_list)

        button_teaching = browser.find_element_by_css_selector('#tab4 a label')
        button_teaching.click()
        teaching_list =  browser.find_elements_by_css_selector('.mlr40') 
        teaching = list_to_allstring(teaching_list)

        button_society = browser.find_element_by_css_selector('#tab5 a label')
        button_society.click()
        socity_list =  browser.find_elements_by_css_selector('.mlr40') 
        socity = list_to_allstring(socity_list)

        button_achievement = browser.find_element_by_css_selector('#tab6 a label')
        button_achievement.click()
        achievement_list =  browser.find_elements_by_css_selector('.mlr40') 
        achievement = list_to_allstring(achievement_list)

        button_honer = browser.find_element_by_css_selector('#tab7 a label')
        button_honer.click()
        honer_list =  browser.find_elements_by_css_selector('.mlr40') 
        honer = list_to_allstring(honer_list)
               
    except selenium.common.exceptions.NoSuchElementException :
        print('teacher change page.')
    except Exception as e:
        print('no meaning exception'+e.args)
    else:
        teacher = {
            'name' : name ,
            'depart' : depart,
            'science':science,
            'localed':localed,
            'localed_c':localed_c,
            'guider' : guider,
            'telephone':telephone,
            'email':email,
            'yb':yb,
            'address':address,
            'profile':profile,
            'sci_study':sci_study,
            'teaching' :teaching,
            'socity' :socity,
            'achievement' :achievement,
            'honer':honer 
        }
        return teacher 

def save_to_mongo(teacher):
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.HEUteacher
    colltions_teacher = db.teachers
    res = colltions_teacher.insert_one(teacher)
    print(res)

def main():
    names = get_all_name()
    browser = webdriver.Chrome()
    for n in names :
        url = 'http://homepage.hrbeu.edu.cn/web/'+n
        teacher = get_one_page(browser,url)
        if teacher is not None:
            save_to_mongo(teacher)

if __name__ == '__main__':
    main()
