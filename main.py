CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "회의록 요약",
        "content": "회의 내용을 핵심 요약, 결정사항, 담당자, 일정으로 정리해 주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "AI 뉴스 요약",
        "content": "AI 또는 IT 관련 뉴스를 한국어 3줄 이내로 요약해 주세요.",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "광고 영상 생성",
        "content": "30초 분량의 제품 광고 영상 스토리보드와 내레이션을 작성해 주세요.",
        "category": "영상 생성",
        "favorite": True
    }
]


# 메뉴를 출력하고 사용자의 선택을 입력받아 반환한다
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    return input("선택: ").strip()


# 제목, 내용, 카테고리를 입력받아 새 프롬프트를 목록에 추가한다
def add_prompt(prompts):
    title = input("제목: ").strip()
    while not title:
        title = input("제목을 입력해 주세요: ").strip()

    content = input("내용: ").strip()
    while not content:
        content = input("내용을 입력해 주세요: ").strip()

    print("카테고리를 선택하세요:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}. {c}")
    print(f"{len(CATEGORIES) + 1}. 직접 입력")

    category = ""
    while not category:
        choice = input("선택: ").strip()
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(CATEGORIES):
                category = CATEGORIES[choice_num - 1]
            elif choice_num == len(CATEGORIES) + 1:
                category = input("카테고리 이름을 입력해 주세요: ").strip()
        if not category:
            print("잘못된 입력입니다. 다시 선택해 주세요.")

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("프롬프트가 추가되었습니다.")


# 전체 프롬프트 목록을 번호와 함께 출력한다
def show_list(prompts):
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} [{p['category']}] {star}")


# 선택한 카테고리에 해당하는 프롬프트만 필터링해 출력한다
def show_by_category(prompts):
    print("카테고리를 선택하세요:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}. {c}")

    category = ""
    while not category:
        choice = input("선택: ").strip()
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(CATEGORIES):
                category = CATEGORIES[choice_num - 1]
        if not category:
            print("잘못된 입력입니다. 다시 선택해 주세요.")

    filtered = [p for p in prompts if p["category"] == category]
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(filtered, start=1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} {star}")


# 제목이나 내용에 검색어가 포함된 프롬프트를 찾아 출력한다
def search_prompt(prompts):
    keyword = input("검색어: ").strip()
    while not keyword:
        keyword = input("검색어를 입력해 주세요: ").strip()

    result = [
        p for p in prompts
        if keyword in p["title"] or keyword in p["content"]
    ]
    if not result:
        print("검색 결과가 없습니다.")
        return

    for i, p in enumerate(result, start=1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} [{p['category']}] {star}")


# 번호를 입력받아 해당 프롬프트의 상세 정보를 출력한다
def show_detail(prompts):
    show_list(prompts)
    number = input("상세히 볼 번호: ").strip()

    if not number.isdigit() or not (1 <= int(number) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(number) - 1]
    star = "⭐" if p["favorite"] else ""
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(f"내용: {p['content']}")


# 번호를 입력받아 해당 프롬프트의 즐겨찾기 상태를 토글한다
def toggle_favorite(prompts):
    show_list(prompts)
    number = input("즐겨찾기 토글할 번호: ").strip()

    if not number.isdigit() or not (1 <= int(number) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(number) - 1]
    p["favorite"] = not p["favorite"]
    status = "등록" if p["favorite"] else "해제"
    print(f"'{p['title']}' 즐겨찾기 {status}되었습니다.")


# 즐겨찾기로 등록된 프롬프트만 필터링해 출력한다
def show_favorites(prompts):
    favorites = [p for p in prompts if p["favorite"]]
    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in enumerate(favorites, start=1):
        print(f"{i}. {p['title']} [{p['category']}] ⭐")


# 메뉴 선택을 반복 입력받아 각 기능 함수로 분기한다
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            show_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            toggle_favorite(prompts)
        elif choice == "7":
            show_favorites(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
