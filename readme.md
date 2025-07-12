# 📊 Gráfico de Fluxo Interativo com Plotly

Este projeto em Python cria um gráfico de fluxo interativo (streamgraph) utilizando a biblioteca [Plotly](https://plotly.com/python/). A aplicação permite alternar entre diferentes combinações de funções trigonométricas (seno, cosseno, tangente), escolher a linha de base da pilha (baseline) e ajustar dinamicamente o número de pontos da curva.

## 🚀 Funcionalidades

- ✅ Visualização interativa com **mudança dinâmica de dados**
- ✅ Três combinações de funções trigonométricas:
  - Seno e Cosseno
  - Seno e Tangente
  - Cosseno e Tangente
- ✅ Três modos de baseline para preenchimento de área:
  - `Zero`
  - `Wiggle`
  - `Simétrico`
- ✅ Slider interativo para alterar o número de pontos:
  - 50, 100, 200, 500
- ✅ Exibição responsiva no navegador com **hover unificado no eixo X**

## 🧠 Tecnologias Utilizadas

- Python 3.7+
- [Plotly Graph Objects](https://plotly.com/python/plotly-express/)
- [NumPy](https://numpy.org/)

## 📦 Instalação

### Clone o repositório ou crie o arquivo local

Você pode salvar o código principal como `streamgraph.py` ou clonar seu repositório:

```bash
git clone https://github.com/seu-usuario/streamgraph-interativo.git
cd streamgraph-interativo
```

### Instale as dependências

```bash
pip install plotly numpy
```

## ▶️ Como Executar

Execute o script Python:

```bash
python streamgraph.py
```

O gráfico será exibido automaticamente no seu navegador padrão com todos os controles interativos disponíveis.

## 📁 Estrutura do Projeto

```bash
.
├── streamgraph.py     # Código principal com Plotly
├── README.md          # Documentação detalhada do projeto
```

## ⚙️ Explicação do Código

### `generate_data(num_points, func_type)`

Gera os dados X e Y de acordo com o tipo de função:

- `'sin_cos'`: seno e cosseno
- `'sin_tan'`: seno e tangente (tangente suavizada)
- `'cos_tan'`: cosseno e tangente (tangente suavizada)

```python
x = np.linspace(0, 10, num_points)
```

A função retorna:
- Vetor X
- Lista de vetores Y
- Lista de nomes para legenda

### `create_streamgraph(baseline, num_points, func_type)`

Cria o gráfico interativo com:
- Traces do tipo `Scatter` com preenchimento em área (`stackgroup`)
- Botões dropdown para:
  - Escolher o baseline (`zero`, `wiggle`, `simétrico`)
  - Trocar a função trigonométrica
- Slider para mudar a resolução (quantidade de pontos)

```python
fig.update_layout(
    updatemenus=[...],
    sliders=[...]
)
```

## 🎮 Como Usar

- **Dropdown 1**: Altera o baseline:
  - `Wiggle`: centraliza verticalmente
  - `Zero`: parte do eixo X
  - `Simétrico`: empilha os dados em forma contínua
- **Dropdown 2**: Troca os dados entre:
  - Seno e Cosseno
  - Seno e Tangente
  - Cosseno e Tangente
- **Slider**: Modifica a densidade dos pontos (resolução)

## 📸 Exemplo Visual

> O gráfico será exibido dinamicamente com suavidade e visual agradável:

![Exemplo Streamgraph](https://crm.comerciodosite.com.br/layouts/streamgraph.png)
<sub>*Imagem ilustrativa*</sub>

## 📄 Licença

Este projeto é de uso livre para fins educacionais, acadêmicos ou pessoais. Você pode modificar, redistribuir e adaptar conforme necessário.

---

Desenvolvido por Miguel Faria (Comércio do Site) (https://comerciodosite.com.br/).
