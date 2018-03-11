class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def go_to(self, url):
        if not self.app.wd.current_url == url:
            self.app.wd.get(url)

    def go_to_admin_root(self):
        self.go_to(self.app.admin_root)

    def go_to_admin_countries(self):
        self.go_to(self.app.admin_root + self.app.admin_countries_url)

    def go_to_admin_zones(self):
        self.go_to(self.app.admin_root + self.app.admin_zones_url)

    def go_to_shop_root(self):
        self.go_to(self.app.shop_root)

    def go_to_catalog(self):
        self.go_to(self.app.admin_root + self.app.admin_catalog_url)
