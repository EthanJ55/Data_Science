import requests
from lxml import etree
import os


def search_article(url):
	header = {
		'Accept': '*/*',
		'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) '
						'AppleWebKit/537.36 (KHTML, like Gecko) '
						'Chrome/87.0.4280.88 Safari/537.36'
	}
	resp = requests.get(url, headers=header)
	try:
		html_str = str(resp.content, 'utf-8')
		selector = etree.HTML(html_str)
		return selector
	except Exception:
		return '牛牛'


def parse_html(selector):
	try:
		title = selector.xpath('//h1/text()')[0]
		article = selector.xpath('//div[@class="article"]/p//text()')
		return {title: article}
	except Exception:
		return {'解析错误': [Exception]}


def write_article(article, directory):
	title = list(article.keys())[0]
	file_path = directory + title + '.txt'
	try:
		f = open(file_path, 'w', encoding='utf-8')
		for content in article[title]:
			f.write(str(content) + '\n')
		f.close()
	except Exception:
		return


def extract_url(url):
	temp = search_article(url)
	if temp == '牛牛':
		return temp
	href_list = temp.xpath("//div[@id='syncad_1']//h1//a//@href")
	return href_list


def get_date():
	# 从2020.01.01到2020.12.31
	res = []
	for month in range(1, 13):
		if month in [1, 3, 5, 7, 8]:
			for day in range(1, 32):
				if day < 10:
					res.append('0' + str(month) + '0' + str(day))
				else:
					res.append('0' + str(month) + str(day))
		elif month in [4, 6, 9]:
			for day in range(1, 31):
				if day < 10:
					res.append('0' + str(month) + '0' + str(day))
				else:
					res.append('0' + str(month) + str(day))
		elif month in [10, 12]:
			for day in range(1, 32):
				if day < 10:
					res.append(str(month) + '0' + str(day))
				else:
					res.append(str(month) + str(day))
		elif month == 11:
			for day in range(1, 31):
				if day < 10:
					res.append(str(month) + '0' + str(day))
				else:
					res.append(str(month) + str(day))
		else:
			for day in range(1, 30):
				if day < 10:
					res.append('0' + str(month) + '0' + str(day))
				else:
					res.append('0' + str(month) + str(day))
	return res


if __name__ == '__main__':
	words = ['疫', '肺炎', 'COVID', 'covid', '感染', '症状', '新冠', '病例', '武汉', 'WTO', '世卫', '湖北', '病毒']
	words = set(words)
	count = 0
	date_list = get_date()
	path = 'http://news.sina.com.cn/head/news2020'
	for i in date_list[0]:
		# 早上的要闻
		directory = 'data/' + i + 'am/'
		os.mkdir(directory)
		url = path + i + 'am.shtml'
		href_list = extract_url(url=url)
		if href_list == '牛牛':
			pass
		else:
			for href in href_list:
				html = search_article(href)
				article = parse_html(html)
				for title in article:
					for word in words:
						if word in title:
							write_article(article, directory)

		# 晚上的要闻
		directory = 'data/' + i + 'pm/'
		os.mkdir(directory)
		url = path + i + 'pm.shtml'
		href_list = extract_url(url=url)
		if href_list == '牛牛':
			continue
		for href in href_list:
			html = search_article(href)
			article = parse_html(html)
			for title in article:
				for word in words:
					if word in title:
						write_article(article, directory)

		print(i[:2] + '.' + i[2:] + ' done')
