let btn_articles_list = document.getElementById("btn_articles_list");
let info = document.getElementById("info");
btn_articles_list.addEventListener("click", async function () {
	let response = await fetch("/articles_list", { method: "GET" });
	let data = await response.json();
	show_docs(data);
});

function show_docs(docs) {
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