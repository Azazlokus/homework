const express = require('express');
const mongo = require('./mongo.js');
const bodyParser = require("body-parser");
const app = express();


app.use(express.static("static"));
app.use(bodyParser.json());

app.get("/articles_list", async function(request, response){
	let data = await mongo.async_getArticles();
	response.send(JSON.stringify(data));
});

app.post("/articles_by_title", async function (request, response) {
	let data_req = request.body;
	let data = await mongo.async_getArticlesByTitle(data_req['title']);
	response.send(JSON.stringify(data));
});

app.post("/articles_by_author", async function (request, response){
	let data_req = request.body;
	let data = await mongo.async_getArticlesByAuthor(data_req['author']);
	response.send(JSON.stringify(data));
});

app.listen(3000);

