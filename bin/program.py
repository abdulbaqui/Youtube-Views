import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.add_argument("--disable-blink-features=AutomationControlled") 
Options.add_experimental_option("excludeSwitches", ["enable-automation"])
Options.add_experimental_option("useAutomationExtension", False) 
Options.add_argument("--mute-audio")
Options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=Options)
driver.maximize_window()
Options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.refresh()

_url ="https://www.youtube.com/watch?v=AhCPVDVGosQ&ab_channel=GameInfoGraphics"
_videoduration_inseconds = 95
_videoiteration_time = 500
intilization_flag = True

# get video time
def video_duration():
    if driver.find_element("xpath","//span[@class='ytp-time-duration']"):
        video_time = driver.find_element("xpath","//span[@class='ytp-time-duration']")
        print("Video time",video_time.text)
    return video_time

#  get ads time
def ad_duration():
    ad_time = 0
    if driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[2]/span[2]/div"):
        ad_time = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[2]/span[2]/div").text
        print("Ad time",ad_time.text)
    return int(ad_time)
    
def iniailize(url):
    driver.get(url)
    time.sleep(2)

def accept_agreement():
    scrollbar_div =  driver.find_element("xpath",'/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]')
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollbar_div)
    time.sleep(1)
    btn_AcceptAll = driver.find_element("xpath","/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
    btn_AcceptAll.click()


def start(url,videoduration,intilization_flag):
    iniailize(url)
    try:
        accept_agreement()
    except:
        pass
    time.sleep(6)
    try:
        if driver.find_elements("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[3]/div/span/div"):
            print("Video will play after the ad")
        else:
            time.sleep(10)
    except:
        pass
    try: 
        if driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button"):
            driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button").click()
    except:
        pass
    time.sleep(videoduration + 10)
counter = 0 
for  i in range(0,_videoiteration_time,1):
    driver.refresh()
    start(_url,_videoduration_inseconds,intilization_flag)
    counter += 1
    intilization_flag = False
    print(counter)
    time.sleep(5)


print("activity end")
