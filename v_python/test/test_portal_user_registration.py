from data.user_generator import generate_user


def test_portal_user_registration(app):
    app.navigation.go_to_shop_root()
    app.session.user_smart_logout()  # logout in case some user is logged in
    user = generate_user()
    app.shop.create_user(user)
    app.session.user_logout()
    app.session.user_login(user)
    assert app.session.is_correct_user_logged_in(user)
    app.session.user_logout()
