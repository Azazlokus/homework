const express = require('express');
const mongo = require('./mongo.js');
const bodyParser = require("body-parser");
const app = express();


app.use(express.static("static"));
app.use(express.static("static/pages"));
app.use(express.static("static/model"));
app.use(bodyParser.json());

app.get("/collections", async function (request, response) {
	let data = await mongo.async_getCollections();
	response.send(data);
});

app.get("/collections/:name", async function (request, response) {
	let name = request.params["name"];
	let data = await mongo.async_getDocs(name);
	response.send(data);
});

app.delete("/collections/:name", async function (request, response) {
	let name = request.params["name"];
	let req_data = request.headers["data"];
	req_data = JSON.parse(req_data);
	for (let i = 0; i < req_data.length; i++) {
		const el = req_data[i];
		await mongo.async_deleteDoc(name, el["id"]);
	}
	response.send();
});

app.get("/collections/:name/:id", async function (request, response) {
	let name = request.params["name"];
	let id = request.params["id"];
	let data = await mongo.async_getDoc(name, id);
	response.send(data);
});

app.post("/collections/:name/:id", async function (request, response) {
	let name = request.params["name"];
	let id = request.params["id"];
	let req_data = request.body;
	await mongo.async_updateDoc(name, id, req_data);
	response.send();
});

app.post("/collections/:name", async function (request, response) {
	let name = request.params["name"];
	let req_data = request.body;
	await mongo.async_addDoc(name, req_data);
	response.send();
});

app.listen(3000);

