from main.models import Post
import requests
from bs4 import BeautifulSoup
from slugify import slugify
import time
from .telegraph_telebot import CreatePage, channel_id, bot



# # Main Post-Updater
# def schedule_api():
# 	print(' ___ Update Start ___')
# 	r = requests.get("https://kun.uz/news/list")
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})
# 	cd_headings_hrefs = [i['href'] for i in cd_headings] 

# 	time.sleep(2)

# 	for th in cd_headings_hrefs:
# 		href = th['href']
# 		slug = slugify(th)
# 		post_url = f"https://kun.uz{th}"
# 		single_r = requests.get(post_url)
# 		single_soup = BeautifulSoup(single_r.text, 'html.parser')

# 		body_html_code = single_soup.find('div', {"class":"single-layout__center slc"})
# 		all_paragraphs = body_html_code.findAll('p')
# 		title = body_html_code.find('div', {"class":"single-header__title"}).text
# 		num_of_views = body_html_code.find("div", {"class": "view"}).text
# 		published_date = body_html_code.find("div", {"class":"date"}).text
# 		all_images = body_html_code.findAll("img")
# 		main_image = ''
# 		if len(all_images) != 0:
# 			main_image = str(all_images[0]['src'])
# 		else:
# 			main_image = 'https://storage.kun.uz/source/7/aBPEwW3hHczPbUVmaUNMxzh2tKnsp8Dg.jpg'
				
# 		print(' =================== ')
# 		print('Title = ', title)
# 		print('Views = ', num_of_views)
# 		print('Published date = ', published_date)
# 		print('Num of images', len(all_images))
# 		for image in all_images:
# 			print('  Image = ', image)
# 		try:
# 			post = Post.objects.get(slug=str(slug))
# 			post.source = post_url
# 			post.image = main_image
# 			post.save()
# 		except :
# 			Post.objects.create( body=str(body_html_code) ,slug=slug, title=title, views=num_of_views, image_2=main_image)
# 			CreatePage(title, html_content=body_html_code)
# 			tg_link = CreatePage(title, body_html_code)
# 			bot.send_photo(
# 			parse_mode='HTML',
# 			chat_id=channel_id, 
# 			photo=main_image , 
# 			caption=f' <b> {title} </b>  \n   {str(all_paragraphs[0].text) } \n \n  {tg_link} \n \n \n 	')
# 			bot.send_message(parse_mode='HTML', text='<video width="320" height="240" controls>  <source src="movie.mp4" type="video/mp4"><source src="movie.ogg" type="video/ogg">  Your browser does not support the video tag.</video>', chat_id=channel_id)

# 	print(' ___ Update End ___')	
# 	return True	
# 




def schedule_api():
	r = requests.get("https://kun.uz/news/list")
	soup = BeautifulSoup(r.text, 'html.parser')
	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})
	print(len(cd_headings))
	for th in soup.findAll("a", {"class": "daily-block l-item"}):
		href = th['href']
		slug = slugify(href)
		post_url = f"https://kun.uz{href}"
		single_r = requests.get(post_url)
		single_soup = BeautifulSoup(single_r.text, 'html.parser')
		view = single_soup.find("div", {"class": "view"}).text
		title = single_soup.find('div', {"class":"single-header__title"}).text	
		body_code = single_soup.find('div', {"class":"single-content"})

		main_img_ls = body_code.findAll('img')
		paragraphs = body_code.findAll('p')

		main_img = ''

		if len(main_img_ls) != 0:
			main_img = main_img_ls[0]['src']
		else:
			main_img = 'https://storage.kun.uz/source/thumbnails/_medium/7/L88XGffdJ2B1z7VmOZQTVboR-FMgL2mP_medium.jpg'

		body = str(body_code)


		try :
			post = Post.objects.get(slug=str(slug))
			post.source = post_url
			post.image = main_img
			post.save()
		except :
			Post.objects.create( body=str(body_code), rich_body=str(body_code) ,slug=slug, title=title, views=view)
			CreatePage(title, html_content=body_code)
			tg_link = CreatePage(title, body_code)
			bot.send_photo(
			parse_mode='HTML',
			chat_id=channel_id, 
			photo=main_img, 
			caption=f' <b> {title} </b>  \n   {str(paragraphs[0].text) } \n \n  {tg_link} \n \n \n 	')
			bot.send_message(parse_mode='HTML', text=f" <b> {title} </b> \n \n {paragraphs[0].text} ", chat_id=channel_id)

		print(title, 'Title')
		print(slug, 'Slug')
		print(post_url, ' Post Url')
		print(view, 'views')
		print(body[:20], 'Body Code')
		print(main_img, 'Main IMG')
		print('all')
		print('=================================================================')
	return True