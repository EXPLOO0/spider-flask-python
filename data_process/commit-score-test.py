from snownlp import SnowNLP

from data_storage.Data_select import Data_select


def analyze_sentiment_detailed(comment):
    s = SnowNLP(comment)
    sentiment_score = s.sentiments
    # 根据情感得分划分为积极、中性和消极三个维度
    if sentiment_score > 0.6:
        sentiment = '积极'
    elif sentiment_score < 0.4:
        sentiment = '消极'
    else:
        sentiment = '中性'
    return {
        'Sentiment': sentiment,
        'Positive': sentiment_score,
        'Negative': 1 - sentiment_score
    }

ds = Data_select()
a = ds.selectCommit(17,100061054752)

for comment in a[3]:
    result = analyze_sentiment_detailed(comment)
    print(f"评论: {comment}")
    print(f"情感偏向: {result['Sentiment']}")
    print(f"积极得分: {result['Positive']:.2f}")
    print(f"消极得分: {result['Negative']:.2f}")
    print()



