const express = require('express');
const mongo = require('./mongo.js');
const bodyParser = require("body-parser");
const app = express();


app.use(express.static("static"));
app.use(express.static("static/pages"));
app.use(express.static("static/model"));
app.use(bodyParser.json());

app.get("/articles_list", async function(request, response){
	let data = await mongo.async_getArticles();
	response.send(JSON.stringify(data));
});

app.get("/articles/:object_id", async function(request, response){
	let object_id = request.params["object_id"];
	let data = await mongo.async_getFullInfo(object_id);
	response.send(data);
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

app.delete("/articles/:object_id", async function (request, response) {
	let object_id = request.params["object_id"];
	await mongo.async_delete(object_id);
	response.send();
});

app.get("/best_articles", async function(request, response){
	let data = await mongo.async_getBestArticles();
	response.send(JSON.stringify(data));
});

app.post("/articles_by_date", async function(request, response){
	let data_req = request.body;
	let data = await mongo.async_getArticlesByDate(data_req["start_date"], data_req["end_date"]);
	response.send(JSON.stringify(data));
});

app.post("/new_article", async function(request, response){
	let data_req = request.body;
	await mongo.async_addArticle(data_req);
	response.send();
})

app.listen(3000);

