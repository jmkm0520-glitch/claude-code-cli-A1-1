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
    # TODO(5-1): 제목/내용/카테고리 입력, 빈 값 검증, 카테고리 선택/직접입력, favorite=False로 추가
    print("(프롬프트 추가 기능은 구현 예정입니다)")


def show_list(prompts):
    # TODO(5-2): 번호와 함께 제목/카테고리/즐겨찾기(⭐) 출력, 없으면 안내 메시지
    print("(프롬프트 목록 기능은 구현 예정입니다)")


def show_by_category(prompts):
    # TODO(5-3): 카테고리 목록 출력 후 선택한 카테고리만 필터링해서 출력
    print("(카테고리별 조회 기능은 구현 예정입니다)")


def search_prompt(prompts):
    # TODO(5-4): 키워드 입력받아 제목/내용에 포함된 프롬프트 검색
    print("(프롬프트 검색 기능은 구현 예정입니다)")


def show_detail(prompts):
    # TODO(5-5): 번호 입력받아 해당 프롬프트 전체 내용 출력, 잘못된 번호 처리
    print("(프롬프트 상세 보기 기능은 구현 예정입니다)")


def toggle_favorite(prompts):
    # TODO(5-6): 번호 입력받아 즐겨찾기 여부 토글
    print("(즐겨찾기 관리 기능은 구현 예정입니다)")


def show_favorites(prompts):
    # TODO(5-6): 즐겨찾기된 프롬프트만 모아서 출력
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
