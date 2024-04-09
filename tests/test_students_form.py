import os
from selene import browser, be, have, command

from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_fill_and_send():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.should_open_page_with_title('DEMOQA')

    registration_page.fill_first_name('Akhil')

    registration_page.fill_last_name('Nadar')

    registration_page.fill_email('nadar@test.in')

    registration_page.choose_gender('Male')

    registration_page.fill_phone_number('9112345678')

    registration_page.fill_birthday('1992', 'July', '31')

    registration_page.fill_subjects('Maths', 'Physics')

    registration_page.choose_hobbies('Sports', 'Reading')

    registration_page.fill_photo('avatar.jpg')

    registration_page.fill_address('14, Ashoka Rd, Sansad Marg Area')

    registration_page.fill_state('NCR')

    registration_page.fill_city('Delhi')

    registration_page.submit()

    registration_page.should_open_form_with_text('Thanks for submitting the form')

    registration_page.should_registered_user_with(
        'Akhil Nadar',
        'nadar@test.in',
        'Male',
        '9112345678',
        '31 July,1992',
        'Maths, Physics',
        'Sports, Reading',
        'avatar.jpg',
        '14, Ashoka Rd, Sansad Marg Area',
        'NCR Delhi'
    )

