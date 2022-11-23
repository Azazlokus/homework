import render_info from "./page_info.js"
import render_add from "./page_add.js";
import { show_docs, show_docs_w } from "../model/data_action.js"
import { async_deleteArticleById, async_getAllInfo, async_getArticles, async_getArticlesByAuthor, async_getArticlesByDate, async_getArticlesByTitle, async_getBestArticles, async_addArticle } from "../model/request.js";

export function render_main() {
	let root = document.body;
	root.innerHTML = "";

	let btn_articles_list = document.createElement("button");
	btn_articles_list.id = "btn_articles_list";
	btn_articles_list.textContent = "Список статей";
	btn_articles_list.addEventListener('click', showArticles);

	let btn_best_articles = document.createElement("button");
	btn_best_articles.id = "btn_best_articles";
	btn_best_articles.textContent = "Топ статей";
	btn_best_articles.addEventListener('click', showBestArticles);

	let btn_create_article = document.createElement("button");
	btn_create_article.id = "btn_create_article";
	btn_create_article.textContent = "Создать статью";
	btn_create_article.addEventListener('click', render_add);

	let div_input_info = document.createElement("div");
	div_input_info.className = "input_info";
	let input_info = document.createElement("input");
	input_info.id = "title_info";
	let btn_title_info = document.createElement("button");
	btn_title_info.id = "btn_title_info";
	btn_title_info.textContent = "Поиск по названию";
	btn_title_info.addEventListener('click', showArticlesByTitle);
	div_input_info.appendChild(input_info);
	div_input_info.appendChild(btn_title_info);

	let div_input_info2 = document.createElement("div");
	div_input_info2.className = "input_info";
	let input_select = document.createElement("select");
	input_select.id = "author_info";
	let options = ["Воробьев Максим Витальевич", "Иванов Петр Михайлович", "Борисов Иван Евгеньевич", "Клиенчук Владислав Сергеевич", "Иванов Иван Иванович"];
	options.forEach(option => {
		let op = document.createElement("option");
		op.textContent = option;
		input_select.appendChild(op);
	});
	let btn_author_info = document.createElement("button");
	btn_author_info.id = "btn_author_info";
	btn_author_info.textContent = "Поиск по автору";
	btn_author_info.addEventListener('click', showArticlesByAuthor);
	div_input_info2.appendChild(input_select);
	div_input_info2.appendChild(btn_author_info);

	let div_input_date = document.createElement("div");
	div_input_date.className = "input_info";
	let input_date_start = document.createElement("input");
	input_date_start.id = "start_date";
	let input_date_end = document.createElement("input");
	input_date_end.id = "end_date";
	let btn_date_info = document.createElement("button");
	btn_date_info.id = "btn_date_info";
	btn_date_info.textContent = "Поиск по дате";
	btn_date_info.addEventListener("click", showArticlesByDate);
	div_input_date.appendChild(input_date_start);
	div_input_date.appendChild(input_date_end);
	div_input_date.appendChild(btn_date_info);

	let div_info = document.createElement("div");
	div_info.id = "info";

	root.appendChild(btn_articles_list);
	root.appendChild(btn_best_articles);
	root.appendChild(btn_create_article);
	root.appendChild(div_input_info);
	root.appendChild(div_input_info2);
	root.appendChild(div_input_date);
	root.appendChild(div_info);
}

function getId(event){
	let item = event.target.closest(".item");
	let object_id = item.querySelector("._id").textContent;
	let id = object_id.replace("_id: ", "");
	return id;
}

async function showArticles() {
	let data = await async_getArticles();
	show_docs_w(data, showArticleInfo, deleteArticle);
}

async function showArticlesByTitle() {
	let input_title_info = document.getElementById('title_info');
	let title = {
		title: input_title_info.value,
	}
	let data = await async_getArticlesByTitle(title);
	show_docs(data);
}

async function showArticlesByAuthor() {
	let input_author_info = document.getElementById('author_info');
	let author = {
		author: input_author_info.value,
	}
	let data = await async_getArticlesByAuthor(author);
	show_docs(data);
}

async function showArticleInfo(event) {
	let id = getId(event);
	let data = await async_getAllInfo(id);
	render_info(data);
}

async function deleteArticle(event){
	let id = getId(event);
	await async_deleteArticleById(id);
	showArticles();
}

async function showBestArticles(){
	let data = await async_getBestArticles();
	show_docs(data);
}

async function showArticlesByDate(){
	let input_date_start = document.getElementById("start_date");
	let input_date_end = document.getElementById("end_date");
	let date = {
		start_date: input_date_start.value,
		end_date: input_date_end.value,
	}
	let data = await async_getArticlesByDate(date);
	show_docs(data);
}

render_main();