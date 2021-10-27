    # Telegram bot settings
import telebot
bot = telebot.TeleBot('2018620537:AAFRlA6ilkvL2g2guN0_0OWpY-eNgWecOQo')
channel_id = '@world_news_on'
group_id = ''



# TElegraph settings
from telegraph import Telegraph
telegraph = Telegraph()
telegraph.create_account(short_name='News World')
def CreatePage( title ,html_content):
    print('   Creating Telegraph page !!!   ')

    for i in html_content.select('script'):
        i.extract()    
    html_content = str(html_content).replace('div', 'p')
    response = telegraph.create_page(
        title,
        html_content=str(html_content)
    )
    link = 'https://telegra.ph/{}'.format(response['path']) 
    return link



