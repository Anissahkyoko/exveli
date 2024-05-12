def info_panel_closer(driver):
    """Closes the info panel in the bottom right corner.

    Args:
        driver: WebDriver object representing the web browser.
    """

    try:
        # Click on the close button.
        close_button = driver.find_element_by_css_selector(
            ".info-panel-close-button"
        )
        close_button.click()
    except NoSuchElementException:
        # The info panel is already closed. Do nothing.
        pass

