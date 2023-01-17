const {MongoClient} = require("mongodb");

const url = "mongodb://127.0.0.1:27017/";
const mongoClient = new MongoClient(url);
async function run() {
	try {
		await mongoClient.connect();
		const fb = mongoClient.db("Lab8");
		const collection = fb.collection("articles");
		await collection.insertOne({test: "test"});
		let count = await collection.countDocuments();
		console.log(`Кол-во документов в коллекции articles: ${count}`);
		await collection.deleteMany({});
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}

run();