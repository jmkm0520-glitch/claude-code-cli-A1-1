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


def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ").strip()
    while not title:
        title = input("제목을 입력해주세요: ").strip()

    content = input("내용: ").strip()
    while not content:
        content = input("내용을 입력해주세요: ").strip()

    print("\n카테고리 선택:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}) {category}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    category_input = input("선택: ").strip()
    if category_input.isdigit() and 1 <= int(category_input) <= len(CATEGORIES):
        category = CATEGORIES[int(category_input) - 1]
    else:
        category = input("카테고리 직접 입력: ").strip()
        while not category:
            category = input("카테고리를 입력해주세요: ").strip()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print("\n프롬프트가 추가되었습니다!")


def show_list(prompts):
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}) {category}")

    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return

    selected = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected]

    print(f"\n[{selected}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(filtered, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']}{star}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt(prompts):
    print("(프롬프트 검색 기능은 구현 예정입니다)")


def show_detail(prompts):
    print("(프롬프트 상세 보기 기능은 구현 예정입니다)")


def toggle_favorite(prompts):
    print("(즐겨찾기 관리 기능은 구현 예정입니다)")


def show_favorites(prompts):
    print("(즐겨찾기 목록 기능은 구현 예정입니다)")


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
