def get_element(path, driver):
    return driver.find_element_by_css_selector(path)


def get_elements(className, driver):
    return driver.find_elements_by_class_name(className)


