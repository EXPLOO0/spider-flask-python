class Record:  # 定义数据处理的类
    ProductId = None
    ID = None
    Content = None
    Score = None
    ProductColor = None
    ProductSize = None

    def __init__(self, ProductId, ProductColor, ProductSize, ID, Content, Score):
        self.ProductId = ProductId
        self.ProductColor = ProductColor
        self.ProductSize = ProductSize
        self.ID = ID
        self.Content = Content
        self.Score = Score

    def __str__(self):
        return f"ProductId:{self.ProductId},ProductColor:{self.ProductColor},ProductSize:{self.ProductSize},ID:{self.ID},\nContent:{self.Content},\nScore:{self.Score}\n"
