import os
from selene import browser, be, have, command

def test_fill_and_send():
    def test_fill_and_send():
        browser.open('/automation-practice-form')
        browser.should(have.title('DEMOQA'))
        browser.element('#firstName').type('Akhil')
        browser.element('#lastName').type('Nadar')
        browser.element('#userEmail').type('nadar@test.in')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').type('9112345678')
        # browser.element('#dateOfBirthInput').perform(command.select_all).type('31 Jul 1992').press_enter()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1992"]').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
        browser.element('.react-datepicker__day--031').click()
        browser.element('#subjectsInput').type('Maths').press_enter().type('Physics').press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
        browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/avatar.jpg'))
        browser.element('#currentAddress').type('14, Ashoka Rd, Sansad Marg Area')
        browser.element('#react-select-3-input').type('NCR').press_enter()
        browser.element('#react-select-4-input').type('Delhi').press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(
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
        )

