const API_URL = "http://127.0.0.1:8000";

import { biblia, abreviacoes } from "./biblia.js";

window.onload = function () {
  var livroSel = document.getElementById("livro");
  var capituloSel = document.getElementById("capitulo");
  var versiculoSel = document.getElementById("versiculo");
  var form = document.getElementById("form1");
  var resultado = document.getElementById("resultado");

  for (var x in biblia) {
    livroSel.options[livroSel.options.length] = new Option(x, x);
  }

  livroSel.onchange = function () {
    versiculoSel.length = 1;
    capituloSel.length = 1;
    for (var y in biblia[this.value]) {
      capituloSel.options[capituloSel.options.length] = new Option(y, y);
    }
  };

  capituloSel.onchange = function () {
    versiculoSel.length = 1;
    var z = biblia[livroSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      versiculoSel.options[versiculoSel.options.length] = new Option(z[i], z[i]);
    }
  };

  
  form.addEventListener("submit", async function (evento) {
    evento.preventDefault();

    var livro = livroSel.value;          // ex.: "João"
    var capitulo = capituloSel.value;    // ex.: "3"
    var versiculo = versiculoSel.value;  // ex.: "16"

    if (!livro || !capitulo || !versiculo) {
      resultado.textContent = "Escolha o livro, o capítulo e o versículo.";
      return;
    }
    
    var abv = abreviacoes[livro];       
    var url = API_URL + "/biblia/" + encodeURIComponent(abv) + "/" + capitulo + "/" + versiculo;

    resultado.textContent = "Buscando...";

    try {
      var resposta = await fetch(url);

      if (!resposta.ok) {
        resultado.textContent = "Versículo não encontrado.";
        return;
      }

      var dados = await resposta.json();
      // dados = { nome: "João", capitulo: 3, versiculo: 16, texto: "Porque Deus amou..." }

      resultado.textContent =
        dados.nome + " " + dados.capitulo + ":" + dados.versiculo + " — " + dados.texto;
    } catch (erro) {
      resultado.textContent = "Não foi possível conectar à API.";
      console.error(erro);
    }
  });
};