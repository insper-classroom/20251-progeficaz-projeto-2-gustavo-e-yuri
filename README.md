# **API RESTful - Imobiliária**

## **Descrição**

Esta API RESTful foi desenvolvida para uma empresa imobiliária, permitindo a gestão de imóveis com operações CRUD completas. A API segue o **modelo RESTful com maturidade de Richardson Nível 3**, garantindo boas práticas de padronização e hiperlinks para facilitar a navegação.

A API possui as seguintes funcionalidades:

- Listar todos os imóveis
- Adicionar um novo imóvel
- Atualizar um imóvel existente
- Remover um imóvel
- Filtrar imóveis por tipo
- Filtrar imóveis por cidade
- Buscar um imóvel específico

A API foi desenvolvida utilizando **Flask** e armazena os dados em um banco de dados **MySQL** hospedado na plataforma **Aiven**. O desenvolvimento foi baseado nos princípios de **Test Driven Development (TDD)**, garantindo que todas as rotas possuam testes automatizados.

---

## **Instalação**

### **Criar um ambiente virtual**

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto, caso queira rodá-lo localmente.

#### **Linux/macOS:**

```sh
python3 -m venv venv
source venv/bin/activate
```

#### **Windows:**

```sh
python -m venv venv
venv\Scripts\activate
```

### **Instalar dependências**

Com o ambiente virtual ativado, instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

---

## **Execução do Servidor**

Para iniciar o servidor Flask, execute o seguinte comando:

```sh
flask run
```

A API estará disponível em:

```
http://34.228.24.35
```

---

## **Endpoints**

### **Listar todos os imóveis**

```
GET /api/imoveis
```

Retorna uma lista com todos os imóveis cadastrados.

### **Adicionar um novo imóvel**

```
POST /api/imoveis
```

Body (JSON):

```json
{
  "tipo": "Apartamento",
  "cidade": "São Paulo",
  "preco": 500000,
}
```

### **Atualizar um imóvel**

```
PUT /api/imoveis/{id}
```

Body (JSON):

```json
{
  "preco": 550000
}
```

### **Remover um imóvel**

```
DELETE /api/imoveis/{id}
```

### **Filtrar imóveis por tipo**

```
GET /api/imoveis/tipo/{tipo}
```

### **Filtrar imóveis por cidade**

```
GET /api/imoveis/cidade/{cidade}
```

### **Buscar um imóvel específico**

```
GET /api/imoveis/{id}
```

---

## **TDD e Testes Automatizados**

Todos os endpoints possuem testes automatizados para garantir confiabilidade e estabilidade. Os testes são escritos utilizando **pytest** e podem ser executados com o seguinte comando:

```sh
pytest
```

---

## **Maturidade de Richardson - Nível 3**

Esta API atinge o nível **3** do modelo de maturidade de Richardson, pois:

- **Nível 1:** Segue o padrão de recursos (ex: `/imoveis/{id}`)
- **Nível 2:** Usa métodos HTTP corretamente (GET, POST, PUT, DELETE)
- **Nível 3:** Implementa **HATEOAS**, fornecendo hiperlinks para facilitar a navegação entre os recursos

Exemplo de resposta JSON com HATEOAS:

```json
[{
  "id": 1,
  "tipo": "Apartamento",
  "cidade": "São Paulo",
  "preco": 500000,
},
  "_links": {
    "add": "http://34.228.24.35/api/add_imovel",
    "filter_by_city": "http://34.228.24.35/api/view_imoveis_by_cidade/NOME_CIDADE",
    "filter_by_type": "http://34.228.24.35/api/view_imoveis_by_tipo/TIPO_IMOVEL",
    "self": "http://34.228.24.35/api/view_imoveis"
}]
```

---