var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    // firefox = require('selenium-webdriver/firefox'),
    // safari = require('selenium-webdriver/safari'),
    test = require('selenium-webdriver/testing'),
    helper = require('./helpers.js');

test.describe('LiteCart Admin Login', function() {
    var driver;

    test.before(function() {
        var options = new chrome.Options();
        options.addArguments(["start-fullscreen"]);
        // var ff_options = new firefox.Options().setBinary('/Applications/FirefoxNightly.app/Contents/MacOS/firefox');

        driver = new webdriver.Builder()
            .forBrowser('chrome')
            .setChromeOptions(options)
            // .forBrowser('firefox')
            // .setFirefoxOptions(ff_options)
            // .forBrowser('safari')
            .build();
        driver.getCapabilities().then(function(caps) {
            console.log(caps);
        });
    });

    test.it('should login with valid credentials', function() {
        helper.navigateToAdminPortal(driver);
        helper.adminLogin(driver);
        helper.waitForElementToBeVisible(driver, '#box-apps-menu-wrapper');
    });

    test.after(function() {
        driver.quit();
    });
});
