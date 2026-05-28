# Assets 图片保存与引用规范

> 提取自 [[华为文档HTML转Markdown整理方法论]]，作为图片处理的独立参考规范。

---

## 一、目录结构

每个项目/文档的图片存放在独立的 `assets/` 子目录中：

```text
项目名/
  项目名.md
  assets/
    项目名/
      file-20260525143000123.png
      file-20260525143000456.gif
```

- assets 子目录名必须与 markdown 文件名一致
- 不允许文件名是中文而附件目录用英文 slug

## 二、图片命名

图片文件统一使用时间戳命名：

```
file-${YYYYMMDDHHmmssSSS}.{ext}
```

示例：`file-20260414091711168.png`

## 三、Markdown 引用格式

### 基本引用

```md
![](assets/项目名/file-20260525143000123.png)
```

### 引用规则

1. **必须使用本地路径**，不允许使用远程 URL（官网图片链接含临时签名，会过期）
2. **路径相对于 markdown 文件所在目录**，使用 `./assets/` 前缀
3. **图片引用必须独立成行**，不能与正文文本挤在同一行

错误：
```md
![](assets/doc/file.png)     **说明：** 正文内容...
```

正确：
```md
![](assets/doc/file.png)

**说明：** 正文内容...
```

4. **路径中的空格必须 URL 编码为 `%20`**

错误：
```md
![](assets/ohos.app.ServiceExtension/file-xxx.png)
```

正确：
```md
![](assets/ohos.app.ServiceExtension%20应用/file-xxx.png)
```

## 四、表格中的图片

表格单元格内的图片同样使用 `![]()` 格式：

```md
| 场景一 | 场景二 |
|--------|--------|
| ![](./assets/project/device/scene1.png) | ![](./assets/project/device/scene2.png) |
```

- 禁止在 markdown 中使用 HTML `<img>` 标签
- 每个图片引用独立占据单元格内容

## 五、图片获取流程

1. 从原始来源（网页/仓库）获取有效图片 URL
2. 下载图片到本地 `assets/{项目名}/` 目录
3. 按 `file-{时间戳}.{ext}` 格式重命名
4. 在 markdown 中按上述规则引用本地路径

## 六、检查清单

- [ ] 图片是否已本地化（无远程 URL）
- [ ] 图片路径是否使用 `./assets/` 相对路径
- [ ] 附件目录名是否与 markdown 文件名一致
- [ ] 图片引用是否独立成行（无同行文本）
- [ ] 路径中的空格是否编码为 `%20`
- [ ] 是否残留 HTML `<img>` 标签（应全部替换为 `![]()`）
