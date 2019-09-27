# appium-douyin

crawl douyin with appium & mitmproxy

## 依赖安装

appium 安装

```bash
npm install -g appium
```

iOS 环境依赖

```bash
brew install carthage
```

### 参考

- [Appium Getting Started](https://github.com/appium/appium/blob/master/docs/en/about-appium/getting-started.md)
- [The XCUITest Driver for iOS](https://github.com/appium/appium/blob/master/docs/en/drivers/ios-xcuitest.md)
- [Appium XCUITest Driver Real Device Setup](https://github.com/appium/appium/blob/master/docs/en/drivers/ios-xcuitest-real-devices.md)

## mitmproxy

### 安装和信任证书

- https://docs.mitmproxy.org/stable/concepts-certificates/


### mitmproxy 启动

```bash
make run
```

### 真机需要设置的环境变量

```bash
export udid=xxxxx; xcodeOrgId=xxxxx
```

- [Basic (automatic) configuration](https://github.com/appium/appium/blob/master/docs/en/drivers/ios-xcuitest-real-devices.md#basic-automatic-configuration)


## 查看爬取到的数据

http://127.0.0.1:8081/

## FAQ

- 首页慢或者卡死可能的原因: https://github.com/alibaba/macaca/issues/755
