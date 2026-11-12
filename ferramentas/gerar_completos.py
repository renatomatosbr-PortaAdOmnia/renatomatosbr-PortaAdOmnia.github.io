"""Gera os sites completos de exemplo (modelo de serviços) a partir de modelo_servicos.html.
CSS e ícone do WhatsApp vêm do modelo Aurora (exemplo-confeitaria/index.html).
Uso: python3 gerar_completos.py <pasta do repositório>"""
import json, os, re, sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/renatomatosbr-portaadomnia.github.io"
AQUI = os.path.dirname(os.path.abspath(__file__))
aurora = open(os.path.join(REPO, "exemplo-confeitaria", "index.html"), encoding="utf-8").read()
CSS = aurora.split("<style>", 1)[1].split("</style>", 1)[0]
WHATS = re.search(r'<symbol id="i-whats".*?</symbol>', aurora, re.S).group(0)
MODELO = open(os.path.join(AQUI, "modelo_servicos.html"), encoding="utf-8").read()

CAMPINAS_ZONAS = [
    {"nome": "Até 3 km", "preco": 10, "cor": "#7bd389", "bairros": ["Centro", "Cambuí", "Guanabara", "Bosque", "Botafogo", "Vila Itapura", "Jardim Chapadão", "Castelo", "Nova Campinas", "Taquaral", "Jardim Brasil"]},
    {"nome": "De 3 a 6 km", "preco": 15, "cor": "#f0c05a", "bairros": ["Barão Geraldo", "Vila Industrial", "Swift", "Proença", "Bonfim", "Jardim Proença", "Parque Taquaral", "Vila Nova", "São Bernardo", "Jardim Nova Europa", "Ponte Preta", "Jardim Leonor", "Jardim Campos Elíseos", "Jardim Estoril"]},
    {"nome": "De 6 a 10 km", "preco": 22, "cor": "#e8899e", "bairros": ["Sousas", "Joaquim Egídio", "Ouro Verde", "Campo Grande", "Jardim Aurélia", "Parque Prado", "Jardim Ipaussurama", "Vila União", "Jardim do Lago", "Parque Industrial", "Jardim Amazonas", "Cidade Universitária"]},
]

PET = {
    "pasta": "exemplo-pet",
    "titulo": "Pelúcia Pet Spa · Banho e tosa com leva e traz em Campinas · Site de exemplo",
    "descricao": "Site de exemplo criado pela Porta Ad Omnia para pet shops: preço do banho e tosa na hora pelo porte, leva e traz por bairro, plano mensal e agendamento pelo WhatsApp.",
    "og": "1698313790088-c59e134c75e8",
    "cores": {"--creme": "#f5fafa", "--creme-2": "#e6f1f1", "--branco": "#fdfefe", "--cacau": "#17323a", "--cacau-2": "#3d5a62", "--cacau-3": "#6f878d",
              "--framboesa": "#2a7f8c", "--framboesa-escura": "#1f6570", "--framboesa-suave": "#dcf0f2", "--linha": "#d6e5e5", "--ouro": "#e0a43a"},
    "cfg": {
        "nome": "Pelúcia Pet Spa", "marcaCurta": "Pelúcia", "marcaSub": "Pet spa · Campinas", "icone": "i-pata", "whatsapp": "",
        "statusExtra": "Leva e traz em Campinas · Agendamento pelo WhatsApp · Pix e cartão",
        "cta_topo": "Ver preço do banho",
        "horarios": {"0": None, "1": [8, 18], "2": [8, 18], "3": [8, 18], "4": [8, 18], "5": [8, 18], "6": [8, 16]},
        "periodos": ["Manhã (8h às 12h)", "Tarde (13h às 18h)"],
        "hero": {
            "selo": ["Novo", "Banho de Natal com lacinho"],
            "titulo": ["Banho e tosa", "com <em>preço na hora</em>", "e leva e traz"],
            "texto": "Escolha o porte, o serviço e o dia: o valor aparece na hora e o agendamento chega pronto no WhatsApp. A gente busca e devolve o seu pet.",
            "cta1": "Ver o preço do meu pet", "cta2": "Ver serviços",
            "provas": [["5,0", "no Google", True], ["800+", "pets atendidos", False], ["1 a 1", "atendimento individual", False]],
            "fotoA": {"id": "1698313790088-c59e134c75e8", "alt": "Cachorro enrolado na toalha depois do banho"},
            "fotoB": {"id": "1583534778255-5d67d3dcf95d", "alt": "Cachorro tomando banho"},
            "flutua": {"titulo": "Leva e traz", "texto": "Taxa a partir de R$ 10 em Campinas"},
            "giro": "Banho com carinho · Sem gaiola · Campinas ·",
        },
        "beneficios": [["i-calc", "Preço na hora", "Pelo porte e pelo serviço, antes de agendar"], ["i-moto", "Leva e traz", "Buscamos e devolvemos no horário"],
                       ["i-check", "Sem gaiola", "Seu pet fica solto e acompanhado"], ["i-folha", "Produtos suaves", "Linha própria para cada tipo de pelo"]],
        "temporada": {"sobre": "Natal", "titulo": "A agenda do banho de Natal fecha em", "prazo": "2026-12-20T18:00:00-03:00",
                      "texto": "Banho caprichado, perfume especial e lacinho de Natal para o seu pet chegar lindo na ceia. As vagas acabam rápido em dezembro.",
                      "botao": "Garantir o banho de Natal", "foto": {"id": "1534361960057-19889db9621e", "alt": "Cachorro feliz depois do banho"}},
        "servicos": {
            "titulo": "Escolha e <em>agende em um toque</em>",
            "categorias": {"todos": "Todos", "banho": "Banho", "tosa": "Tosa", "cuidados": "Cuidados"},
            "aviso": "Fotos ilustrativas. Os preços variam pelo porte: o botão \"Personalizar\" leva para o simulador com o serviço já escolhido.",
            "itens": [
                {"id": "banho", "cat": "banho", "nome": "Banho", "desc": "Banho completo com secagem, escovação e perfume.", "foto": "1583534778255-5d67d3dcf95d", "info1": "1h a 1h30", "info2": "Porte pequeno", "preco": 55, "unid": "a partir de", "monta": {"servico": "Banho"}, "etiqueta": "Mais pedido"},
                {"id": "higienica", "cat": "tosa", "nome": "Banho + tosa higiênica", "desc": "Banho completo e tosa das patas, barriga e partes íntimas.", "foto": "1611173622933-91942d394b04", "info1": "1h30", "info2": "Porte pequeno", "preco": 70, "unid": "a partir de", "monta": {"servico": "Banho + tosa higiênica"}},
                {"id": "tesoura", "cat": "tosa", "nome": "Tosa na tesoura", "desc": "Acabamento feito à mão, para raças de pelo longo.", "foto": "1772437883387-8076cf660c65", "info1": "2h a 3h", "info2": "Porte pequeno", "preco": 120, "unid": "a partir de", "monta": {"servico": "Banho + tosa na tesoura"}, "etiqueta": "Especialidade"},
                {"id": "hidratacao", "cat": "cuidados", "nome": "Hidratação", "desc": "Pelo macio e brilhante por mais tempo.", "foto": "1698313790088-c59e134c75e8", "info1": "+20 min", "info2": "Qualquer porte", "preco": 25, "unid": "adicional"},
                {"id": "unhas", "cat": "cuidados", "nome": "Corte de unhas", "desc": "Rápido, com cuidado e sem estresse.", "foto": "1733964659477-35534815c626", "info1": "10 min", "info2": "Qualquer porte", "preco": 15, "unid": "avulso"},
                {"id": "dentes", "cat": "cuidados", "nome": "Escovação de dentes", "desc": "Hálito fresco e prevenção de tártaro.", "foto": "1534361960057-19889db9621e", "info1": "10 min", "info2": "Qualquer porte", "preco": 15, "unid": "avulso"},
            ],
        },
        "montador": {
            "sobre": "Simulador", "menu": "Simulador", "titulo": "Quanto fica o <em>banho do seu pet?</em>",
            "intro": "Escolha o porte, o serviço e os cuidados extras. O preço aparece na hora e o agendamento sai pronto no WhatsApp.",
            "resumo": "Seu atendimento", "botao": "Agendar pelo WhatsApp", "principal": 1, "mostrarSoma": True,
            "nota": "Valor final confirmado no WhatsApp.",
            "obsRotulo": "Nome e raça do pet", "obsDica": "Ex.: Thor, shih-tzu, um pouco agitado",
            "grupos": [
                {"id": "porte", "titulo": "Qual o porte?", "curto": "Porte", "tipo": "radio", "opcoes": [
                    {"nome": "Pequeno (até 10 kg)", "mult": 1}, {"nome": "Médio (10 a 25 kg)", "mult": 1.35}, {"nome": "Grande (25 a 40 kg)", "mult": 1.7}, {"nome": "Gigante (40 kg+)", "mult": 2.1}]},
                {"id": "servico", "titulo": "Serviço", "curto": "Serviço", "tipo": "radio", "opcoes": [
                    {"nome": "Banho", "soma": 55, "min": 75}, {"nome": "Banho + tosa higiênica", "soma": 70, "min": 90}, {"nome": "Banho + tosa na máquina", "soma": 95, "min": 120}, {"nome": "Banho + tosa na tesoura", "soma": 120, "min": 150}]},
                {"id": "pelo", "titulo": "Como é o pelo?", "curto": "Pelo", "tipo": "radio", "opcoes": [
                    {"nome": "Curto", "mult": 1}, {"nome": "Longo ou com nós", "mult": 1.2, "min": 20}]},
                {"id": "extras", "titulo": "Cuidados extras", "curto": "Extras", "dica": "Opcional", "tipo": "checkbox", "opcoes": [
                    {"nome": "Hidratação", "fixo": 25, "min": 20}, {"nome": "Corte de unhas", "fixo": 10}, {"nome": "Limpeza de ouvidos", "fixo": 10}, {"nome": "Escovação de dentes", "fixo": 15}, {"nome": "Lacinho ou bandana", "fixo": 0}]},
            ],
        },
        "zonas": CAMPINAS_ZONAS,
        "entregaRotulo": "Leva e traz",
        "leva": {"rotulo": "Leva e traz?", "sim": "Sim, buscar em casa", "nao": "Eu levo e busco"},
        "info": {"sobre": "Leva e traz", "menu": "Leva e traz", "titulo": "Quanto custa buscar <em style=\"color:#9fe0e8\">o seu pet?</em>",
                 "intro": "A taxa é fixa por distância, ida e volta incluídas. Digite o bairro para ver o valor.",
                 "padrao": "Buscamos e devolvemos em toda Campinas, de segunda a sábado.", "rotuloTaxa": "Leva e traz",
                 "semTaxa": ["Você leva e busca", "Sem taxa, com horário marcado"]},
        "plano": {"sobre": "Plano mensal", "titulo": "Banho toda semana <em>sai mais barato</em>",
                  "intro": "Quem dá banho com frequência economiza no plano mensal. Escolha o serviço e quantas vezes por mês.",
                  "rotulo": "Banhos", "padrao": 4, "max": 4, "desconto": 0.15,
                  "opcoes": [["Banho · porte pequeno", 55], ["Banho · porte médio", 74], ["Banho · porte grande", 94], ["Banho + tosa higiênica · pequeno", 70]],
                  "foto": {"id": "1611173622933-91942d394b04", "alt": "Pet sendo escovado"}},
        "passosTitulo": "Do agendamento ao pet <em>cheiroso</em>",
        "passos": [["Simule e agende", "Veja o preço no site e mande o agendamento pelo WhatsApp."], ["Confirmamos o horário", "Respondemos em até 1 hora no horário de atendimento."],
                   ["Buscamos o seu pet", "No leva e traz, avisamos quando estivermos chegando."], ["Volta cheiroso", "Com fotos do antes e depois no seu WhatsApp."]],
        "politicas": [["Vacinas em dia", "Pedimos a carteirinha na primeira visita, para a segurança de todos."], ["Pets idosos ou ansiosos", "Atendimento com pausas e sem pressa. Avise no agendamento."], ["Remarcação", "Sem custo com até 24 horas de aviso."]],
        "depoimentos": [["Simulei o preço no site e já mandei o agendamento. Buscaram o Thor no horário e ele voltou lindo.", "Juliana M.", "Shih-tzu · Cambuí"],
                        ["O plano mensal compensou demais. Banho toda semana pagando menos.", "Ricardo P.", "Golden · Taquaral"],
                        ["Minha cachorra é idosa e ansiosa. Fizeram tudo com calma e me mandaram fotos.", "Fernanda A.", "Poodle · Barão Geraldo"]],
        "faq": [["Como sei o preço do banho?", "Use o simulador: escolha o porte, o serviço e o tipo de pelo. O valor aparece na hora."],
                ["Vocês buscam o pet em casa?", "Sim. A taxa de leva e traz depende do bairro e inclui ida e volta. Veja na seção Leva e traz."],
                ["Meu pet fica em gaiola?", "Não. Ele fica solto, em área segura e sempre acompanhado."],
                ["Quanto tempo demora?", "De 1h a 3h, conforme o serviço e o porte. No leva e traz, avisamos quando estivermos a caminho."],
                ["Atendem gatos?", "Sim, com horário exclusivo para eles ficarem tranquilos. Avise no agendamento."],
                ["E se eu precisar remarcar?", "Sem custo com até 24 horas de aviso."]],
        "final": {"titulo": "O seu pet merece um dia de spa", "texto": "Veja o preço agora, escolha o dia e a gente cuida do resto, inclusive da busca.", "botao": "Ver o preço do meu pet"},
        "rodape": "Banho, tosa e cuidados com leva e traz em Campinas.",
    },
}

BELEZA = {
    "pasta": "exemplo-beleza",
    "titulo": "Íris Studio · Cílios e sobrancelhas em Campinas · Site de exemplo",
    "descricao": "Site de exemplo criado pela Porta Ad Omnia para estúdios de beleza: preço e duração do procedimento na hora, data da manutenção, plano mensal e agendamento pelo WhatsApp.",
    "og": "1589710751893-f9a6770ad71b",
    "cores": {"--creme": "#fbf7f6", "--creme-2": "#f3e8e5", "--branco": "#fffdfc", "--cacau": "#2b1e22", "--cacau-2": "#5a464b", "--cacau-3": "#8a777b",
              "--framboesa": "#a5566a", "--framboesa-escura": "#874255", "--framboesa-suave": "#f6e3e8", "--linha": "#eadbd7", "--ouro": "#c79a4a"},
    "cfg": {
        "nome": "Íris Studio", "marcaCurta": "Íris", "marcaSub": "Cílios · Campinas", "icone": "i-olho", "whatsapp": "",
        "statusExtra": "Atendimento com hora marcada · Agendamento pelo WhatsApp · Pix e cartão",
        "cta_topo": "Ver preço e duração",
        "horarios": {"0": None, "1": None, "2": [9, 19], "3": [9, 19], "4": [9, 19], "5": [9, 19], "6": [9, 17]},
        "periodos": ["Manhã (9h às 12h)", "Tarde (13h às 16h)", "Fim da tarde (16h às 19h)"],
        "hero": {
            "selo": ["Novo", "Agenda de festas de fim de ano aberta"],
            "titulo": ["Cílios e sobrancelhas", "com <em>preço na hora</em>"],
            "texto": "Escolha o procedimento e o efeito: o site mostra o valor, quanto tempo leva e já sugere a data da manutenção. O agendamento chega pronto no WhatsApp.",
            "cta1": "Ver preço e duração", "cta2": "Ver procedimentos",
            "provas": [["5,0", "no Google", True], ["1.500+", "atendimentos", False], ["21 dias", "de durabilidade", False]],
            "fotoA": {"id": "1589710751893-f9a6770ad71b", "alt": "Profissional aplicando extensão de cílios"},
            "fotoB": {"id": "1683719312734-e31de63957ab", "alt": "Olho com cílios longos"},
            "flutua": {"titulo": "Manutenção lembrada", "texto": "O site sugere a data certa da volta"},
            "giro": "Olhar natural · Materiais de qualidade · Campinas ·",
        },
        "beneficios": [["i-calc", "Preço e duração", "Você sabe tudo antes de agendar"], ["i-relogio", "Manutenção na data", "O site calcula a próxima visita"],
                       ["i-check", "Materiais de qualidade", "Conforto e durabilidade no dia a dia"], ["i-folha", "Resultado natural", "Efeito combinado antes de começar"]],
        "temporada": {"sobre": "Festas de fim de ano", "titulo": "A agenda de dezembro fecha em", "prazo": "2026-12-18T19:00:00-03:00",
                      "texto": "Cílios prontos para as fotos de Natal e Ano-Novo. Dezembro lota rápido: garanta o seu horário com antecedência.",
                      "botao": "Garantir meu horário", "foto": {"id": "1772236617396-2f8460293c07", "alt": "Profissional atendendo uma cliente"}},
        "servicos": {
            "titulo": "Escolha o seu e <em>agende em um toque</em>",
            "categorias": {"todos": "Todos", "cilios": "Cílios", "sobrancelhas": "Sobrancelhas"},
            "aviso": "Fotos ilustrativas. O botão \"Personalizar\" leva para o simulador com o procedimento já escolhido.",
            "itens": [
                {"id": "fio", "cat": "cilios", "nome": "Extensão fio a fio", "desc": "Efeito natural, como se fossem os seus cílios, só que mais longos.", "foto": "1639629509821-c54cdd984227", "info1": "2h", "info2": "Dura até 21 dias", "preco": 160, "unid": "a partir de", "monta": {"procedimento": "Extensão fio a fio"}, "etiqueta": "Mais pedido"},
                {"id": "volume", "cat": "cilios", "nome": "Volume brasileiro", "desc": "Mais volume e definição, ainda leve no dia a dia.", "foto": "1674049406467-824ea37c7184", "info1": "2h20", "info2": "Dura até 21 dias", "preco": 180, "unid": "a partir de", "monta": {"procedimento": "Volume brasileiro"}},
                {"id": "lifting", "cat": "cilios", "nome": "Lash lifting", "desc": "Curvatura e alongamento dos seus próprios cílios, sem extensão.", "foto": "1683719312734-e31de63957ab", "info1": "1h", "info2": "Dura até 45 dias", "preco": 120, "unid": "a partir de", "monta": {"procedimento": "Lash lifting"}},
                {"id": "manut", "cat": "cilios", "nome": "Manutenção de cílios", "desc": "Reposição dos fios para manter o efeito por mais tempo.", "foto": "1770999086860-143f54adf01b", "info1": "1h", "info2": "Até 21 dias", "preco": 90, "unid": "a partir de", "monta": {"procedimento": "Manutenção de cílios"}},
                {"id": "design", "cat": "sobrancelhas", "nome": "Design de sobrancelhas", "desc": "Desenho que valoriza o seu rosto, limpinho e alinhado.", "foto": "1674049406179-d7bf2c263e71", "info1": "30 min", "info2": "A cada 20 dias", "preco": 45, "unid": "avulso"},
                {"id": "henna", "cat": "sobrancelhas", "nome": "Design com henna", "desc": "Preenche falhas e realça o formato por até 15 dias.", "foto": "1718720410649-7524fcb0f0a5", "info1": "40 min", "info2": "A cada 20 dias", "preco": 65, "unid": "avulso"},
            ],
        },
        "montador": {
            "sobre": "Simulador", "menu": "Simulador", "titulo": "Quanto custa e <em>quanto tempo leva?</em>",
            "intro": "Escolha o procedimento, o efeito e os complementos. O site mostra o preço, a duração e a data da próxima manutenção.",
            "resumo": "Seu atendimento", "botao": "Agendar pelo WhatsApp", "principal": 0, "mostrarSoma": True,
            "nota": "Valor final confirmado no WhatsApp.",
            "obsRotulo": "Alguma observação?", "obsDica": "Ex.: primeira vez, alergia, referência do efeito",
            "grupos": [
                {"id": "procedimento", "titulo": "Procedimento", "curto": "Procedimento", "tipo": "radio", "opcoes": [
                    {"nome": "Extensão fio a fio", "soma": 160, "min": 120, "manut": 21}, {"nome": "Volume brasileiro", "soma": 180, "min": 140, "manut": 21},
                    {"nome": "Volume russo", "soma": 220, "min": 160, "manut": 21}, {"nome": "Lash lifting", "soma": 120, "min": 60, "manut": 45},
                    {"nome": "Manutenção de cílios", "soma": 90, "min": 60, "manut": 21}]},
                {"id": "efeito", "titulo": "Efeito", "curto": "Efeito", "tipo": "radio", "opcoes": [
                    {"nome": "Natural"}, {"nome": "Gatinho"}, {"nome": "Boneca"}, {"nome": "Marcante"}]},
                {"id": "sobrancelha", "titulo": "Sobrancelhas no mesmo horário", "curto": "Sobrancelhas", "dica": "Opcional · até 2", "tipo": "checkbox", "max": 2, "opcoes": [
                    {"nome": "Design", "fixo": 40, "min": 30}, {"nome": "Design com henna", "fixo": 60, "min": 40}, {"nome": "Brow lamination", "fixo": 120, "min": 60}, {"nome": "Buço", "fixo": 18, "min": 10}]},
                {"id": "extras", "titulo": "Precisa de mais alguma coisa?", "curto": "Extras", "dica": "Opcional", "tipo": "checkbox", "opcoes": [
                    {"nome": "Remover extensão de outro lugar", "fixo": 40, "min": 30}, {"nome": "Kit de cuidados (escovinha + espuma)", "fixo": 25}]},
            ],
        },
        "zonas": None,
        "entregaRotulo": "",
        "info": {"sobre": "Depois do procedimento", "menu": "Cuidados", "titulo": "Cuidados para durar <em style=\"color:#f1b6c6\">muito mais</em>",
                 "intro": "Seguindo estes cuidados, os cílios ficam bonitos até a manutenção. A gente também manda tudo por escrito no WhatsApp.",
                 "itens": [["Nas primeiras 24 horas", "Evite molhar os cílios, vapor e sauna."], ["Todos os dias", "Escove com a escovinha e lave com espuma própria para cílios."],
                           ["Na hora de dormir", "Prefira dormir de barriga para cima ou de lado, sem esfregar o rosto."], ["Maquiagem", "Use demaquilante sem óleo e evite rímel nos fios."]]},
        "plano": {"sobre": "Plano mensal", "titulo": "Manutenção em dia <em>sai mais barato</em>",
                  "intro": "Quem mantém os cílios e as sobrancelhas sempre em dia economiza no plano mensal. Escolha o serviço e a frequência.",
                  "rotulo": "Atendimentos", "padrao": 2, "max": 4, "desconto": 0.1,
                  "opcoes": [["Manutenção de cílios", 90], ["Design de sobrancelhas", 45], ["Design com henna", 65], ["Manutenção + design", 130]],
                  "foto": {"id": "1770999086860-143f54adf01b", "alt": "Materiais de extensão de cílios"}},
        "passosTitulo": "Do agendamento ao <em>olhar renovado</em>",
        "passos": [["Simule e agende", "Veja preço e duração no site e mande pelo WhatsApp."], ["Confirmamos o horário", "Respondemos em até 1 hora no horário de atendimento."],
                   ["Combinamos o efeito", "Antes de começar, a gente alinha o resultado com você."], ["Volte na data certa", "Avisamos no WhatsApp quando chegar a hora da manutenção."]],
        "politicas": [["Primeira vez", "Fazemos uma conversa rápida antes para escolher o efeito ideal."], ["Alergias", "Avise no agendamento. Temos opções para olhos sensíveis."], ["Remarcação", "Sem custo com até 24 horas de aviso."]],
        "depoimentos": [["Vi o preço e o tempo no site antes de marcar. Fiquei tranquila e o resultado ficou muito natural.", "Camila R.", "Fio a fio · Cambuí"],
                        ["Adoro que me avisam a data da manutenção. Nunca mais deixei falhar.", "Patrícia L.", "Volume brasileiro · Taquaral"],
                        ["Já tinha feito em outros lugares e nunca ficou do jeito que eu queria. Aqui acertaram de primeira.", "Larissa M.", "Lash lifting · Barão Geraldo"]],
        "faq": [["Quanto tempo dura a extensão?", "Com os cuidados certos, de 15 a 21 dias até a manutenção. O simulador já sugere a data."],
                ["Dói ou incomoda?", "Não. Você fica deitada, de olhos fechados, e muita gente até cochila."],
                ["Qual efeito combina comigo?", "Na primeira vez, conversamos antes para escolher o efeito pelo formato dos seus olhos."],
                ["Posso fazer sobrancelha no mesmo horário?", "Pode. Escolha no simulador e somamos o tempo e o valor."],
                ["Tenho olhos sensíveis. Posso fazer?", "Avise no agendamento: temos cola e materiais para olhos sensíveis."],
                ["E se eu precisar remarcar?", "Sem custo com até 24 horas de aviso."]],
        "final": {"titulo": "O seu olhar, do jeitinho que você quer", "texto": "Veja preço e duração agora, escolha o dia e a gente cuida do resto.", "botao": "Ver preço e duração"},
        "rodape": "Extensão de cílios, lash lifting e sobrancelhas em Campinas.",
    },
}


def gera(n):
    cores = "<style>:root{" + ";".join(f"{k}:{v}" for k, v in n["cores"].items()) + "}</style>"
    og = f"https://images.unsplash.com/photo-{n['og']}?w=1200&h=630&fit=crop&q=75&fm=jpg"
    head = (f'<title>{n["titulo"]}</title>\n<meta name="description" content="{n["descricao"]}">\n'
            f'<meta property="og:title" content="{n["titulo"]}">\n<meta property="og:description" content="{n["descricao"]}">\n'
            f'<meta property="og:image" content="{og}">\n<meta name="theme-color" content="{n["cores"]["--creme"]}">')
    html = (MODELO.replace("/*CSS*/", CSS).replace("<!--CORES-->", cores).replace("<!--HEAD-->", head)
            .replace("<!--WHATS-->", WHATS).replace("/*CONFIG*/", json.dumps(n["cfg"], ensure_ascii=False, indent=1)))
    d = os.path.join(REPO, n["pasta"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    print("ok", n["pasta"], len(html))


if __name__ == "__main__":
    for n in (PET, BELEZA):
        gera(n)
