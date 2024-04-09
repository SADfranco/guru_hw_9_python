import pytest
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User


@pytest.fixture
def test_user():
    return User(
        first_name='Akhil',
        last_name='Nadar',
        email='nadar@test.in',
        gender='Male',
        phone_number='9112345678',
        bdmonth='July',
        bdyear='1992',
        bdday='31',
        subjects='Maths, Physics',
        hobbies='Sports',
        photo='avatar.jpg',
        address='14, Ashoka Rd, Sansad Marg Area',
        state='NCR',
        city='Delhi'
                )


def test_fill_and_send(test_user):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.register_user(test_user)

    registration_page.should_registered_user_with(test_user)
