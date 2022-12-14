const { MongoClient, ObjectId } = require('mongodb');
const url_mongo = 'mongodb://127.0.0.1:27017/';
const mongoClient = new MongoClient(url_mongo);

module.exports = {
	async_getCollections: async_getCollections,
	async_getDocs: async_getDocs,
	async_deleteDoc: async_deleteDoc,
	async_getDoc: async_getDoc,
	async_updateDoc: async_updateDoc,
	async_addDoc: async_addDoc,
}

async function async_getCollections() {
	let result = [];
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		result = await db.listCollections().toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_getDocs(coll_name) {
	let result = [];
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		const coll = db.collection(coll_name);
		result = await coll.aggregate([]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_deleteDoc(coll_name, id) {
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		const coll = db.collection(coll_name);
		await coll.deleteOne({ _id: ObjectId(id) });
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}

async function async_getDoc(coll_name, id) {
	let result = [];
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		const coll = db.collection(coll_name);
		result = await coll.findOne({ _id: ObjectId(id) });
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_updateDoc(coll_name, id, data) {
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		const coll = db.collection(coll_name);
		await coll.updateOne({ _id: ObjectId(id) }, { $set: data });
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}

async function async_addDoc(coll_name, data) {
	try {
		await mongoClient.connect();
		const db = mongoClient.db('semestr');
		const coll = db.collection(coll_name);
		await coll.insertOne(data);
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}