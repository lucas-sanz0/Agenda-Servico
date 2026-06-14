document.addEventListener('DOMContentLoaded', function () {
    var campoCep = document.getElementById('id_cep');
    if (campoCep) {
        campoCep.addEventListener('blur', function () {
            var cep = campoCep.value.replace(/\D/g, '');
            if (cep.length !== 8) { return; }
            fetch('/agendamentos/api/cep/' + cep + '/')
                .then(function (r) { return r.json(); })
                .then(function (dados) {
                    if (dados.erro) { return; }
                    document.getElementById('id_logradouro').value = dados.logradouro;
                    document.getElementById('id_bairro').value = dados.bairro;
                    document.getElementById('id_cidade').value = dados.localidade; 
                    document.getElementById('id_uf').value = dados.uf;
                });
        });
    }
});
