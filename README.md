# Desafio Fábrica de Software 2024

<h3>📝 Consumindo API de temperatura com Django REST Frame Work</h3>
<br>


<b>Neste Projeto utilizei a API Openweathermap que retorna a partir do nome da cidade, sua temperatura.</b><br><br>
<h3>Como Usar:</h3>
<br>
<h3>Get</h3>
<b>
Utilizando o caminho http://127.0.0.1:8000/clima/ {nome da cidade}/ no insomnia, ira retornar o seguinte json
<br>
<br>

	"temperatura": 11.44,
	"temperatura_maxima": 12.32,
	"temperatura_minima": 10.59

</b>
<br>
<h3>Post</h3>
<b>Utilizando o caminho http://127.0.0.1:8000/api/clima/ no insomnia, adicione no campo 'name' a palavra 'cidade' e em 'value' adicione a cidade da busca que deseja, ira retornar o seguinte Json: <br><br>


	"id": 1,
	"cidade": "Paris",
	"temperatura": "11.44",
	"temperatura_maxima": "12.32",
	"temperatura_minima": "10.59",
	"data": "2024-03-16T01:16:45.541888Z"

 </b>

 <h3>Put</h3>
 <b>
 Utilizando o caminho http://127.0.0.1:8000/api/clima/ {id de qual deseja editar}/ no insomnia, utilize a opção json para editar.
 </b>
 <h3>Delete</h3>

 <b> Utilizando o caminho http://127.0.0.1:8000/api/clima/ {id de qual deseja apagar}/ no insomnia</b>
<br>
<br>
<b>  API utilizada Openweathermap</b>
<ul>
    <li>https://openweathermap.org/api</li>
</ul>
<br>

<b> Informações sobre o Projeto</b>
<ul>
    <li>Projeto realizado em Django REST FrameWork</li>
    <li>Nome do Projeto: previsaodotempo</li>
    <li>Nome do app: clima</li>
    <li>Utilizando banco de dados local Sqllite3</li>
   
</ul>
<br>

<b>Funcionalidades</b>
<br>
<ul>
    <li>Cadastro de Previsões: Os usuários podem cadastrar previsões de temperatura para diferentes cidades.</li><br>
    <li>Consulta de Previsões: Os usuários podem consultar as previsões cadastradas, incluindo informações como temperatura atual, máxima e mínima.</li><br>
    <li>Atualização e Exclusão de Previsões: Os usuários autorizados podem atualizar e excluir previsões existentes.</li>
</ul>
<br>

<b> Como Iniciar</b>
<ol>
    <li>Clone o projeto;</li>
    <li>Crie um ambiente de desenvolvimento;</li>
    <li>Ative o ambiente do passo anterior;</li>
    <li>Instale as dependências;</li>
    <li>Faça as migrações;</li>
</ol>
<br>


