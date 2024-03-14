import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# 定义目标论坛的URL
url = 'https://www.reddit.com/r/Python/'

# 发送HTTP请求获取页面内容
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

# 确保请求成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取帖子标题和评论内容
    # 注意：这里的类名是假设的，你需要根据实际页面结构调整
    posts = soup.find_all('div', class_='Post')

    # 统计不同情感的数量
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for post in posts:
        # 假设的标题和评论选择器，根据实际情况调整
        title = post.find('h3').text.strip()  # 假设帖子标题在<h3>标签内
        comments = post.find_all('p', class_='comment')  # 假设评论在<p>标签内，类名为'comment'

        # 对帖子标题进行情感分析
        title_sentiment = TextBlob(title).sentiment.polarity

        if title_sentiment > 0:
            positive_count += 1
        elif title_sentiment < 0:
            negative_count += 1
        else:
            neutral_count += 1

        # 对评论内容进行情感分析
        for comment in comments:
            comment_text = comment.text.strip()
            comment_sentiment = TextBlob(comment_text).sentiment.polarity

            if comment_sentiment > 0:
                positive_count += 1
            elif comment_sentiment < 0:
                negative_count += 1
            else:
                neutral_count += 1

    # 统计情感比例
    total_count = positive_count + negative_count + neutral_count

    if total_count > 0:
        positive_ratio = positive_count / total_count
        negative_ratio = negative_count / total_count
        neutral_ratio = neutral_count / total_count

        print(f"Positive ratio: {positive_ratio}")
        print(f"Negative ratio: {negative_ratio}")
        print(f"Neutral ratio: {neutral_ratio}")
    else:
        print("No posts or comments found.")
else:
    print("Failed to retrieve the webpage.")
