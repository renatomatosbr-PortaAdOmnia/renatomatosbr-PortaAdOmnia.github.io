"""Gera as demos estáticas (Fábrica de sites) para os prospects 4 e 5.

Saída: ./site/<slug>/index.html e ./site/<slug>/opcoes/index.html
"""
import html
import json
import os
import urllib.parse

BASE_URL = "https://renatomatosbr-portaadomnia.github.io"
U = "https://images.unsplash.com/photo-{}?w={}&q=70&auto=format&fit=crop"

NEGOCIOS = [
    {
        "slug": "silfer-cake",
        "nome": "SilFér Cake",
        "nome_longo": "SilFér Cake · Bolos e Bentô Cakes",
        "nicho": "Confeitaria",
        "titulo_seo": "SilFér Cake | Bolos personalizados e bentô cakes no Parque das Águas, Campinas",
        "descricao_seo": "Bolos personalizados feitos igualzinho à sua referência, bentô cakes e docinhos no Parque das Águas, Campinas. Nota 5,0 no Google. Encomende pelo WhatsApp.",
        "subtitulo": "Bolos personalizados e bentô cakes feitos do jeitinho que você imaginou, no Parque das Águas, Campinas",
        "endereco": "Av. São José dos Campos, 3385 – Parque das Águas, Campinas – SP, CEP 13040-735",
        "rua_curta": "Av. São José dos Campos, 3385 – Parque das Águas",
        "tel_display": "(19) 98846-0905",
        "tel": "5519988460905",
        "wa_msg": "Olá! Vi o site e gostaria de encomendar um bolo.",
        "wa_msg_destaque": "Olá! Vi o site e gostaria de encomendar um bentô cake.",
        "place_id": "ChIJO-PQforPyJQRBswu4mf4Tho",
        "horarios": [("Terça a sexta", "11h às 18h"), ("Sábado", "10h às 13h"), ("Domingo e segunda", "Fechado")],
        "horas_ld": [(["Tuesday", "Wednesday", "Thursday", "Friday"], "11:00", "18:00"), (["Saturday"], "10:00", "13:00")],
        "cores": {"bg": "#FBF7FD", "fg": "#2E2340", "muted": "#6E6282", "primary": "#8B5CC4", "primary_soft": "#EFE6FA",
                   "accent": "#F2A7C3", "card": "#FFFFFF", "dark": "#2E2340"},
        "fonte_titulo": "Fraunces", "fonte_texto": "Nunito Sans",
        "hero_img": "1653469742883-c47111ae3bc4",
        "hero_legenda": ("Bolo do seu jeito", "decorado igualzinho à sua referência"),
        "destaque": {
            "selo": "A queridinha da casa",
            "titulo": "Bentô cakes para presentear",
            "texto": "Bolinhos individuais e personalizados, com a frase e a decoração que você escolher. Perfeitos para surpreender alguém especial, até em cima da hora.",
            "botao": "Encomendar um bentô cake",
            "img": "1647773470364-dac99d52c721",
        },
        "cardapio_titulo": "Feito para cada comemoração",
        "cardapio": [
            ("Bolos personalizados", "Você manda a referência e a gente faz igualzinho, com capricho em cada detalhe.", "1659271940584-25589f320198"),
            ("Bentô cakes", "Bolinhos individuais com frase e decoração do seu jeito.", "1562440499-64c9a111f713"),
            ("Bolos de aniversário", "Molhadinhos e super recheados, do primeiro aninho em diante.", "1604413191066-4dd20bedf486"),
            ("Docinhos", "Docinhos para acompanhar o bolo e completar a mesa da festa.", "1767396867485-7e41ee6fec97"),
        ],
        "diferenciais_titulo": "Por que os clientes voltam",
        "diferenciais": [
            ("Igualzinho à referência", "O bolo sai do jeitinho que você idealizou."),
            ("Molhadinho e recheado", "Sabor que faz todo mundo pedir mais um pedaço."),
            ("Atende em cima da hora", "Encomendas com prazo curto, sempre que a agenda permite."),
            ("Atendimento atencioso", "Cuidado do primeiro contato até o pós-venda."),
        ],
        "passos": [
            ("Mande sua ideia", "Envie uma foto de referência e a data pelo WhatsApp."),
            ("Combine os detalhes", "Sabor, tamanho, frase e decoração do seu jeito."),
            ("Retire ou receba", "Retire na loja ou combine a entrega por aplicativo."),
        ],
        "dominio_exemplo": "www.silfercake.com.br",
    },
    {
        "slug": "dolce-nina",
        "nome": "Dolce Nina",
        "nome_longo": "Dolce Nina Confeitaria",
        "nicho": "Confeitaria",
        "titulo_seo": "Dolce Nina Confeitaria | Naked cakes, bolos e brigadeiros no Jardim Guanabara, Campinas",
        "descricao_seo": "Naked cakes, bolos de festa, bentô cakes e brigadeiros feitos com ingredientes de qualidade no Jardim Guanabara, Campinas. Nota 5,0 no Google. Encomende pelo WhatsApp.",
        "subtitulo": "Naked cakes, bolos de festa e brigadeiros feitos com ingredientes de qualidade, no Jardim Guanabara, Campinas",
        "endereco": "Rua Frei Manoel da Ressurreição, 480 – Jardim Guanabara, Campinas – SP, CEP 13073-221",
        "rua_curta": "Rua Frei Manoel da Ressurreição, 480 – Jardim Guanabara",
        "tel_display": "(19) 99902-4522",
        "tel": "5519999024522",
        "wa_msg": "Olá! Vi o site e gostaria de fazer uma encomenda.",
        "wa_msg_destaque": "Olá! Vi o site e gostaria de encomendar um naked cake.",
        "place_id": "ChIJGXPDRgDJyJQRZGaMd6Rr_E8",
        "horarios": [("Terça a sexta", "10h às 18h"), ("Sábado", "10h às 13h"), ("Domingo e segunda", "Fechado")],
        "horas_ld": [(["Tuesday", "Wednesday", "Thursday", "Friday"], "10:00", "18:00"), (["Saturday"], "10:00", "13:00")],
        "cores": {"bg": "#F8F6EF", "fg": "#2B3A2E", "muted": "#66705F", "primary": "#5E7F4F", "primary_soft": "#E5EDDC",
                   "accent": "#C7505A", "card": "#FFFFFF", "dark": "#24322A"},
        "fonte_titulo": "Cormorant Garamond", "fonte_texto": "Mulish",
        "hero_img": "1565661834013-d196ca46e14e",
        "hero_legenda": ("Naked cake", "massa leve, recheio generoso e frutas frescas"),
        "destaque": {
            "selo": "Especialidade da casa",
            "titulo": "Naked cakes com frutas frescas",
            "texto": "Camadas aparentes, recheio generoso e frutas por cima. Pistache com frutas vermelhas é um dos sabores que mais encantam quem prova.",
            "botao": "Encomendar um naked cake",
            "img": "1568827999250-3f6afff96e66",
        },
        "cardapio_titulo": "Feito com ingredientes de qualidade",
        "cardapio": [
            ("Naked cakes", "Camadas aparentes, frutas frescas e sabores como pistache com frutas vermelhas.", "1557925923-33b27f891f88"),
            ("Bolos de festa", "No tamanho certo para a sua comemoração.", "1542007920-992d2c424d09"),
            ("Bentô cakes", "Bolinhos individuais e personalizados para presentear.", "1488477304112-4944851de03d"),
            ("Brigadeiros", "Docinhos caprichados para completar a mesa.", "1630953900039-960a64b49176"),
        ],
        "diferenciais_titulo": "Por que os clientes voltam",
        "diferenciais": [
            ("Ingredientes de qualidade", "Sabor que aparece em cada camada."),
            ("Acima das expectativas", "Bolos que surpreendem na aparência e no sabor."),
            ("Clientes recorrentes", "Quem prova costuma voltar para a próxima festa."),
            ("Bem atendido sempre", "Atenção do pedido até a retirada."),
        ],
        "passos": [
            ("Escolha o bolo", "Veja as opções e pense no tamanho da sua festa."),
            ("Chame no WhatsApp", "Combine sabor, data e detalhes da decoração."),
            ("Retire na loja", "Seu bolo pronto no dia combinado."),
        ],
        "dominio_exemplo": "www.dolcenina.com.br",
    },
    {
        "slug": "doce-lar-da-carol",
        "nome": "Doce Lar",
        "nome_longo": "Doce Lar da Carol",
        "nicho": "Confeitaria",
        "nota": "4,9",
        "titulo_seo": "Doce Lar da Carol | Confeitaria no Jardim Nova Europa, Campinas",
        "descricao_seo": "Bolos caprichados, doces e encomendas para o mesmo dia no Jardim Nova Europa, Campinas. Aberto também aos domingos. Nota 4,9 no Google. Peça pelo WhatsApp.",
        "subtitulo": "Bolos feitos com capricho, amor e qualidade, com pedido para o mesmo dia e entrega, no Jardim Nova Europa, Campinas",
        "endereco": "Av. São José dos Campos, 1235 – Jardim Nova Europa, Campinas – SP, CEP 13040-145",
        "rua_curta": "Av. São José dos Campos, 1235 – Jardim Nova Europa",
        "tel_display": "(19) 99255-8282",
        "tel": "5519992558282",
        "wa_msg": "Olá! Vi o site e gostaria de encomendar um bolo.",
        "wa_msg_destaque": "Olá! Vi o site e preciso de um bolo para hoje. Vocês conseguem?",
        "place_id": "ChIJmYUeMnzLyJQRH7OIe0rqb94",
        "horarios": [("Segunda a sábado", "9h às 18h"), ("Domingo", "9h às 16h")],
        "horas_ld": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00", "18:00"), (["Sunday"], "09:00", "16:00")],
        "cores": {"bg": "#FFF8F3", "fg": "#3A2420", "muted": "#7A625A", "primary": "#C8553D", "primary_soft": "#FBE6DC",
                   "accent": "#F2B880", "card": "#FFFFFF", "dark": "#3A2420"},
        "fonte_titulo": "Playfair Display", "fonte_texto": "Nunito",
        "hero_img": "1559553156-2e97137af16f",
        "hero_alt": "Bolo de chocolate com frutas vermelhas",
        "hero_legenda": ("Bolo de brigadeiro", "com morangos e chantininho"),
        "destaque": {
            "selo": "Precisa para hoje?",
            "titulo": "Bolo para o mesmo dia, com entrega",
            "texto": "Esqueceu o aniversário ou surgiu uma visita? Chame no WhatsApp: sempre que a produção permite, o bolo sai no mesmo dia e chega perfeito na sua casa. E aqui abre até aos domingos.",
            "botao": "Pedir um bolo para hoje",
            "img": "1643064207161-bca640dfde4c",
        },
        "cardapio_titulo": "Feito com capricho e amor",
        "cardapio": [
            ("Bolo de brigadeiro", "Brigadeiro preto com morangos e chantininho, um dos queridinhos.", "1702744382319-20efefc9dc19"),
            ("Bolos de festa", "Para aniversários e comemorações em família.", "1542007920-992d2c424d09"),
            ("Bolos caseiros", "Para o café da tarde ou para levar de presente.", "1630953899650-0ee223bb29d6"),
            ("Doces", "Brigadeiros e docinhos para completar a mesa.", "1565814598158-c9e60d235405"),
        ],
        "diferenciais_titulo": "Por que os clientes voltam",
        "diferenciais": [
            ("Capricho e qualidade", "Tudo feito com cuidado, do recheio à decoração."),
            ("Pedido para o mesmo dia", "Sempre que a produção permite, o bolo sai no dia."),
            ("Entrega", "O bolo chega perfeito na sua casa."),
            ("Aberto aos domingos", "Das 9h às 16h, para o almoço de família."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Diga o bolo, o tamanho e para quando precisa."),
            ("Combine os detalhes", "Sabor, recheio, decoração e entrega ou retirada."),
            ("Receba ou retire", "Seu bolo pronto no horário combinado."),
        ],
        "dominio_exemplo": "www.docelardacarol.com.br",
    },
    {
        "slug": "familia-pet",
        "nome": "Família Pet",
        "nome_longo": "Família Pet Campinas · Banho e Tosa",
        "nicho": "Pet",
        "ld_type": "PetStore",
        "cta": "Agendar pelo WhatsApp",
        "sec_btn": "Ver serviços",
        "sec_eyebrow": "Serviços",
        "sec_lead": "Consulte valores e horários pelo WhatsApp.",
        "como_eyebrow": "Como agendar",
        "favicon": "%F0%9F%90%BE",
        "titulo_seo": "Família Pet Campinas | Banho e tosa com busca e entrega no Jardim Campos Elíseos",
        "descricao_seo": "Banho e tosa com carinho, busca e entrega do seu pet no Jardim Campos Elíseos, Campinas. Estrutura limpa e segura. Nota 5,0 no Google. Agende pelo WhatsApp.",
        "subtitulo": "Banho e tosa com carinho, busca e entrega do seu pet e uma estrutura limpa e segura, no Jardim Campos Elíseos, Campinas",
        "endereco": "Rua Silvio Rizzardo, 132 – Jardim Campos Elíseos, Campinas – SP, CEP 13060-871",
        "rua_curta": "Rua Silvio Rizzardo, 132 – Jardim Campos Elíseos",
        "tel_display": "(19) 99999-4225",
        "tel": "5519999994225",
        "wa_msg": "Olá! Vi o site e gostaria de agendar um banho e tosa.",
        "wa_msg_destaque": "Olá! Vi o site e gostaria de agendar um banho com busca e entrega.",
        "place_id": "ChIJ5YnbKRvJyJQRRyOmtBCF98g",
        "horarios": [("Terça a sábado", "9h às 18h"), ("Domingo e segunda", "Fechado")],
        "horas_ld": [(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00", "18:00")],
        "cores": {"bg": "#F4FAFB", "fg": "#17323A", "muted": "#57707A", "primary": "#2A8C9A", "primary_soft": "#DDF1F3",
                   "accent": "#FFB86B", "card": "#FFFFFF", "dark": "#17323A"},
        "fonte_titulo": "Baloo 2", "fonte_titulo_eixos": "wght@500;600;700;800", "fonte_texto": "Nunito Sans",
        "hero_img": "1698313790088-c59e134c75e8",
        "hero_alt": "Cachorro enrolado na toalha depois do banho",
        "hero_legenda": ("Cheiroso e feliz", "e sem estresse do começo ao fim"),
        "destaque": {
            "selo": "Comodidade para você",
            "titulo": "Buscamos e levamos o seu pet",
            "texto": "Você não precisa sair de casa: o seu pet é buscado, toma o banho com todo o cuidado e volta cheiroso e tranquilo. Pergunte pelo WhatsApp se a sua região é atendida.",
            "botao": "Agendar com busca e entrega",
            "img": "1534361960057-19889db9621e",
        },
        "cardapio_titulo": "Cuidado completo para o seu pet",
        "cardapio": [
            ("Banho", "Banho caprichado para o seu pet voltar limpinho e cheiroso.", "1583534778255-5d67d3dcf95d"),
            ("Secagem e escovação", "Feitas com calma, no ritmo do seu pet.", "1611173622933-91942d394b04"),
            ("Tosa", "Tosa do jeito que você pedir, com acabamento caprichado.", "1772437883387-8076cf660c65"),
            ("Busca e entrega", "O seu pet vai e volta sem você precisar sair de casa.", "1733964659477-35534815c626"),
        ],
        "diferenciais_titulo": "Por que os tutores confiam",
        "diferenciais": [
            ("Sem estresse", "O pet volta tranquilo, cheiroso e feliz."),
            ("Estrutura limpa e segura", "Espaço organizado e bem equipado."),
            ("Profissionais capacitados", "Banho e tosa feitos do jeito que você pediu."),
            ("Busca e entrega", "Comodidade do começo ao fim."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Conte qual é o seu pet e o serviço que ele precisa."),
            ("Escolha dia e horário", "Combine também se quer a busca e entrega."),
            ("Pet de volta, cheiroso", "Limpinho, feliz e sem estresse."),
        ],
        "dominio_exemplo": "www.familiapetcampinas.com.br",
    },
    {
        "slug": "studio-pet-campinas",
        "nome": "Studio Pet",
        "nome_longo": "Studio Pet Campinas · Banho e Tosa",
        "nicho": "Pet",
        "ld_type": "PetStore",
        "cta": "Agendar pelo WhatsApp",
        "sec_btn": "Ver serviços",
        "sec_eyebrow": "Serviços",
        "sec_lead": "Valores por porte do pet. Consulte pelo WhatsApp.",
        "como_eyebrow": "Como agendar",
        "favicon": "%F0%9F%90%BE",
        "nota": "5,0",
        "titulo_seo": "Studio Pet Campinas | Banho e tosa com leva e traz no Jardim Nova Europa",
        "descricao_seo": "Banho e tosa individual e carinhoso, com leva e traz do seu pet, no Jardim Nova Europa, Campinas. Nota 5,0 no Google. Agende pelo WhatsApp.",
        "subtitulo": "Banho e tosa com atendimento individual, carinho e pontualidade, com leva e traz do seu pet, no Jardim Nova Europa, Campinas",
        "endereco": "Av. Baden Powell, 1621 – Jardim Nova Europa, Campinas – SP, CEP 13040-093",
        "rua_curta": "Av. Baden Powell, 1621 – Jardim Nova Europa",
        "tel_display": "(19) 99799-0109",
        "tel": "5519997990109",
        "wa_msg": "Olá! Vi o site e gostaria de agendar um banho e tosa.",
        "wa_msg_destaque": "Olá! Vi o site e gostaria de agendar um banho com leva e traz.",
        "place_id": "ChIJBVdDPQLPyJQRvfpymL4R-5o",
        "horarios": [("Segunda", "10h às 17h"), ("Terça a sexta", "9h às 17h"), ("Sábado", "9h às 16h"), ("Domingo", "Fechado")],
        "horas_ld": [(["Monday"], "10:00", "17:00"), (["Tuesday", "Wednesday", "Thursday", "Friday"], "09:00", "17:00"), (["Saturday"], "09:00", "16:00")],
        "cores": {"bg": "#F8F6FC", "fg": "#2A2140", "muted": "#6A6080", "primary": "#6C4FC2", "primary_soft": "#ECE6FA",
                   "accent": "#FFC857", "card": "#FFFFFF", "dark": "#2A2140"},
        "fonte_titulo": "Fredoka", "fonte_titulo_eixos": "wght@500;600;700", "fonte_texto": "Nunito Sans",
        "hero_img": "1583534778255-5d67d3dcf95d",
        "hero_alt": "Cachorro tomando banho",
        "hero_legenda": ("Banho individual", "um pet por vez, sem pressa"),
        "destaque": {
            "selo": "Leva e traz",
            "titulo": "A gente busca e devolve o seu pet",
            "texto": "Você não precisa sair de casa nem mudar a sua rotina: o seu pet é buscado, cuidado com atenção individual e volta limpinho e feliz. Pergunte pelo WhatsApp se a sua região é atendida.",
            "botao": "Agendar com leva e traz",
            "img": "1733964659477-35534815c626",
        },
        "cardapio_titulo": "Cuidado individual para o seu pet",
        "cardapio": [
            ("Banho", "Banho caprichado, com produtos adequados ao pelo do seu pet.", "1698313790088-c59e134c75e8"),
            ("Tosa", "Tosa do jeito que você pedir, com paciência até com os mais agitados.", "1772437883387-8076cf660c65"),
            ("Secagem e escovação", "Com calma e no ritmo do seu pet.", "1611173622933-91942d394b04"),
            ("Leva e traz", "Buscamos e devolvemos o seu pet no horário combinado.", "1534361960057-19889db9621e"),
        ],
        "diferenciais_titulo": "Por que os tutores voltam",
        "diferenciais": [
            ("Atendimento individual", "Cada pet recebe atenção só para ele."),
            ("Pontualidade", "Busca e entrega no horário combinado."),
            ("Espaço limpinho", "Ambiente organizado e cuidado todos os dias."),
            ("Preço por porte", "Você sabe quanto vai pagar antes de agendar."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Conte o porte do seu pet e o serviço que ele precisa."),
            ("Combine o leva e traz", "Escolha dia, horário e se quer a busca em casa."),
            ("Pet de volta, feliz", "Limpinho, cheiroso e bem tratado."),
        ],
        "dominio_exemplo": "www.studiopetcampinas.com.br",
    },
    {
        "slug": "caoamor-pet-spa",
        "nome": "Cãoamor",
        "nome_longo": "Cãoamor Pet Spa · Banho e Tosa",
        "nicho": "Pet",
        "ld_type": "PetStore",
        "cta": "Agendar pelo WhatsApp",
        "sec_btn": "Ver serviços",
        "sec_eyebrow": "Serviços",
        "sec_lead": "Consulte valores e horários pelo WhatsApp.",
        "como_eyebrow": "Como agendar",
        "favicon": "%F0%9F%90%BE",
        "nota": "4,9",
        "titulo_seo": "Cãoamor Pet Spa | Banho e tosa na tesoura no Jardim Estoril, Campinas",
        "descricao_seo": "Pet spa com banho, tosa na tesoura e cuidado especial com pets sensíveis e idosos, no Jardim Estoril, Campinas. Aberto a partir das 7h. Nota 4,9 no Google.",
        "subtitulo": "Banho, tosa na tesoura e muito carinho, com cuidado especial para pets sensíveis e idosos, no Jardim Estoril, Campinas",
        "endereco": "R. Fernando de Almeida Batista, 174 – Jardim Estoril, Campinas – SP, CEP 13101-203",
        "rua_curta": "R. Fernando de Almeida Batista, 174 – Jardim Estoril",
        "tel_display": "(19) 99479-3962",
        "tel": "5519994793962",
        "wa_msg": "Olá! Vi o site e gostaria de agendar um banho e tosa.",
        "wa_msg_destaque": "Olá! Vi o site e gostaria de agendar um horário logo cedo, antes do trabalho.",
        "place_id": "ChIJK12gP97PyJQR41bhCuP30eE",
        "horarios": [("Segunda a sexta", "7h às 18h"), ("Sábado", "7h às 17h"), ("Domingo", "Fechado")],
        "horas_ld": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "07:00", "18:00"), (["Saturday"], "07:00", "17:00")],
        "cores": {"bg": "#FFF7F6", "fg": "#3B2228", "muted": "#7D6066", "primary": "#C4506A", "primary_soft": "#FBE4E8",
                   "accent": "#8CC5B0", "card": "#FFFFFF", "dark": "#3B2228"},
        "fonte_titulo": "Playfair Display", "fonte_texto": "Nunito Sans",
        "hero_img": "1698313790088-c59e134c75e8",
        "hero_alt": "Cachorro enrolado na toalha depois do banho",
        "hero_legenda": ("Volta lindo e perfumado", "e saindo todo feliz"),
        "destaque": {
            "selo": "Abre às 7h",
            "titulo": "Deixe o seu pet antes do trabalho",
            "texto": "Abrimos às 7h de segunda a sábado: você deixa o seu pet a caminho do trabalho e busca no fim do dia, limpinho e perfumado. Pets sensíveis e idosos recebem um cuidado ainda mais calmo.",
            "botao": "Agendar logo cedo",
            "img": "1611173622933-91942d394b04",
        },
        "cardapio_titulo": "Um spa feito com carinho",
        "cardapio": [
            ("Banho", "Banho caprichado para o seu pet voltar limpinho e perfumado.", "1583534778255-5d67d3dcf95d"),
            ("Tosa na tesoura", "Acabamento feito à mão, para o pet voltar realmente bonito.", "1772437883387-8076cf660c65"),
            ("Pets sensíveis e idosos", "Atendimento calmo, com pausas e muita paciência.", "1534361960057-19889db9621e"),
            ("Hidratação e cuidados", "Pelos macios, unhas e ouvidos cuidados.", "1733964659477-35534815c626"),
        ],
        "diferenciais_titulo": "Por que os tutores indicam",
        "diferenciais": [
            ("Carinho de verdade", "O seu pet é tratado como da família."),
            ("Tosa na tesoura", "Acabamento caprichado, feito à mão."),
            ("Abre às 7h", "Dá para deixar o pet antes do trabalho."),
            ("Cuidado com idosos", "Paciência extra para pets sensíveis."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Conte qual é o seu pet e o serviço que ele precisa."),
            ("Escolha o horário", "Inclusive logo cedo, a partir das 7h."),
            ("Pet lindo e feliz", "Volta limpinho, perfumado e tranquilo."),
        ],
        "dominio_exemplo": "www.caoamorpetspa.com.br",
    },
    {
        "slug": "studio-caroline-gomes-lash",
        "nome": "Caroline Gomes",
        "nome_longo": "Studio Caroline Gomes Lash · Cílios e Sobrancelhas",
        "nicho": "Cílios",
        "ld_type": "BeautySalon",
        "cta": "Agendar pelo WhatsApp",
        "sec_btn": "Ver procedimentos",
        "sec_eyebrow": "Procedimentos",
        "sec_lead": "Consulte valores e horários disponíveis pelo WhatsApp.",
        "como_eyebrow": "Como agendar",
        "favicon": "%E2%9C%A8",
        "nota": "5,0",
        "titulo_seo": "Studio Caroline Gomes Lash | Cílios e sobrancelhas no Jardim Andorinhas, Campinas",
        "descricao_seo": "Extensão de cílios e design de sobrancelhas feitos com capricho e materiais de qualidade, no Jardim Andorinhas, Campinas. Nota 5,0 em 82 avaliações no Google.",
        "subtitulo": "Extensão de cílios e sobrancelhas do jeitinho que você quer, com materiais de qualidade e um espaço aconchegante, no Jardim Andorinhas, Campinas",
        "endereco": "Av. das Andorinhas, 377 – Jardim Andorinhas, Campinas – SP, CEP 13040-093",
        "rua_curta": "Av. das Andorinhas, 377 – Jardim Andorinhas",
        "tel_display": "(19) 99726-6523",
        "tel": "5519997266523",
        "wa_msg": "Olá! Vi o site e gostaria de agendar um horário.",
        "wa_msg_destaque": "Olá! Vi o site e é a minha primeira vez. Pode me ajudar a escolher o efeito dos cílios?",
        "place_id": "ChIJdeZFXgDPyJQR1lzcXopVD6o",
        "horarios": [("Terça a sábado", "9h às 19h"), ("Domingo e segunda", "Fechado")],
        "horas_ld": [(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00", "19:00")],
        "cores": {"bg": "#FBF7F4", "fg": "#2B1F1D", "muted": "#7A6964", "primary": "#A6655A", "primary_soft": "#F4E4DF",
                   "accent": "#D8B26E", "card": "#FFFFFF", "dark": "#2B1F1D"},
        "fonte_titulo": "Cormorant Garamond", "fonte_titulo_eixos": "ital,wght@0,500;0,600;0,700;1,500", "fonte_texto": "Nunito Sans",
        "hero_img": "1589710751893-f9a6770ad71b",
        "hero_alt": "Profissional aplicando extensão de cílios",
        "hero_legenda": ("Do jeitinho que você quer", "e sem incômodo no dia a dia"),
        "destaque": {
            "selo": "Primeira vez?",
            "titulo": "A gente escolhe o efeito com você",
            "texto": "Volume, fio a fio ou mais natural: antes de começar, conversamos sobre o seu olhar e a sua rotina para o resultado ficar exatamente como você imaginou. Muitas clientes chegam depois de não se acertarem em outros lugares.",
            "botao": "Quero tirar dúvidas",
            "img": "1683719312734-e31de63957ab",
        },
        "cardapio_titulo": "Cuidado em cada detalhe",
        "cardapio": [
            ("Extensão de cílios", "Fio a fio, volume e efeitos sob medida para o seu olhar.", "1639629509821-c54cdd984227"),
            ("Manutenção", "Para os cílios continuarem lindos por mais tempo.", "1770999086860-143f54adf01b"),
            ("Design de sobrancelhas", "Desenho que valoriza o seu rosto, com acabamento caprichado.", "1674049406179-d7bf2c263e71"),
            ("Atendimento acolhedor", "Um espaço aconchegante para você relaxar enquanto se cuida.", "1772236617396-2f8460293c07"),
        ],
        "diferenciais_titulo": "Por que as clientes voltam",
        "diferenciais": [
            ("Resultado do seu jeito", "O efeito é combinado antes, sem surpresa."),
            ("Materiais de qualidade", "Conforto e durabilidade no dia a dia."),
            ("Cílios e sobrancelhas", "Tudo no mesmo atendimento."),
            ("Nota 5,0 no Google", "Mais de 80 avaliações de clientes."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Conte o que você quer fazer e tire suas dúvidas."),
            ("Escolha o horário", "De terça a sábado, das 9h às 19h."),
            ("Saia se sentindo linda", "Com o olhar do jeitinho que você queria."),
        ],
        "dominio_exemplo": "www.carolinegomeslash.com.br",
    },
    {
        "slug": "brenda-alves-cilios",
        "nome": "Brenda Alves",
        "nome_longo": "Brenda Alves · Cílios e Sobrancelhas Campinas",
        "nicho": "Cílios",
        "ld_type": "BeautySalon",
        "cta": "Agendar pelo WhatsApp",
        "sec_btn": "Ver procedimentos",
        "sec_eyebrow": "Procedimentos",
        "sec_lead": "Consulte valores e horários disponíveis pelo WhatsApp.",
        "como_eyebrow": "Como agendar",
        "favicon": "%E2%9C%A8",
        "nota": "5,0",
        "titulo_seo": "Brenda Alves | Cílios, lash lifting e sobrancelhas no Jardim Campos Elíseos, Campinas",
        "descricao_seo": "Lash lifting, design de sobrancelhas e recuperação de fios com resultado natural, no Jardim Campos Elíseos, Campinas. Nota 5,0 em 111 avaliações no Google.",
        "subtitulo": "Lash lifting, design de sobrancelhas e recuperação de fios, com resultado natural e muito cuidado, no Jardim Campos Elíseos, Campinas",
        "endereco": "R. Cons. Martim Francisco, 20 – Jardim Campos Elíseos, Campinas – SP, CEP 13060-033",
        "rua_curta": "R. Cons. Martim Francisco, 20 – Jardim Campos Elíseos",
        "tel_display": "(19) 99894-4728",
        "tel": "5519998944728",
        "wa_msg": "Olá! Vi o site e gostaria de agendar um horário.",
        "wa_msg_destaque": "Olá! Vi o site e queria recuperar minhas sobrancelhas. Como funciona o acompanhamento?",
        "place_id": "ChIJoVOR6n7JyJQRUQAKJ3dArUg",
        "horarios": [("Terça a sábado", "9h às 18h"), ("Domingo e segunda", "Fechado")],
        "horas_ld": [(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00", "18:00")],
        "cores": {"bg": "#F5F8FC", "fg": "#1C2A3D", "muted": "#5E6B7D", "primary": "#3E6FB0", "primary_soft": "#E2ECF8",
                   "accent": "#E8B4B8", "card": "#FFFFFF", "dark": "#1C2A3D"},
        "fonte_titulo": "Playfair Display", "fonte_texto": "Nunito Sans",
        "hero_img": "1674049406467-824ea37c7184",
        "hero_alt": "Profissional cuidando dos cílios de uma cliente",
        "hero_legenda": ("Olhar lindo e natural", "nada exagerado, do seu jeito"),
        "destaque": {
            "selo": "Sobrancelhas ralas?",
            "titulo": "Recupere os fios com acompanhamento",
            "texto": "Sobrancelhas falhadas ou sem forma voltam a ficar cheias com um acompanhamento sessão a sessão. A Brenda pergunta como você prefere e cuida de cada detalhe, até o design ficar perfeito.",
            "botao": "Quero recuperar minhas sobrancelhas",
            "img": "1718720410649-7524fcb0f0a5",
        },
        "cardapio_titulo": "Delicadeza em cada procedimento",
        "cardapio": [
            ("Lash lifting", "Cílios curvados e alongados, com efeito natural e sem extensão.", "1683719312734-e31de63957ab"),
            ("Design de sobrancelhas", "Limpinho, alinhado e pensado para o seu rosto.", "1674049406179-d7bf2c263e71"),
            ("Recuperação de fios", "Acompanhamento para sobrancelhas ralas voltarem a encher.", "1718720410649-7524fcb0f0a5"),
            ("Extensão de cílios", "Para quem quer um olhar marcante no dia a dia.", "1639629509821-c54cdd984227"),
        ],
        "diferenciais_titulo": "Por que as clientes indicam",
        "diferenciais": [
            ("Resultado natural", "Nada superficial: o seu olhar, só que mais bonito."),
            ("Atendimento do seu jeito", "A Brenda pergunta como você prefere antes de começar."),
            ("Espaço aconchegante", "Organizado, limpinho e pensado para você relaxar."),
            ("Nota 5,0 no Google", "Mais de 110 avaliações de clientes."),
        ],
        "passos": [
            ("Chame no WhatsApp", "Conte o procedimento que você quer fazer."),
            ("Escolha o horário", "De terça a sábado, das 9h às 18h."),
            ("Saia com o olhar renovado", "Natural, delicado e do seu jeito."),
        ],
        "dominio_exemplo": "www.brendaalvescilios.com.br",
    },
]


def e(s):
    return html.escape(s, quote=True)


def wa(n, msg):
    return f"https://wa.me/{n['tel']}?text={urllib.parse.quote(msg)}"


def fonts_link(n):
    fams = []
    for f, w in ((n["fonte_titulo"], n.get("fonte_titulo_eixos", "ital,wght@0,500;0,600;0,700;1,500")), (n["fonte_texto"], "wght@400;600;700;800")):
        fams.append("family=" + f.replace(" ", "+") + ":" + w)
    return "https://fonts.googleapis.com/css2?" + "&".join(fams) + "&display=swap"


def css(n):
    c = n["cores"]
    return f"""
:root{{--bg:{c['bg']};--fg:{c['fg']};--muted:{c['muted']};--primary:{c['primary']};--primary-soft:{c['primary_soft']};--accent:{c['accent']};--card:{c['card']};--dark:{c['dark']};--wa:#1FA855;--radius:22px;--ft:'{n['fonte_titulo']}',Georgia,serif;--fb:'{n['fonte_texto']}',system-ui,sans-serif}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--fg);font-family:var(--fb);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}}
img{{max-width:100%;display:block}}a{{color:inherit}}h1,h2,h3{{font-family:var(--ft);line-height:1.08;margin:0;font-weight:600;letter-spacing:-.01em}}
.wrap{{width:min(1120px,100% - 40px);margin-inline:auto}}
.strip{{background:var(--dark);color:#fff;text-align:center;font-size:12px;padding:6px 12px;letter-spacing:.02em;opacity:.95}}
.eyebrow{{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--primary)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-weight:800;font-size:16px;text-decoration:none;border-radius:999px;padding:16px 26px;transition:transform .2s,box-shadow .2s;border:0;cursor:pointer}}
.btn:hover{{transform:translateY(-2px)}}.btn-wa{{background:var(--wa);color:#fff;box-shadow:0 12px 28px -12px rgba(31,168,85,.7)}}
.btn-ghost{{background:transparent;color:var(--fg);border:2px solid color-mix(in srgb,var(--fg) 18%,transparent)}}
.btn-light{{background:#fff;color:var(--dark)}}
.btn svg{{width:20px;height:20px;flex:none}}
.badge{{display:inline-flex;align-items:center;gap:6px;background:var(--card);border:1px solid color-mix(in srgb,var(--fg) 10%,transparent);border-radius:999px;padding:6px 14px;font-weight:800;font-size:14px;text-decoration:none}}
.badge .star{{color:#F4B400}}
header.hero{{position:relative;overflow:hidden;background:radial-gradient(1200px 500px at 85% 10%,var(--primary-soft),transparent 60%),radial-gradient(800px 400px at 0% 100%,color-mix(in srgb,var(--accent) 22%,transparent),transparent 70%)}}
.hero-grid{{display:grid;gap:40px;align-items:center;padding:36px 0 72px}}
.brand{{display:flex;align-items:center;gap:10px;font-family:var(--ft);font-size:22px;font-weight:700;margin-bottom:28px}}
.brand i{{width:38px;height:38px;border-radius:50%;background:var(--primary);display:grid;place-items:center;color:#fff;font-style:normal;font-size:18px}}
.hero h1{{font-size:clamp(44px,9vw,84px);margin:18px 0 14px}}.hero h1 em{{color:var(--primary);font-style:italic}}
.hero p.lead{{font-size:clamp(17px,2.4vw,20px);color:var(--muted);max-width:34ch;margin:0 0 28px}}
.ctas{{display:flex;flex-wrap:wrap;gap:12px}}
.addr{{display:flex;gap:8px;align-items:flex-start;margin-top:22px;color:var(--muted);font-size:14px}}
.hero-art{{position:relative;max-width:480px;margin-inline:auto;width:100%}}
.hero-art .blob{{position:absolute;inset:-14px;border-radius:44% 56% 52% 48%/48% 42% 58% 52%;background:var(--accent);opacity:.35;transform:rotate(-6deg);animation:morph 12s ease-in-out infinite}}
.hero-art img{{position:relative;border-radius:36px;aspect-ratio:4/5;object-fit:cover;width:100%;box-shadow:0 30px 60px -30px rgba(0,0,0,.45)}}
.hero-art .tag{{position:absolute;left:-10px;bottom:22px;background:var(--card);border-radius:18px;padding:12px 16px;box-shadow:0 14px 30px -14px rgba(0,0,0,.35);max-width:240px;animation:float 5s ease-in-out infinite}}
.hero-art .tag b{{display:block;font-family:var(--ft);font-size:18px}}.hero-art .tag span{{font-size:13px;color:var(--muted)}}
@keyframes float{{50%{{transform:translateY(-8px)}}}}@keyframes morph{{50%{{border-radius:56% 44% 40% 60%/52% 60% 40% 48%;transform:rotate(4deg)}}}}
section{{padding:84px 0}}.center{{text-align:center}}.sec-title{{font-size:clamp(34px,5.6vw,52px);margin:10px 0 12px}}.sec-lead{{color:var(--muted);max-width:52ch;margin:0 auto}}
.feature{{background:var(--dark);color:#fff;border-radius:36px;overflow:hidden;display:grid}}
.feature img{{width:100%;height:100%;min-height:280px;object-fit:cover}}.feature .txt{{padding:40px 32px}}
.feature .pill{{display:inline-block;background:color-mix(in srgb,#fff 14%,transparent);border-radius:999px;padding:6px 14px;font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}}
.feature h2{{font-size:clamp(32px,5vw,48px);margin:16px 0 12px}}.feature p{{opacity:.85;margin:0 0 26px}}
.cards{{display:grid;gap:20px;margin-top:44px}}
.card{{background:var(--card);border-radius:var(--radius);overflow:hidden;box-shadow:0 18px 40px -28px rgba(0,0,0,.35);transition:transform .3s}}.card:hover{{transform:translateY(-6px)}}
.card img{{aspect-ratio:4/3;object-fit:cover;width:100%}}.card div{{padding:20px 22px 24px}}.card h3{{font-size:26px}}.card p{{margin:6px 0 0;color:var(--muted);font-size:15px}}
.note{{margin-top:26px;text-align:center;color:var(--muted);font-size:15px}}
.why{{background:var(--primary-soft)}}.grid4{{display:grid;gap:16px;margin-top:40px}}
.why .item{{background:var(--card);border-radius:var(--radius);padding:24px}}.why .num{{font-family:var(--ft);font-size:40px;color:var(--primary);line-height:1}}
.why h3{{font-size:24px;margin-top:10px}}.why p{{margin:6px 0 0;color:var(--muted);font-size:15px}}
.rating{{margin-top:28px;display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:center;background:var(--card);border-radius:var(--radius);padding:18px 22px}}
.rating b{{font-family:var(--ft);font-size:26px}}.rating .stars{{color:#F4B400;letter-spacing:2px;font-size:20px}}
.steps{{display:grid;gap:18px;margin-top:40px;counter-reset:s}}
.step{{position:relative;background:var(--card);border-radius:var(--radius);padding:30px 24px 24px;box-shadow:0 18px 40px -30px rgba(0,0,0,.3)}}
.step:before{{counter-increment:s;content:counter(s);position:absolute;top:-16px;left:22px;width:38px;height:38px;border-radius:50%;background:var(--primary);color:#fff;display:grid;place-items:center;font-weight:800}}
.step h3{{font-size:24px}}.step p{{margin:6px 0 0;color:var(--muted);font-size:15px}}
.loc{{display:grid;gap:20px;margin-top:40px}}.map{{border-radius:var(--radius);overflow:hidden;min-height:320px;background:#ddd}}.map iframe{{border:0;width:100%;height:100%;min-height:320px}}
.info{{background:var(--card);border-radius:var(--radius);padding:26px;display:flex;flex-direction:column;gap:18px}}
.info h3{{font-size:22px}}.info p{{margin:4px 0 0;color:var(--muted)}}
.hours{{width:100%;border-collapse:collapse;margin-top:6px}}.hours td{{padding:7px 0;border-bottom:1px dashed color-mix(in srgb,var(--fg) 15%,transparent)}}.hours td:last-child{{text-align:right;font-weight:700}}
footer{{background:var(--dark);color:#fff;padding:48px 0 110px;text-align:center}}footer h3{{font-size:28px}}footer p{{opacity:.8;margin:6px 0}}footer small{{display:block;margin-top:26px;opacity:.55}}
.fab{{position:fixed;right:18px;bottom:18px;z-index:50;width:62px;height:62px;border-radius:50%;background:var(--wa);display:grid;place-items:center;box-shadow:0 14px 30px -10px rgba(0,0,0,.4)}}
.fab svg{{width:32px;height:32px;fill:#fff}}.fab:after{{content:"";position:absolute;inset:0;border-radius:50%;border:2px solid var(--wa);animation:ring 2.2s infinite}}
@keyframes ring{{from{{transform:scale(1);opacity:.8}}to{{transform:scale(1.6);opacity:0}}}}
.reveal{{opacity:0;transform:translateY(26px);transition:opacity .8s ease,transform .8s ease}}.reveal.in{{opacity:1;transform:none}}
@media (min-width:720px){{.cards{{grid-template-columns:repeat(2,1fr)}}.grid4{{grid-template-columns:repeat(2,1fr)}}.steps{{grid-template-columns:repeat(3,1fr)}}}}
@media (min-width:960px){{.hero-grid{{grid-template-columns:1.05fr .95fr;padding:48px 0 96px}}.feature{{grid-template-columns:1fr 1fr}}.feature .txt{{padding:64px 56px;align-self:center}}.cards{{grid-template-columns:repeat(4,1fr)}}.grid4{{grid-template-columns:repeat(4,1fr)}}.loc{{grid-template-columns:1.4fr 1fr}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.reveal{{opacity:1;transform:none}}}}
"""


WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.2-3.8 1.2 1.2-3.7-.3-.4c-1.2-1.8-1.8-3.8-1.8-5.9C5 9.9 9.9 5.1 16 5.1S27 9.9 27 15.8 22.1 26.4 16 26.4zm6-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'


def head(n, title, desc, url, image, extra=""):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="{n['cores']['dark']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts_link(n)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E{n.get('favicon', '%F0%9F%8E%82')}%3C/text%3E%3C/svg%3E">
<style>{css(n)}</style>
{extra}
</head>
"""


REVEAL_JS = """<script>
(function(){var els=document.querySelectorAll('.reveal');if(!('IntersectionObserver' in window)){els.forEach(function(x){x.classList.add('in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.12});els.forEach(function(x){io.observe(x)})})();
</script>"""


def pagina_index(n):
    url = f"{BASE_URL}/{n['slug']}/"
    og = U.format(n["hero_img"], 1200) + "&h=630"
    wa_main = wa(n, n["wa_msg"])
    wa_dest = wa(n, n["wa_msg_destaque"])
    maps_q = urllib.parse.quote(n["endereco"])
    reviews = f"https://www.google.com/maps/place/?q=place_id:{n['place_id']}"
    ld = {
        "@context": "https://schema.org", "@type": n.get("ld_type", "Bakery"), "name": n["nome_longo"], "url": url, "image": og,
        "telephone": "+" + n["tel"],
        "address": {"@type": "PostalAddress", "streetAddress": n["endereco"].split(" – ")[0],
                    "addressLocality": "Campinas", "addressRegion": "SP", "postalCode": n["endereco"].split("CEP ")[1], "addressCountry": "BR"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c} for d, o, c in n["horas_ld"]],
    }
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    cards = "".join(
        f'<article class="card reveal" style="transition-delay:{i*80}ms"><img loading="lazy" src="{U.format(img, 640)}" alt="{e(t)}" width="640" height="480"><div><h3>{e(t)}</h3><p>{e(d)}</p></div></article>'
        for i, (t, d, img) in enumerate(n["cardapio"]))
    why = "".join(
        f'<div class="item reveal" style="transition-delay:{i*80}ms"><div class="num">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (t, d) in enumerate(n["diferenciais"]))
    steps = "".join(f'<div class="step reveal"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in n["passos"])
    hours = "".join(f"<tr><td>{e(d)}</td><td>{e(h)}</td></tr>" for d, h in n["horarios"])
    nome_parts = n["nome"].split(" ", 1)
    h1 = e(nome_parts[0]) + (f" <em>{e(nome_parts[1])}</em>" if len(nome_parts) > 1 else "")
    d = n["destaque"]
    return head(n, n["titulo_seo"], n["descricao_seo"], url, og, extra) + f"""<body>
<div class="strip">Prévia de site criada por Porta Ad Omnia</div>
<header class="hero">
  <div class="wrap hero-grid">
    <div class="reveal in">
      <div class="brand"><i>✦</i>{e(n['nome_longo'])}</div>
      <a class="badge" href="{reviews}" target="_blank" rel="noopener"><span class="star">★</span> {n.get('nota', '5,0')} no Google</a>
      <h1>{h1}</h1>
      <p class="lead">{e(n['subtitulo'])}</p>
      <div class="ctas">
        <a class="btn btn-wa" href="{wa_main}" target="_blank" rel="noopener">{WA_SVG} {e(n.get('cta', 'Encomendar pelo WhatsApp'))}</a>
        <a class="btn btn-ghost" href="#cardapio">{e(n.get('sec_btn', 'Ver cardápio'))}</a>
      </div>
      <p class="addr">📍 {e(n['rua_curta'])}, Campinas</p>
    </div>
    <div class="hero-art reveal in">
      <div class="blob"></div>
      <img src="{U.format(n['hero_img'], 900)}" alt="{e(n.get('hero_alt', 'Bolo da ' + n['nome']))}" width="900" height="1125" fetchpriority="high">
      <div class="tag"><b>{e(n['hero_legenda'][0])}</b><span>{e(n['hero_legenda'][1])}</span></div>
    </div>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="feature reveal">
        <img loading="lazy" src="{U.format(d['img'], 900)}" alt="{e(d['titulo'])}" width="900" height="900">
        <div class="txt">
          <span class="pill">{e(d['selo'])}</span>
          <h2>{e(d['titulo'])}</h2>
          <p>{e(d['texto'])}</p>
          <a class="btn btn-light" href="{wa_dest}" target="_blank" rel="noopener">{WA_SVG} {e(d['botao'])}</a>
        </div>
      </div>
    </div>
  </section>
  <section id="cardapio" style="padding-top:20px">
    <div class="wrap center">
      <div class="eyebrow">{e(n.get('sec_eyebrow', 'Cardápio'))}</div>
      <h2 class="sec-title">{e(n['cardapio_titulo'])}</h2>
      <p class="sec-lead">{e(n.get('sec_lead', 'Tudo sob encomenda. Consulte sabores e valores pelo WhatsApp.'))}</p>
      <div class="cards">{cards}</div>
      <p class="note">Fotos ilustrativas.</p>
    </div>
  </section>
  <section class="why">
    <div class="wrap center">
      <div class="eyebrow">Avaliações</div>
      <h2 class="sec-title">{e(n['diferenciais_titulo'])}</h2>
      <div class="grid4" style="text-align:left">{why}</div>
      <div class="rating reveal"><span class="stars">★★★★★</span><b>Nota {n.get('nota', '5,0')} no Google</b><a class="btn btn-ghost" style="padding:10px 18px;font-size:14px" href="{reviews}" target="_blank" rel="noopener">Ver avaliações no Google</a></div>
    </div>
  </section>
  <section>
    <div class="wrap center">
      <div class="eyebrow">{e(n.get('como_eyebrow', 'Como encomendar'))}</div>
      <h2 class="sec-title">Em 3 passos</h2>
      <div class="steps" style="text-align:left">{steps}</div>
      <div style="margin-top:34px"><a class="btn btn-wa" href="{wa_main}" target="_blank" rel="noopener">{WA_SVG} Falar no WhatsApp</a></div>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="center"><div class="eyebrow">Onde estamos</div><h2 class="sec-title">Localização e horário</h2></div>
      <div class="loc">
        <div class="map reveal"><iframe title="Mapa {e(n['nome'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={maps_q}&output=embed"></iframe></div>
        <div class="info reveal">
          <div><h3>Endereço</h3><p>{e(n['endereco'])}</p></div>
          <div><h3>Horário</h3><table class="hours">{hours}</table></div>
          <a class="btn btn-ghost" href="https://www.google.com/maps/dir/?api=1&destination={maps_q}" target="_blank" rel="noopener">Como chegar</a>
          <a class="btn btn-wa" href="{wa_main}" target="_blank" rel="noopener">{WA_SVG} {e(n['tel_display'])}</a>
        </div>
      </div>
    </div>
  </section>
</main>
<footer>
  <div class="wrap">
    <h3>{e(n['nome_longo'])}</h3>
    <p>{e(n['endereco'])}</p>
    <p>WhatsApp: <a href="{wa_main}" target="_blank" rel="noopener">{e(n['tel_display'])}</a></p>
    <small>Site criado por Porta Ad Omnia</small>
  </div>
</footer>
<a class="fab" href="{wa_main}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{WA_SVG}</a>
{REVEAL_JS}
</body>
</html>
"""


def pagina_opcoes(n):
    url = f"{BASE_URL}/{n['slug']}/opcoes/"
    og = U.format(n["hero_img"], 1200) + "&h=630"
    gratis = f"renatomatosbr-portaadomnia.github.io/{n['slug']}"
    passos = [
        "Acesse registro.br e pesquise o nome desejado.",
        "Se estiver disponível, clique em “Registrar” e crie sua conta com seu CPF ou CNPJ.",
        "Pague a taxa anual de R$ 40 pelas formas de pagamento do próprio site.",
        "Me avise: configuramos juntos o endereço para abrir o seu site em até 48h. Você não precisa me passar sua senha.",
    ]
    incl = ["Cadeado de segurança (HTTPS)", "Botão de WhatsApp com mensagem pronta", "Mapa e horário", "Ajustes de fotos e textos antes de publicar"]
    passos_html = "".join(f'<li class="step reveal"><p style="margin:0;color:var(--fg)">{e(p)}</p></li>' for p in passos)
    incl_html = "".join(f'<div class="item reveal"><div class="num">✓</div><p style="color:var(--fg);font-weight:700">{e(i)}</p></div>' for i in incl)

    def opcao(rotulo, titulo, ex, nota, linhas, bullets, rec):
        borda = "border:3px solid var(--primary);" if rec else ""
        selo = '<span style="position:absolute;top:-14px;right:22px;background:var(--primary);color:#fff;border-radius:999px;padding:5px 14px;font-size:12px;font-weight:800">★ Recomendado</span>' if rec else ""
        ls = "".join(f'<tr><td>{e(a)}{("<br><small style=color:var(--muted)>" + e(b) + "</small>") if b else ""}</td><td>{e(v)}</td></tr>' for a, v, b in linhas)
        bs = "".join(f"<li>{e(b)}</li>" for b in bullets)
        return f"""<article class="card reveal" style="position:relative;overflow:visible;{borda}"><div style="padding:30px 26px">{selo}
<div class="eyebrow">{e(rotulo)}</div><h2 style="font-size:34px;margin:6px 0 16px">{e(titulo)}</h2>
<div style="background:var(--primary-soft);border-radius:16px;padding:12px 16px"><small style="color:var(--muted)">Exemplo de endereço</small><div style="font-weight:800;word-break:break-all">{e(ex)}</div>{('<small style="color:var(--muted)">' + e(nota) + '</small>') if nota else ''}</div>
<table class="hours" style="margin-top:14px">{ls}</table>
<ul style="margin:16px 0 0;padding-left:20px;color:var(--muted)">{bs}</ul></div></article>"""

    o1 = opcao("Opção 1", "Endereço gratuito", gratis, "",
               [("Custo do endereço", "R$ 0", ""), ("Hospedagem", "R$ 0", "")],
               ["Site no ar sem custo de domínio", "Ideal para começar e testar", "Dá para trocar por um domínio próprio depois, sem refazer o site"], False)
    o2 = opcao("Opção 2", "Domínio próprio", n["dominio_exemplo"], "sujeito a disponibilidade",
               [("Domínio", "R$ 40 por ano", "pago direto ao Registro.br"), ("Hospedagem", "R$ 0", "")],
               ["Endereço profissional, fácil de lembrar e de divulgar", "O domínio fica no seu nome (CPF ou CNPJ): ele é seu", "Renovação anual direto com o Registro.br, sem intermediário"], True)
    return head(n, f"Como colocar o seu site no ar | Proposta para {n['nome_longo']}",
                "Proposta da Porta Ad Omnia: endereço gratuito ou domínio próprio. Hospedagem gratuita nas duas opções.", url, og) + f"""<body>
<div class="strip">Porta Ad Omnia · Proposta para {e(n['nome_longo'])}</div>
<header class="hero"><div class="wrap center" style="padding:64px 0 40px">
<div class="eyebrow">Proposta</div><h1 style="font-size:clamp(40px,8vw,72px);margin:14px 0">Como colocar o seu <em style="color:var(--primary)">site</em> no ar</h1>
<p class="sec-lead" style="font-size:19px">O site já está pronto. Você só escolhe o endereço. A hospedagem é gratuita nas duas opções.</p></div></header>
<main>
<section style="padding-top:20px"><div class="wrap"><div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:34px">{o1}{o2}</div></div></section>
<section class="why"><div class="wrap"><div class="center"><div class="eyebrow">Passo a passo</div><h2 class="sec-title">Como registrar o domínio próprio (Opção 2)</h2></div>
<ol class="steps" style="list-style:none;padding:0;grid-template-columns:1fr;max-width:760px;margin-inline:auto">{passos_html}</ol></div></section>
<section><div class="wrap center"><div class="eyebrow">Sem custo extra</div><h2 class="sec-title">Incluído nas duas opções</h2>
<div class="grid4 why" style="background:none;text-align:left">{incl_html}</div></div></section>
</main>
<footer><div class="wrap"><p>Porta Ad Omnia · Renato, estudante de Economia da Unicamp · Responda pelo WhatsApp da nossa conversa</p>
<div style="margin-top:20px"><a class="btn btn-light" href="../">← Voltar para a prévia do site</a></div></div></footer>
{REVEAL_JS}
</body>
</html>
"""


ROOT = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow"><title>Porta Ad Omnia</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;font-family:system-ui,sans-serif;background:#141414;color:#f5f5f5;text-align:center;padding:24px}h1{font-family:Georgia,serif;font-weight:500;font-size:40px;margin:0 0 8px}p{opacity:.7}</style></head>
<body><div><h1>Porta Ad Omnia</h1><p>Soluções de inteligência de mercado e vendas para empreendedores.</p></div></body></html>
"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(ROOT)
    open(os.path.join(out, ".nojekyll"), "w").write("")
    open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    for n in NEGOCIOS:
        d = os.path.join(out, n["slug"])
        os.makedirs(os.path.join(d, "opcoes"), exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(pagina_index(n))
        open(os.path.join(d, "opcoes", "index.html"), "w").write(pagina_opcoes(n))
        print("ok", n["slug"])
