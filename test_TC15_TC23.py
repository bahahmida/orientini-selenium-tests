# Test cases TC15 to TC23: Search + Calculate orientation + Specefic search  
from os import link
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import  ElementClickInterceptedException, NoAlertPresentException
import time 
import random 
BASE_URL="https://www.orientini.com/accueil.php"
class TestOrientini(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Edge()
        cls.driver.get(BASE_URL)
        cls.wait = WebDriverWait(cls.driver, 10)
    @classmethod
    def tearDown(cls):
        cls.driver.quit()        
    def test_TC15_search_functionality(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français'))).click()
        time.sleep(2)
        
        search_input = self.driver.find_element(By.ID, 'searchinput')
        search_term = 'orientation'
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Search results page is empty")
        self.assertIn(search_term.lower(), body_text.lower() or '', f"Search term '{search_term}' not found in results")
    
    def test_TC16_sign_up_functionality(self):
        self.driver.find_element(By.LINK_TEXT, "Français").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='yt_sticky_right']/div/div[2]/a").click()
        time.sleep(3) 
        dismiss=self.driver.find_elements(By.ID, "dismiss-button-element")
        if dismiss:
            try:
                dismiss[0].click()
                time.sleep(2)
            except (ElementClickInterceptedException, NoAlertPresentException):
                pass
        self.driver.find_element(By.LINK_TEXT, "S'inscrire").click()
        time.sleep(3)
        
        
            
        body = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
        self.assertTrue(len(body) > 0)

        email_fields = self.driver.find_elements(By.NAME, "email")
        self.assertTrue(len(email_fields) > 0 or "email" in body.lower())


    def test_TC17_sign_in_functionality(self):
        self.driver.find_element(By.LINK_TEXT, "Français").click()
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Se connecter").click()
        time.sleep(3)

        body = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
        self.assertTrue(len(body) > 0)

        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))

        username.send_keys("testuser")
        password.send_keys("testpassword")

        self.driver.find_element(By.CSS_SELECTOR, "input.submit-btn[type='submit']").click()

        self.assertNotIn("error_login", self.driver.page_source)
    def test_TC18_calculate_orientation_functionality(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Français'))).click()
        time.sleep(2)

        calculate_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='Calcul_Score']")))
        self.driver.execute_script("arguments[0].click();", calculate_link)
        time.sleep(3)

        self.assertIn('sms', self.driver.current_url.lower(), "Not redirected to score calculation page")
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.ID, 'udata'))).is_displayed(), "Form not displayed")

        gouv_select = self.wait.until(EC.presence_of_element_located((By.ID, 'gouv')))
        self.driver.execute_script("arguments[0].value = '11';", gouv_select)

        self.driver.execute_script("document.querySelector('input[name=\"sexe\"][value=\"0\"]').click();")

        sms_field = self.driver.find_element(By.ID, 'sms')
        sms_field.clear()
        sms_field.send_keys("Moye=14.18 Math=13.5 ScPh=12.75 ScVT=11.75 Angl=15 Fran=13.75 Arab=14.62 Phil=7 Info=18.37 EdPh=18.08 Alle=19.25")

        filieres = self.driver.find_elements(By.ID, 'filieres')
        visible_filieres = [f for f in filieres if f.is_displayed()]
        if visible_filieres:
            visible_filieres[0].clear()
            visible_filieres[0].send_keys("523")

        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input.submit-btn[type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(3)

        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Results page is empty")
        self.assertTrue(
            any(kw in body_text for kw in ['523', 'إعلامية', 'Informatique', 'score', 'مجموع', 'résultat']),
            f"Expected results not found on page. URL: {self.driver.current_url}"
        )
        print(f" Form submitted successfully → {self.driver.current_url}")
    def test_TC19_job_offers_search(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'goalBoxes')))
        
        job_search_input = self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='searchText1']")
        search_term = 'ingénieur'
        job_search_input.send_keys(search_term)
        time.sleep(2)
        
        job_search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Job search results page is empty")
        
    
    def test_TC20_vocational_training_search(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'goalBoxes')))
        
        training_search_input = self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='searchText2']")
        search_term = 'informatique'
        training_search_input.send_keys(search_term)
        time.sleep(2)
        
        training_search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Vocational training search results page is empty")
        
    
    def test_TC21_university_branches_search(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'goalBoxes')))
        
        university_search_input = self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='searchText3']")
        search_term = 'informatique'
        university_search_input.send_keys(search_term)
        time.sleep(2)
        
        university_search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "University branches search results page is empty")
        
    
    def test_TC22_scholarships_search(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'goalBoxes')))
        
        scholarship_search_input = self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='searchText4']")
        search_term = 'france'
        scholarship_search_input.send_keys(search_term)
        time.sleep(2)
        
        scholarship_search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Scholarships search results page is empty")
        
    
    def test_TC23_important_dates_section(self):
        important_dates_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Orientation_Tunisie_Evenements')]"))
        )
        important_dates_button.click()
        time.sleep(3)
        
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertTrue(len(body_text) > 0, "Important dates page is empty")
        
if __name__ == '__main__':
    test_cases = [
        ("test_TC15_search_functionality",            "Functional", "Search Functionality"),
        ("test_TC16_sign_up_functionality",           "Functional", "Sign In Functionality"),
        ("test_TC17_sign_in_functionality",           "Functional", "Sign Up Functionality"),
        ("test_TC18_calculate_orientation_functionality", "Functional", "Calculate Orientation"),
        ("test_TC19_job_offers_search",               "Functional", "Job Offers Search"),
        ("test_TC20_vocational_training_search",     "Functional", "Vocational Training Search"),
        ("test_TC21_university_branches_search",      "Functional", "University Branches Search"),
        ("test_TC22_scholarships_search",              "Functional", "Scholarships Search"),
        ("test_TC23_important_dates_section",          "Functional", "Important Dates Section"),
    ]

    suite = unittest.TestSuite()
    for test_id, _, _ in test_cases:
        suite.addTest(TestOrientini(test_id))

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