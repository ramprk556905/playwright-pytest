from playwright.sync_api import Page, expect
import time

def test_uichecks(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role('button',name='hide').click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()

    page.on('dialog',lambda dialog:dialog.accept())
    page.get_by_role('button', name='Confirm').click()
    time.sleep(4)


    #framehandling
    pageframe=page.frame_locator('#courses-iframe')
    pageframe.get_by_role('link',name='All Access plan').click()
    expect(pageframe.locator('body')).to_contain_text('Happy Subscibers')

    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    for index in range(page.locator('th').count()):
         if page.locator('th').nth('index').filter(has_text='Price').count()>0:
              column_value=index
              print(f'Price column value is {column_value}')
              break
         
    
         
    
              

