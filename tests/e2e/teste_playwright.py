"""
Teste end-to-end do MVP Mochila Cheia com Playwright + screenshots.
Navega o fluxo real (cadastro -> publicar -> moderar -> aprovar -> solicitar)
em viewport mobile e salva as evidencias em docs/evidencias/playwright/.
"""

import sys
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5001"
OUT = "docs/evidencias/playwright"

resultados = []


def ok(nome, cond, detalhe=""):
    resultados.append((nome, cond, detalhe))
    print(("  OK  " if cond else " FALHA") + f" {nome} {detalhe}")


def login(page, email, senha):
    page.goto(f"{BASE}/auth/login")
    page.fill("input[name=email]", email)
    page.fill("input[name=senha]", senha)
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")


def logout(page):
    page.goto(f"{BASE}/auth/logout")
    page.wait_for_load_state("networkidle")


def shot(page, nome):
    page.screenshot(path=f"{OUT}/{nome}.png", full_page=True)


with sync_playwright() as p:
    browser = p.chromium.launch()
    # Viewport de celular (design mobile-first)
    ctx = browser.new_context(viewport={"width": 390, "height": 844},
                              device_scale_factor=2)
    page = ctx.new_page()

    # 01 - Tela de login
    page.goto(f"{BASE}/auth/login")
    shot(page, "01-login")
    ok("login renderiza", "Mochila Cheia" in page.content())

    # 02 - Cadastro
    page.goto(f"{BASE}/auth/cadastro")
    shot(page, "02-cadastro")
    ok("cadastro tem formulario", page.locator("form[action*='cadastro']").count() > 0)

    # 03 - Home / busca (itens reais do banco, sem login)
    page.goto(f"{BASE}/")
    page.wait_for_load_state("networkidle")
    shot(page, "03-home-busca")
    ok("home lista itens disponiveis", "Estojo Completo" in page.content()
       or "Mochila Escolar Azul" in page.content())

    # 04 - Detalhe de um item disponivel
    page.goto(f"{BASE}/itens/3")
    shot(page, "04-detalhe-item")
    ok("detalhe mostra item real (sem erro 500)", "Solicitar Item" in page.content())

    # === FLUXO DOADOR: publica um item ===
    login(page, "maria.silva@email.com", "senha123")
    page.goto(f"{BASE}/itens/publicar")
    shot(page, "05-publicar-form")
    page.fill("input[name=titulo]", "Mochila Demo Verde (Playwright)")
    page.select_option("select[name=categoria]", "Mochilas")
    page.select_option("select[name=estado]", "Novo")
    page.fill("textarea[name=descricao]",
              "Item publicado automaticamente no teste end-to-end.")
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")
    shot(page, "06-meus-itens")
    ok("item publicado aparece em 'meus itens' como pendente",
       "Mochila Demo Verde" in page.content() and "Pendente" in page.content())
    page.goto(f"{BASE}/")
    page.wait_for_load_state("networkidle")
    ok("item pendente NAO aparece na home",
       "Mochila Demo Verde" not in page.content())

    # === FLUXO MODERADOR: revisa e aprova ===
    logout(page)
    login(page, "admin@mochilacheia.com", "senha123")
    page.goto(f"{BASE}/moderacao/")
    page.wait_for_load_state("networkidle")
    shot(page, "07-fila-moderacao")
    ok("fila de moderacao lista o item novo",
       "Mochila Demo Verde" in page.content())

    # O item novo e o mais recente (maior id) entre os pendentes da fila.
    import re
    hrefs = page.locator("a:has-text('Revisar')").evaluate_all(
        "els => els.map(e => e.getAttribute('href'))")
    ids = [int(re.search(r"/moderacao/(\d+)/", h).group(1)) for h in hrefs]
    novo_id = max(ids)
    page.goto(f"{BASE}/moderacao/{novo_id}/revisar")
    shot(page, "08-revisar-item")
    ok("revisar mostra dados reais do item", "ID: #" in page.content())

    # Aprova via botao da tela de revisao
    page.click("button:has-text('Aprovar')")
    page.wait_for_load_state("networkidle")

    # 09 - Home com item aprovado visivel
    page.goto(f"{BASE}/")
    page.wait_for_load_state("networkidle")
    shot(page, "09-home-item-aprovado")
    ok("item aprovado aparece na home",
       "Mochila Demo Verde" in page.content())

    # === FLUXO RECEPTOR: solicita o item aprovado ===
    logout(page)
    login(page, "joao.pedro@email.com", "senha123")
    # Acha o card do item novo na home e abre o detalhe
    page.goto(f"{BASE}/")
    page.wait_for_load_state("networkidle")
    page.click("a:has-text('Mochila Demo Verde')")
    page.wait_for_load_state("networkidle")
    shot(page, "10-detalhe-para-solicitar")
    page.click("a:has-text('Solicitar Item')")
    page.wait_for_load_state("networkidle")
    shot(page, "11-minhas-solicitacoes")
    ok("solicitacao criada aparece em 'minhas solicitacoes'",
       "Mochila Demo Verde" in page.content())

    # 12 - Perfil do usuario logado
    page.goto(f"{BASE}/auth/perfil")
    shot(page, "12-perfil")
    ok("perfil mostra o usuario logado (Joao Pedro)",
       "joao.pedro@email.com" in page.content())

    # 13 - Login com senha errada (mensagem de erro)
    logout(page)
    page.goto(f"{BASE}/auth/login")
    page.fill("input[name=email]", "joao.pedro@email.com")
    page.fill("input[name=senha]", "senha_errada")
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")
    shot(page, "13-login-erro")
    ok("login invalido mostra mensagem de erro",
       "incorret" in page.content().lower())

    browser.close()

# Resumo
print("\n=== RESUMO ===")
total = len(resultados)
passou = sum(1 for _, c, _ in resultados if c)
print(f"{passou}/{total} verificacoes OK")
sys.exit(0 if passou == total else 1)
