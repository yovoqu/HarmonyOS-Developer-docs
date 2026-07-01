# 如何在C++侧打开Picker获取的用户文件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-8

#### 问题现象

通过Picker方式获取用户文件URI，在C++侧无法通过URI打开文件。
 
 

#### 背景知识

[用户文件URI介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro)：用户文件URI是文件的唯一标识，在ArkTS侧可以通过该URI访问用户文件，在C++侧需要转换为路径或文件句柄访问。
 
 

#### 解决方案

- 将URI直接传递到C++侧，通过C++侧提供的转换接口，将URI转换为path后访问文件。
```text
<span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">ReadFileFromUri</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> argc <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(env, info, <span style="color: rgb(128,128,128);">&</span>argc, args, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(0,0,255);">size_t</span> length <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(128,128,128);">&</span>length);
    <span style="color: rgb(0,0,255);">char</span><span style="color: rgb(128,128,128);">*</span> uri <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">char</span>[length <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>];
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], uri, length <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span>length);
    <span style="color: rgb(0,0,255);">uri</span>[length] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">'</span><span style="color: rgb(181,106,1);">\0</span><span style="color: rgb(181,106,1);">'</span>;
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromUri Uri: %{public}s"</span>, uri);
    <span style="color: rgb(0,0,255);">char</span> <span style="color: rgb(128,128,128);">*</span>pathResult <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(0,0,255);">NULL</span>;
    <span style="color: rgb(0,0,255);">int</span> ret <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">OH_FileUri_GetPathFromUri</span>(uri, length, <span style="color: rgb(128,128,128);">&</span>pathResult);
    <span style="color: rgb(255,0,170);">if</span> (ret <span style="color: rgb(128,128,128);">!=</span> <span style="color: rgb(80,160,79);">0</span> <span style="color: rgb(128,128,128);">||</span> pathResult <span style="color: rgb(128,128,128);">==</span> <span style="color: rgb(0,0,255);">NULL</span>) {
        <span style="color: rgb(255,0,170);">delete</span> []uri;
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromUri Path: %{public}s"</span>, pathResult);
    <span style="color: rgb(0,0,255);">int</span> fd <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">open</span>(pathResult, O_RDONLY);
    <span style="color: rgb(0,0,255);">struct</span> <span style="color: rgb(0,0,255);">stat</span> <span style="color: rgb(0,0,255);">fileInfo</span>;
    <span style="color: rgb(255,0,170);">if</span> (<span style="color: rgb(181,106,1);">fstat</span>(fd, <span style="color: rgb(128,128,128);">&</span>fileInfo) <span style="color: rgb(128,128,128);">==</span> <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1</span>) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromUri failed"</span>);
        <span style="color: rgb(255,0,170);">delete</span> []uri;
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromUri: %{public}d"</span>, (<span style="color: rgb(0,0,255);">int</span>)<span style="color: rgb(0,0,255);">fileInfo</span>.<span style="color: rgb(0,0,255);">st_size</span>);
    <span style="color: rgb(181,106,1);">close</span>(fd);
    <span style="color: rgb(255,0,170);">delete</span> []uri;
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```

- 在ArkTS侧，通过URI打开文件，将文件句柄fd传递到C++侧，通过句柄访问文件。
```text
<span style="color: rgb(255,255,255);">photoViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">photoSelectOptions</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PhotoSelectResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">photoUris</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_ONLY</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'file fd: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readFileFromFd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`photoPicker failed, code is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
```text
<span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">ReadFileFromFd</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> argc <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(env, info, <span style="color: rgb(128,128,128);">&</span>argc, args, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(0,0,255);">int</span> fd;
    <span style="color: rgb(181,106,1);">napi_get_value_int32</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(128,128,128);">&</span>fd);
    <span style="color: rgb(0,0,255);">struct</span> <span style="color: rgb(0,0,255);">stat</span> <span style="color: rgb(0,0,255);">fileInfo</span>;
    <span style="color: rgb(255,0,170);">if</span> (<span style="color: rgb(181,106,1);">fstat</span>(fd, <span style="color: rgb(128,128,128);">&</span>fileInfo) <span style="color: rgb(128,128,128);">==</span> <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1</span>) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromFd failed"</span>);
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromFd: %{public}d"</span>, (<span style="color: rgb(0,0,255);">int</span>)<span style="color: rgb(0,0,255);">fileInfo</span>.<span style="color: rgb(0,0,255);">st_size</span>);
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```

- 文件URI可以通过在ArkTS侧获取文件path，传递到C++侧访问（媒体URI和应用目录不可用）。
```text
<span style="color: rgb(255,255,255);">documentViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">documentSelectOptions</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">documentSelectResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readFileFromUri</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">documentSelectResult</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">documentSelectResult</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_ONLY</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'file path: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readFileFromPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`filePicker failed, code is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
```text
<span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">ReadFileFromPath</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> argc <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">1</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(env, info, <span style="color: rgb(128,128,128);">&</span>argc, args, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(0,0,255);">size_t</span> length <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>;
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(128,128,128);">&</span>length);
    <span style="color: rgb(0,0,255);">char</span><span style="color: rgb(128,128,128);">*</span> path <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">char</span>[length <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>];
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], path, length <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span>length);
    <span style="color: rgb(0,0,255);">path</span>[length] <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">'</span><span style="color: rgb(181,106,1);">\0</span><span style="color: rgb(181,106,1);">'</span>;
    
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromPath: %{public}s"</span>, path);
    <span style="color: rgb(0,0,255);">int</span> fd <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">open</span>(path, O_RDONLY);
    <span style="color: rgb(0,0,255);">struct</span> <span style="color: rgb(0,0,255);">stat</span> <span style="color: rgb(0,0,255);">fileInfo</span>;
    <span style="color: rgb(255,0,170);">if</span> (<span style="color: rgb(181,106,1);">fstat</span>(fd, <span style="color: rgb(128,128,128);">&</span>fileInfo) <span style="color: rgb(128,128,128);">==</span> <span style="color: rgb(128,128,128);">-</span><span style="color: rgb(80,160,79);">1</span>) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromPath failed"</span>);
        <span style="color: rgb(255,0,170);">delete</span> []path;
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Native ReadFileFromPath: %{public}d"</span>, (<span style="color: rgb(0,0,255);">int</span>)<span style="color: rgb(0,0,255);">fileInfo</span>.<span style="color: rgb(0,0,255);">st_size</span>);
    <span style="color: rgb(181,106,1);">close</span>(fd);
    <span style="color: rgb(255,0,170);">delete</span> []path;
    <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
}
```


 
 

#### 常见FAQ

Q：应用[沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)文件如何在C++侧访问？
 
A：文件的沙箱路径，即文件在设备上的path，C++侧可通过文件操作接口访问。
 
Q：应用资源文件在C++侧如何访问？
 
A：需要访问的资源文件建议放在Rawfile目录，通过[Rawfile开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawfile-guidelines)提供的C++接口访问，或是将文件拷贝到沙箱目录，通过文件接口访问。
