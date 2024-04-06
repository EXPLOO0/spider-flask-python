class Record:  # 定义数据处理的类
    ID = None
    Content = None
    Score = None
    ProductColor = None
    ProductSize = None
    sentimentScore = None

    def __init__(self, ProductColor, ProductSize, ID, Content, Score, sentimentScore):
        self.ProductColor = ProductColor
        self.ProductSize = ProductSize
        self.ID = ID
        self.Content = Content
        self.Score = Score
        self.sentimentScore = sentimentScore

    def __str__(self):
        return f"ProductColor:{self.ProductColor},ProductSize:{self.ProductSize},ID:{self.ID},\nContent:{self.Content},\nScore:{self.Score},\nsentimentScore:{self.sentimentScore}\n"

class Record2:  # 定义数据处理的类
    ProductId = None
    ID = None

    def __init__(self, ProductId, ID):
        self.ProductId = ProductId
        self.ID = ID
    def __str__(self):
        return f"ProductId:{self.ProductId},ID:{self.ID}"
