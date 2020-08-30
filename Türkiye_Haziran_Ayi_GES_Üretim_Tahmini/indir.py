import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



startt="01.10.2019"
finishh="31.07.2020"
gess=["AFTA GES-40W000000013383H","ALİBEY GES-40W000000014503S","ALİBEYHÖYÜĞÜ GES-40W000000013603T","APA GES-40W000000013463J",
      "CINGILLI GES-40W000000013605P","DENİZLİ TAVAS GES-40W000000013743D","HALK ENERJİ ERZURUM GES-40W000000010600D","HAMAL GES-40W0000000123055",
      "ME-SE GES-40W0000000123500","MT GES-40W000000012349M","OMİCRON ENGİL208 GES-40W000000012347Q","OMİCRON ERCİŞ GES-40W000000012346S",
      "PSİ ENGİL 207 GES-40W000000013023A","RA GÜNEŞ MARDİN GES-40W0000000137661","RENOE GES-40W000000011623X","SOLANA KONYA GES-40W000000013363N",
      "SOLENTEGRE GES-40W000000010590R","YAYSUN GES-40W000000012348O"]



def tam_indirr(start,finish,ges):
    driver = webdriver.Chrome(executable_path=r'C:\Users\Ahmet YÜKSEL\Downloads\chromedriver.exe')
    driver.get('https://seffaflik.epias.com.tr/transparency/uretim/gerceklesen-uretim/gercek-zamanli-uretim.xhtml');

    x=driver.find_element_by_id("j_idt206:date1_input")
    x.clear()
    x.send_keys(start)
    x.send_keys(Keys.ENTER)
    #print("tarih1")
    y=driver.find_element_by_id("j_idt206:date2_input")
    y.clear()
    y.send_keys(finish)
    y.send_keys(Keys.ENTER)
    #print("tarih2")
    #time.sleep(5) # Let the user actually see something!
    t=driver.find_element_by_id("j_idt206:powerPlant")
    t.click()
    f=driver.find_element_by_id("j_idt206:powerPlant_filter")

    #print("yer")
    k=f.send_keys(ges)
    f.send_keys(Keys.ENTER)

    #print("entirr")
    h=driver.find_element_by_id("j_idt206:goster")
    h.click()
    time.sleep(5)
    print("indir")
    y=driver.find_element_by_id("j_idt206:dt:j_idt264").click()
    time.sleep(5)
    driver.quit()
    ress="indi"
    return ress




tam_indirr(startt,finishh,gess[1])
