from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()
browser.get("填入你要爬取的网址相应的登录页面")  # 这里只是简单的模拟登陆，必要时需要传入cookies信息保持登陆状态
browser.find_element_by_name('userName').send_keys('此处输入用户名')
browser.find_element_by_name('userPwd').send_keys('此处输入密码')
browser.find_element_by_class_name('btn').click()


def get_page(id_0):

    base_url = '填入通过提取得到的爬取的网址,为了配合get请求传参需后缀加入"？"'
    id_0 = '&id=' + str(id_0)
    ref = '&ref=s%3Deboss%2Flist%26repeat%3D0%26cta%3D0%26ctb%3D0%26pubuser%3D24%26field%3Did%26kwd%3D%26u%3Dproduct'
    u = 'u=product'
    url = base_url + u + id_0 + ref
    try:
        time.sleep(1)
        js = "window.open('%s')" % url
        print(js)
        browser.execute_script(js)  # 打开一个新的标签页并请求你要爬取的网址
        handles = browser.window_handles  # 返回值为所有标签页组成的列表 
        browser.switch_to_window(handles[1])  # 切换标签页执行后续页面操作
        sel = browser.find_element_by_name('ctb')  # 选择新标签页下的下拉菜单节点元素
        Select(sel).select_by_value("1327")  # 选择需要的键值
        btn = browser.find_element_by_css_selector("[class='btn fixed']")  # 选择保存按钮的节点元素
        btn.click()  # 给按钮添加点击事件
        browser.close()  # 关闭当前标签页
        browser.switch_to_window(handles[0])  # 再切回到第一个标签页
    except:
        print(id, "访问失败")


def main():

    for i in range(1000):
        get_page(i)


if __name__ == '__main__':

    main()
