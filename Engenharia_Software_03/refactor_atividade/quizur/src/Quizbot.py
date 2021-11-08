from time import sleep
from random import choice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .helpers.appHelpers import generate_random_names
from .helpers.seleniumHelpers import get_element, get_elements

# This algorithms works doing the quiz in a random way in order to get the right answers, after that, the browser its clean up and the user can start the quiz again with the right aswers

driver = webdriver.Chrome()

url = input("url >> ")
print("")
nome = input("nome >> ")

RIGHT_ANSWERS_IDS = []
LAST_QUESTION_ID = []
RANDOM_NAMES = generate_random_names()


def main():
    primeira_selecao()
    selecao_inteligente()
    sleep(10)
    driver.close()


def getTheRightAnswersFromThePage(quizpage: str, driver):
    driver.get(quizpage)
    sleep(3)

    print("Excluindo cookies anteriores...")
    driver.delete_all_cookies()
    sleep(3)

    preencher_input_nome(choice(RANDOM_NAMES))

    _btn_iniciar = get_element("span.startBtn.a-dropTop.js-startQuiz")
    _lista_sections = get_elements("questionWrapper")

    quantidade_de_questoes = len(_lista_sections)

    _btn_iniciar.click()
    sleep(3)

    print("iniciando selecao burra...")
    for questao in range(quantidade_de_questoes):
        for _section in _lista_sections:
            sleep(0.2)
            if _section.value_of_css_property("display") == "block":
                _alternativa = _section.find_element_by_class_name("alternativeWrapper")

                if questao == (quantidade_de_questoes - 1):

                    js_pegar_ultima_section = f"window.ultima_section = document.querySelector(\"section[data-question='{pegar_id(_section)}']\")"
                    js_gerar_alt_certa_var = "window.alt_certa = ''"
                    js_func_onclick = """
                        window.pegar_alt_certa = function(e)
                        {
                            alt_certa = ultima_section.querySelector('li.right').getAttribute('data-alternative')
                            
                            localStorage.setItem("alt_certa",alt_certa)
                            
                            document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });

                            document.location.reload(true)
                        }
                    """
                    js_onclick = (
                        "window.ultima_section.onclick = window.pegar_alt_certa"
                    )

                    driver.execute_script(js_pegar_ultima_section)
                    driver.execute_script(js_gerar_alt_certa_var)
                    driver.execute_script(js_func_onclick)
                    driver.execute_script(js_onclick)

                    RIGHT_ANSWERS_IDS(_lista_sections)
                    LAST_QUESTION_ID.append(pegar_id(_section))

                    sleep(2)

                    _alternativa.click()
                    break

                _alternativa.click()
                sleep(3)
                break


def selecao_inteligente():
    sleep(5)
    js_del_cookies = 'document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });'
    driver.execute_script(js_del_cookies)
    driver.refresh()
    sleep(5)

    print("iniciando...")
    print(f"url: {url}")
    print(f"RIGHT_ANSWERS_IDS {nome}")
    LAST_QUESTION_ID.append(get_ls("alt_certa"))

    RIGHT_ANSWERS_IDS.append(LAST_QUESTION_ID)
    user_registration(nome)

    _btn_iniciar = get_element("span.startBtn.a-dropTop.js-startQuiz")
    _lista_sections = get_elements("questionWrapper")

    quantidade_de_questoes = len(_lista_sections)

    sleep(2)
    _btn_iniciar.click()
    sleep(3)

    print("iniciando selecao inteligente...")
    for questao in range(quantidade_de_questoes):
        for _section in _lista_sections:
            sleep(0.2)
            if _section.value_of_css_property("display") == "block":
                _alternativa = get_element(
                    f"li[data-alternative='{procurar_alternativa(pegar_id(_section))}']",
                    _section,
                )
                _alternativa.click()
                sleep(3)
                break

    print("Hacking terminado huashusah")
    print("Fechando...")
    driver.close()


def user_registration(name):
    _input_name = get_element("input.js-nameInput")
    _input_name.clear()
    _input_name.send_keys(name)
    _input_name.send_keys(Keys.RETURN)


def minerar_alternativas_certas(_lista_sections):
    print("minerando alternativas corretas")
    for _section in _lista_sections:
        sleep(0.2)
        if _section.value_of_css_property("display") == "none":
            section_id = _section.get_attribute("data-question")
            _alternativa = _section.find_element_by_class_name("right")
            alternativa_id = _alternativa.get_attribute("data-alternative")

            RIGHT_ANSWERS_IDS.append([section_id, alternativa_id])


def procurar_alternativa(section_id):
    for id in RIGHT_ANSWERS_IDS:
        if id[0] == section_id:
            return id[1]


def get_ls(key):
    return driver.execute_script(
        "return window.localStorage.getItem(arguments[0]);", key
    )


def pegar_id(_section):
    id = _section.get_attribute("data-question")
    return id


def acessar_url(url):
    driver.get(url)


main()
