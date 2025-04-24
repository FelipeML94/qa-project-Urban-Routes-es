from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import utilidades
import data

class UrbanRoutesPage:
    # Selectores agrupados por método
    # Métodos: set_from, get_from
    from_field = (By.ID, 'from')
    # Métodos: set_to, get_to
    to_field = (By.ID, 'to')
    # Método: select_taxi_button
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    # Método: select_comfort_rate
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    # Método: select_number_button
    select_phone_insert = (By.CLASS_NAME, 'np-text')
    # Método: get_phone
    phone_input = (By.ID, 'phone')
    # Método: add_phone_number
    number = (By.XPATH, '//*[@id="phone"]')
    # Método: the_next_button
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    # Método: code_click, code_number, get_code
    click_code = (By.ID, 'code_input')
    code = (By.ID, 'code')
    # Método: send_cell_info
    cell_next = (By.XPATH, '//*[text()="Confirmar"]')
    # Método: pay_click
    payment_method = (By.CLASS_NAME, "pp-button")
    # Método: add_click
    card_add_button = (By.CLASS_NAME, "pp-plus")
    # Método: number_click
    credit_click = (By.CLASS_NAME, 'card-number-input')
    # Métodos: number_input, get_card_input
    add_credit_card = (By.XPATH, '//*[@id="number"]')
    # Métodos: cvv_add, code_card_input, get_cvv_card
    card_cvv = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    # Método: registered_card
    confirm_agree_card = (By.XPATH, "//div[@class='pp-buttons']//button[@type='submit']")
    # Método: close_window
    x_button = (By.XPATH,"//div[@class='payment-picker open']//div[@class='modal']//div[@class='section active']//button[@class='close-button section-close']")
    # Métodos: write_drive_message, get_message
    driver_message = (By.XPATH, '//*[@id="comment"]')
    # Método: request_blanket_and_tissues, get_blanket_and_scarves
    blanket_and_scarves = (
    By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    # Método: value_blanket_and_scarves
    blanket_and_scarves_slider = (By.CLASS_NAME, "switch-input")
    # Método: request_ice_cream
    ice_cream_counter = (By.CLASS_NAME, "counter-plus")
    # Método: get_ice_cream
    ice_cream_value = (By.CLASS_NAME, "counter-value")
    # Métodos: search_taxi, get_taxi
    taxi_search_button = (By.CLASS_NAME, "smart-button-main")
    # Método: wait_for_driver_info
    modal_taxi = (By.CLASS_NAME, "order-details")
    # Método: details_travel_click
    travel_details = (By.XPATH, '//button[descendant::img[@alt="burger"]]')

    def __init__(self, driver):
        self.driver = driver

    # Establecer dirección de origen
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    # Establecer dirección de destino
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    # Establecer ruta completa
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    # Obtener dirección de origen desde el campo
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Obtener dirección de destino desde el campo
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Hacer clic en el botón para seleccionar taxi
    def select_taxi_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.select_taxi).click()

    # Seleccionar tarifa "Comfort"
    def select_comfort_rate(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.comfort_button).click()

    # Seleccionar opción para introducir número telefónico
    def select_number_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.select_phone_insert).click()

    # Escribir el número de teléfono en el campo correspondiente
    def add_phone_number(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.number).send_keys(data.phone_number)

    # Configurar el teléfono en la interfaz de la app
    def set_phone(self):
        self.driver.implicitly_wait(30)
        self.select_number_button()
        self.driver.implicitly_wait(30)
        self.add_phone_number()

    # Hacer clic en el botón "Siguiente"
    def the_next_button(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.next_button).click()

    # Confirmar datos del teléfono
    def send_cell_info(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.cell_next).click()

    # Obtener número de teléfono del campo correspondiente
    def get_phone(self):
        return self.driver.find_element(*self.phone_input).get_property('value')

    # Hacer clic en el campo del código de verificación
    def code_click(self):
        self.driver.find_element(*self.click_code).click()

    # Insertar código de verificación de teléfono
    def code_number(self):
        self.driver.implicitly_wait(20)
        phone_code = utilidades.retrieve_phone_code(driver=self.driver)
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.code).send_keys(phone_code)

    # Obtener el código ingresado
    def get_code(self):
        return self.driver.find_element(*self.code).get_property('value')

    # Hacer clic para acceder al método de pago
    def pay_click(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.payment_method).click()

    # Hacer clic para agregar nueva tarjeta
    def add_click(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.card_add_button).click()

    # Iniciar el proceso para agregar tarjeta de crédito
    def click_card(self):
        self.driver.implicitly_wait(30)
        self.pay_click()
        self.driver.implicitly_wait(30)
        self.add_click()

    # Hacer clic en el campo de número de tarjeta
    def number_click(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.credit_click).click()

    # Ingresar el número de tarjeta
    def number_input(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.add_credit_card).send_keys(data.card_number)

    # Método que ejecuta la entrada del número de tarjeta
    def card_input(self):
        self.driver.implicitly_wait(20)
        self.number_click()
        self.driver.implicitly_wait(20)
        self.number_input()

    # Obtener valor del campo de número de tarjeta
    def get_card_input(self):
        return self.driver.find_element(*self.add_credit_card).get_property('value')

    # Hacer clic en el campo CVV
    def cvv_add(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.card_cvv).click()

    # Ingresar código de seguridad de la tarjeta
    def code_card_input(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.card_cvv).send_keys(data.card_code)

    # Método que ejecuta la entrada del CVV
    def cvv_code(self):
        self.driver.implicitly_wait(20)
        self.code_card_input()

    # Obtener código CVV ingresado
    def get_cvv_card(self):
        return self.driver.find_element(*self.card_cvv).get_property('value')

    # Confirmar el registro de la tarjeta
    def registered_card(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.confirm_agree_card).click()

    # Método para añadir una tarjeta de crédito
    def add_card(self):
        self.driver.implicitly_wait(20)
        self.card_input()
        self.driver.implicitly_wait(20)
        self.cvv_code()
        self.driver.implicitly_wait(20)
        self.registered_card()

    # Cerrar ventana modal
    def close_window(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.x_button).click()

    # Escribir mensaje para el conductor
    def write_drive_message(self, message):
        self.driver.implicitly_wait(20)
        message_field = self.driver.find_element(*self.driver_message)
        message_field.send_keys(message)

    # Obtener el mensaje escrito
    def get_message(self):
        return self.driver.find_element(*self.driver_message).get_property('value')

    # Seleccionar manta y pañuelos
    def request_blanket_and_tissues(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.blanket_and_scarves).click()

    # Obtener valor del campo de manta y pañuelos
    def get_blanket_and_scarves(self):
        return self.driver.find_element(*self.blanket_and_scarves).get_property('value')

    def value_blanket_and_scarves(self):
        slider = self.driver.find_element(*self.blanket_and_scarves_slider)
        return slider.is_selected()

    # Seleccionar dos helados
    def request_ice_cream(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.ice_cream_counter).click()
        self.driver.find_element(*self.ice_cream_counter).click()

    # Obtener número de helados seleccionados
    def get_ice_cream(self):
        return int(self.driver.find_element(*self.ice_cream_value).text)

    # Buscar taxi disponible
    def search_taxi(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.taxi_search_button).click()

    # Obtener valor del botón de búsqueda de taxi
    def get_taxi(self):
        button = self.driver.find_element(*self.taxi_search_button)
        return button.is_displayed() and button.is_enabled()

    # Esperar información del conductor (modal)
    def wait_for_driver_info(self):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal_taxi))
        button = self.driver.find_element(*self.travel_details)
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", button)

