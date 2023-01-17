db.students.insertMany(	
	[{firstName: "Максим", lastName: "Воробьев", middleName: "Витальевич",
	birthday: 2002, course: 3, direction_study: "ФИТ",
	languages: ["Английский"],
	studed: [{title: "МатАнализ", semestr: 3, mark: 4},
			{title: "Дифференциальные уравнения", semestr: 4, mark: 5}
			]},
	{firstName: "Петр", lastName: "Иванов", middleName: "Михайлович", birthday: 2002,
	course: 3, direction_study: "ФИТ", languages: ["Английский"],
	studed: [{title: "МатАнализ", semestr: 3, mark: 4},
			{title: "История", semestr: 1, mark: 5}
			]},
	{firstName: "Максим", lastName: "Дубов", middleName: "Анатольевич",
	birthday: 2001, course: 4, direction_study: "ФИТ",
	languages: ["Английский", "Французский"],
	studed: [{title: "МатАнализ", semestr: 1, mark: 3},
			{title: "Дифференциальные уравнения", semestr: 4, mark: 5}
			]},
		{firstName: "Андрей", lastName: "Белозелов", middleName: "Владимирович",
		birthday: 2004, course: 1, direction_study: "ФИТ", languages: ["Китайский"],
		studed: [{title: "МатСтатистика", semestr: 3, mark: 5},
				{title: "Дифференциальные уравнения", semestr: 3, mark: 3}
			]}
	]
)
