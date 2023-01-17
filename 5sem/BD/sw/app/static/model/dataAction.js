export function convertJsonToHtml(json){
	let info = ``;
	let i = 1;
	json.forEach(el => {
		let keys = Object.keys(el);
		let content = ``;

		keys.forEach(key => {
			let block = ``;
			if (typeof el[key] === "object" & !Array.isArray(el[key])){
				block =  "[\n" + objToHtml(el[key]) + "]";
			} else {
				block = el[key];
			}
			content += `<li class="${key}"><p class='obj-key'>${key}:</p>${block}</li>`;
		});

		info += `<ul class='root-ul'><span class='obj-title'>Document ${i}</span>
			${content}
		</ul>`;
		i++;
	});

	let res = `
		<div class='documents'>
			${info}
		</div>
	`
	return res;
}

export function objToHtml(obj){
	let keys = Object.keys(obj);
	let content = ``;
	keys.forEach(key => {
		if (typeof obj[key] === "object" & !Array.isArray(obj[key])){
			content += `<li><p class='obj-key'>\t${key}: [</p>${objToHtml(obj[key])}]</li>`;
		} else {
			content += `<li><p class='obj-key'>\t${key}:</p>${obj[key]}</li>`;
		}
	});
	let block = `<ul>${content}</ul>`;
	return block;
}

export function convertObj(obj) {
	let keys = Object.keys(obj);
	let new_obj = {};
	keys.forEach(key => {
		if (typeof obj[key] !== "object" & key !== "_id") {
			new_obj[key] = obj[key];
		}
	});
	return new_obj;
}

export function textToObject(text) {
	let obj = {};
	obj = JSON.parse("{" + text + "}");
	let keys = Object.keys(obj);
	keys.forEach(key => {
		obj[key] = convertField(obj[key]);
	});
	return obj;
}

function convertField(value) {
	if (typeof value === "object" & !Array.isArray(value)) {
		let keys = Object.keys(value);
		keys.forEach(key => {
			value[key] = convertField(value[key]);
		});
	} else {
		let temp;
		try {
			temp = new Date(getDate(value));
			if (temp != "Invalid Date") return temp;
		} catch (error) {

		}
	}
	return value;
}

function getDate(word) {
	let parts = word.split('.');
	let day = parts[0];
	let month = parts[1];
	let year = parts[2];
	return year + '-' + month + '-' + day;
}
