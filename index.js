const express = require('express');
const fs = require('fs');
const app = express();

// Rota para consultar um CPF
app.get('/cpf/:cpf', (req, res) => {
  const cpf = req.params.cpf;

  // Lê o arquivo JSON de clientes
  fs.readFile('clientes.json', (err, data) => {
    if (err) {
      console.error('Erro ao ler arquivo JSON:', err);
      res.status(500).send('Erro interno do servidor');
      return;
    }

    const clientes = JSON.parse(data);

    // Procura pelo cliente com o CPF especificado
    const cliente = clientes.find(cliente => cliente.cpf === cpf);

    if (!cliente) {
      res.status(404).send('CPF não encontrado');
      return;
    }

    res.json(cliente);
  });
});

// Inicia o servidor na porta 3000
app.listen(3000, () => {
  console.log('Servidor iniciado na porta 3000');
});
