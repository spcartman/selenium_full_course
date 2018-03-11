class User:

    def __init__(self, f_name, l_name, address, postcode, city, country, email, phone, password):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.postcode = postcode
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '%s:%s:%s' % (self.email, self.f_name, self.l_name)
