import pymysql as pymysql
import configparser


class Data_insert:
    config = configparser.ConfigParser()
    config.read('configData.ini')  # 读取配置文件

    host = config.get('MySQL', 'host')
    port = int(config.get('MySQL', 'port'))
    user = config.get('MySQL', 'user')
    password = config.get('MySQL', 'password')
    db = config.get('MySQL', 'db')
    charset = config.get('MySQL', 'charset')

    # 连接本地数据库spider_jd
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    # 创建游标对象
    cursor = conn.cursor()

    def insertKeyword(self, keyword):
        try:
            # 执行SQL插入语句
            sql = "INSERT INTO keyword_t (keyword,stus) VALUES (%s,1)"
            self.cursor.execute(sql, (keyword))
        except Exception as e:
            print('123'+e)


    def insertGoods(self, keyId, pid, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, p_img, detail_url,sentimentScore, sentiment1, sentiment2, sentiment3, sentiment4, sentiment5,commit_count,count1,count2,count3,count4,count5):
        # 执行SQL插入语句
        sql = "INSERT INTO goods_t (pid,keyId,brand1,brand2,brand3,brand4,brand5,title,price,commit,shop,p_img,detail_url,sentimentScore, sentiment1, sentiment2, sentiment3, sentiment4, sentiment5, commit_count,count1,count2,count3,count4,count5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (pid, keyId, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, p_img, detail_url,sentimentScore, sentiment1, sentiment2, sentiment3, sentiment4, sentiment5,commit_count,count1,count2,count3,count4,count5))


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

    def insertGoodsCommit(self,kid, pid, cid):
        # 执行SQL插入语句
        sql = "INSERT INTO goods_commit_t (kid,pid,cid) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, cid))

    def insertCommit(self,kid, ProductColor, ProductSize, ID, score, content, sentimentScore):
        # 执行SQL插入语句
        sql = "INSERT INTO commit_t (kid,ProductColor,ProductSize,ID,score,content,sentimentScore) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, ProductColor, ProductSize, ID, score, content, sentimentScore))

    def insertCommitImg(self,kid, qid, img):
        # 执行SQL插入语句
        sql = "INSERT INTO commit_img_t (kid, qid, img) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (kid, qid, img))


    def insertQa(self,kid, pid, num, question, answer):
        # 执行SQL插入语句
        sql = "INSERT INTO qa_t (kid,pid,num,question,answer) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (kid, pid, num, question, answer))


    def commit(self):
        # 提交
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
