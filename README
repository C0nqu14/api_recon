# API de Reconhecimento Facial

Esta API de reconhecimento facial permite verificar se uma foto carregada é a mesma que a capturada pela webcam. Ela utiliza algoritmos avançados de reconhecimento facial para comparar e autenticar imagens, além de gerar relatórios e sintetizar voz.

## Funcionalidades

- **Comparação de Imagens**: Compara uma foto enviada com a imagem capturada pela webcam.
- **Autenticação Facial**: Verifica se ambas as imagens pertencem à mesma pessoa.
- **Geração de Relatórios**: Cria relatórios sobre a verificação usando a API do Google.
- **Síntese de Voz**: Lê em voz alta o relatório gerado.

## Endpoints

### 1. `/upload-imagem`

**Método:** `POST`

**Descrição:** Envia uma foto para ser comparada com a imagem capturada pela webcam.

**Requisitos:**
- O arquivo da foto deve estar no formato JPEG ou PNG.
- O arquivo deve ter um tamanho máximo de 5MB.

**Request:**

```http
POST /upload-imagem HTTP/1.1
Host: api.exemplo.com
Content-Type: multipart/form-data
Authorization: Bearer <token_de_acesso>
```

**Body (multipart/form-data):**

- `file` (arquivo): A foto a ser comparada.

**Resposta:**

```json
{
  "verified": true,
  "similarity": 95.3
}
```

**Campos da Resposta:**

- `verified`: Indica se as imagens correspondem.
- `similarity`: Nível de confiança na correspondência (em porcentagem).

## Autenticação

A API usa tokens Bearer para autenticação. Inclua o token no cabeçalho da solicitação em todos os endpoints.

**Exemplo de Cabeçalho:**

```http
Authorization: Bearer <token_de_acesso>
```

## Exemplos de Uso

### Enviar Foto para Comparação

**Curl:**

```sh
curl -X POST "https://api.exemplo.com/upload-imagem" \
  -H "Authorization: Bearer <token_de_acesso>" \
  -F "file=@/caminho/para/foto.jpg"
```

**Resposta Esperada:**

```json
{
  "verified": true,
  "similarity": 95.3
}
```

## Estrutura do Projeto

### Módulos

1. **app.py**: Define a API e os endpoints.
2. **recon.py**: Realiza o reconhecimento facial utilizando OpenCV e DeepFace.
3. **voice.py**: Utiliza a biblioteca gTTS para sintetizar a voz.
4. **genai.py**: Gera relatórios utilizando a API do Google Generative AI.

## Requisitos

- Python 3.8 ou superior
- Dependências: `opencv-python`, `deepface`, `fastapi`, `uvicorn`, `gtts`, `pygame`, `google-generativeai`
- Pasta `uploads` para armazenar as imagens carregadas

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/C0nqu14/api_upload.git
   ```

2. Navegue até o diretório do projeto:

   ```sh
   cd api_upload
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Inicie o servidor:

   ```sh
   uvicorn app:app --reload
   ```

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Faça um pull request descrevendo suas mudanças.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

- **Email:** joaomanuelconquia@gmail.com
- **GitHub:** [https://github.com/C0nqu14/api_upload](https://github.com/C0nqu14/api_upload)

---

Obrigado por usar nossa API de reconhecimento facial!
