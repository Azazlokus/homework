db.Sellers.drop();
db.Sales.drop();
db.Points_of_sale.drop();
db.Products.drop();
db.Storages.drop();
db.Ords.drop();


/* P R O D U C T S */

let product_1 = db.Products.insertOne({
	name: "banana",
	measure_unit: "kg",
	manufacturer: "Akibaplace",
})

let product_2 = db.Products.insertOne({
	name: "apple",
	measure_unit: "kg",
	manufacturer: "Plobiget",
})

let product_3 = db.Products.insertOne({
	name: "orange",
	measure_unit: "kg",
	manufacturer: "Kagmal",
})

let product_4 = db.Products.insertOne({
	name: "beef",
	measure_unit: "kg",
	manufacturer: "Pandl",
})

let product_5 = db.Products.insertOne({
	name: "ice cream",
	measure_unit: "kg",
	manufacturer: "IceLand",
})

/* P O I N T S _ O F _ S A L E */

let point_1 = db.Points_of_sale.insertOne({
	type: "store",
	address: "72 Via Bahia",
	name: "Super Products",
	city: "Chicago",
})

let point_2 = db.Points_of_sale.insertOne({
	type: "stall",
	address: "6741 Takashi Blvd.",
	name: "Your Choice",
	city: "Moscow",
})

let point_3 = db.Points_of_sale.insertOne({
	type: "store",
	address: "11368 Chanakya",
	name: "My products",
	city: "New Delhi",
})

let point_4 = db.Points_of_sale.insertOne({
	type: "stand",
	address: "281 King Street",
	name: "Magns",
	city: "Paris",
})

let point_5 = db.Points_of_sale.insertOne({
	type: "store",
	address: "15 Henessey Road",
	name: "Akina",
	city: "Tokio",
})

/* S U P P L I E R S */
let supplier_1 = {
	name: "The Fasters",
	address: "15 Henessey Road",
	phone: "852-3692888",
}

let supplier_2 = {
	name: "Food Delivery",
	address: "172 Rue de Rivoli",
	phone: "33-2257201",
}

let supplier_3 = {
	name: "The PA",
	address: "6 Saint Antoine",
	phone: "234-6036201",
}

let supplier_4 = {
	name: "Not only it",
	address: "435 Gruenestrasse",
	phone: "49-527454",
}

let supplier_5 = {
	name: "The Best Prod",
	address: "3 Via Saguaro",
	phone: "52-404562",
}

/* O R D S */

let ord_1 = db.Ords.insertOne({
	date_ordered: new Date("07-01-2020"),
	date_shipped: new Date("07-28-2020"),
	total_price: 1660,
	point_of_sale: point_1.insertedId,
	products: [
		{
			product: db.Products.findOne({_id: product_1.insertedId}),
			price: 100,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 70,
			quantity: 6,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			price: 120,
			quantity: 2,
		},
	],
	supplier: supplier_1,
})

let ord_2 = db.Ords.insertOne({
	date_ordered: new Date("08-01-2021"),
	date_shipped: new Date("08-05-2021"),
	total_price: 3960,
	point_of_sale: point_1.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 200,
			quantity: 15,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 120,
			quantity: 8,
		},
	],
	supplier: supplier_2,
})

let ord_3 = db.Ords.insertOne({
	date_ordered: new Date("03-07-2022"),
	date_shipped: new Date("03-10-2022"),
	total_price: 4720,
	point_of_sale: point_2.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_1.insertedId }),
			price: 200,
			quantity: 8,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 120,
			quantity: 12,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			price: 120,
			quantity: 14,
		},
	],
	supplier: supplier_3,
})

let ord_4 = db.Ords.insertOne({
	date_ordered: new Date("04-10-2022"),
	date_shipped: new Date("04-24-2022"),
	total_price: 3390,
	point_of_sale: point_3.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_1.insertedId }),
			price: 150,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 70,
			quantity: 12,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 210,
			quantity: 5,
		},
	],
	supplier: supplier_4,
})

let ord_5 = db.Ords.insertOne({
	date_ordered: new Date("07-07-2022"),
	date_shipped: new Date("08-01-2022"),
	total_price: 4640,
	point_of_sale: point_4.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 100,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 135,
			quantity: 9,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 95,
			quantity: 15,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			price: 250,
			quantity: 4,
		},
	],
	supplier: supplier_4,
})

let ord_6 = db.Ords.insertOne({
	date_ordered: new Date("23-10-2022"),
	date_shipped: new Date("27-10-2022"),
	total_price: 3170,
	point_of_sale: point_5.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 120,
			quantity: 20,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 110,
			quantity: 7,
		},
	],
	supplier: supplier_5,
})

/* S T O R A G E S */

let storage_1 = db.Storages.insertOne({
	point_of_sale: point_1.insertedId,
	products: [
		{
			product: db.Products.findOne({_id: product_1.insertedId}),
			quantity: 10,
			price: 100,
		},
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			quantity: 25,
			price: 250,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			quantity: 30,
			price: 90,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			quantity: 10,
			price: 70,
		}
	]
})

let storage_2 = db.Storages.insertOne({
	point_of_sale: point_2.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_1.insertedId }),
			quantity: 10,
			price: 200,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			quantity: 15,
			price: 130,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			quantity: 35,
			price: 100,
		}
	]
})

let storage_3 = db.Storages.insertOne({
	point_of_sale: point_3.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_1.insertedId }),
			quantity: 20,
			price: 130,
		},
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			quantity: 25,
			price: 220,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			quantity: 30,
			price: 140,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			quantity: 160,
			price: 100,
		}
	]
})

let storage_4 = db.Storages.insertOne({
	point_of_sale: point_4.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			quantity: 20,
			price: 200,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			quantity: 30,
			price: 125,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			quantity: 90,
			price: 125,
		}
	]
})

let storage_5 = db.Storages.insertOne({
	point_of_sale: point_5.insertedId,
	products: [
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			quantity: 40,
			price: 130,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			quantity: 70,
			price: 90,
		}
	]
})

/* S E L L E R S */
let seller_1 = db.Sellers.insertOne({
	first_name: "Max",
	last_name: "Blaber",
	phone: "88294-832",
	salary: 1000,
	point_of_sale: point_1.insertedId,
})

let seller_2 = db.Sellers.insertOne({
	first_name: "Petr",
	last_name: "Symal",
	phone: "882-421-832",
	salary: 2000,
	point_of_sale: point_2.insertedId,
})

let seller_3 = db.Sellers.insertOne({
	first_name: "John",
	last_name: "Cyber",
	phone: "84-832-38-482",
	salary: 2500,
	point_of_sale: point_3.insertedId,
})

let seller_4 = db.Sellers.insertOne({
	first_name: "John",
	last_name: "Stradinsky",
	phone: "4385-575-4839",
	salary: 1000,
	point_of_sale: point_4.insertedId,
})

let seller_5 = db.Sellers.insertOne({
	first_name: "Mike",
	last_name: "Ponder",
	phone: "847-48395-328",
	salary: 800,
	point_of_sale: point_5.insertedId,
})

/* C U S T O M E R S */
let customer_1 = {
	first_name: "William",
	last_name: "Hart",
}

let customer_2 = {
	first_name: "Jose",
	last_name: "Adams",
}

let customer_3 = {
	first_name: "Brian",
	last_name: "Diaz",
}

let customer_4 = {
	first_name: "Paul",
	last_name: "Johnson",
}

let customer_5 = {
	first_name: "Ralph",
	last_name: "Smith",
}

let customer_6 = {
	first_name: "Roger",
	last_name: "Klein",
}

let customer_7 = {
	first_name: "Ronald",
	last_name: "Walker",
}

/* S A L E S */
let sale_1 = db.Sales.insertOne({
	date: new Date("02-05-2022"),
	total_price: 1000,
	customer: customer_1,
	products: [
		{
			product: db.Products.findOne({_id: product_1.insertedId}),
			price: 100,
			quantity: 10,
		}
	],
	seller: db.Sellers.findOne({_id: seller_1.insertedId}),
})

let sale_2 = db.Sales.insertOne({
	date: new Date("02-05-2022"),
	total_price: 2250,
	customer: customer_2,
	products: [
		{
			product: db.Products.findOne({ _id: product_1.insertedId }),
			price: 100,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 250,
			quantity: 5,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_1.insertedId }),
})

let sale_3 = db.Sales.insertOne({
	date: new Date("05-05-2022"),
	total_price: 650,
	customer: customer_3,
	products: [
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 130,
			quantity: 5,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_2.insertedId }),
})

let sale_4 = db.Sales.insertOne({
	date: new Date("05-05-2022"),
	total_price: 360,
	customer: customer_4,
	products: [
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 130,
			quantity: 2,
		},
		{
			product: db.Products.findOne({ _id: product_5.insertedId }),
			price: 100,
			quantity: 1,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_2.insertedId }),

})

let sale_5 = db.Sales.insertOne({
	date: new Date("12-01-2022"),
	total_price: 1400,
	customer: customer_5,
	products: [
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 140,
			quantity: 10,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_3.insertedId }),

})

let sale_6 = db.Sales.insertOne({
	date: new Date("07-07-2022"),
	total_price: 3875,
	customer: customer_6,
	products: [
		{
			product: db.Products.findOne({ _id: product_2.insertedId }),
			price: 200,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 125,
			quantity: 10,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 125,
			quantity: 5,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_4.insertedId }),

})

let sale_7 = db.Sales.insertOne({
	date: new Date("08-07-2022"),
	total_price: 1100,
	customer: customer_7,
	products: [
		{
			product: db.Products.findOne({ _id: product_3.insertedId }),
			price: 130,
			quantity: 5,
		},
		{
			product: db.Products.findOne({ _id: product_4.insertedId }),
			price: 90,
			quantity: 5,
		}
	],
	seller: db.Sellers.findOne({ _id: seller_5.insertedId }),
})

