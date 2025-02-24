<div align="center">
    <h1>Conversor de MarkDown para HTML</h1>
</div>

### Autor:
*Nome:* Beatriz Salgado Fernandes 

*ID:* A100602

## Descrição
Este programa **conversorMD**, em Python, é um Conversor de Markdown para HTML, que transforma arquivos escritos em Markdown nos seus equivalentes em HTML. Este suporta os principais elementos da sintaxe Markdown, permitindo uma conversão eficiente e automática.

## Regras de Funcionamento
- Cabeçalhos: converte `#`, `##`, `###` para `<h1>`, `<h2>`, `<h3>`;
- Negrito: converte `**texto**` para `<b>texto</b>`;
- Itálico: converte `*texto*` para `<i>texto</i>`;
- Listas Ordenadas: converte listas numeradas (1. item) em `<ol><li>item</li></ol>`;
- Listas Não Ordenadas: converte listas com -, *, ou + em `<ul><li>item</li></ul>`;
- Links: converte `[texto](url)` para `<a href="url">texto</a>`;
- Imagens: converte `![alt](url)` para `<img src="url" alt="alt"/>`.


## Resultado
Os resultados da conversão do ficheiro Input.md são escritos num novo ficheiro Output.html. 
Para visualizar os resultados basta então abrir o ficheiro Output.html.


