Tutorial Completo – Automação de Mensagens WhatsApp
1️⃣ Ferramentas necessárias

Antes de usar o script, você precisa instalar:

Visual Studio Code (VS Code)

Acesse: https://code.visualstudio.com/
Instale e abra o programa, ele será usado para editar e rodar os scripts.

Python 3

Acesse: https://www.python.org/downloads/
Baixe e instale a versão 3.11 ou superior.
Marque a opção “Add Python to PATH” durante a instalação.




2️⃣ Estrutura de pastas

Crie uma pasta principal chamada WhatsApp_URL. Dentro dela:

WhatsApp_URL/
│
├─ numeros.txt           ← Lista de contatos e informações
├─ gerar_links.py        ← Script Python que abre os links
├─ códigos.txt           ← Modelos de mensagem (consulta/exame)
├─ README.txt            ← Este tutorial (opcional)

⚠️ É importante que numeros.txt e gerar_links.py fiquem na mesma pasta.




3️⃣ Preparar o arquivo numeros.txt

O arquivo deve conter os dados dos pacientes. Para cada paciente, use um formato por linha:

Consultas:
5511999990001;5511999990002;Nome do Paciente;Especialidade

Exames:
5511999990001;5511999990002;Nome do Paciente;Nome do Exame

O script lê dois números de telefone por paciente e o nome + tipo de consulta/exame.




4️⃣ Editar o script gerar_links.py

O script já está pronto. Ele abre os links do WhatsApp automaticamente e insere:

Nome do paciente
Especialidade ou exame
Datas de retirada do comprovante

Você pode alterar:

time.sleep(10)  # segundos entre cada link

Para definir o intervalo entre o envio de links.

Se quiser mudar a mensagem, edite a variável modelo dentro do script.




5️⃣ Rodar o script

Abra o VS Code.
Abra o terminal integrado (Ctrl + ` — tecla abaixo do Esc).
Navegue até a pasta do script:

cd "C:\Users\alyso\OneDrive\Área de Trabalho\WhatsApp_URL"

4. Execute o script:
python gerar_links.py

5. Siga as instruções no terminal:

Digite data de início e data de fim.
Escolha o modelo de mensagem (consulta ou exame, se aplicável).

6. O script abrirá cada link no navegador automaticamente.
⚠️ Evite abrir muitos links de uma vez. O WhatsApp pode limitar envios automáticos.




6️⃣ Observações importantes

Se precisar parar o envio, pressione Ctrl + C no terminal.
Sempre verifique se o numeros.txt está formatado corretamente e se todos os arquivos estão na mesma pasta.
Este projeto é para abrir links e preparar mensagens. Ele não envia automaticamente no WhatsApp Web por limitações do próprio WhatsApp.
