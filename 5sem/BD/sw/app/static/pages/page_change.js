import { convertObj, objToHtml, textToObject } from "../model/dataAction.js";
import { async_getDoc, async_updateDoc } from "../model/request.js";
import { render_collection_space } from "./page_coll.js";

let root = undefined;
let name_coll = undefined;
let doc_id = undefined;
let status = undefined;
let text = undefined;

export async function render_page_change(name, id){
	root = document.body;
	name_coll = name;
	doc_id = id;
	let data = await async_getDoc(name_coll, doc_id);
	data = convertObj(data);
	let text = objToHtml(data);

	root.innerHTML = `
		<div class='wrap-content'>
			<button id='back-btn'>Назад</button>
			<span class='title'>${name_coll}</span>
			<div class='documents'>
				${text}
			</div>
			<textarea id='text-update'></textarea>
			<span id="status"></span>
			<button id='submit-btn'>Изменить</button>
		</div>`;
	let back_btn = root.querySelector("#back-btn");
	back_btn.addEventListener("click", () => render_collection_space(name_coll));
	let submit_btn = root.querySelector("#submit-btn");
	submit_btn.addEventListener("click", updateDoc);
	status = root.querySelector("#status");
	text = root.querySelector("#text-update");
	text.addEventListener("keydown", (event) => {
		if (event.code !== "Tab") {
			return;
		}
		event.preventDefault();
		text.value += "    ";
	});
}

async function updateDoc(){
	let obj = {};
	try {
		obj = textToObject(text.value);
	} catch (error) {
		status.textContent = "Неправильно заполнена форма";
		return;
	}
	if (Object.keys(obj).length === 0) return;
	status.textContent = "";
	await async_updateDoc(name_coll, doc_id, obj);
	render_page_change(name_coll, doc_id);
}



