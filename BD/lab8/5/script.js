let btn_articles_list = document.getElementById("btn_articles_list");

let btn_title_info = document.getElementById("btn_title_info");
let input_title_info = document.getElementById("title_info");

let btn_author_info = document.getElementById("btn_author_info");
let input_author_info = document.getElementById("author_info");

let info = document.getElementById("info");

btn_articles_list.addEventListener("click", async function () {
	let response = await fetch("/articles_list", { method: "GET" });
	let data = await response.json();
	show_docs(data);
});

btn_title_info.addEventListener("click", async function() {
	let title = {
		title: input_title_info.value,
	}
	let response = await fetch("/articles_by_title", { method: "POST", body: JSON.stringify(title)});
	let data = await response.json();
	show_docs(data);
});

btn_author_info.addEventListener("click", async function(){
	let author = {
		author: input_author_info.value,
	}
	let response = await fetch("/articles_by_author", { method: "POST", body: JSON.stringify(author) });
	let data = await response.json();
	show_docs(data);
});

function show_docs(docs){
	info.innerHTML = "";
	let keys = Object.keys(docs[0]);
	for (let i = 0; i < docs.length; i++) {
		let node = document.createTextNode(i + 1 + "\n");
		info.appendChild(node);
		for (let j = 0; j < keys.length; j++) {
			let text = keys[j] + ": " + docs[i][keys[j]] + "\n"
			let node = document.createTextNode(text);
			info.appendChild(node);
		}
	}
}