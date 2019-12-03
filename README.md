
# 五笔的设计与英文键盘无关

五笔的设计思路，是将汉字的「五种笔划」（横，竖，撇，捺，折）归为「五个区」。它的布局方式，与键面字符「叫什么名称」毫无关系。

但是普通五笔码表的「编码」是基于「QWERTY」的键名映射，只需将「键名映射」改一改，那五笔就可以契合与任意一种英文键盘布局。

# 映射关系

这个脚本 [映射数据.py](https://github.com/98wb/qwerty2other/blob/master/%E6%98%A0%E5%B0%84%E6%95%B0%E6%8D%AE.py) 可以建立「QWERTY」与其它键面布局的键名对应关系：

QWERTY 是 [示例数据](https://github.com/98wb/qwerty2other/blob/master/base/MAPPING.txt) 的「第一列」，Dvorak 是 [示例数据](https://github.com/98wb/qwerty2other/blob/master/base/MAPPING.txt) 的「第二列」。

运行该脚本之前，需要在 [示例数据](https://github.com/98wb/qwerty2other/blob/master/base/MAPPING.txt) 中改好你自己的映射。

```````
python3 映射数据.py
```````

# 准备码表正文

在 [fcitx-rime](https://github.com/98wb/fcitx-rime) 这个存档中，有 [wubi98_U.dict.yaml](https://github.com/98wb/fcitx-rime/blob/master/wubi98_U.dict.yaml) 和 [wubi98_ci.dict.yaml](https://github.com/98wb/fcitx-rime/blob/master/wubi98_ci.dict.yaml) ，以及 [py.dict.yaml](https://github.com/98wb/fcitx-rime/blob/master/py.dict.yaml)  三份码表文件。

至于哪些是码表正文，如何取出码表正文，在 [qwerty2other](https://github.com/98wb/qwerty2other) 下，有 wubi98_ci.txt， wubi98_U.txt, py.txt 三份文本样版，对比着取出类似的「正文」即可。

注意一点，「 py.txt 」其实没有必要一并转码，假如你能适应新模式下的「拼音」编码布局。转了之后，将保持「QWERTY」键位下的拼音映射关系，这个看个人需求了。


``````
python3 新表生成.py
``````

# 取出 YAML 新表

脚本会直接合成新的 YAML 表，它们在 [new-tables](https://github.com/98wb/qwerty2other/tree/master/new-tables) 下面。

# 替换旧数据

目标文档是 [fcitx-rime](https://github.com/98wb/fcitx-rime) 这个存档。诚如所见，它的根目录下，有 wubi98_ci.dict.yaml 与 wubi98_U.dict.yaml 两份「RIME 码表」。你用新生成的 YAML 表替换掉旧的。

然后到它的 「linux」 子文件夹下，去执行 「rime.sh」 脚本。但是要注意，「rime.sh」是按照 Debian 系的「apt install」写的。要改为你的「发行版」它所认可的「安装命令」，安装 rime 的必要组件 opencc 和 fcitx-rime，脚本执行要以「普通用户」进行，直到它要求 sudo 权限时再给它。

因为不同的发行版对环境变量设计不同，如果直接以 sudo 运行，在有些发行版中，会把输入法装给超级管理员。

``````
sh rime.sh
``````

# 要点回顾

- 填写「qwerty2other/base/MAPPING.txt」，生成「映射数据」，作为码表转换的依据
- 取码表正文放到「qwerty2other」根目录下面，名称要与模版进行替换，以防意外发生
- 生成新的 YAML 表在「qwerty2other/new-tables」中，取出，替换掉「fcitx-rime」包中的旧表
- 在「fcitx-rime」包下的「linux」目录中，将「rime.sh」改为适合你发行版的 install 命令，然后以普通用户权限执行
- 重启计算机，在设置，区域与语言中添加「RIME」。


# 超集字体支持

建议以 [98wubi-unicode](https://github.com/yanhuacuo/98wubi-unicode) 发布的字体为准。
