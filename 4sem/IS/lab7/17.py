import datetime


class Report:

    reports = []

    def add(self, count):
        for i in range(count):
            print("Доклад №" + str(i+1))
            theme = input("Введите тему выступления: ")
            time = input("Введите время начала выступления в формате ЧЧ:ММ: ")
            start_time = time.split(":")
            start_time = datetime.timedelta(hours=float(
                start_time[0]), minutes=float(start_time[1]), seconds=float(0))
            time = input(
                "Введите продолжительность выступления в формате ЧЧ:ММ: ")
            duration = time.split(":")
            duration = datetime.timedelta(hours=float(
                duration[0]), minutes=float(duration[1]), seconds=float(0))
            self.reports.append((theme, start_time, duration))

    def check_reports(self):
        self.reports = sorted(self.reports, key=lambda x: x[1])
        for i in range(len(self.reports) - 1):
            start_time1 = self.reports[i][1]
            end_time1 = self.reports[i][1] + self.reports[i][2]
            start_time2 = self.reports[i + 1][1]
            end_time2 = self.reports[i + 1][1] + self.reports[i + 1][2]
            if start_time1 >= start_time2 and (end_time1 < end_time2 or end_time2 < end_time1) \
            or start_time1 == start_time2 and (end_time1 < end_time2 or end_time2 < end_time1):
                print(f"Доклады №{i + 1} и №{i + 2} перекрывают друг друга")
                print("Попробуйте пересоздать доклады")
                exit(1)


class Conference:

    def __init__(self):
        self.reports = Report()

    def output_info(self):
        sorted_reports = self.reports.reports
        sorted_reports = sorted(sorted_reports, key=lambda x: x[1])

        max_rel = datetime.timedelta(hours=0, minutes=0, seconds=0)
        for i in range(len(sorted_reports) - 1):
            sub = sorted_reports[i + 1][1] - \
                (sorted_reports[i][2] + sorted_reports[i][1])
            if sub > max_rel:
                max_rel = sub

        print(f"\tЧисло выступлений: {len(sorted_reports)}")
        print(
            f"\tОбщая продолжительность: {sorted_reports[-1][1] + sorted_reports[-1][2] - sorted_reports[0][1]}")
        print(f"\tВремя самого длительного перерыва: {max_rel}")

    def start_create(self):
        count = int(input("Сколько выступлений добавить в конференцию: "))
        self.reports.add(count)
        print("Доклады были добавлены")
        self.reports.check_reports()
        print("Вы успешно создали конференцию: ")
        self.output_info()


conf = Conference()
conf.start_create()
