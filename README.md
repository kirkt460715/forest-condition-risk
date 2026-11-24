# 森林质量监测资料

本项目整理遥感观测、林分调查、巡护记录和核查安排，供森林质量监测人员复核观测变化及现场核查情况。

## 资料

`data/manifest.json` 记录本地合成数据的字段。影像摘要保留设备与观测期，现场调查和保护巡护分别记录。

字段含义及有效期约定见[资料口径](资料口径.md)。

## 本地检查

使用 Python 3.11 或更新版本，无需安装第三方依赖。

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```
