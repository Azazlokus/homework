import { convertJsonToHtml } from "../model/dataAction.js";
import { async_deleteDocs, async_getDocs } from "../model/request.js";
import { render_page_add } from "./page_add.js";
import { render_page_change } from "./page_change.js";
import { render_main } from "./page_main.js";

let root = undefined;
let name_coll = undefined;

export async function render_collection_space(name) {
	root = document.body;
	name_coll = name;
	let data = await async_getDocs(name_coll);
	let text = convertJsonToHtml(data);
	root.innerHTML = `
		<div class='wrap-content'>
			<button id='back-btn'>Назад</button>
			<span class='title'>${name_coll}</span>
			<div class="actions">
				<button id='add_btn' class='green_btn'>Добавить</button>
				<button id='remove_btn' class='red_btn'>Удалить</button>
				<button id='change_btn' class='blue_btn'>Изменить</button>
			</div>
			${text}
		</div>`;

	let back_btn = root.querySelector("#back-btn");
	back_btn.addEventListener("click", render_main);
	let add_btn = root.querySelector("#add_btn");
	add_btn.addEventListener("click", () => render_page_add(name_coll));
	let remove_btn = root.querySelector("#remove_btn");
	remove_btn.addEventListener("click", send_deleteInfo);
	let change_btn = root.querySelector("#change_btn");
	change_btn.addEventListener("click", goToChange);

	let documents = root.querySelectorAll(".root-ul");
	highlightDocs(documents);

}

function highlightDocs(documents) {
	[].forEach.call(documents, (doc) => {
		doc.addEventListener("click", () => {
			if (doc.style.background == "") {
				doc.style.background = "rgb(209, 255, 223)";
			} else {
				doc.style.background = "";
			}
		});
	});
}

function get_deleteInfo(){
	let documents = root.querySelectorAll(".root-ul");
	let result = [];
	documents.forEach(doc => {
		if (doc.style.background == "rgb(209, 255, 223)"){
			let id_block = doc.querySelector("._id");
			let id = id_block.textContent.split(":")[1];
			result.push({id: id});
		}
	});
	return result;
}

async function send_deleteInfo(){
	let jsonDeleteInfo = get_deleteInfo();
	await async_deleteDocs(name_coll, jsonDeleteInfo);
	render_collection_space(name_coll);
}

function goToChange(){
	let documents = root.querySelectorAll(".root-ul");
	for (let i = 0; i < documents.length; i++) {
		let doc = documents[i];
		if (doc.style.background == "rgb(209, 255, 223)") {
			let id_block = doc.querySelector("._id");
			let id = id_block.textContent.split(":")[1];
			render_page_change(name_coll, id);
			break;
		}
	}
}
