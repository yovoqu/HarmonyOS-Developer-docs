# 离屏获取文本像素图并使用OpenGL绘制

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-32

#### 问题现象

在音视频应用中，当需要在视频画面上叠加实时字幕，或在直播场景下实现高速滚动的弹幕时，使用OpenGL绘制文字能实现流畅低延时的渲染效果。在HarmonyOS中，如何获取文本像素数据并使用OpenGL绘制文字？
 
 

#### 背景知识

- [EGL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl)是OpenGL与本地窗口系统之间的接口，将OpenGL的渲染输出连接到HarmonyOS的显示窗口。
- [OpenGL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengles)不能直接绘制文字，而是先将文字渲染成纹理（图片），再将纹理贴到指定的矩形方块中显示。
[glTexImage2D](https://developer.huawei.com/consumer/cn/doc/graphics-References/glteximage-0000001050170287)接口用于加载图像像素数据创建二维纹理对象。

 - [OffscreenCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas)是一个可以在屏幕外渲染的画布，可以离屏绘制文本。
[fillText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d#filltext)接口用于在画布指定位置绘制填充类文本内容。
- [getPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d#getpixelmap)接口用于拷贝画布指定区域的像素数据。

 - [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)模块支持创建[CPU后端](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c#cpu后端canvas的创建与显示)或[GPU后端](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c#gpu后端canvas的创建与显示)的离屏画布，可以离屏绘制文本。
[OH_Drawing_CanvasDrawSingleCharacter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h#oh_drawing_canvasdrawsinglecharacter)用于绘制单个字符，当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。
- [OH_Drawing_CanvasReadPixels](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h#oh_drawing_canvasreadpixels)接口从画布中拷贝像素数据到指定地址。

 
 
 

#### 解决方案

使用OpenGL绘制文本，首先需要获取绘制文本的像素数据，获得文本像素图数据后，OpenGL可以根据文本像素数据生成纹理对象，并将纹理对象渲染到指定的矩形方块上显示在屏幕上。在HarmonyOS中支持通过OffscreenCanvas以及Drawing模块离屏绘制文本内容并获取文本绘制的图像像素数据。
 
- **方案一**：使用OffscreenCanvas离屏绘制文本取得文本像素数据。1. ArkTS侧，创建OffscreenCanvas组件，使用OffscreenCanvasRenderingContext2D在OffscreenCanvas上绘制文本内容。拷贝离屏画布文本绘制区域的像素数据，与图像宽、高以及XComponent的SurfaceID一同传递到Native侧绘制。
```text
<span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController3 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">离屏绘制文本</span></em>
    let <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">你好</span>\u<span style="color: rgb(132,63,161);">{D83D}</span>\u<span style="color: rgb(132,63,161);">{DE02}'</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">offCanvas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">OffscreenCanvas </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">OffscreenCanvas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">offContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">offCanvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'2d'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'#000000'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">font </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'100px sans-serif'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从离屏画布上读取位图数据。</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">buffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelBytesNumber</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readPixelsToBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取位图的宽、高信息。</span></em>
    let <span style="color: rgb(255,255,255);">imgInfo </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImageInfo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">imgWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">imgInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">imgHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">imgInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">XComponent</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">SurfaceID</span><span style="color: rgb(128,128,128);">。</span></em>
    let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController3</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将位图数据、宽、高，</span><span style="color: rgb(128,128,128);">SurfaceID</span><span style="color: rgb(128,128,128);">传递到</span><span style="color: rgb(128,128,128);">Native</span><span style="color: rgb(128,128,128);">侧使用</span><span style="color: rgb(128,128,128);">OpenGL ES</span><span style="color: rgb(128,128,128);">完成绘制。</span></em>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">drawText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">imgWidth</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">imgHeight</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```


2. 在Native侧接收位图像素数据，位图宽、高以及XComponent的SurfaceID。
```text
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">DrawImage</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> argc <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">5</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">5</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(env, info, <span style="color: rgb(128,128,128);">&</span>argc, args, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
  <em>  // 获取SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> lossless <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> surfaceId <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span>surfaceId, <span style="color: rgb(128,128,128);">&</span>lossless);
   <em> // 获取位图数据</em>
    <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(128,128,128);">*</span>data <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(0,0,255);">size_t</span> byteLength <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_arraybuffer_info</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>], <span style="color: rgb(128,128,128);">&</span>data, <span style="color: rgb(128,128,128);">&</span>byteLength);
   <em> // 获取位图宽、高</em>
    <span style="color: rgb(0,0,255);">int32_t</span> imageWidth <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> imageHeight <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_int32</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">2</span>], <span style="color: rgb(128,128,128);">&</span>imageWidth);
    <span style="color: rgb(181,106,1);">napi_get_value_int32</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span>imageHeight);
   <em> // 创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span>window <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(surfaceId, <span style="color: rgb(128,128,128);">&</span>window);
  <em>  // 使用OpenGL ES绘制位图</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(window, imageWidth, imageHeight, data);
 <em>   // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(window);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```


3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。
```text
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">OHNativeWindow</span> <span style="color: rgb(0,0,255);">*</span><span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(0,0,255);">*</span><span style="color: rgb(0,0,255);">data</span>)
{
    EGLDisplay <span style="color: rgb(0,0,255);">display</span>;
    EGLint <span style="color: rgb(0,0,255);">majorVersion</span>;
    EGLint <span style="color: rgb(0,0,255);">minorVersion</span>;
    <span style="color: rgb(0,0,255);">display</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglGetDisplay</span>(EGL_DEFAULT_DISPLAY);
    <span style="color: rgb(181,106,1);">eglInitialize</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">majorVersion</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">minorVersion</span>);
    EGLConfig <span style="color: rgb(0,0,255);">config</span>;
    EGLint <span style="color: rgb(0,0,255);">numConfigs</span>;
    EGLint <span style="color: rgb(0,0,255);">attribs</span>[] <span style="color: rgb(128,128,128);">=</span> {
        EGL_SURFACE_TYPE,
        EGL_WINDOW_BIT,
        EGL_RENDERABLE_TYPE,
        EGL_OPENGL_ES3_BIT,
        EGL_BLUE_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_GREEN_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_RED_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_ALPHA_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_NONE,
    };
    <span style="color: rgb(181,106,1);">eglChooseConfig</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">attribs</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">config</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">numConfigs</span>);
    EGLSurface <span style="color: rgb(0,0,255);">surface</span>;
    EGLContext <span style="color: rgb(0,0,255);">context</span>;
    EGLint <span style="color: rgb(0,0,255);">contextAttribs</span>[] <span style="color: rgb(128,128,128);">=</span> {EGL_CONTEXT_CLIENT_VERSION, <span style="color: rgb(80,160,79);">3</span>, EGL_NONE};
    <span style="color: rgb(0,0,255);">surface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateWindowSurface</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">config</span>, (EGLNativeWindowType)<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">NULL</span>);
    <span style="color: rgb(0,0,255);">context</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateContext</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">config</span>, EGL_NO_CONTEXT, <span style="color: rgb(0,0,255);">contextAttribs</span>);
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>, <span style="color: rgb(0,0,255);">surface</span>, <span style="color: rgb(0,0,255);">context</span>);
    <span style="color: rgb(181,106,1);">glViewport</span>(<span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>);
    <span style="color: rgb(181,106,1);">glClearColor</span>(<span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>);
    <span style="color: rgb(181,106,1);">glClear</span>(GL_COLOR_BUFFER_BIT);
    GLfloat <span style="color: rgb(0,0,255);">vertices</span>[] <span style="color: rgb(128,128,128);">=</span> {
        <em>// First triangle</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,  <em> // ...</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>,  <em>// ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <em>// ...</em>
      <em>  // Second triangle</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,   <em>// ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <em>// ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,  <em>// ...</em>
    };
    GLuint <span style="color: rgb(0,0,255);">vbo</span>;
    GLuint <span style="color: rgb(0,0,255);">vao</span>[<span style="color: rgb(80,160,79);">0</span>];
    <span style="color: rgb(181,106,1);">glGenVertexArrays</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(0,0,255);">vao</span>);
    <span style="color: rgb(181,106,1);">glBindVertexArray</span>(<span style="color: rgb(0,0,255);">vao</span>[<span style="color: rgb(80,160,79);">0</span>]);
    <span style="color: rgb(181,106,1);">glGenBuffers</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(181,106,1);">glBindBuffer</span>(GL_ARRAY_BUFFER, <span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(181,106,1);">glBufferData</span>(GL_ARRAY_BUFFER, <span style="color: rgb(0,0,255);">sizeof</span>(<span style="color: rgb(0,0,255);">vertices</span>), <span style="color: rgb(0,0,255);">vertices</span>, GL_STATIC_DRAW);
    <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">vertexShaderSource</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">R"(#version 300 es</span>
<span style="color: rgb(181,106,1);">        layout (location = 0) in vec4 vPosition;</span>
<span style="color: rgb(181,106,1);">        layout (location = 1) in vec2 vTexCoord;</span>
<span style="color: rgb(181,106,1);">        out vec2 TexCoord;</span>
<span style="color: rgb(181,106,1);">        void main() {</span>
<span style="color: rgb(181,106,1);">            gl_Position = vPosition;</span>
<span style="color: rgb(181,106,1);">            TexCoord = vTexCoord;</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">    )"</span>;
    <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">fragmentShaderSource</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">R"(#version 300 es</span>
<span style="color: rgb(181,106,1);">        precision mediump float;</span>
<span style="color: rgb(181,106,1);">        out vec4 FragColor;</span>
<span style="color: rgb(181,106,1);">        in vec2 TexCoord;</span>
<span style="color: rgb(181,106,1);">        uniform sampler2D testTexture;</span>
<span style="color: rgb(181,106,1);">        void main() {</span>
<span style="color: rgb(181,106,1);">            FragColor = texture(testTexture, TexCoord);</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">    )"</span>;
    GLuint <span style="color: rgb(0,0,255);">vertexShader</span>;
    <span style="color: rgb(0,0,255);">vertexShader</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateShader</span>(GL_VERTEX_SHADER);
    <span style="color: rgb(181,106,1);">glShaderSource</span>(<span style="color: rgb(0,0,255);">vertexShader</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vertexShaderSource</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(181,106,1);">glCompileShader</span>(<span style="color: rgb(0,0,255);">vertexShader</span>);
    GLuint <span style="color: rgb(0,0,255);">fragmentShader</span>;
    <span style="color: rgb(0,0,255);">fragmentShader</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateShader</span>(GL_FRAGMENT_SHADER);
    <span style="color: rgb(181,106,1);">glShaderSource</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">fragmentShaderSource</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(181,106,1);">glCompileShader</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>);
    GLuint <span style="color: rgb(0,0,255);">shaderProgram</span>;
    <span style="color: rgb(0,0,255);">shaderProgram</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateProgram</span>();
    <span style="color: rgb(181,106,1);">glAttachShader</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(0,0,255);">vertexShader</span>);
    <span style="color: rgb(181,106,1);">glAttachShader</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(0,0,255);">fragmentShader</span>);
    <span style="color: rgb(181,106,1);">glLinkProgram</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>);
    <span style="color: rgb(181,106,1);">glUseProgram</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>);
    GLuint <span style="color: rgb(0,0,255);">textureId</span>;
    <span style="color: rgb(181,106,1);">glGenTextures</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glBindTexture</span>(GL_TEXTURE_2D, <span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    <span style="color: rgb(181,106,1);">glTexImage2D</span>(GL_TEXTURE_2D, <span style="color: rgb(80,160,79);">0</span>, GL_RGBA, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(80,160,79);">0</span>, GL_RGBA, GL_UNSIGNED_BYTE, <span style="color: rgb(0,0,255);">data</span>);
    <span style="color: rgb(181,106,1);">glGenerateMipmap</span>(GL_TEXTURE_2D);
    <span style="color: rgb(181,106,1);">glUniform1i</span>(<span style="color: rgb(181,106,1);">glGetUniformLocation</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(181,106,1);">"testTexture"</span>), <span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glActiveTexture</span>(GL_TEXTURE0);
    <span style="color: rgb(181,106,1);">glBindTexture</span>(GL_TEXTURE_2D, <span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glVertexAttribPointer</span>(<span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">3</span>, GL_FLOAT, GL_FALSE, <span style="color: rgb(80,160,79);">5</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat), (GLvoid <span style="color: rgb(128,128,128);">*</span>)<span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glEnableVertexAttribArray</span>(<span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glVertexAttribPointer</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(80,160,79);">2</span>, GL_FLOAT, GL_FALSE, <span style="color: rgb(80,160,79);">5</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat), (GLvoid <span style="color: rgb(128,128,128);">*</span>)(<span style="color: rgb(80,160,79);">3</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat)));
    <span style="color: rgb(181,106,1);">glEnableVertexAttribArray</span>(<span style="color: rgb(80,160,79);">1</span>);
    <span style="color: rgb(181,106,1);">glDrawArrays</span>(GL_TRIANGLES, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">6</span>);
    <span style="color: rgb(181,106,1);">eglSwapBuffers</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>);
    <span style="color: rgb(181,106,1);">glDeleteShader</span>(<span style="color: rgb(0,0,255);">vertexShader</span>);
    <span style="color: rgb(181,106,1);">glDeleteShader</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>);
    <span style="color: rgb(181,106,1);">glDeleteBuffers</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(0,0,255);">std</span>::<span style="color: rgb(0,0,255);">this_thread</span>::<span style="color: rgb(181,106,1);">sleep_for</span>(<span style="color: rgb(0,0,255);">std</span>::<span style="color: rgb(0,0,255);">chrono</span>::<span style="color: rgb(181,106,1);">milliseconds</span>(<span style="color: rgb(80,160,79);">50</span>));
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">display</span>, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    <span style="color: rgb(181,106,1);">eglDestroySurface</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>);
    <span style="color: rgb(181,106,1);">eglDestroyContext</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">context</span>);
    <span style="color: rgb(181,106,1);">eglTerminate</span>(<span style="color: rgb(0,0,255);">display</span>);
}
```

- **方案二**：使用CPU后端的离屏画布绘制文本取得文本像素数据。1. 在ArkTS侧，创建XComponent用作OpenGL ES绘制窗口，将SurfaceID传递到Native侧。
```text
<span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController1</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nativeDrawCpu</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```


2. 创建CPU后端的离屏画布，使用单字绘制接口逐个绘制文字字符（单字绘制能够利用字体退化机制，提升对特殊字符的兼容性）。拷贝离屏画布文本绘制区域的像素数据，用于OpenGL生成纹理对象。
```text
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">NativeDrawCpu</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">900</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">300</span>;
  <em>  // 创建位图对象</em>
    OH_Drawing_Bitmap <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">bitmap</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_BitmapCreate</span>();
    OH_Drawing_BitmapFormat <span style="color: rgb(0,0,255);">cFormat</span>{COLOR_FORMAT_BGRA_8888, ALPHA_FORMAT_PREMUL};
 <em>   // 初始化位图</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_BitmapBuild</span>(<span style="color: rgb(0,0,255);">bitmap</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">cFormat</span>);
  <em>  // 创建Canvas对象</em>
    OH_Drawing_Canvas <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">bitmapCanvas</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_CanvasCreate</span>();
  <em>  // 将Canvas与位图绑定，Canvas绘制的内容会输出到绑定的bitmap内存中</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasBind</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(0,0,255);">bitmap</span>);
  <em>  // 绘制字块</em>
    <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(0,0,255);">text</span>[] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"你好</span><span style="color: rgb(181,106,1);">\xF0\x9F\x98\x82</span><span style="color: rgb(181,106,1);">"</span>;
    OH_Drawing_Font <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">font</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_FontCreate</span>();
    <span style="color: rgb(181,106,1);">OH_Drawing_FontSetTextSize</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(80,160,79);">100</span>);
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posY</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">150</span>;
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">2</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">1</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(181,106,1);">OH_Drawing_FontDestroy</span>(<span style="color: rgb(0,0,255);">font</span>);
   <em> // 从Canvas上拷贝绘制结果位图数据</em>
    <span style="color: rgb(0,0,255);">std</span>::unique_ptr<span style="color: rgb(128,128,128);"><</span><span style="color: rgb(0,0,255);">uint8_t</span><span style="color: rgb(128,128,128);">></span> <span style="color: rgb(0,0,255);">dstPixels</span>(<span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">uint8_t</span>[<span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span>]);
    OH_Drawing_Image_Info <span style="color: rgb(0,0,255);">imageInfo</span> <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasReadPixels</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageInfo</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>(), <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>);
  <em>  // 清理资源</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDestroy</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>);
    <span style="color: rgb(181,106,1);">OH_Drawing_BitmapDestroy</span>(<span style="color: rgb(0,0,255);">bitmap</span>);
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">argc</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">info</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">argc</span>, <span style="color: rgb(0,0,255);">args</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
  <em>  // 获取XComponent的SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> <span style="color: rgb(0,0,255);">lossless</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> <span style="color: rgb(0,0,255);">surfaceId</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">lossless</span>);
 <em>   // 通过SurfaceID创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">window</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(<span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">window</span>);
  <em>  // 通过OpenGL ES绘制图像</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>());
  <em>  // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(<span style="color: rgb(0,0,255);">window</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```


3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。同方案一步骤三。
- **方案三**：使用GPU后端的离屏画布绘制文本取得文本像素数据。1. 在ArkTS侧，创建XComponent用作OpenGL ES绘制窗口，将SurfaceID传递到Native侧。
```text
<span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController2 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController2</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nativeDrawGpu</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```


2. 初始化EGL上下文。创建GPU后端离屏画布。在离屏画布上，使用单字绘制接口逐个绘制文字字符。拷贝离屏画布文本绘制区域的像素数据，用于OpenGL生成纹理对象。
```text
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">NativeDrawGpu</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
   <em> // 初始化EGL上下文</em>
    EGLDisplay <span style="color: rgb(0,0,255);">bufDisplay</span>;
    EGLConfig <span style="color: rgb(0,0,255);">bufConfig</span>;
    EGLSurface <span style="color: rgb(0,0,255);">bufSurface</span>;
    EGLContext <span style="color: rgb(0,0,255);">bufContext</span>;
    EGLint <span style="color: rgb(0,0,255);">majorVersion</span>;
    EGLint <span style="color: rgb(0,0,255);">minorVersion</span>;
    <span style="color: rgb(0,0,255);">bufDisplay</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglGetDisplay</span>(EGL_DEFAULT_DISPLAY);
    <span style="color: rgb(181,106,1);">eglInitialize</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">majorVersion</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">minorVersion</span>);
    EGLint <span style="color: rgb(0,0,255);">numConfigs</span>;
    EGLint <span style="color: rgb(0,0,255);">attribs</span>[] <span style="color: rgb(128,128,128);">=</span> {
        EGL_SURFACE_TYPE,
        EGL_WINDOW_BIT,
        EGL_RENDERABLE_TYPE,
        EGL_OPENGL_ES3_BIT,
        EGL_BLUE_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_GREEN_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_RED_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_ALPHA_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_NONE,
    };
    <span style="color: rgb(181,106,1);">eglChooseConfig</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">attribs</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">bufConfig</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">numConfigs</span>);
    EGLint <span style="color: rgb(0,0,255);">contextAttribs</span>[] <span style="color: rgb(128,128,128);">=</span> {EGL_CONTEXT_CLIENT_VERSION, <span style="color: rgb(80,160,79);">3</span>, EGL_NONE};
    <span style="color: rgb(0,0,255);">bufSurface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreatePbufferSurface</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufConfig</span>, <span style="color: rgb(0,0,255);">attribs</span>);
    <span style="color: rgb(0,0,255);">bufContext</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateContext</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufConfig</span>, EGL_NO_CONTEXT, <span style="color: rgb(0,0,255);">contextAttribs</span>);
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufSurface</span>, <span style="color: rgb(0,0,255);">bufSurface</span>, <span style="color: rgb(0,0,255);">bufContext</span>);
   <em> // 设置宽高（按需设定）</em>
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">900</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">300</span>;
   <em> // 设置图像宽、高、颜色格式和透明度格式</em>
    OH_Drawing_Image_Info <span style="color: rgb(0,0,255);">imageInfo</span> <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
 <em>   // 创建GPU后端的绘图上下文</em>
    OH_Drawing_GpuContext <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">gpuContext</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_GpuContextCreate</span>();
 <em>   // 创建Surface对象</em>
    OH_Drawing_Surface <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">drawSurface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_SurfaceCreateFromGpuContext</span>(<span style="color: rgb(0,0,255);">gpuContext</span>, <span style="color: rgb(0,0,255);">true</span>, <span style="color: rgb(0,0,255);">imageInfo</span>);
 <em>   // 创建Canvas对象</em>
    OH_Drawing_Canvas <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">gpuCanvas</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_SurfaceGetCanvas</span>(<span style="color: rgb(0,0,255);">drawSurface</span>);
 <em>   // 绘制字块</em>
    <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(0,0,255);">text</span>[] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"你好</span><span style="color: rgb(181,106,1);">\xF0\x9F\x98\x82</span><span style="color: rgb(181,106,1);">"</span>;
    OH_Drawing_Font <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">font</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_FontCreate</span>();
    <span style="color: rgb(181,106,1);">OH_Drawing_FontSetTextSize</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(80,160,79);">100</span>);
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posY</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">150</span>;
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">2</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">1</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(181,106,1);">OH_Drawing_FontDestroy</span>(<span style="color: rgb(0,0,255);">font</span>);
  <em>  // 从Canvas 上拷贝绘制结果位图数据</em>
    <span style="color: rgb(0,0,255);">std</span>::unique_ptr<span style="color: rgb(128,128,128);"><</span><span style="color: rgb(0,0,255);">uint8_t</span><span style="color: rgb(128,128,128);">></span> <span style="color: rgb(0,0,255);">dstPixels</span>(<span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">uint8_t</span>[<span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span>]);
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasReadPixels</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageInfo</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>(), <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>);
  <em>  // 清理资源</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDestroy</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>);
  <em>  // 清理EGL</em>
    <span style="color: rgb(181,106,1);">eglDestroySurface</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufSurface</span>);
    <span style="color: rgb(181,106,1);">eglDestroyContext</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufContext</span>);
    <span style="color: rgb(181,106,1);">eglTerminate</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>);
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">argc</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">info</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">argc</span>, <span style="color: rgb(0,0,255);">args</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
<em>    // 获取XComponent的SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> <span style="color: rgb(0,0,255);">lossless</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> <span style="color: rgb(0,0,255);">surfaceId</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">lossless</span>);
   <em> // 通过SurfaceID创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">window</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(<span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">window</span>);
  <em>  // 通过OpenGL ES绘制图像</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>());
   <em> // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(<span style="color: rgb(0,0,255);">window</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```


3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。同方案一步骤三。

 
完整示例参考如下：
 
- ArkTS侧：
```text
import <span style="color: rgb(255,255,255);">testNapi </span>from <span style="color: rgb(132,63,161);">'libentry.so'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,255,255);">image </span>from <span style="color: rgb(132,63,161);">'@ohos.multimedia.image'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">xController1 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">XComponentController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">xController2 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">XComponentController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">xController3 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">XComponentController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PixelMap </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'CPU Canvas'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController1</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nativeDrawCpu</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'GPU Canvas'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController2 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController2</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nativeDrawGpu</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'OffScreenCanvas'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SURFACE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController3 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">离屏绘制文本</span></em>
            let <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">你好</span>\u<span style="color: rgb(132,63,161);">{D83D}</span>\u<span style="color: rgb(132,63,161);">{DE02}'</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">offCanvas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">OffscreenCanvas </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">OffscreenCanvas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">offContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">offCanvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'2d'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'#000000'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">font </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'100px sans-serif'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
       <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从离屏画布上读取位图数据。</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">offContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">buffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelBytesNumber</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
            await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readPixelsToBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取位图的宽、高信息。</span></em>
            let <span style="color: rgb(255,255,255);">imgInfo </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImageInfo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">imgWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">imgInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">imgHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">imgInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">;</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">XComponent</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">SurfaceID</span><span style="color: rgb(128,128,128);">。</span></em>
            let <span style="color: rgb(255,255,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xController3</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将位图数据、宽、高，</span><span style="color: rgb(128,128,128);">SurfaceID</span><span style="color: rgb(128,128,128);">传递到</span><span style="color: rgb(128,128,128);">Native</span><span style="color: rgb(128,128,128);">侧使用</span><span style="color: rgb(128,128,128);">OpenGL ES</span><span style="color: rgb(128,128,128);">完成绘制。</span></em>
            <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">drawText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">surfaceId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">imgWidth</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">imgHeight</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

- Native侧：
```text
<em>/*</em>
<em><span style="color: rgb(80,160,79);"> * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.</span></em>
<em><span style="color: rgb(80,160,79);"> */</span></em>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);">"napi/native_api.h"</span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">EGL/egl.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">EGL/eglext.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">EGL/eglplatform.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">GLES3/gl3.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">ace/xcomponent/native_interface_xcomponent.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">cstdint</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_bitmap.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_canvas.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_color.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_font.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_gpu_context.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_surface.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_drawing/drawing_text_blob.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">native_window/external_window.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">thread</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#undef</span> <span style="color: rgb(0,0,255);">LOG_DOMAIN</span>
<span style="color: rgb(255,0,170);">#undef</span> <span style="color: rgb(0,0,255);">LOG_TAG</span>
<span style="color: rgb(255,0,170);">#define</span> <span style="color: rgb(0,0,255);">LOG_DOMAIN</span> <span style="color: rgb(80,160,79);">0x3200</span>
<span style="color: rgb(255,0,170);">#define</span> <span style="color: rgb(0,0,255);">LOG_TAG</span> <span style="color: rgb(181,106,1);">"GL_Image"</span>
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">OHNativeWindow</span> <span style="color: rgb(0,0,255);">*</span><span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(0,0,255);">*</span><span style="color: rgb(0,0,255);">data</span>)
{
    EGLDisplay <span style="color: rgb(0,0,255);">display</span>;
    EGLint <span style="color: rgb(0,0,255);">majorVersion</span>;
    EGLint <span style="color: rgb(0,0,255);">minorVersion</span>;
    <span style="color: rgb(0,0,255);">display</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglGetDisplay</span>(EGL_DEFAULT_DISPLAY);
    <span style="color: rgb(181,106,1);">eglInitialize</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">majorVersion</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">minorVersion</span>);
    EGLConfig <span style="color: rgb(0,0,255);">config</span>;
    EGLint <span style="color: rgb(0,0,255);">numConfigs</span>;
    EGLint <span style="color: rgb(0,0,255);">attribs</span>[] <span style="color: rgb(128,128,128);">=</span> {
        EGL_SURFACE_TYPE,
        EGL_WINDOW_BIT,
        EGL_RENDERABLE_TYPE,
        EGL_OPENGL_ES3_BIT,
        EGL_BLUE_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_GREEN_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_RED_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_ALPHA_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_NONE,
    };
    <span style="color: rgb(181,106,1);">eglChooseConfig</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">attribs</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">config</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">numConfigs</span>);
    EGLSurface <span style="color: rgb(0,0,255);">surface</span>;
    EGLContext <span style="color: rgb(0,0,255);">context</span>;
    EGLint <span style="color: rgb(0,0,255);">contextAttribs</span>[] <span style="color: rgb(128,128,128);">=</span> {EGL_CONTEXT_CLIENT_VERSION, <span style="color: rgb(80,160,79);">3</span>, EGL_NONE};
    <span style="color: rgb(0,0,255);">surface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateWindowSurface</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">config</span>, (EGLNativeWindowType)<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">NULL</span>);
    <span style="color: rgb(0,0,255);">context</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateContext</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">config</span>, EGL_NO_CONTEXT, <span style="color: rgb(0,0,255);">contextAttribs</span>);
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>, <span style="color: rgb(0,0,255);">surface</span>, <span style="color: rgb(0,0,255);">context</span>);
    <span style="color: rgb(181,106,1);">glViewport</span>(<span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>);
    <span style="color: rgb(181,106,1);">glClearColor</span>(<span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>);
    <span style="color: rgb(181,106,1);">glClear</span>(GL_COLOR_BUFFER_BIT);
    GLfloat <span style="color: rgb(0,0,255);">vertices</span>[] <span style="color: rgb(128,128,128);">=</span> {
        <em>// First triangle</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,  <em> // ...</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <em> // ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <em>// ...</em>
      <em>  // Second triangle</em>
        <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,  <em> // ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <em>// ...</em>
        <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">1.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>, <span style="color: rgb(80,160,79);">0.0f</span>,  <em>// ...</em>
    };
    GLuint <span style="color: rgb(0,0,255);">vbo</span>;
    GLuint <span style="color: rgb(0,0,255);">vao</span>[<span style="color: rgb(80,160,79);">0</span>];
    <span style="color: rgb(181,106,1);">glGenVertexArrays</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(0,0,255);">vao</span>);
    <span style="color: rgb(181,106,1);">glBindVertexArray</span>(<span style="color: rgb(0,0,255);">vao</span>[<span style="color: rgb(80,160,79);">0</span>]);
    <span style="color: rgb(181,106,1);">glGenBuffers</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(181,106,1);">glBindBuffer</span>(GL_ARRAY_BUFFER, <span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(181,106,1);">glBufferData</span>(GL_ARRAY_BUFFER, <span style="color: rgb(0,0,255);">sizeof</span>(<span style="color: rgb(0,0,255);">vertices</span>), <span style="color: rgb(0,0,255);">vertices</span>, GL_STATIC_DRAW);
    <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">vertexShaderSource</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">R"(#version 300 es</span>
<span style="color: rgb(181,106,1);">        layout (location = 0) in vec4 vPosition;</span>
<span style="color: rgb(181,106,1);">        layout (location = 1) in vec2 vTexCoord;</span>
<span style="color: rgb(181,106,1);">        out vec2 TexCoord;</span>
<span style="color: rgb(181,106,1);">        void main() {</span>
<span style="color: rgb(181,106,1);">            gl_Position = vPosition;</span>
<span style="color: rgb(181,106,1);">            TexCoord = vTexCoord;</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">    )"</span>;
    <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">fragmentShaderSource</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">R"(#version 300 es</span>
<span style="color: rgb(181,106,1);">        precision mediump float;</span>
<span style="color: rgb(181,106,1);">        out vec4 FragColor;</span>
<span style="color: rgb(181,106,1);">        in vec2 TexCoord;</span>
<span style="color: rgb(181,106,1);">        uniform sampler2D testTexture;</span>
<span style="color: rgb(181,106,1);">        void main() {</span>
<span style="color: rgb(181,106,1);">            FragColor = texture(testTexture, TexCoord);</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">    )"</span>;
    GLuint <span style="color: rgb(0,0,255);">vertexShader</span>;
    <span style="color: rgb(0,0,255);">vertexShader</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateShader</span>(GL_VERTEX_SHADER);
    <span style="color: rgb(181,106,1);">glShaderSource</span>(<span style="color: rgb(0,0,255);">vertexShader</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vertexShaderSource</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(181,106,1);">glCompileShader</span>(<span style="color: rgb(0,0,255);">vertexShader</span>);
    GLuint <span style="color: rgb(0,0,255);">fragmentShader</span>;
    <span style="color: rgb(0,0,255);">fragmentShader</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateShader</span>(GL_FRAGMENT_SHADER);
    <span style="color: rgb(181,106,1);">glShaderSource</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">fragmentShaderSource</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(181,106,1);">glCompileShader</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>);
    GLuint <span style="color: rgb(0,0,255);">shaderProgram</span>;
    <span style="color: rgb(0,0,255);">shaderProgram</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">glCreateProgram</span>();
    <span style="color: rgb(181,106,1);">glAttachShader</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(0,0,255);">vertexShader</span>);
    <span style="color: rgb(181,106,1);">glAttachShader</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(0,0,255);">fragmentShader</span>);
    <span style="color: rgb(181,106,1);">glLinkProgram</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>);
    <span style="color: rgb(181,106,1);">glUseProgram</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>);
    GLuint <span style="color: rgb(0,0,255);">textureId</span>;
    <span style="color: rgb(181,106,1);">glGenTextures</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glBindTexture</span>(GL_TEXTURE_2D, <span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    <span style="color: rgb(181,106,1);">glTexParameteri</span>(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    <span style="color: rgb(181,106,1);">glTexImage2D</span>(GL_TEXTURE_2D, <span style="color: rgb(80,160,79);">0</span>, GL_RGBA, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(80,160,79);">0</span>, GL_RGBA, GL_UNSIGNED_BYTE, <span style="color: rgb(0,0,255);">data</span>);
    <span style="color: rgb(181,106,1);">glGenerateMipmap</span>(GL_TEXTURE_2D);
    <span style="color: rgb(181,106,1);">glUniform1i</span>(<span style="color: rgb(181,106,1);">glGetUniformLocation</span>(<span style="color: rgb(0,0,255);">shaderProgram</span>, <span style="color: rgb(181,106,1);">"testTexture"</span>), <span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glActiveTexture</span>(GL_TEXTURE0);
    <span style="color: rgb(181,106,1);">glBindTexture</span>(GL_TEXTURE_2D, <span style="color: rgb(0,0,255);">textureId</span>);
    <span style="color: rgb(181,106,1);">glVertexAttribPointer</span>(<span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">3</span>, GL_FLOAT, GL_FALSE, <span style="color: rgb(80,160,79);">5</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat), (GLvoid <span style="color: rgb(128,128,128);">*</span>)<span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glEnableVertexAttribArray</span>(<span style="color: rgb(80,160,79);">0</span>);
    <span style="color: rgb(181,106,1);">glVertexAttribPointer</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(80,160,79);">2</span>, GL_FLOAT, GL_FALSE, <span style="color: rgb(80,160,79);">5</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat), (GLvoid <span style="color: rgb(128,128,128);">*</span>)(<span style="color: rgb(80,160,79);">3</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">sizeof</span>(GLfloat)));
    <span style="color: rgb(181,106,1);">glEnableVertexAttribArray</span>(<span style="color: rgb(80,160,79);">1</span>);
    <span style="color: rgb(181,106,1);">glDrawArrays</span>(GL_TRIANGLES, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">6</span>);
    <span style="color: rgb(181,106,1);">eglSwapBuffers</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>);
    <span style="color: rgb(181,106,1);">glDeleteShader</span>(<span style="color: rgb(0,0,255);">vertexShader</span>);
    <span style="color: rgb(181,106,1);">glDeleteShader</span>(<span style="color: rgb(0,0,255);">fragmentShader</span>);
    <span style="color: rgb(181,106,1);">glDeleteBuffers</span>(<span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">vbo</span>);
    <span style="color: rgb(0,0,255);">std</span>::<span style="color: rgb(0,0,255);">this_thread</span>::<span style="color: rgb(181,106,1);">sleep_for</span>(<span style="color: rgb(0,0,255);">std</span>::<span style="color: rgb(0,0,255);">chrono</span>::<span style="color: rgb(181,106,1);">milliseconds</span>(<span style="color: rgb(80,160,79);">50</span>));
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">display</span>, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    <span style="color: rgb(181,106,1);">eglDestroySurface</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">surface</span>);
    <span style="color: rgb(181,106,1);">eglDestroyContext</span>(<span style="color: rgb(0,0,255);">display</span>, <span style="color: rgb(0,0,255);">context</span>);
    <span style="color: rgb(181,106,1);">eglTerminate</span>(<span style="color: rgb(0,0,255);">display</span>);
}
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">NativeDrawGpu</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
  <em>  // 初始化EGL上下文</em>
    EGLDisplay <span style="color: rgb(0,0,255);">bufDisplay</span>;
    EGLConfig <span style="color: rgb(0,0,255);">bufConfig</span>;
    EGLSurface <span style="color: rgb(0,0,255);">bufSurface</span>;
    EGLContext <span style="color: rgb(0,0,255);">bufContext</span>;
    EGLint <span style="color: rgb(0,0,255);">majorVersion</span>;
    EGLint <span style="color: rgb(0,0,255);">minorVersion</span>;
    <span style="color: rgb(0,0,255);">bufDisplay</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglGetDisplay</span>(EGL_DEFAULT_DISPLAY);
    <span style="color: rgb(181,106,1);">eglInitialize</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">majorVersion</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">minorVersion</span>);
    EGLint <span style="color: rgb(0,0,255);">numConfigs</span>;
    EGLint <span style="color: rgb(0,0,255);">attribs</span>[] <span style="color: rgb(128,128,128);">=</span> {
        EGL_SURFACE_TYPE,
        EGL_WINDOW_BIT,
        EGL_RENDERABLE_TYPE,
        EGL_OPENGL_ES3_BIT,
        EGL_BLUE_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_GREEN_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_RED_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_ALPHA_SIZE,
        <span style="color: rgb(80,160,79);">8</span>,
        EGL_NONE,
    };
    <span style="color: rgb(181,106,1);">eglChooseConfig</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">attribs</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">bufConfig</span>, <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">numConfigs</span>);
    EGLint <span style="color: rgb(0,0,255);">contextAttribs</span>[] <span style="color: rgb(128,128,128);">=</span> {EGL_CONTEXT_CLIENT_VERSION, <span style="color: rgb(80,160,79);">3</span>, EGL_NONE};
    <span style="color: rgb(0,0,255);">bufSurface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreatePbufferSurface</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufConfig</span>, <span style="color: rgb(0,0,255);">attribs</span>);
    <span style="color: rgb(0,0,255);">bufContext</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">eglCreateContext</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufConfig</span>, EGL_NO_CONTEXT, <span style="color: rgb(0,0,255);">contextAttribs</span>);
    <span style="color: rgb(181,106,1);">eglMakeCurrent</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufSurface</span>, <span style="color: rgb(0,0,255);">bufSurface</span>, <span style="color: rgb(0,0,255);">bufContext</span>);
  <em>  // 设置宽高（按需设定）</em>
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">900</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">300</span>;
  <em>  // 设置图像宽、高、颜色格式和透明度格式</em>
    OH_Drawing_Image_Info <span style="color: rgb(0,0,255);">imageInfo</span> <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
 <em>   // 创建GPU后端的绘图上下文</em>
    OH_Drawing_GpuContext <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">gpuContext</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_GpuContextCreate</span>();
  <em>  // 创建Surface对象</em>
    OH_Drawing_Surface <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">drawSurface</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_SurfaceCreateFromGpuContext</span>(<span style="color: rgb(0,0,255);">gpuContext</span>, <span style="color: rgb(0,0,255);">true</span>, <span style="color: rgb(0,0,255);">imageInfo</span>);
 <em>   // 创建Canvas对象</em>
    OH_Drawing_Canvas <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">gpuCanvas</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_SurfaceGetCanvas</span>(<span style="color: rgb(0,0,255);">drawSurface</span>);
  <em>  // 绘制字块</em>
    <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(0,0,255);">text</span>[] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"你好</span><span style="color: rgb(181,106,1);">\xF0\x9F\x98\x82</span><span style="color: rgb(181,106,1);">"</span>;
    OH_Drawing_Font <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">font</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_FontCreate</span>();
    <span style="color: rgb(181,106,1);">OH_Drawing_FontSetTextSize</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(80,160,79);">100</span>);
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posY</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">150</span>;
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">2</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">1</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(181,106,1);">OH_Drawing_FontDestroy</span>(<span style="color: rgb(0,0,255);">font</span>);
  <em>  // 从Canvas 上拷贝绘制结果位图数据</em>
    <span style="color: rgb(0,0,255);">std</span>::unique_ptr<span style="color: rgb(128,128,128);"><</span><span style="color: rgb(0,0,255);">uint8_t</span><span style="color: rgb(128,128,128);">></span> <span style="color: rgb(0,0,255);">dstPixels</span>(<span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">uint8_t</span>[<span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span>]);
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasReadPixels</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageInfo</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>(), <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>);
  <em>  // 清理资源</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDestroy</span>(<span style="color: rgb(0,0,255);">gpuCanvas</span>);
   <em> // 清理EGL</em>
    <span style="color: rgb(181,106,1);">eglDestroySurface</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufSurface</span>);
    <span style="color: rgb(181,106,1);">eglDestroyContext</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>, <span style="color: rgb(0,0,255);">bufContext</span>);
    <span style="color: rgb(181,106,1);">eglTerminate</span>(<span style="color: rgb(0,0,255);">bufDisplay</span>);
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">argc</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">info</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">argc</span>, <span style="color: rgb(0,0,255);">args</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
   <em> // 获取XComponent的SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> <span style="color: rgb(0,0,255);">lossless</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> <span style="color: rgb(0,0,255);">surfaceId</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">lossless</span>);
  <em>  // 通过SurfaceID创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">window</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(<span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">window</span>);
 <em>   // 通过OpenGL ES绘制图像</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>());
 <em>   // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(<span style="color: rgb(0,0,255);">window</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">NativeDrawCpu</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">900</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">300</span>;
 <em>   // 创建位图对象</em>
    OH_Drawing_Bitmap <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">bitmap</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_BitmapCreate</span>();
    OH_Drawing_BitmapFormat <span style="color: rgb(0,0,255);">cFormat</span>{COLOR_FORMAT_BGRA_8888, ALPHA_FORMAT_PREMUL};
  <em>  // 初始化位图</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_BitmapBuild</span>(<span style="color: rgb(0,0,255);">bitmap</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">cFormat</span>);
   <em> // 创建Canvas对象</em>
    OH_Drawing_Canvas <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">bitmapCanvas</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_CanvasCreate</span>();
<em>    // 将Canvas与位图绑定，Canvas绘制的内容会输出到绑定的bitmap内存中</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasBind</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(0,0,255);">bitmap</span>);
   <em> // 绘制字块</em>
    <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(0,0,255);">text</span>[] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"你好</span><span style="color: rgb(181,106,1);">\xF0\x9F\x98\x82</span><span style="color: rgb(181,106,1);">"</span>;
    OH_Drawing_Font <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">font</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_Drawing_FontCreate</span>();
    <span style="color: rgb(181,106,1);">OH_Drawing_FontSetTextSize</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(80,160,79);">100</span>);
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">posY</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">150</span>;
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">2</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(255,0,170);">for</span> (<span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; <span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);"><</span> <span style="color: rgb(80,160,79);">1</span>; <span style="color: rgb(0,0,255);">idx</span><span style="color: rgb(128,128,128);">++</span>) {
        <span style="color: rgb(0,0,255);">float</span> <span style="color: rgb(0,0,255);">textWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0.0f</span>;
        <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDrawSingleCharacter</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(0,0,255);">posX</span>, <span style="color: rgb(0,0,255);">posY</span>);
        <span style="color: rgb(181,106,1);">OH_Drawing_FontMeasureSingleCharacter</span>(<span style="color: rgb(0,0,255);">font</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">text</span>[<span style="color: rgb(0,0,255);">idx</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">6</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">textWidth</span>);
        <span style="color: rgb(0,0,255);">posX</span> <span style="color: rgb(128,128,128);">+=</span> <span style="color: rgb(0,0,255);">textWidth</span>;
    }
    <span style="color: rgb(181,106,1);">OH_Drawing_FontDestroy</span>(<span style="color: rgb(0,0,255);">font</span>);
  <em>  // 从Canvas上拷贝绘制结果位图数据</em>
    <span style="color: rgb(0,0,255);">std</span>::unique_ptr<span style="color: rgb(128,128,128);"><</span><span style="color: rgb(0,0,255);">uint8_t</span><span style="color: rgb(128,128,128);">></span> <span style="color: rgb(0,0,255);">dstPixels</span>(<span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">uint8_t</span>[<span style="color: rgb(0,0,255);">width</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">height</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(80,160,79);">4</span>]);
    OH_Drawing_Image_Info <span style="color: rgb(0,0,255);">imageInfo</span> <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasReadPixels</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageInfo</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>(), <span style="color: rgb(80,160,79);">4</span> <span style="color: rgb(128,128,128);">*</span> <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(80,160,79);">0</span>);
   <em> // 清理资源</em>
    <span style="color: rgb(181,106,1);">OH_Drawing_CanvasDestroy</span>(<span style="color: rgb(0,0,255);">bitmapCanvas</span>);
    <span style="color: rgb(181,106,1);">OH_Drawing_BitmapDestroy</span>(<span style="color: rgb(0,0,255);">bitmap</span>);
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">argc</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">info</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">argc</span>, <span style="color: rgb(0,0,255);">args</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
 <em>   // 获取XComponent的SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> <span style="color: rgb(0,0,255);">lossless</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> <span style="color: rgb(0,0,255);">surfaceId</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">lossless</span>);
  <em>  // 通过SurfaceID创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">window</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(<span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">window</span>);
  <em>  // 通过OpenGL ES绘制图像</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">width</span>, <span style="color: rgb(0,0,255);">height</span>, <span style="color: rgb(0,0,255);">dstPixels</span>.<span style="color: rgb(181,106,1);">get</span>());
   <em> // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(<span style="color: rgb(0,0,255);">window</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">DrawImage</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">argc</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">5</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">5</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">info</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">argc</span>, <span style="color: rgb(0,0,255);">args</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
   <em> // 获取SurfaceID</em>
    <span style="color: rgb(0,0,255);">bool</span> <span style="color: rgb(0,0,255);">lossless</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">true</span>;
    <span style="color: rgb(0,0,255);">uint64_t</span> <span style="color: rgb(0,0,255);">surfaceId</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_bigint_uint64</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">lossless</span>);
   <em> // 获取位图数据</em>
    <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">data</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(0,0,255);">size_t</span> <span style="color: rgb(0,0,255);">byteLength</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_arraybuffer_info</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">data</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">byteLength</span>);
   <em> // 获取位图宽、高</em>
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">imageWidth</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(0,0,255);">int32_t</span> <span style="color: rgb(0,0,255);">imageHeight</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_int32</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">2</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageWidth</span>);
    <span style="color: rgb(181,106,1);">napi_get_value_int32</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">3</span>], <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">imageHeight</span>);
    <em>// 创建NativeWindow对象</em>
    OHNativeWindow <span style="color: rgb(128,128,128);">*</span><span style="color: rgb(0,0,255);">window</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    <span style="color: rgb(181,106,1);">OH_NativeWindow_CreateNativeWindowFromSurfaceId</span>(<span style="color: rgb(0,0,255);">surfaceId</span>, <span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">window</span>);
   <em> // 使用OpenGL ES绘制位图</em>
    <span style="color: rgb(181,106,1);">GLDraw</span>(<span style="color: rgb(0,0,255);">window</span>, <span style="color: rgb(0,0,255);">imageWidth</span>, <span style="color: rgb(0,0,255);">imageHeight</span>, <span style="color: rgb(0,0,255);">data</span>);
   <em> // 销毁NativeWindow</em>
    <span style="color: rgb(181,106,1);">OH_NativeWindow_DestroyNativeWindow</span>(<span style="color: rgb(0,0,255);">window</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
EXTERN_C_START
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">Init</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(0,0,255);">exports</span>)
{
    napi_property_descriptor <span style="color: rgb(0,0,255);">desc</span>[] <span style="color: rgb(128,128,128);">=</span> {
        {<span style="color: rgb(181,106,1);">"drawText"</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(181,106,1);">DrawImage</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, napi_default, <span style="color: rgb(0,0,255);">nullptr</span>},
        {<span style="color: rgb(181,106,1);">"nativeDrawCpu"</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(181,106,1);">NativeDrawCpu</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, napi_default, <span style="color: rgb(0,0,255);">nullptr</span>},
        {<span style="color: rgb(181,106,1);">"nativeDrawGpu"</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(181,106,1);">NativeDrawGpu</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>, napi_default, <span style="color: rgb(0,0,255);">nullptr</span>},
    };
    <span style="color: rgb(181,106,1);">napi_define_properties</span>(<span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">exports</span>, <span style="color: rgb(0,0,255);">sizeof</span>(<span style="color: rgb(0,0,255);">desc</span>) <span style="color: rgb(128,128,128);">/</span> <span style="color: rgb(0,0,255);">sizeof</span>(<span style="color: rgb(0,0,255);">desc</span>[<span style="color: rgb(80,160,79);">0</span>]), <span style="color: rgb(0,0,255);">desc</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">exports</span>;
}
EXTERN_C_END
<span style="color: rgb(0,0,255);">static</span> napi_module <span style="color: rgb(0,0,255);">demoModule</span> <span style="color: rgb(128,128,128);">=</span> {
    .<span style="color: rgb(0,0,255);">nm_version</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>,
    .<span style="color: rgb(0,0,255);">nm_flags</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>,
    .<span style="color: rgb(0,0,255);">nm_filename</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">nullptr</span>,
    .<span style="color: rgb(0,0,255);">nm_register_func</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">Init</span>,
    .<span style="color: rgb(0,0,255);">nm_modname</span> <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"entry"</span>,
    .<span style="color: rgb(0,0,255);">nm_priv</span> <span style="color: rgb(128,128,128);">=</span> ((<span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(128,128,128);">*</span>)<span style="color: rgb(80,160,79);">0</span>),
    .<span style="color: rgb(0,0,255);">reserved</span> <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(80,160,79);">0</span>},
};
<span style="color: rgb(0,0,255);">extern</span> <span style="color: rgb(181,106,1);">"C"</span> <span style="color: rgb(181,106,1);">__attribute__</span>((constructor)) <span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(181,106,1);">RegisterEntryModule</span>(<span style="color: rgb(0,0,255);">void</span>) { <span style="color: rgb(181,106,1);">napi_module_register</span>(<span style="color: rgb(128,128,128);">&</span><span style="color: rgb(0,0,255);">demoModule</span>); }
```


 
 

#### 总结

使用OpenGL绘制文字的关键在于取得绘制文字内容的像素数据，获得文本的像素数据后，OpenGL生成纹理对象并在屏幕绘制。目前HarmonyOS支持通过上述三种方式取得文字绘制的像素数据，它们之间的对比如下表所示：
  
| 方案 | 对比 |
| --- | --- |
| OffscreenCanvas组件 | 在ArkTS侧实现，实现逻辑简单，使用CPU绘制，需要两次数据拷贝。 |
| CPU后端的离屏画布 | 在Native侧实现，使用CPU绘制，一次数据拷贝。 |
| GPU后端的离屏画布 | 在Native侧实现，使用GPU绘制，一次数据拷贝。 |
