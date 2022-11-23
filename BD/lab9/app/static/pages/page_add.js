import { async_addArticle } from "../model/request.js";
import { render_main } from "./page_main.js";

export default function render() {
	let root = document.body;
	root.innerHTML = "";
	let btn_back = document.createElement("button");
	btn_back.textContent = "Назад";
	btn_back.addEventListener("click", render_main);
	root.appendChild(btn_back);
	let fields = ["title", "authors", "placement_date", "content", "tags"]
	fields.forEach(field => {
		let div_item = document.createElement("div");
		div_item.className = "add_info"; 
		let label = document.createElement("label");
		label.textContent = field + ": ";
		let input = document.createElement("input");
		input.className = field;
		div_item.appendChild(label);
		div_item.appendChild(input);
		root.appendChild(div_item);
	});
	let btn_create = document.createElement("button");
	btn_create.textContent = "Создать";
	btn_create.addEventListener("click", createArticle);
	root.appendChild(btn_create);
}

function createArticle(){
	let inputs = document.querySelectorAll("input");
	let article_info = {};
	inputs.forEach(input => {
		let value = input.value;
		if (input.className == "authors" || input.className == "tags"){
			value = input.value.split(";");
		}
		article_info[input.className] = value;
	});
	async_addArticle(article_info);
}