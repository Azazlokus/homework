const { MongoClient, ObjectId } = require('mongodb');
const url_mongo = 'mongodb://127.0.0.1:27017/';
const mongoClient = new MongoClient(url_mongo);

module.exports = {
	async_getArticles: async_getArticles,
	async_getArticlesByAuthor: async_getArticlesByAuthor,
	async_getArticlesByTitle: async_getArticlesByTitle,
	async_getFullInfo: async_getFullInfo,
	async_delete: async_delete,
	async_getBestArticles: async_getBestArticles,
	async_getArticlesByDate: async_getArticlesByDate,
	async_addArticle: async_addArticle,
}

async function async_getArticles() {
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
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
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		result = await articles.aggregate([
			{ $addFields: { result: { $regexMatch: { input: '$title', regex: title } } } },
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
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		result = await articles.aggregate([
			{ $addFields: { result: { $in: [author, '$authors'] } } },
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

async function async_getFullInfo(object_id) {
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		result = await articles.find(
			{ _id: ObjectId(object_id) },
		).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_delete(object_id) {
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		await articles.deleteOne(
			{ _id: ObjectId(object_id) }
		);
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}

async function async_getBestArticles() {
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		result = await articles.aggregate([
			{ $addFields: { sumMarks: { $sum: "$reviews.mark" } } },
			{ $addFields: { countReviews: { $size: "$reviews" } } },
			{ $match: { countReviews: { $gt: 0 } } },
			{ $addFields: { rate: { $divide: ["$sumMarks", "$countReviews"] } } },
			{ $project: { _id: 0, rate: 1 } }
		]).toArray();
		let max = -1;
		result.forEach(obj => {
			if (obj["rate"] > max) {
				max = obj["rate"];
			}
		});
		result = await articles.aggregate([
			{ $addFields: { sumMarks: { $sum: "$reviews.mark" } } },
			{ $addFields: { countReviews: { $size: "$reviews" } } },
			{ $match: { countReviews: { $gt: 0 } } },
			{ $addFields: { rate: { $divide: ["$sumMarks", "$countReviews"] } } },
			{ $match: { rate: { $eq: max } } },
			{ $sort: { countReviews: -1 } },
			{ $project: { title: 1, authors: 1, placement_date: 1, rate: { $round: ['$rate', 2] }, countReviews: 1 } }
		]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_getArticlesByDate(start_date, end_date) {
	let result = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		result = await articles.aggregate([
			{ $match: { placement_date: { $gte: new Date(start_date), $lte: new Date(end_date) } } },
			{ $project: { title: 1, authors: 1, placement_date: 1 } }
		]).toArray();
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
	return result;
}

async function async_addArticle(article) {
	article.placement_date = new Date(article.placement_date);
	article["reviews"] = [];
	try {
		await mongoClient.connect();
		const fb = mongoClient.db('Lab8');
		const articles = fb.collection('articles');
		await articles.insertOne(article);
	} catch (err) {
		console.log(err);
	} finally {
		await mongoClient.close();
	}
}