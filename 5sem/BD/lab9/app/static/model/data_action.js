export function show_docs(docs) {
	let info = document.getElementById('info');
	info.innerHTML = '';
	let i = 1;
	docs.forEach(doc => {
		let keys = Object.keys(doc);
		let div_element = document.createElement("div");
		let div_info = document.createElement("div");
		div_element.className = "item";
		div_info.className = "info";
		let span_num = document.createElement("span");
		span_num.className = "number";
		let node = document.createTextNode(i + '\n');
		span_num.appendChild(node);
		div_info.appendChild(span_num);
		keys.forEach(key => {
			let span = document.createElement("span");
			span.className = key;
			if (key == "reviews") {
				let text = key + ":\n";
				let node = document.createTextNode(text);
				span.appendChild(node);
				show_object(span, doc[key]);
			} else {
				let text = key + ': ' + doc[key];
				let node = document.createTextNode(text);
				span.appendChild(node);
			}
			div_info.appendChild(span);
			div_element.appendChild(div_info);
		});
		i += 1
		info.appendChild(div_element);
	});
}

export function show_docs_w(docs, info_func, delete_func) {
	let info = document.getElementById('info');
	info.innerHTML = '';
	let i = 1;
	docs.forEach(doc => {
		let keys = Object.keys(doc);
		let div_element = document.createElement("div");
		let div_info = document.createElement("div");
		let div_button = document.createElement("div");
		div_element.className = "item";
		div_info.className = "info";
		div_button.className = "controls";

		let btn_info = document.createElement("button");
		btn_info.textContent = "Полная информация";
		btn_info.addEventListener("click", info_func);

		let btn_delete = document.createElement("button");
		btn_delete.textContent = "Удалить";
		btn_delete.addEventListener("click", delete_func);

		div_button.appendChild(btn_info);
		div_button.appendChild(btn_delete);

		let span_num = document.createElement("span");
		span_num.className = "number";
		let node = document.createTextNode(i + '\n');
		span_num.appendChild(node);
		div_info.appendChild(span_num);
		keys.forEach(key => {
			let span = document.createElement("span");
			span.className = key;
			let text = key + ': ' + doc[key] + '\n'
			let node = document.createTextNode(text);
			span.appendChild(node);
			div_info.appendChild(span);
			div_element.appendChild(div_info);
		});
		div_element.appendChild(div_button);
		info.appendChild(div_element);
		i += 1;
	});
}

function show_object(span, object) {
	let keys = Object.keys(object[0]);
	object.forEach(review => {
		let text = "\t[\n";
		let node = document.createTextNode(text);
		span.appendChild(node);
		keys.forEach(key => {
			let text = "\t\t" + key + ":" + review[key] + "\n";
			let node = document.createTextNode(text);
			span.appendChild(node)
		});
		text = "\t]\n";
		node = document.createTextNode(text);
		span.appendChild(node);
	});
}