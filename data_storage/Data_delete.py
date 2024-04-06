import pymysql as pymysql


class Data_delete:
    # 连接本地数据库spider_jd
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spider_jd', charset='utf8mb4')
    # 创建游标对象
    cursor = conn.cursor()

    def deleteKeyword(self, keyId):
        # 执行SQL插入语句
        sql = "delete from keyword_t where keyId = %s"
        self.cursor.execute(sql, (keyId))

    def deleteGoods(self, keyId):
        # 执行SQL插入语句
        sql = "delete from goods_t where keyId = %s"
        self.cursor.execute(sql, (keyId))

    def deleteIntroduce(self, kid):
        # 执行SQL插入语句
        sql = "delete from introduce_t where kid = %s"
        self.cursor.execute(sql, (kid))

    def deleteSpec(self, keyId):
        # 执行SQL插入语句
        sql = "delete from spec_t where kid = %s"
        self.cursor.execute(sql, (keyId))

    def deleteSpecImg(self, keyId):
        # 执行SQL插入语句
        sql = "delete from spec_img_t where kid = %s"
        self.cursor.execute(sql, (keyId))

    def deleteGoodsCommit(self, keyId):
        # 执行SQL插入语句
        sql = "delete from goods_commit_t where kid = %s"
        self.cursor.execute(sql, (keyId))

    def deleteCommit(self, keyId):
        # 执行SQL插入语句
        sql = "delete from commit_t where kid = %s"
        self.cursor.execute(sql, (keyId))

    def deleteCommitImg(self, keyId):
        # 执行SQL插入语句
        sql = "delete from commit_img_t where kid = %s"
        self.cursor.execute(sql, (keyId))

    def deleteQa(self, kid):
        # 执行SQL插入语句
        sql = "delete from qa_t where kid = %s"
        self.cursor.execute(sql, (kid))

    def deleteAll(self, kid):
        try:
            print('----------删除Goods开始----------')
            self.deleteGoods(kid)
            print('----------删除Goods完成----------')
            print('----------删除Introduce开始----------')
            self.deleteIntroduce(kid)
            print('----------删除Introduce完成----------')
            print('----------删除Spec开始----------')
            self.deleteSpec(kid)
            print('----------删除Spec完成----------')
            print('----------删除SpecImg开始----------')
            self.deleteSpecImg(kid)
            print('----------删除SpecImg完成----------')
            print('----------删除GoodsCommit开始----------')
            self.deleteGoodsCommit(kid)
            print('----------删除GoodsCommit完成----------')
            print('----------删除Commit开始----------')
            self.deleteCommit(kid)
            print('----------删除Commit完成----------')
            print('----------删除CommitImg开始----------')
            self.deleteCommitImg(kid)
            print('----------删除CommitImg完成----------')
            # print('----------删除Qa开始----------')
            # self.deleteQa(kid)
            # print('----------删除Qa完成----------')

            self.commit()

        except:

            print('----------回滚----------')
            self.rollback()


    def commit(self):
        # 提交
        self.conn.commit()

    # 回滚
    def rollback(self):
        self.conn.rollback()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

if __name__ == '__main__':
    dd = Data_delete()

    dd.deleteAll(1)