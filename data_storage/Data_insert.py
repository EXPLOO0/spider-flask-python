import pymysql as pymysql


class Data_insert:
    # 连接本地数据库spider_jd
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spider_jd', charset='utf8mb4')
    # 创建游标对象
    cursor = conn.cursor()

    def insertKeyword(self, keyword):
        # 执行SQL插入语句
        sql = "INSERT INTO keyword_t (keyword) VALUES (%s)"
        self.cursor.execute(sql, (keyword))


    def insertGoods(self, keyId, pid, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, p_img, detail_url):
        # 执行SQL插入语句
        sql = "INSERT INTO goods_t (pid,keyId,brand1,brand2,brand3,brand4,brand5,title,price,commit,shop,p_img,detail_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (pid, keyId, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, p_img, detail_url))


    def insertIntroduce(self,kid, pid, param1, param2, param3):
        # 执行SQL插入语句
        sql = "INSERT INTO introduce_t (kid,pid,param1,param2,param3) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, param1, param2, param3))


    def insertSpec(self,kid, pid, param1, param2, param3, param4):
        # 执行SQL插入语句
        sql = "INSERT INTO spec_t (kid,pid,param1,param2,param3,param4) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, param1, param2, param3, param4))

    def insertSpecImg(self,kid, pid, p_img):
        # 执行SQL插入语句
        sql = "INSERT INTO spec_img_t (kid,pid,p_img) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, p_img))


    def insertCommit(self,kid, pid, ProductColor, ProductSize, ID, score, content):
        # 执行SQL插入语句
        sql = "INSERT INTO commit_t (kid,pid,ProductColor,ProductSize,ID,score,content) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, ProductColor, ProductSize, ID, score, content))

    def insertCommitImg(self,kid, pid, qid, img):
        # 执行SQL插入语句
        sql = "INSERT INTO commit_img_t (kid, pid, qid, img) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, qid, img))


    def insertQa(self,kid, pid, num, question, answer):
        # 执行SQL插入语句
        sql = "INSERT INTO qa_t (kid,pid,num,question,answer) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, num, question, answer))


    def commit(self):
        # 提交
        self.conn.commit()
    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
