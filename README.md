# Description

Tired of fancy pagan witticisms? Display a daily verse of God's eternal Truth on your desktop!

This is a variety plugin. You need to install [variety](https://github.com/varietywalls/variety) first to make it work.

This simple script fetches content from [BibleGateway](https://www.biblegateway.com), and it is possible to use any version the site supports (I've only tested three).

# How to use

First download the script with the following command:

```bash
curl -o $HOME/.config/variety/plugins/verse.py https://raw.githubusercontent.com/Crissium/variety-daily-verse/master/verse.py
```

Then restart `variety` and go to Preferences > Quotes > Sources and Filtering, uncheck all checkboxes except, of course, "Bible Gateway's Verse of the Day". You could specify versions using the Tags or Authors fields, or leave them blank to use the default version (ESV). Only one _random_ version is displayed at a time.

The version codes are listed [here](https://www.biblegateway.com/versions/), e.g. "English Standard Version (ESV)" has the code 'ESV'.

![Settings](https://user-images.githubusercontent.com/19600707/242344017-3ab70f21-e5ce-46f5-8aa2-84faea15a3ea.png)

_NB: `variety` sets an upper limit of 250 on the length of the quote, and sometimes the daily verse exceeds this. If you see the message 'Could not find any quotes', you could try increasing the limit in `~/.config/variety/variety.conf` by setting `max_quote_length` to 4096 or something._

# 中文说明

这是一个 [variety](https://github.com/varietywalls/variety) 插件，可以在 Linux 桌面上显示下载自 Bible Gateway 的每日经文。

使用时，首先用以下命令下载脚本：

```bash
curl -o $HOME/.config/variety/plugins/verse.py https://raw.githubusercontent.com/Crissium/variety-daily-verse/master/verse.py
```

然后重启，并在设置中启用该插件（勾选 Bible Gateway's Verse of the Day，其他选项不用勾选）。

本脚本使用的默认版本为 ESV, 如需更改，请参见上图修改版本号，注意一次只能使用一种版本。Bible Gateway 上有如下中文圣经：

- 和合本：简体 CUVS, 正體 CUV
- 新标点和合本：简体 CUVMPS, 正體 CUVMPT
- 新译本：简体 CNVS, 正體 CNVT
- 和修本　神版：简体 RCU17SS, 正體 RCU17TS
- [当代译本](https://wd.bible/gen.1.ccbs)：简体 CCB, 正體 CCBT

**注意：`variety` 对 quotes 的长度做了限制，有时候经文会超过这个限制，导致无法显示。如果看到 “Could not find any quotes” 这样的提示，可以尝试在 `~/.config/variety/variety.conf` 中将 `max_quote_length` 的值改为 4096 或更大。**

# Screenshots

![ESV](screenshots/ESV.png)

![CUV](screenshots/CUV.png)
