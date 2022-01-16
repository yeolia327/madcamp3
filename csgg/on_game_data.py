from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import requests

champion_name = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu',
             'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelionsol', 'Azir',
             'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille',
             'Cassiopeia', 'Chogath', 'Corki', 'Darius', 'Diana', 'Drmundo',
             'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks',
             'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
             'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi',
             'Irelia', 'Ivern', 'Janna', 'Jarvaniv', 'Jax', 'Jayce',
             'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Karma', 'Karthus',
             'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Khazix',
             'Kindred', 'Kled', 'Kogmaw', 'Leblanc', 'Leesin', 'Leona',
             'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite',
             'Malzahar', 'Maokai', 'Masteryi', 'Missfortune', 'Mordekaiser', 'Morgana',
             'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne',
             'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy',
             'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', 'Reksai',
             'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze',
             'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco',
             'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner',
             'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahmkench',
             'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana',
             'Trundle', 'Tryndamere', 'Twistedfate', 'Twitch', 'Udyr', 'Urgot',
             'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vex', 'Vi',
             'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Monkeyking',
             'Xayah', 'Xerath', 'Xinzhao', 'Yasuo', 'Yone', 'Yorick',
             'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

ImgList = ['https://opgg-static.akamaized.net/images/lol/champion/Aatrox.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ahri.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Akali.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Akshan.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Alistar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Amumu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Anivia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Annie.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Aphelios.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ashe.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Aurelionsol.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Azir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Bard.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Blitzcrank.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Brand.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Braum.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Caitlyn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Camille.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Cassiopeia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Chogath.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Corki.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Darius.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Diana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Drmundo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Draven.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ekko.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Elise.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Evelynn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ezreal.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fiddlesticks.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fiora.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fizz.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Galio.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gangplank.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Garen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gnar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gragas.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Graves.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gwen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Hecarim.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Heimerdinger.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Illaoi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Irelia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ivern.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Janna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jarvaniv.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jax.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jayce.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jhin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jinx.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kaisa.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kalista.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Karma.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Karthus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kassadin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Katarina.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kayle.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kayn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kennen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Khazix.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kindred.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kled.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kogmaw.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Leblanc.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Leesin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Leona.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lillia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lissandra.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lucian.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lulu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lux.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Malphite.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Malzahar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Maokai.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Masteryi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Missfortune.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Mordekaiser.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Morgana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nami.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nasus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nautilus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Neeko.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nidalee.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nocturne.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nunu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Olaf.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Orianna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ornn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Pantheon.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Poppy.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Pyke.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Qiyana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Quinn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rakan.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rammus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Reksai.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rell.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Renekton.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rengar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Riven.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rumble.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ryze.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Samira.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sejuani.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Senna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Seraphine.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sett.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shaco.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shyvana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Singed.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sion.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sivir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Skarner.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sona.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Soraka.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Swain.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sylas.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Syndra.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Tahmkench.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Taliyah.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Talon.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Taric.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Teemo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Thresh.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Tristana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Trundle.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Tryndamere.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Twistedfate.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Twitch.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Udyr.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Urgot.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Varus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vayne.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Veigar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Velkoz.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vex.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Viego.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Viktor.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vladimir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Volibear.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Warwick.png',
 'https://opgg-static.akamaized.net/images/lol/champion/MonkeyKing.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Xayah.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Xerath.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Xinzhao.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yasuo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yone.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yorick.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yuumi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zac.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zed.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ziggs.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zilean.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zoe.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zyra.png']


def renewalOPGG(Name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
    url = 'https://www.op.gg/summoner/userName=' + Name
    action = ActionChains(driver)
    driver.get(url)

    try:
        driver.find_element_by_css_selector('.Button.SemiRound.Blue').click()
        action.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get_screenshot_as_file('opgg.png')
    except Exception as ex:
        print("exception: ", ex)
        driver.quit()
    driver.quit()


def ingameOPGG(Name):
    print("분석중")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    url = 'https://www.op.gg/summoner/userName=' + Name

    driver.get(url)
    Container = {}

    driver.find_element_by_css_selector('.SpectateTabButton').click()
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find("link").attrs['href']

    Container['Link'] = link

    ingameInfo = soup.find("div", {"class": "tabItem Content SummonerLayoutContent summonerLayout-spectator"})

    names = ingameInfo.find_all("td", {"class": "SummonerName Cell"})
    Container['Names'] = []

    if len(names) == 0:
        return Container

    for name in names:
        Container['Names'].append(name.text.strip())

    champions = ingameInfo.find_all("td", {"class": "ChampionImage Cell"})
    Container['Champions'] = []
    for champion in champions:
        champ = str(champion.find("a").attrs['href'])
        champ = champ.replace("/champion/", '').replace("/statistics", '').capitalize()
        Container['Champions'].append(champ)

    tiers = ingameInfo.find_all("td", {"class": "CurrentSeasonTierRank Cell"})
    Container['Tiers'] = []
    for tier in tiers:
        Container['Tiers'].append(tier.text.strip())

    ratios = ingameInfo.find_all("td", {"class": "RankedWinRatio Cell"})
    Container['Ratios'] = []
    for ratio in ratios:
        Container['Ratios'].append(ratio.text.replace('\n', '').replace('\t', '').strip())

    champRatios = ingameInfo.find_all("td", {"class": "ChampionInfo Cell"})
    Container['Champion Ratios'] = []
    for champRatio in champRatios:
        Container['Champion Ratios'].append(
            champRatio.text.replace(' ', '').replace('\n', '').replace('\t', '').strip())

    Container['Champion Images'] = []
    for i in range(len(Container['Champions'])):
        Container['Champion Images'].append(ImgList[champion_name.index(Container['Champions'][i])])

    driver.quit()

    return Container

# if __name__ == "__main__":
#     # renewalOPGG("Xqzlomq123")
#     total = ingameOPGG("SeongHw4n")
#     if(len(total['Names']) == 0):
#         print("게임중이 아닙니다")
#     else:
#         idlist = total['Names']
#         champlist = total['Champions']
#         print(idlist)
#         print(champlist)
