Projeto hermeX
===============
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :alt: License: MIT
   :align: left
   :target: https://opensource.org/licenses/MIT

|

Protótipo desenvolvido para o Trabalho de Conclusão de Curso para o curso de Bacharel em Ciência da Computação na Pontifícia Universidade Católica de Sâo Paulo (PUC-SP). Este projeto visa criar rotas para veículos compartilhados.

O projeto hermeX é um sistema que conecta passageiros, motoristas e donos/administradores de veículos coletivos com o propósito de facilitar a criação e a manutenção das rotas destes veículos na locomoção diária. O objetivo principal é diminuir a duração total da locomoção de cada passageiro e aumentar o número de passageiros por veículos, respeitando sua capacidade.

-----------------------------------

Configurações adicionais
========================
Para facilitar a configuração do ambiente de desenvolvimento, este projeto utiliza Docker Compose. Se você não está familiarizado ou não tem Docker ou Docker Compose instalado, você pode consultar o `tutorial na documentação oficial`_.

- Instalação do `Docker no Ubuntu`_
- Instalação do `Docker no Windows`_
- Instalação do `Docker Compose`_

Apesar de utilizar Docker, algumas vezes pode ser necessário (ou simplesmente mais fácil) executar algum comando ou teste fora do container. Neste, caso é recomendado instalar `virtualenv`_. Para criar um ambiente virtual com Python 3.6, basta executar :code:`virtualenv -p python3 hermex_env`



Configurando o Projeto
----------------------

Depois disto, basta:

1. Clonar este repositório no seu diretório de trabalho: `https://github.com/joaofouyer/hermex.git`

2. No diretório raiz do projeto *(tcc)*, execute o comando `docker-compose build`

3. Para subir os *containers*, execute o comando `docker-compose up`.

Pronto, você já deve ter tudo configurado e rodando localmente em `localhost:8008`! |rocket|


------------------------------------


Código de Conduta
=================

1. Documentação
---------------

2. Diretrizes de Código
-----------------------

    A Foolish Consistency is the Hobgoblin of Little Minds

Se for utilizar alguma IDE que cria arquivos de configuração (e.g. Visual Studio, PyCharm etc), lembre-se de adicionar os arquivos no `.gitignore`_.

Nos serviços que são implementados em Python, é fortemente recomendável seguir as especificações definidas (principalmente) no `PEP8`_. Algumas diretrizes básicas:

- `Indentação com espaço`_ é recomendável.
- Linhas de código com até `79 caracteres`_.
- `UTF-8`_!!!!
- Uso de `espaço em expressões`_
- Nome de Classes `devem seguir a convenção`_ CamelCase, `métodos e variáveis`_ devem ser lowercase.

Para Javascript, CSS e HTML é recomendável utilizar a `convenção do Google`_.

3. Testes
----------


4. *Commits* e *Pull Requests*
------------------------------
O *commit* na master está fechado. Quando for desenvolver alguma funcionalidade nova é necessário criar uma nova branch, preferencialmente a partir da master (ou development, se necessário). Ao terminar o trabalho, pode criar um pull-request para o development. Só para lembrar:

- Para criar nova branch, basta dar um :code:`git pull` e :code:`git checkout -b <nome_da_feature>`
- Para subir, basta :code:`git push origin <nome_da_branch>`



Orientador:
-----------
`Prof. Dr. Carlos Eduardo de Barros Paes`_


Autores:
--------

`Caroline C. Appolinario`_ <caroline.appolinario@gmail.com>

Hector Rauer <hector.rauer@gmail.com>

`João E. Fouyer`_ <jfouyer@gmail.com>


.. _Prof. Dr. Carlos Eduardo de Barros Paes: http://lattes.cnpq.br/6550336604432810
.. _Caroline C. Appolinario: http://lattes.cnpq.br/1746001355108337
.. _João E. Fouyer: http://lattes.cnpq.br/9901346603428982
.. _tutorial na documentação oficial: https://docs.docker.com/compose/install/
.. _Docker no Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
.. _Docker no Windows: https://docs.docker.com/docker-for-windows/install/
.. _Docker Compose: https://docs.docker.com/compose/install/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/installation/
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _Indentação com espaço: https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces
.. _79 caracteres: https://www.python.org/dev/peps/pep-0008/#maximum-line-length
.. _devem seguir a convenção: https://www.python.org/dev/peps/pep-0008/#class-names
.. _UTF-8: https://www.python.org/dev/peps/pep-0008/#source-file-encoding
.. _espaço em expressões: https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements
.. _métodos e variáveis: https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
.. _.gitignore: https://www.gitignore.io/
.. _convenção do Google: https://google.github.io/styleguide/jsguide.html


.. |rocket| replace:: 🚀