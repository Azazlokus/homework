const http = require("http");
const fs = require("fs");

const { MongoClient } = require("mongodb");
const url_mongo = "mongodb://127.0.0.1:27017/";
const mongoClient = new MongoClient(url_mongo);

http.createServer(async function (request, response) {

	let url = request.url;
	response.writeHead(200, { "Content-Type": "application/json; charset=utf8" });
	if (url == "/") {
		const index = fs.readFileSync("./index.html");
		response.writeHead(200, { "Content-Type": "text/html; charset=utf8" });
		response.end(index);
	}
	else if (url.endsWith(".js")) {
		const script = fs.readFileSync("." + url);
		response.writeHead(200, { "Content-Type": "text/javascript; charset=utf8" });
		response.end(script);
	}
	else if (url == "/articles_list") {
		let data = await async_getArticles();
		response.write(JSON.stringify(data));
		response.end();
	}
	else if (url == "/articles_by_title") {
		let data_req = "";
		request.on("data", chunk => {
			data_req += chunk;
		});
		request.on("end", async function () {
			data_req = JSON.parse(data_req);
			let data = await async_getArticlesByTitle(data_req["title"]);
			response.write(JSON.stringify(data));
			response.end();
		});
	}
	else if (url == "/articles_by_author") {
		let data_req = "";
		request.on("data", chunk => {
			data_req += chunk;
		});
		request.on("end", async function () {
			data_req = JSON.parse(data_req);
			let data = await async_getArticlesByAuthor(data_req["author"]);
			response.write(JSON.stringify(data));
			response.end();
		});
	}

}).listen(3000, "127.0.0.1", function () {
	console.log("Сервер начал прослушивание запросов на порту 3000");
});

async function async_getArticles() {
	let result = null;
	try {
		await mongoClient.connect();
		const fb = mongoClient.db("Lab8");
		const articles = fb.collection("articles");
		result = await articles.aggregate([
			{ $project: { title: 1, authors: 1, placement_date: 1 } }
		]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_getArticlesByTitle(title) {
	let result = null;
	try {
		await mongoClient.connect();
		const fb = mongoClient.db("Lab8");
		const articles = fb.collection("articles");
		result = await articles.aggregate([
			{ $addFields: { result: { $regexMatch: { input: "$title", regex: title } } } },
			{ $match: { result: true } },
			{ $project: { title: 1, authors: 1, placement_date: 1 } }
		]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_getArticlesByAuthor(author) {
	let result = null;
	try {
		await mongoClient.connect();
		const fb = mongoClient.db("Lab8");
		const articles = fb.collection("articles");
		result = await articles.aggregate([
			{ $addFields: { result: { $in: [author, "$authors"] } } },
			{ $match: { result: true } },
			{ $project: { title: 1 } }
		]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}