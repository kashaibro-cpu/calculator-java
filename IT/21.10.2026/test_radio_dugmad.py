import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRadioDugmad(unittest.TestCase):
    def test_odabir_jednog_dugmeta_ponistava_prethodni_odabir(self):
        preglednik = webdriver.Chrome()
        self.addCleanup(preglednik.quit)
        preglednik.get("https://www.selenium.dev/selenium/web/web-form.html")

        dugmad = preglednik.find_elements(By.CSS_SELECTOR, 'form input[type="radio"]')
        self.assertEqual(len(dugmad), 2, "Forma treba imati dva radio dugmeta.")
        self.assertEqual(
            sum(dugme.is_selected() for dugme in dugmad),
            1,
            "Na početku treba biti odabrano tačno jedno radio dugme.",
        )

        prvo, drugo = dugmad
        # Prvo odaberi drugo dugme, a zatim se vrati na prvo.
        drugo.click()
        self.assertTrue(drugo.is_selected(), "Drugo dugme treba biti odabrano.")
        self.assertFalse(prvo.is_selected(), "Prvo dugme treba biti odselektovano.")

        prvo.click()
        self.assertTrue(prvo.is_selected(), "Prvo dugme treba biti odabrano.")
        self.assertFalse(drugo.is_selected(), "Drugo dugme treba biti odselektovano.")


if __name__ == "__main__":
    unittest.main()
