# Description

Tired of fancy pagan witticisms? Display a daily verse of God's eternal Truth on your desktop!

This is a variety plugin. You need to install [variety](https://github.com/varietywalls/variety) first to make it work.

This simple script fetches content from [BibleGateway](https://www.biblegateway.com), and it is possible to use any version the site supports (I've only tested three).

# How to use

Download the `verse.py` script and replace `version` with your preferred one. (Look up version codes [here](https://www.biblegateway.com/versions/), for example, the site lists "English Standard Version (ESV)", so the version code would be `ESV`.) Then copy the script to `$HOME/.config/variety/plugins/`. Restart `variety` and go to Preferences > Effects > Quotes > Sources and Filtering, uncheck all checkboxes except, of course, "Bible Gateway's Verse of the Day". Remove all tags and authors. Now it should work perfectly!

# 中文说明

这是一个 [variety](https://github.com/varietywalls/variety) 插件，可以在 Linux 桌面上显示下载自 Bible Gateway 的每日经文。

使用时，首先下载 `verse.py`，放到 `$HOME/.config/variety/plugins/` 目录下，然后重启 variety 并在设置中启用该插件，并禁用其他 Quotes 插件。

本脚本使用的默认版本为 ESV, 如需更改，将脚本中的 version 改为对应代码即可：

- 和合本：简体 CUVS, 正體 CUV
- 新标点和合本：简体 CUVMPS, 正體 CUVMPT
- 新译本：简体 CNVS, 正體 CNVT
- 和修本　神版：简体 RCU17SS, 正體 RCU17TS

# Screenshots

![ESV](screenshots/ESV.png)

![CUV](screenshots/CUV.png)
