from selenium import webdriver
import time


#driver = webdriver.Chrome(executable_path, port, options, service_args, desired_capabilities, service_log_path, chrome_options, keep_alive)hrome();
#driver = webdriver.Ie(executable_path, capabilities, port, timeout, host, log_level, service_log_path, options, ie_options, desired_capabilities, log_file, keep_alive)e();
#driver = webdriver.chrom();

print("Hello World")

driver = webdriver.Chrome("D:\Python\Testing\SeleniumFramework\Drivers\chromedriver.exe")
#driver = webdriver.Ie("..\Drivers\IEDriverServer.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step raghav")
time.sleep(5)
driver.find_element_by_name("btnK").click()
driver.maximize_window()
time.sleep(5)

driver.close()