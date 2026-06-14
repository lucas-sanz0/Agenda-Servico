document.addEventListener('DOMContentLoaded', function () {
    var conversa = document.getElementById('conversa');
    var campo = document.getElementById('campo-mensagem');
    var botao = document.getElementById('botao-enviar');
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    function enviarMensagem() {
        var texto = campo.value.trim();
        if (texto === '') { return; }

        var divU = document.createElement('div');
        divU.className = 'mensagem-usuario';
        divU.innerHTML = '<strong>Você:</strong> ' + texto;
        conversa.appendChild(divU);
        campo.value = '';

        fetch('/chatbot/responder/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken
            },
            body: 'mensagem=' + encodeURIComponent(texto)
        })
            .then(function (r) { return r.json(); })
            .then(function (dados) {
                var divB = document.createElement('div');
                divB.className = 'mensagem-bot';
                divB.innerHTML = '<strong>Assistente:</strong> ' + dados.resposta;
                conversa.appendChild(divB);
                conversa.scrollTop = conversa.scrollHeight;
            });
    }

    botao.addEventListener('click', enviarMensagem);
    campo.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') { enviarMensagem(); }
    });
});
