INTENCOES = [
    {'nome': 'saudacao',
     'palavras_chave': ['oi', 'ola', 'opa', 'bom dia', 'boa tarde', 'boa noite', 'eai'],
     'resposta': 'Olá! Eu sou o assistente virtual da AgendaServiço. Posso falar sobre nossos serviços, preços, horários e como agendar. Como posso ajudar?'},

    {'nome': 'servicos',
     'palavras_chave': ['servico', 'servicos', 'oferecem', 'oferece', 'fazem', 'faz', 'trabalham', 'tipos'],
     'resposta': 'Nós oferecemos os seguintes serviços: Faxina residencial, Jardinagem e Pequenos reparos. Qual deles você precisa?'},

    {'nome': 'precos',
     'palavras_chave': ['preco', 'precos', 'valor', 'valores', 'quanto', 'custa', 'custo', 'caro'],
     'resposta': 'Os valores partem de R$ 100,00 para pequenos reparos, R$ 120,00 para jardinagem e R$ 150,00 para faxina residencial. O valor final depende do tamanho do serviço.'},

    {'nome': 'agendar',
     'palavras_chave': ['agendar', 'agendamento', 'marcar', 'marca', 'contratar', 'reservar'],
     'resposta': 'Para agendar, faça login na sua conta, clique em "Novo agendamento", escolha o serviço, a data e informe o endereço. É rápido!'},

    {'nome': 'cancelar',
     'palavras_chave': ['cancelar', 'cancela', 'cancelamento', 'desmarcar', 'desmarca'],
     'resposta': 'Você pode cancelar um agendamento na sua lista de agendamentos, abrindo o agendamento e usando a opção de excluir.'},

    {'nome': 'regiao',
     'palavras_chave': ['regiao', 'atende', 'atendem', 'cidade', 'bairro', 'local', 'lugar', 'onde'],
     'resposta': 'Atendemos a região metropolitana de Recife. Ao agendar, informe o CEP do local e o endereço é preenchido automaticamente.'},

    {'nome': 'horario_funcionamento',
     'palavras_chave': ['horario', 'hora', 'funcionamento', 'aberto', 'abre', 'fecha', 'expediente'],
     'resposta': 'Atendemos de segunda a sábado, das 8h às 18h.'},

    {'nome': 'agradecimento',
     'palavras_chave': ['obrigado', 'obrigada', 'valeu', 'agradeco', 'grato', 'grata'],
     'resposta': 'Por nada! Estou aqui se precisar de mais alguma coisa.'},

    {'nome': 'despedida',
     'palavras_chave': ['tchau', 'ate logo', 'ate mais', 'adeus', 'falou'],
     'resposta': 'Até logo! Quando precisar, é só chamar.'},
]

RESPOSTA_PADRAO = 'Desculpe, não entendi muito bem. Posso ajudar com: serviços, preços, horários, como agendar ou cancelar. Pode reformular?'
