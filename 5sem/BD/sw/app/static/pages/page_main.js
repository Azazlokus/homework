import { async_getCollections } from "../model/request.js";
import { render_collection_space } from "./page_coll.js";

let root = undefined;

export async function render_main() {
	let data = await async_getCollections();
	root = document.body;
	let info = ``;
	data.forEach(collection => {
		info += `
			<button class='collection-btn'>${collection.name}</button>
		`
	});
	root.innerHTML = `
		<div class='wrap-content'>
			<span class='title'>Список коллекций</span>
			<div class="collections-list">
				${info}
			</div>
		</div>
	`;

	let buttons = root.querySelectorAll("button");
	buttons.forEach(button => {
		let name = button.textContent;
		button.addEventListener("click", () => render_collection_space(name));
	});
}

render_main();