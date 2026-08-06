CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = []


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
    print("(프롬프트 추가 기능은 구현 예정입니다)")


def show_list(prompts):
    print("(프롬프트 목록 기능은 구현 예정입니다)")


def show_by_category(prompts):
    print("(카테고리별 조회 기능은 구현 예정입니다)")


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
