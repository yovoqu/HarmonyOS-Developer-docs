# SVG图片在真机和DevEco Studio中颜色显示不一致该如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-8

#### 问题现象

SVG图片在DevEco Studio和浏览器中打开显示为黄色，但是在测试机和DevEco Studio的Previewer上显示为红色。
 
 
- DevEco Studio中预览为黄色：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Xmd0UcF0TEaCqYRYj2-G5Q/zh-cn_image_0000002628408094.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=2A816357AB1823D1474E484EBE68E949682E7B2514685DE966923377D0C6CFE3)


 
- DevEco Studio的Previewer中渲染为红色：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/L84FQ5JGRVyIv5vTjs-tuA/zh-cn_image_0000002628567994.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=C7613EAE7B525498D0D0A082E8CAD142A4066DC3BD0F505535DBD4663E844A49)


  
```xml
<<span style="color: rgb(0,0,255);">svg </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='vector' </span><span style="color: rgb(0,0,255);">xmlns</span><span style="color: rgb(80,160,79);">='http://www.w3.org/2000/svg' </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(80,160,79);">='28' </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(80,160,79);">='28' </span><span style="color: rgb(0,0,255);">viewBox</span><span style="color: rgb(80,160,79);">='0 0 28 28'</span>>
  <<span style="color: rgb(0,0,255);">defs</span>>
    <<span style="color: rgb(0,0,255);">linearGradient </span><span style="color: rgb(0,0,255);">gradientUnits</span><span style="color: rgb(80,160,79);">='userSpaceOnUse' </span><span style="color: rgb(0,0,255);">x1</span><span style="color: rgb(80,160,79);">='6.935' </span><span style="color: rgb(0,0,255);">y1</span><span style="color: rgb(80,160,79);">='3.252' </span><span style="color: rgb(0,0,255);">x2</span><span style="color: rgb(80,160,79);">='6.909' </span><span style="color: rgb(0,0,255);">y2</span><span style="color: rgb(80,160,79);">='10.552' </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='gradient_0'</span>>
      <<span style="color: rgb(0,0,255);">stop </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(80,160,79);">='0' </span><span style="color: rgb(0,0,255);">stop-color</span><span style="color: rgb(80,160,79);">='#FFFE4144'</span>/>
      <<span style="color: rgb(0,0,255);">stop </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(80,160,79);">='1' </span><span style="color: rgb(0,0,255);">stop-color</span><span style="color: rgb(80,160,79);">='#FFFF6D67'</span>/>
    </<span style="color: rgb(0,0,255);">linearGradient</span>>
  </<span style="color: rgb(0,0,255);">defs</span>>
  <<span style="color: rgb(0,0,255);">path </span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(80,160,79);">='url(#gradient_0)' </span><span style="color: rgb(0,0,255);">d</span><span style="color: rgb(80,160,79);">='M10.983,3.951C10.983,3.313 10.461,2.79 9.823,2.79C5.983,2.79 2.862,5.913 2.862,9.755C2.862,10.393 3.384,10.915 4.022,10.915C4.66,10.915 5.182,10.393 5.182,9.755C5.182,7.189 7.259,5.112 9.823,5.112C10.461,5.112 10.983,4.589 10.983,3.951Z' </span><span style="color: rgb(0,0,255);">stroke-width</span><span style="color: rgb(80,160,79);">='1'</span>
        <span style="color: rgb(0,0,255);">fill-rule</span><span style="color: rgb(80,160,79);">='evenodd' </span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(80,160,79);">='#00000000' </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='path_6' </span>/>
</<span style="color: rgb(0,0,255);">svg</span>>
```


 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/il31FXeVR8ymGRBbGn8fFg/zh-cn_image_0000002658927315.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=D9E7007F14A78308EC80E42B47F82C220F1CF02E6F814A3F4F38DF7FB0A8D3A4)

 
 

#### 定位思路

DevEco Studio和浏览器仅支持解析颜色值为RGBA格式的SVG图片，不支持#FFFE4144和#FFFF6D67等十六进制格式，因此如果遇到了DevEco Studio和浏览器的SVG预览错误，可以将SVG图片的颜色值改为RGBA格式。
 
 

#### 解决方案

颜色的十六进制格式改为RGBA格式可自行搜索相关资料。
 
```xml
<<span style="color: rgb(0,0,255);">svg </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='vector' </span><span style="color: rgb(0,0,255);">xmlns</span><span style="color: rgb(80,160,79);">='http://www.w3.org/2000/svg' </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(80,160,79);">='28' </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(80,160,79);">='28' </span><span style="color: rgb(0,0,255);">viewBox</span><span style="color: rgb(80,160,79);">='0 0 28 28'</span>>
  <<span style="color: rgb(0,0,255);">defs</span>>
    <<span style="color: rgb(0,0,255);">linearGradient </span><span style="color: rgb(0,0,255);">gradientUnits</span><span style="color: rgb(80,160,79);">='userSpaceOnUse' </span><span style="color: rgb(0,0,255);">x1</span><span style="color: rgb(80,160,79);">='6.935' </span><span style="color: rgb(0,0,255);">y1</span><span style="color: rgb(80,160,79);">='3.252' </span><span style="color: rgb(0,0,255);">x2</span><span style="color: rgb(80,160,79);">='6.909' </span><span style="color: rgb(0,0,255);">y2</span><span style="color: rgb(80,160,79);">='10.552' </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='gradient_0'</span>>
      <<span style="color: rgb(0,0,255);">stop </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(80,160,79);">='0' </span><span style="color: rgb(0,0,255);">stop-color</span><span style="color: rgb(80,160,79);">='rgba(254,65,68,1)'</span>/> <em>// 修改颜色为RGBA格式</em>
      <<span style="color: rgb(0,0,255);">stop </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(80,160,79);">='1' </span><span style="color: rgb(0,0,255);">stop-color</span><span style="color: rgb(80,160,79);">='rgba(255,109,103,1)'</span>/> <em>// 修改颜色为RGBA格式</em>
    </<span style="color: rgb(0,0,255);">linearGradient</span>>
  </<span style="color: rgb(0,0,255);">defs</span>>
 <<span style="color: rgb(0,0,255);">path </span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(80,160,79);">='url(#gradient_0)' </span><span style="color: rgb(0,0,255);">d</span><span style="color: rgb(80,160,79);">='M10.983,3.951C10.983,3.313 10.461,2.79 9.823,2.79C5.983,2.79 2.862,5.913 2.862,9.755C2.862,10.393 3.384,10.915 4.022,10.915C4.66,10.915 5.182,10.393 5.182,9.755C5.182,7.189 7.259,5.112 9.823,5.112C10.461,5.112 10.983,4.589 10.983,3.951Z' </span><span style="color: rgb(0,0,255);">stroke-width</span><span style="color: rgb(80,160,79);">='1'</span>
       <span style="color: rgb(0,0,255);">fill-rule</span><span style="color: rgb(80,160,79);">='evenodd' </span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(80,160,79);">='#00000000' </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(80,160,79);">='path_6' </span>/>
</<span style="color: rgb(0,0,255);">svg</span>>
```
