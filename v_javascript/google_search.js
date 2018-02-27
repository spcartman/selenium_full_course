var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    // firefox = require('selenium-webdriver/firefox'),
    // safari = require('selenium-webdriver/safari'),
    By = webdriver.By,
    until = webdriver.until,
    test = require('selenium-webdriver/testing');

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
        driver.get('http://localhost/litecart/admin/');
        driver.findElement(By.name('username')).sendKeys('admin');
        driver.findElement(By.name('password')).sendKeys('admin');
        driver.findElement(By.name('login')).click();
        driver.wait(until.elementIsVisible(driver.findElement(By.css('#box-apps-menu-wrapper'))), 1000);
    });

    test.after(function() {
        driver.quit();
    });
});
