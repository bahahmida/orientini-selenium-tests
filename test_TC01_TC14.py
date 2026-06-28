# test cases  TC01 to TC14 : Navigation and interaction with the website
from os import link
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
import random 
BASE_URL="https://www.orientini.com/accueil.php"
class TestOrientiniNavigation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Edge()
        cls.driver.get(BASE_URL)
        cls.wait = WebDriverWait(cls.driver, 10)
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
    def test_TC01_homepage_loading(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue('- أورينتيني - توجيه تونس' in self.driver.title)
    def test_TC02_navigation_menu(self):
        link_texts = ['آخر الأخبار','تشغيل','ملفات','إجابات','إعلانات','تسجيل الدخول','اختبار الشخصية','باك 2026','تكوين مهني','توجيه جامعي','إعادة التوجيه','+آفاق أخرى'] 
        for i in link_texts: 
            link = self.driver.find_element(By.LINK_TEXT, i)
            link.click()
            time.sleep(2)  
            self.assertIn(i, self.driver.find_element(By.TAG_NAME, 'body').text)
            self.driver.get(BASE_URL)
    def test_TC03_page_translation(self):
        translate_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français')))
        translate_button.click()
        time.sleep(2)
        self.assertIn('Orientation', self.driver.title)
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        arabic_keywords = ['آخر الأخبار', 'تسجيل الدخول', 'ملفات']
        for keyword in arabic_keywords:
            self.assertNotIn(
                keyword, body_text,
                f"Arabic keyword '{keyword}' still present after translation"
            )
    def test_TC04_navigation_to_notifications(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français'))).click()
        time.sleep(2)
        try:
            overlay_dismissers = [
                "//button[contains(text(), 'Accept')]",
                "//button[contains(text(), 'Close')]",
                "//button[contains(text(), 'OK')]",
                "//button[contains(text(), 'Got it')]",
                "//button[@class[contains(., 'close')]]",
                "//div[contains(@class,'modal')]//button",
                "//div[contains(@class,'popup')]//button",
            ]
            for xpath in overlay_dismissers:
                elements = self.driver.find_elements(By.XPATH, xpath)
                if elements:
                    elements[0].click()
                    time.sleep(1)
                    break
        except:
            pass
        notifications_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[.//i[contains(@class, 'fa-bell')]]"))
        )
        notifications_link.click()
        time.sleep(10)

        try:
            notif_link = self.wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Notifications'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", notif_link)
            self.driver.execute_script("arguments[0].click();", notif_link)
        except:
            pass

        time.sleep(2)
        self.assertIn('Notifications', self.driver.title)
    def test_TC05_navigation_to_messages(self): 
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français'))).click()
        time.sleep(2)
        messages_link = self.driver.find_element(By.XPATH, "//a[.//i[contains(@class, 'fa-comment')]]")
        messages_link.click()
        time.sleep(2)  
        self.assertIn('Consulting', self.driver.title)  
    def test_TC06_navigation_with_sidebar(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français'))).click()
        time.sleep(2)
        sidebar_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a.btn-special")
        button_data = [
            {
                'href': button.get_attribute('href'),
                'class': button.get_attribute('class')
            }
            for button in sidebar_buttons
        ]

        for data in button_data:
            href = data['href']
            cls = data['class']

            if not href:
                print(f"Skipping button with class '{cls}' — no href found")
                continue
            try:
                self.driver.get(href)
                time.sleep(2)
                print(f"Navigated to: {href} (class: {cls})")
                body_text = self.driver.find_element(By.TAG_NAME, 'body').text
                self.assertTrue(len(body_text) > 0, f"Page body is empty for {href}")
                self.driver.back()
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-special")))
                time.sleep(1)

            except Exception as e:
                print(f"Error navigating to {href}: {e}")
                self.driver.back()
                time.sleep(2)
    def test_TC07_display_mobile_mode(self):
        self.driver.set_window_size(375, 667)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'FR'))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-target='.menu_mobile']"))).click()
        time.sleep(2)

        mobile_links = [(a.get_attribute('href'), a.text.strip()) for a in self.driver.find_elements(By.CSS_SELECTOR, ".menu_mobile a") if a.text.strip()]

        broken_links = [text for href, text in mobile_links if not href]
        working_links = [(href, text) for href, text in mobile_links if href]

        for text in broken_links:
            print(f"BROKEN LINK (no href): '{text}'")
        for href, text in working_links:
            print(f"Working link: '{text}' → {href}")

        self.assertEqual(len(broken_links), 0, f"Found {len(broken_links)} broken links with no href: {broken_links}")

        self.assertTrue(len(working_links) > 0, "No navigable links found in mobile menu")
        href, text = random.choice(working_links)
        print(f"\nRandomly selected: '{text}' → {href}")

        self.driver.get(href)
        time.sleep(2)

        self.assertTrue(len(self.driver.find_element(By.TAG_NAME, 'body').text) > 0, "Page body is empty after navigation")
        print(f"✓ Successfully navigated to '{text}'")
    def test_TC08_pages_loading(self):
        loading_times = []
        link_texts = ['آخر الأخبار','تشغيل','ملفات','إجابات','إعلانات','تسجيل الدخول','اختبار الشخصية','باك 2026','تكوين مهني','توجيه جامعي','إعادة التوجيه','+آفاق أخرى'] 
        for i in link_texts : 
            start=time.time()
            link = self.driver.find_element(By.LINK_TEXT, i)
            link.click()
            end=time.time()
            print(f"Time taken to load {i}: {end-start} seconds")
            loading_times.append(end-start)
            time.sleep(2)  
            self.driver.get(BASE_URL)
            self.assertLess(end-start, 5)
        print(f"Average loading time: {sum(loading_times)/len(loading_times)} seconds")
    def test_TC09_categories_section(self):
        category_section = self.driver.find_element(By.ID, 'category_18247691351534339909')
        link_data = [(a.get_attribute('href'), a.text.strip()) for a in category_section.find_elements(By.CSS_SELECTOR, ".content a") if a.get_attribute('href') and a.text.strip()]
        self.assertTrue(len(link_data) > 0, "No links found in categories section")
        for href, text in link_data:
            self.driver.get(href)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            self.assertTrue(len(self.driver.find_element(By.TAG_NAME, 'body').text) > 0, f"Empty page for: '{text}' → {href}")
            print(f"✓ '{text}' → {href}")
            self.driver.back()
            self.wait.until(EC.presence_of_element_located((By.ID, 'category_18247691351534339909')))
    def test_TC10_open_and_close_publicity(self):
        publicity_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'login_pub')]")))
        self.driver.execute_script("arguments[0].click();", publicity_link)
        time.sleep(3)

        modal = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".myAnnonce.in .modal-content")))
        self.assertTrue(modal.is_displayed(), "Modal did not open")
        try:
            self.driver.execute_script("arguments[0].remove();", self.driver.find_element(By.CSS_SELECTOR, "iframe[title='Advertisement']"))
        except:
            pass

        close_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'myAnnonce')]//a[contains(@onclick, 'annuler_login_pub')]")))
        self.driver.execute_script("arguments[0].click();", close_link)
        time.sleep(2)
        self.assertIn(self.driver.current_url, ["https://www.orientini.com/accueil.php", "https://www.orientini.com/"], "Did not return to main page after closing modal")
    def test_TC11_news_section(self):
        news_section = self.wait.until(EC.presence_of_element_located((By.ID, 'sj_k2_slider_21275211751534339909')))
        item_data = []
        for item in news_section.find_elements(By.CSS_SELECTOR, '.item'):
            try:
                title = item.find_element(By.CSS_SELECTOR, '.item-title a').text.strip()
                href = item.find_element(By.CSS_SELECTOR, '.item-title a').get_attribute('href')
                all_links = item.find_elements(By.TAG_NAME, 'a')
                print(f"\nItem: '{title}'")
                for a in all_links:
                    print(f"  a href='{a.get_attribute('href')}' | onclick='{a.get_attribute('onclick')}' | class='{a.get_attribute('class')}'")
                if title and href:
                    item_data.append({'title': title, 'view_href': href})
            except Exception as e:
                print(f"Skipping item: {e}")

        self.assertTrue(len(item_data) > 0, "No news items found")
        print(f"\nFound {len(item_data)} news items")

        for data in item_data:
            self.driver.get(data['view_href'])
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(2)
            self.assertTrue(len(self.driver.find_element(By.TAG_NAME, 'body').text) > 0, f"Empty page for: '{data['title']}'")
            print(f"✓ '{data['title']}' → {self.driver.current_url}")
            self.driver.back()
            self.wait.until(EC.presence_of_element_located((By.ID, 'sj_k2_slider_21275211751534339909')))
            time.sleep(1)
    def test_TC12_partners_space(self):
        main_url = self.driver.current_url
        partner_links = self.driver.execute_script("return Array.from(document.querySelectorAll(\"a[href*='/e/']\")).map(a => ({href: a.href, text: a.innerText.trim()})).filter(a => a.text)")

        self.assertTrue(len(partner_links) > 0, "No partner links found")
        print(f"\nFound {len(partner_links)} partners")

        for partner in partner_links:
            self.driver.get(main_url)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(1)
            link = self.driver.find_element(By.CSS_SELECTOR, f"a[href='{partner['href']}']")
            self.driver.execute_script("arguments[0].click();", link)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(2)
            body_text = self.driver.find_element(By.TAG_NAME, 'body').text
            self.assertTrue(len(body_text) > 0, f"Empty page for: '{partner['text']}'")
            self.assertIn(partner['text'], body_text, f"Partner name '{partner['text']}' not found on their page")
            print(f"'{partner['text']}' → {self.driver.current_url}")
    def test_TC13_view_important_dates(self):
        translate_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français')))
        translate_button.click()
        time.sleep(2)
        important_dates_link = self.driver.find_element(By.LINK_TEXT, 'Dates importantes')
        important_dates_link.click()
        time.sleep(2)  
        self.assertIn('Calendrier', self.driver.title) 
        self.driver.back()
    def test_TC14_view_socials(self):
        domain_aliases = {'twitter.com': 'x.com', 'plus.google.com': 'googleblog.com'}
        social_data = self.driver.execute_script("return Array.from(document.querySelectorAll('.yt-socialbt a')).map(a => ({href: a.href})).filter(a => a.href)")
        self.assertTrue(len(social_data) > 0, "No social media links found")
        for i, social in enumerate(social_data):
            self.driver.execute_script(f"document.querySelectorAll('.yt-socialbt a')[{i}].click();")
            time.sleep(2)
            original_domain = social['href'].split('/')[2].replace('www.', '')
            expected = domain_aliases.get(original_domain, original_domain)
            if len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(2)
            self.assertIn(expected, self.driver.current_url, f"Expected '{expected}' but got: '{self.driver.current_url}'")
            print(f"'{original_domain}' → {self.driver.current_url}")
            if len(self.driver.window_handles) > 1:
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.driver.back()
            time.sleep(1)
if __name__ == '__main__':
    test_cases = [
        ("test_TC01_homepage_loading",          "Functional", "Homepage Loading"),
        ("test_TC02_navigation_menu",           "Functional", "Navigation Menu"),
        ("test_TC03_page_translation",          "Functional", "Page Translation"),
        ("test_TC04_navigation_to_notifications","Functional", "Navigation to Notifications"),
        ("test_TC05_navigation_to_messages",    "Functional", "Navigation to Messages"),
        ("test_TC06_navigation_with_sidebar",   "Functional", "Navigation with Sidebar"),
        ("test_TC07_display_mobile_mode",       "UI",         "Mobile Mode Display"),
        ("test_TC08_pages_loading",             "Performance","Pages Loading Time"),
        ("test_TC09_categories_section",        "Functional", "Categories Section"),
        ("test_TC10_open_and_close_publicity",  "Functional", "Open and Close Publicity"),
        ("test_TC11_news_section",              "Functional", "News Section"),
        ("test_TC12_partners_space",            "Functional", "Partners Space"),
        ("test_TC13_view_important_dates",      "Functional", "View Important Dates"),
        ("test_TC14_view_socials",              "Functional", "View Socials"),
    ]

    suite = unittest.TestSuite()
    for test_id, _, _ in test_cases:
        suite.addTest(TestOrientiniNavigation(test_id))

    import io
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    passed = [t[0].id().split('.')[-1] for t in result.errors + result.failures]
    bugs = len(result.errors) + len(result.failures)

    print("\n" + "="*70)
    print(f"{'TEST SUMMARY':^70}")
    print("="*70)
    print(f"{'#':<5} {'Test Name':<40} {'Type':<15} {'Result':<10}")
    print("-"*70)
    for i, (test_id, test_type, test_name) in enumerate(test_cases, 1):
        status = " ? FAIL" if test_id in passed else "OK  PASS"
        print(f"{i:<5} {test_name:<40} {test_type:<15} {status:<10}")
    print("="*70)
    print(f"Total Tests : {len(test_cases)}")
    print(f"Passed      : {len(test_cases) - bugs}")
    print(f"Failed      : {bugs}")
    print(f"Bugs Found  : {bugs}")
    print("="*70)

    if result.failures:
        print("\nFAILURES:")
        for test, msg in result.failures:
            print(f"  {test.id().split('.')[-1]}: {msg.splitlines()[-1]}")
    if result.errors:
        print("\nERRORS:")
        for test, msg in result.errors:
            print(f"  {test.id().split('.')[-1]}: {msg.splitlines()[-1]}")           