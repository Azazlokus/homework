export async function async_getCollections() {
	let response = await fetch('/collections', { method: 'GET' });
	let data = await response.json();
	return data;
}

export async function async_getDocs(name) {
	let response = await fetch(`/collections/${name}`, { method: 'GET' });
	let data = await response.json();
	return data;
}

export async function async_deleteDocs(name, docs){
	let response = await fetch(`/collections/${name}`, { method: "DELETE", headers: { "data": JSON.stringify(docs), "Content-type": "application/json; charset=utf-8" }});
	return response;
}

export async function async_getDoc(name, id){
	let response = await fetch(`/collections/${name}/${id}`, { method: 'GET' });
	let data = await response.json();
	return data;
}

export async function async_updateDoc(name, id, data){
	await fetch(`/collections/${name}/${id}`, { method: 'POST', headers: { "Content-type": "application/json; charset=utf-8" }, body:  JSON.stringify(data)});
}

export async function async_addDoc(name, data){
	await fetch(`/collections/${name}`, { method: "POST", headers: { "Content-type": "application/json; charset=utf-8" }, body: JSON.stringify(data)});
}