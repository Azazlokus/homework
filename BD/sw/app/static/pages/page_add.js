import { textToObject } from "../model/dataAction.js";
import { async_addDoc } from "../model/request.js";
import { render_collection_space } from "./page_coll.js";

let root = undefined;
let name_coll = undefined;
let status = undefined;
let text = undefined;

export async function render_page_add(name) {
	root = document.body;
	name_coll = name;

	root.innerHTML = `
		<div class='wrap-content'>
			<button id='back-btn'>Назад</button>
			<span class='title'>${name_coll}</span>
			<textarea id='text-add'></textarea>
			<span id="status"></span>
			<button id='submit-btn'>Добавить</button>
		</div>`;
	let back_btn = root.querySelector("#back-btn");
	back_btn.addEventListener("click", () => render_collection_space(name_coll));
	let submit_btn = root.querySelector("#submit-btn");
	submit_btn.addEventListener("click", add_doc);
	status = root.querySelector("#status");
	text = root.querySelector("#text-add");
	text.addEventListener("keydown", (event) => {
		if (event.code !== "Tab"){
			return;
		}
		event.preventDefault();
		text.value += "\t";
	});
}

async function add_doc(){
	let obj = {};
	try {
		obj = textToObject(text.value);
	} catch (error) {
		status.textContent = "Неправильно заполнена форма";
		return;
	}
	if (Object.keys(obj).length === 0) return;
	await async_addDoc(name_coll, obj);
	render_page_add(name_coll);
}


