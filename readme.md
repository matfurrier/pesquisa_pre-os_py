# Pesquisa Preços

Esta aplicação permite que sejam adicionados produtos de lojas diversas com um preço meta, onde o sistema fará uma verificação periódica do preço e quando este for igual ou menor ao preço meta setado pelo usuário, este receberá um email avisando.

Este projeto foi feito como parte do curso "The Complete Python Web Developer".

Os administradores do sistema podem adicionar, editar e remover lojas. Para isto, vá em 'src/config.py' e indique os administradores do sistema.

![Adicionar administrador](readme-files/administradores.png)

Foi utilizada uma conta no Mailgun para envio dos emails. **O sistema não funciona com lojas que injetam conteúdo dinâmicamente utilizando JavaScript**.

O sistema permite ao usuário: 
- Fazer seu registro; 
- Acessar o sistema; 
- Criar, editar, apagar alertas e verificar preços manualmente.

Os administradores podem realizar as atividades acima, além de criar, editar e excluir lojas.

Tecnologias: MongoDB, Python (Flask e Jinja2), HTML/CSS/Bootstrap, Mailgun.

![Adicionar administrador](readme-files/home.png)

![Adicionar administrador](readme-files/criar-conta.png)

![Adicionar administrador](readme-files/entrar.png)

![Adicionar administrador](readme-files/alertas.png)

![Adicionar administrador](readme-files/detalhe-alerta.png)

![Adicionar administrador](readme-files/lojas.png)

![Adicionar administrador](readme-files/detalhe-loja.png)
