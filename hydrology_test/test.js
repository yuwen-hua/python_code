// npm install chromedriver --chromedriver_cdnurl=http: // cdn.npm.taobao.org /dist/ chromedriver
// npm install selenium-webdriver --save

require('chromedriver');

const { Builder } = require('selenium-webdriver');

const driver = new Builder().forBrowser('chrome').build();

driver.get("http://localhost:3000/#/");
driver.findElement({name:"username"}).sendKeys("你好");
driver.findElement({name:"password"}).sendKeys("你好");
setTimeout(() => {
    driver.quit()
},3000)
