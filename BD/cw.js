db.articles.insertMany([
	{
		title: "статья 1",
		author: "Воробьев Максим Витальевич",
		placement_date: new Date("04.04.2022"),
		url: "ссылка 1",
		tags: ["статья1", "паттерны программирования", "разработка веб-сайтов", "проектирование"],
		comments: [
			{
				user_name: "Иванов Петр Михайлович",
				email: "petya@gmail.com",
				phone:"8(977)345-32-11",
				text:"ну сойдет",
				mark: 7,
			}
		],
	},
	{
		title: "статья 2",
		author: "Иванов Петр Михайлович",
		placement_date: new Date("07.12.2021"),
		url: "ссылка 2",
		tags: ["статья2", "медицина", "спорт"],
		comments: [
			{
				user_name: "Воробьев Максим Витальевич",
				email: "maaaaax@gmail.com",
				phone: "8(977)345-32-11",
				text: "ввввв",
				mark: 5,
			}, 
			{
				user_name: "Борисов Иван Евгеньевич",
				email: "misha@rambler.ru",
				phone: "8(977)111-32-11",
				text: "ууууу",
				mark: 10,
			}, 
		],
	},
	{
		title: "статья 3",
		author: "Воробьев Максим Витальевич",
		placement_date: new Date("02.01.2022"),
		url: "ссылка 3",
		tags: ["3", "точные вычисления", "спорт"],
		comments: [
			{
				user_name: "Иванов Петр Михайлович",
				email: "petya@gmail.com",
				phone: "8(977)222-22-22",
				text: "комментарий к 3 статье",
				mark: 7,
			},
			{
				user_name: "Иванов Иван Иванович",
				email: "vanya@gmail.com",
				phone: "8(977)111-32-11",
				text: "666666",
				mark: 6,
			},
		],
	},
	{
		title: "статья 4",
		author: "Иванов Иван Иванович",
		placement_date: new Date("12.07.2022"),
		url: "ссылка 4",
		tags: ["математика", "экономика и бизнес", "разработка веб-сайтов"],
		comments: [
			{
				user_name: "Воробьев Максим Витальевич",
				email: "rira@yandex.ru",
				phone: "8(977)555-55-55",
				text: "комментарий к 4 статье",
				mark: 2,
			},
			{
				user_name: "Иванов Петр Михайлович",
				email: "misha@rambler.ru",
				phone: "8(977)111-32-11",
				text: "666666",
				mark: 6,
			},
			{
				user_name: "Андроид",
				email: "andrrrrr@yandex.ru",
				phone: "8(222)225-17-77",
				text: "класс!!!!!!",
				mark: 10,
			}
		],
	},
	{
		title: "статья 5",
		author: "Клименчук Владислав Сергеевич",
		placement_date: new Date("04.27.2022"),
		url: "ссылка 5",
		tags: ["5", "садоводство", "селекция"],
		comments: [
			{
				user_name: "Мария",
				email: "masha1718@gmail.com",
				phone: "8(748)555-55-44",
				text: "оооо!",
				mark: 9,
			},
			{
				user_name: "Иванов Иван Иванович",
				email: "vanya@gmail.com",
				phone: "8(111)555-32-11",
				text: "666666",
				mark: 6,
			},
			{
				user_name: "Андроид",
				email: "andrrrrr@yandex.ru",
				phone: "8(222)225-17-77",
				text: "сойдет",
				mark: 5,
			}
		],
	},

])