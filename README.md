# Instruções para a Landing Page Bilíngue

## Visão Geral
Esta landing page foi desenvolvida para um especialista em Cloud, DevOps e AWS, com foco em atrair CTOs, CEOs e Gerentes de TI. A página é bilíngue (Português e Inglês) e detecta automaticamente o idioma do navegador, além de permitir a alternância manual através dos ícones de bandeiras.

## Estrutura de Arquivos
- `index.html` - Arquivo principal HTML
- `css/styles.css` - Estilos CSS
- `js/script.js` - Funcionalidades JavaScript
- `images/` - Diretório para imagens (bandeiras e logotipos)

## Imagens Necessárias
Para o funcionamento completo da landing page, você precisará adicionar as seguintes imagens ao diretório `images/`:

1. Bandeiras para seleção de idioma:
   - `brazil.png` - Bandeira do Brasil
   - `usa.png` - Bandeira dos EUA

2. Logotipos das empresas para a seção "Casos de Sucesso":
   - `coca-cola.png` - Logo da Coca-Cola
   - `99pay.png` - Logo da 99 Pay
   - `global-payments.png` - Logo da Global Payments
   - `touch-of-modern.png` - Logo da Touch Of Modern

## Integração com Calendly
A página está configurada para integração com o Calendly. Para que funcione corretamente:

1. Substitua os URLs de exemplo no arquivo `script.js` pelos seus URLs reais do Calendly:
   ```javascript
   const baseUrl = 'https://calendly.com/renatomateusx/';
   const urlSuffix = lang.startsWith('pt') ? 'strategic-consultant' : 'strategic-consultant';
   ```

2. Certifique-se de criar dois eventos diferentes no Calendly:
   - Um em português: "consulta-estrategica"
   - Um em inglês: "strategic-consultation"

## Personalização
- Substitua os endereços de e-mail e números de telefone pelos seus reais
- Personalize as cores editando as variáveis CSS no início do arquivo `styles.css`
- Adicione seu próprio logotipo ou nome no lugar de "CloudExpert"

## Responsividade
A landing page é totalmente responsiva e funciona bem em dispositivos móveis, tablets e desktops.

## Hospedagem
Para hospedar esta landing page, basta fazer upload de todos os arquivos e diretórios para seu servidor web, mantendo a mesma estrutura de pastas.
