var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;

var Helper = function () {
    
    this.navigateToAdminPortal = function (driver) {
        driver.get('http://localhost/litecart/admin/');
    };
    
    this.adminLogin = function (driver) {
        driver.findElement(By.name('username')).sendKeys('admin');
        driver.findElement(By.name('password')).sendKeys('admin');
        driver.findElement(By.name('login')).click();
    };

    this.waitForElementToBeVisible = function (driver, locator) {
        driver.wait(until.elementIsVisible(driver.findElement(By.css(locator))), 1000);
    }
};

module.exports = new Helper();
