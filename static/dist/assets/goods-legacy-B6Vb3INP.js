System.register(["./index-legacy-BZISNiaX.js"],(function(e,a){"use strict";var d;return{setters:[e=>{d=e.d}],execute:function(){e("a",((e,a,r,t,n,g)=>d.get("/getProductIntroduction",{params:{keyId:e,brand1:a,brand2:r,brand3:t,brand4:n,brand5:g}}))),e("g",((e,a,r)=>d.get("/getBrand5ShopPid",{params:{keyId:e,brand5:a,shop:r}}))),e("c",((e,a)=>d.get("/getShopPageSess",{params:{keyId:e,pid:a}}))),e("d",((e,a)=>d.get("/getGoodsPageSpec",{params:{keyId:e,pid:a}}))),e("e",((e,a)=>d.get("/getGoodsPageChart",{params:{keyId:e,pid:a}}))),e("f",((e,a,r,t)=>d.get("/getGoodsPageCommit",{params:{keyId:e,pid:a,score:r,page:t}}))),e("b",((e,a,r,t,n,g,s)=>d.get("/getPidByBrand5AndIndex",{params:{keyId:e,brand1:a,brand2:r,brand3:t,commitRangeIndex:n,priceRangeIndex:g,brand5:s}})))}}}));