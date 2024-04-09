from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User


def test_fill_and_send():
    test_user = User(
        first_name='Akhil',
        last_name='Nadar',
        email='nadar@test.in',
        gender='Male',
        phone_number='9112345678',
        bd_month='July',
        bd_year='1992',
        bd_day='31',
        subjects='Maths, Physics',
        hobbies='Sports, Reading',
        photo='avatar.jpg',
        address='14, Ashoka Rd, Sansad Marg Area',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register_user(test_user)
    registration_page.should_registered_user_with(test_user)
