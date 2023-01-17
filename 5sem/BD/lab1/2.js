let lessons = ["Базы данных", "Введение в машинное обучение", "Струтуры и алгоритмы обработки данных"]
let list = document.getElementById("lst")
for (let i = 0; i < lessons.length; i++) {
	let row = document.createElement("li")
	row.textContent = lessons[i]
	list.appendChild(row)
}