System.register(["./element-plus-legacy-EQqE5-Mn.js","./@element-plus-legacy-D8kKPOmw.js","./index-legacy-CBGPOuii.js","./vue-router-legacy-CdvQKtwI.js","./echarts-legacy-ks9nkLWU.js","./chart-legacy-Ch4DVQ-V.js","./@vue-legacy-DSzhl0rc.js","./zrender-legacy-Dv1gJkCi.js","./@vueuse-legacy-Bwu8F_Ty.js","./lodash-es-legacy-BhUVsRVA.js","./@ctrl-legacy-BxnR6uzU.js","./@popperjs-legacy-CtArNnFZ.js","./pinia-legacy-C2fv4arT.js","./pinia-plugin-persistedstate-legacy-BNAcvG1t.js","./axios-legacy-Ct8n4Ic7.js","./vue-echarts-legacy-Zu3IWKBK.js","./resize-detector-legacy-lDo7yewp.js","./tslib-legacy-BRErZza_.js"],(function(t,e){"use strict";var a,l,o,r,i,n,s,u,d,c,h,g,p,f,x,v,m,y,A,b,C,w,D,L,I,R,k,j;return{setters:[t=>{a=t.d},t=>{l=t.u,o=t.l,r=t.x,i=t.y,n=t.A},t=>{s=t.u,u=t.b,d=t.a},t=>{c=t.u},t=>{h=t.I},t=>{g=t.g,p=t.a,f=t.b},t=>{x=t.r,v=t.h,m=t.x,y=t.a9,A=t.o,b=t.c,C=t.a,w=t.T,D=t.u,L=t.t,I=t.w,R=t.R,k=t.V},t=>{j=t.$},null,null,null,null,null,null,null,null,null,null],execute:function(){var e=document.createElement("style");e.textContent=".AllChartLeft{width:425px;height:655px;float:left}.AllChartLeft .AllChartLeft1{width:425px;height:49%;background-color:rgba(179,196,198,.3);float:left;border-radius:10px;box-shadow:4px 5px 6px rgba(0,0,0,.3)}.AllChartLeft .AllChartLeft2{width:100%;height:49%;background-color:rgba(179,196,198,.3);float:left;border-radius:10px;margin-top:3%;box-shadow:4px 5px 6px rgba(0,0,0,.3)}.AllChartCenter{width:49.5%;height:100%;float:left;background-color:rgba(179,196,198,.3);border-radius:10px;box-shadow:4px 5px 6px rgba(0,0,0,.3);margin-left:.5%}.AllChartRight{width:24.5%;height:100%;float:left;background-color:rgba(179,196,198,.3);border-radius:10px;box-shadow:4px 5px 6px rgba(0,0,0,.3);margin-left:.5%}.HomeMain{width:1700px;height:760px}.AllData{width:100%;height:100px;float:left;text-align:center}.AllData .textRight{width:200px;float:left;margin-left:10px;text-align:center}.AllData p{font-size:20px;margin-top:8px;margin-bottom:5px}.AllData .AllDataLeft{width:41%;height:90px;margin-top:5px;margin-left:15px;float:left;background-color:rgba(130,139,139,.3);border-radius:5px;box-shadow:3px 3px 5px rgba(0,0,0,.3)}.AllData .AllDataLeft .el-icon{float:left;height:100%;font-size:35px;margin-left:65px;color:rgba(241,39,36,.898);cursor:pointer}.AllData .AllDataLeft span{color:rgba(241,39,36,.85);font-size:28px;cursor:pointer}.AllData .AllDataLeft .el-icon:hover,.AllData .AllDataLeft span:hover{color:rgba(255,150,74,.898)}.AllData .AllDataLeft .AllDataLeft1,.AllData .AllDataLeft .AllDataLeft2{width:50%;height:84px;margin-top:3px;float:left}.AllData .AllDataRight{width:56%;height:90px;margin-top:5px;float:left;margin-left:25px;background-color:rgba(130,139,139,.3);border-radius:5px;box-shadow:3px 3px 5px rgba(0,0,0,.3)}.AllData .AllDataRight .el-icon{float:left;height:100%;font-size:35px;margin-left:65px;color:rgba(0,0,255,.85)}.AllData .AllDataRight span{color:rgba(0,0,255,.85);font-size:28px}.AllData .AllDataRight .AllDataRight1{margin-left:5px;width:33%;height:84px;margin-top:3px;float:left}.AllData .AllDataRight .AllDataRight2,.AllData .AllDataRight .AllDataRight3{width:33%;height:84px;margin-top:3px;float:left}.AllChart{width:100%;height:655px;margin-top:5px;float:left;border-radius:10px}\n",document.head.appendChild(e);const _={class:"AllChartLeft"},O={class:"AllChartLeft1"},S={class:"AllChartLeft2"},z={__name:"AllChartLeft",setup(t){const e=x(null),a=x(null);let l=null,o=null,r={title:{text:"系统中所有商品的分类总计",left:"left",top:5,left:10,textStyle:{color:"rgba(0, 0, 0, 0.8)"}},tooltip:{trigger:"item"},series:[{type:"pie",radius:[50,250],center:["50%","50%"],roseType:"area",type:"pie",radius:"65%",center:["50%","50%"],data:[{value:335,name:"Direct"},{value:310,name:"Email"},{value:274,name:"Union Ads"},{value:235,name:"Video Ads"},{value:400,name:"Search Engine"}].sort((function(t,e){return t.value-e.value})),roseType:"radius",label:{color:"rgba(0, 0, 0, 0.8)"},animationType:"scale",animationEasing:"elasticOut",animationDelay:function(t){return 800*Math.random()}}]},i={title:{text:"系统中所有商品的品牌总计",left:"left",top:5,left:10,textStyle:{color:"rgba(0, 0, 0, 0.8)"}},tooltip:{trigger:"item"},series:[{type:"pie",radius:["40%","70%"],avoidLabelOverlap:!1,emphasis:{label:{show:!0,fontSize:40,fontWeight:"bold"}},labelLine:{show:!1},label:{color:"rgba(0, 0, 0, 0.8)"},data:[]}]};return v((()=>{(async()=>{e.value=document.getElementById("AllChartLeftChartId1"),l=h(e.value),l.setOption(r),a.value=document.getElementById("AllChartLeftChartId2"),o=h(a.value),o.setOption(i);const t=await g();r.series[0].data=t.data[0],i.series[0].data=t.data[1],l.setOption(r),o.setOption(i)})()})),m((()=>{l&&l.dispose()})),(t,e)=>{const a=y("v-chart");return A(),b("div",_,[C("div",O,[w(a,{id:"AllChartLeftChartId1",class:"AllChartLeftChart",option:D(r)},null,8,["option"])]),C("div",S,[w(a,{id:"AllChartLeftChartId2",class:"AllChartLeftChart",option:D(i)},null,8,["option"])])])}}},E={class:"AllChartCenter"},K={__name:"AllChartCenter",setup(t){c();const e=x(null);let a=null;const l=x([]),o=x([]),r=x([]),i=x([]),n=x([]),u=x([]),d=x([]),g=x([]),f=x(10);v((()=>{e.value=document.getElementById("AllChartCenterChartId"),a=h(e.value),a.setOption(m),(async()=>{const t=await p();l.value=t.data[0],o.value=t.data[1],r.value=t.data[2],i.value=t.data[3],n.value=l.value.slice(0,f.value),u.value=o.value.slice(0,f.value),d.value=r.value.slice(0,f.value),g.value=i.value.slice(0,f.value),m.xAxis[0].data=u.value,m.xAxis[1].data=n.value,m.series[0].data=d.value,m.series[1].data=g.value,a.setOption(m)})().then((()=>{setInterval((()=>{d.value.shift(),d.value.push(r.value[f.value%r.value.length]),g.value.shift(),g.value.push(i.value[f.value%r.value.length]),n.value.shift(),n.value.push(l.value[f.value%l.value.length]),u.value.shift(),u.value.push(o.value[f.value%l.value.length]),f.value++,a.setOption(m)}),2100)})),a.on("click",(function(t){const e=s();e.setKeywordID(t.name),e.setKeywordValue(m.xAxis[0].data[t.dataIndex]),e.setCommitRangeIndex(-1),e.setPriceRangeIndex(-1),e.setPriceRanges("")}))}));const m={title:{text:"关键词信息",left:"left",top:5,left:10,textStyle:{color:"rgba(0, 0, 0, 0.8)"}},grid:{top:80,bottom:50},tooltip:{trigger:"axis",axisPointer:{type:"cross",label:{backgroundColor:"#283b56"}}},legend:{},dataZoom:{show:!1,start:0,end:100},xAxis:[{type:"category",boundaryGap:!0,axisLabel:{interval:0},data:[]},{type:"category",boundaryGap:!0,axisLabel:{interval:0},data:[]}],yAxis:[{type:"value",scale:!0,name:"平均价格",min:0,boundaryGap:[.2,.2]},{type:"value",scale:!0,name:"商品数量",min:0,boundaryGap:[.2,.2]}],series:[{name:"商品数量",type:"bar",xAxisIndex:1,yAxisIndex:1,data:[],label:{bottom:0}},{name:"商品平均价格",type:"line",data:[],label:{bottom:0}}]};return(t,e)=>{const a=y("v-chart");return A(),b("div",E,[w(a,{id:"AllChartCenterChartId",class:"AllChartCenterChart",option:m})])}}},G={class:"AllChartRight"},B={__name:"AllChartRight",setup(t){const e=c(),a=x(null);let l=null;const o=[0,50,100,200,500,1e3,2e3,5e3,1e4,2e4,1e6,999999999999],r=[0,50,100,200,500,1e3,2e3,5e3,1e4,2e4,5e4,1e5,2e5,5e5,999999999999],i={title:{text:"选中关键词符合价格销量区间的商品数量",subtext:"",subtextStyle:{fontSize:17},left:"5%",top:"1%"},legend:{right:"10%",top:"3%"},grid:{left:"15%",top:"10%"},xAxis:{type:"value",name:"销量",nameLocation:"middle",nameGap:25,axisLine:{show:!0},axisTick:{show:!0},axisLabel:{formatter:function(t){return r[t]}}},yAxis:{type:"category",name:"价格",nameLocation:"middle",nameGap:35,axisLabel:{formatter:function(t){return o[t]}}},tooltip:{formatter:function(t){const e=t.value;return"销量："+o[e[1]]+"-"+o[e[1]-1]+"<br/>价格："+r[e[0]]+"-"+r[e[0]-1]+"<br/>数量："+e[2]}},series:[{data:[],type:"scatter",symbolSize:function(t){return 8*Math.cbrt(t[2])},emphasis:{focus:"series",label:{show:!0,formatter:function(t){return t.data[2]},position:"top"}},itemStyle:{shadowBlur:10,shadowColor:"rgba(25, 100, 150, 0.5)",shadowOffsetY:5,color:new j(.4,.3,1,[{offset:0,color:"rgb(129, 227, 238)"},{offset:1,color:"rgb(25, 183, 207)"}])}}]};v((()=>{a.value=document.getElementById("AllChartRightChartId"),l=h(a.value),l.setOption(i),l.on("click",(function(t){console.log(t);const a=s(),l=u();t.data[2]>0&&(a.setCommitRangeIndex(t.data[0]),a.setPriceRangeIndex(t.data[1]),e.push("/chart/s3c"),l.setDrawer3Store(!0))}))}));const n=s(),d=L((()=>n.keywordID));return I(d,((t,e)=>{(async()=>{const t=s();if(null==t.keywordID||""==t.keywordID);else{const e=await f(t.keywordID,"","","");i.series[0].data=e.data,i.title.subtext=t.keywordValue,l.setOption(i)}})()}),{immediate:!0,deep:!0}),(t,e)=>{const a=y("v-chart");return A(),b("div",G,[w(a,{id:"AllChartRightChartId",class:"AllChartRightChart",option:i})])}}},P={class:"HomeMain"},T={class:"AllData"},M={class:"AllDataLeft"},V={class:"AllDataLeft1"},H={class:"textRight"},q=C("p",{style:{"font-weight":"600"}},"关键词采集数量",-1),U={class:"AllDataLeft2"},W={class:"textRight"},Y=C("p",{style:{"font-weight":"600"}},"正在采集的关键词",-1),Z={class:"AllDataRight"},$={class:"AllDataRight1"},F={class:"textRight"},J=C("p",{style:{"font-weight":"600"}},"已采集商品数据量",-1),N={class:"AllDataRight2"},Q={class:"textRight"},X=C("p",{style:{"font-weight":"600"}},"已采集评论量",-1),tt={class:"AllDataRight3"},et={class:"textRight"},at=C("p",{style:{"font-weight":"600"}},"已采集评论图片量",-1),lt={class:"AllChart"};t("default",{__name:"HomePage",setup(t){const e=c(),s=x({keywordCount:0,keywordLoaading:"",goodsCount:0,commitCount:0,commitImg:0}),u=async()=>{const t=d();""==t.insertKeyword?s.value.keywordLoaading="无":s.value.keywordLoaading=t.insertKeyword,s.value.keywordCount=t.allData.keywordCount,s.value.goodsCount=t.allData.goodsCount,s.value.commitCount=t.allData.commitCount,s.value.commitImg=t.allData.commitImg},h=()=>{e.push("/history")},g=d();v((()=>{g.verifyInsertKeyword(),u()}));const p=L((()=>g.insertKeyword));return I(p,(()=>{g.verifyInsertKeyword(),u()}),{immediate:!0,deep:!0}),(t,e)=>{const u=a;return A(),b("div",P,[C("div",T,[C("div",M,[C("div",V,[w(u,{onClick:e[0]||(e[0]=t=>h())},{default:R((()=>[w(D(l))])),_:1}),C("div",H,[q,C("span",{onClick:e[1]||(e[1]=t=>h())},k(s.value.keywordCount),1)])]),C("div",U,[w(u,{onClick:e[2]||(e[2]=t=>h())},{default:R((()=>[w(D(o))])),_:1}),C("div",W,[Y,C("span",{onClick:e[3]||(e[3]=t=>h())},k(s.value.keywordLoaading),1)])])]),C("div",Z,[C("div",$,[w(u,null,{default:R((()=>[w(D(r))])),_:1}),C("div",F,[J,C("span",null,k(s.value.goodsCount),1)])]),C("div",N,[w(u,null,{default:R((()=>[w(D(i))])),_:1}),C("div",Q,[X,C("span",null,k(s.value.commitCount),1)])]),C("div",tt,[w(u,null,{default:R((()=>[w(D(n))])),_:1}),C("div",et,[at,C("span",null,k(s.value.commitImg),1)])])])]),C("div",lt,[w(z),w(K),w(B)])])}}})}}}));
