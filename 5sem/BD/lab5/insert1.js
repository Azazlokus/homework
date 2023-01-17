db.employee_blank.insertMany([
	{
		id: 1,
		name: "Иван",
		sername: "Иванов",
		father_name: "Иванович",
		email: "ivan@gmail.com",
		telefone_number: "8(777)111-11-11",
		birthday: "10.10.1987",
		hobby: ["плавание", "шахматы", "футбол"],
		prikaz: {
			"Номер уведомления": 123
		}
	},
	{
		id: 2,
		name: "Николай",
		sername: "Семерук",
		father_name: "Александрович",
		email: "killer@rambler.ru",
		telefone_number: "7(777)523-68-91",
		hobby: ["бокс", "волейбол", "баскетбол"],
		prikaz: {
			"Номер приказа": 1001
		}
	},
	{
		id: 3,
		name: "Александр",
		sername: "Хопта",
		father_name: "Петрович",
		email: "sasha@.ru",
		telefone_number: "(2-20-47)",
		hobby: ["плавание", "компьютерные игры"],
		prikaz: {
			"Номер распоряжения": 202
		}
	},
	{
		id: 4,
		name: "Владимир",
		sername: "Никифоров",
		father_name: "Александрович",
		email: "vova@rambler.ru",
		telefone_number: "2-45-48",
		birthday: "12.07.1967",
		prikaz: {
			"Номер приказа": 404
		}
	},
	{
		id: 5,
		name: "Семен",
		sername: "Лобанов",
		father_name: "Иванович",
		email: "semen@yandex.com",
		telefone_number: "8(777)654-12-21",
		hobby: ["борьба", "волейбол", "танцы"],
		prikaz: {
			"Номер приказа": 15
		}
	},
	{
		id: 6,
		name: "Глеб",
		sername: "Кисегач",
		father_name: "Викторович",
		email: "gleb@mail.",
		telefone_number: "2-87-98",
		hobby: ["компьютерные игры", "вязание", "сеги", "волонтерство"],
		prikaz: {
			"Номер распоряжения": 333
		}
	},
	{
		id: 7,
		name: "Варя",
		sername: "Черноус",
		father_name: "Петрович",
		email: "cher@mail.ru",
		birthday: "14.01.1980",
		prikaz: {
			"Номер приказа": 1
		}
	}
])