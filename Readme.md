# Trabalho de Conclusão de Curso

**Alunos:** João Gabriel e Carlos Eduardo.

## Projeto TCC

O **Projeto TCC** é a estrutura completa do nosso trabalho, composta pelo front-end e banco de dados. A partir dele, é possível acessar toda a base de dados e utilizar as funcionalidades do sistema.

### Instalação

Antes de iniciar a aplicação descompacte o arquivo `init.zip` para receber o arquivo `init.sql` para inicializar o banco de dados junto ao docker.

Para iniciar o projeto utilizando Docker, execute o seguinte comando:

```sh
docker compose up -d --build
```

Na primeira execução, será realizada uma migração completa da base de dados, processo que pode levar aproximadamente **6 minutos**. Os logs do container indicarão quando o banco de dados estiver pronto para uso.

### Utilização

- O projeto será iniciado na porta **8000** do seu ambiente local.
- O banco de dados **PostgreSQL** estará disponível na porta **5434**.

## Projeto TCC_ETL

### O que é?

O **Projeto TCC_ETL** é responsável pelo processo de **Extração, Transformação e Carga (ETL)** dos dados. Ele combina códigos em **Python** e **SQL**, sendo executado na plataforma [DeepNote](https://deepnote.com/).

### Instalação

O **TCC_ETL** não requer instalação local, pois sua execução ocorre diretamente na plataforma **DeepNote**.

### Utilização

O código pode ser executado diretamente na plataforma. No entanto, devido ao grande volume de requisições feitas à API e à complexidade dos cálculos de correlação, o processo pode levar **várias horas** para ser concluído. Após a execução, os arquivos gerados são migrados para o banco de dados.

---

Este repositório contém todas as informações necessárias para rodar e entender o funcionamento do projeto. Para dúvidas ou contribuições, entre em contato com os autores.
