export async function async_getArticles() {
	let response = await fetch('/articles_list', { method: 'GET' });
	let data = await response.json();
	return data;
}

export async function async_getArticlesByTitle(title) {
	let response = await fetch('/articles_by_title', { method: 'POST', headers: { "Content-type": "application/json; charset=utf-8" }, body: JSON.stringify(title) });
	let data = await response.json();
	return data;
}

export async function async_getArticlesByAuthor(author) {
	let response = await fetch('/articles_by_author', { method: 'POST', headers: { "Content-type": "application/json; charset=utf-8" }, body: JSON.stringify(author) });
	let data = await response.json();
	return data;
}

export async function async_getAllInfo(id) {
	let response = await fetch('/articles/' + id, { method: 'GET', headers: { "Content-type": "application/json; charset=utf-8" } });
	let data = await response.json();
	return data;
}

export async function async_deleteArticleById(id){
	await fetch('/articles/' + id, { method: 'DELETE', headers: { "Content-type": "application/json; charset=utf-8" } });
}

export async function async_getBestArticles(){
	let response = await fetch('/best_articles', { method: 'GET', headers: { "Content-type": "application/json; charset=utf-8" } });
	let data = await response.json();
	return data;
}

export async function async_getArticlesByDate(date){
	let response = await fetch('/articles_by_date', { method: 'POST', headers: { "Content-type": "application/json; charset=utf-8" }, body: JSON.stringify(date) });
	let data = await response.json();
	return data;
}

export async function async_addArticle(article){
	await fetch("/new_article", { method: "POST", headers: { "Content-type": "application/json; charset=utf-8" }, body: JSON.stringify(article) });
}