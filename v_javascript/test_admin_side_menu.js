var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    By = webdriver.By,
    until = webdriver.until,
    test = require('selenium-webdriver/testing'),
    helper = require('./helpers.js');

test.describe('Click Through Side Menu', function() {
    var driver;

    test.before(function() {
        var options = new chrome.Options();
        options.addArguments(["start-fullscreen"]);

        driver = new webdriver.Builder()
            .forBrowser('chrome')
            .setChromeOptions(options)
            .build();
    });

    test.it('should click each menu and submenu', function() {
        helper.navigateToAdminPortal(driver);
        helper.adminLogin(driver);
        helper.waitForElementToBeVisible(driver, '#box-apps-menu-wrapper');

        for (i = 0; i < driver.findElements(By.css('li#app-')).length; i++) {
            driver.findElements(By.css('li#app-'))[i].click();
            helper.waitForElementToBeVisible(driver, 'h1');
            for (j = 0; j < driver.findElements(By.css('li[id^=doc]')).length; j++) {
                driver.findElements(By.css('li[id^=doc]'))[j].click();
                helper.waitForElementToBeVisible(driver, 'h1');
            }
        }
    });

    test.after(function() {
        driver.quit();
    });
});
