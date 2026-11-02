def add_attendance(records):
    date = input("날짜를 입력하세요 (예: 2024-01-15): ").strip()
    if not date:
        print("날짜는 비워 둘 수 없습니다.")
        return

    name = input("이름을 입력하세요: ").strip()
    if not name:
        print("이름은 비워 둘 수 없습니다.")
        return

    records.append({"date": date, "name": name})
    print(f"{date} {name} 출석이 추가되었습니다.")


def show_attendance(records):
    if not records:
        print("출석 기록이 없습니다.")
        return

    print("\n[출석 목록]")
    for i, record in enumerate(records, start=1):
        print(f"{i}. 날짜: {record['date']} / 이름: {record['name']}")


def main():
    records = []

    while True:
        print("\n=== 스터디 출석부 ===")
        print("1. 출석 추가")
        print("2. 출석 목록 보기")
        print("3. 종료")

        menu = input("메뉴를 선택하세요: ").strip()

        if menu == "1":
            add_attendance(records)
        elif menu == "2":
            show_attendance(records)
        elif menu == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")


if __name__ == "__main__":
    main()