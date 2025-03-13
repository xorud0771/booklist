import sys  # 프로그램 종료를 위해 sys 모듈 사용

# 사용자에게 보여줄 메뉴 화면
# 여러 가지 기능(도서 추가, 수정, 삭제, 검색, 대여/반납, 종료)이 있음
display = '''
-------------------------------------------------------------
1. 도서 추가, 2. 도서 수정, 3. 도서 삭제, 4. 도서 검색, 5. 도서 대여 반납 6. 프로그램 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

# 도서를 저장할 리스트 (기본적으로 한 개의 예제 도서 포함)
books = [
    {"ISBN": "0000", "제목": "파이썬 프로그래밍", "저자": "홍길동", "대여 여부": False}
]

# 프로그램이 종료될 때까지 계속 실행
while True:
    menu = input(display)  # 사용자 입력 받기 (input 함수 사용: 사용자의 입력을 문자열로 받음)

    if menu == '1':  # 도서 추가 기능 (if 조건문 사용: 사용자의 선택에 따라 기능 실행)
        print('\n📚 도서 추가')  # print 함수 사용: 사용자에게 도서 추가 기능을 알림
        while True:
            book_number = input("번호를 입력하세요(4자리로 설정하시오) >>> ")  # 사용자 입력 받기
            check = 0  # 중복 여부 확인을 위한 변수 (0: 중복 없음, 1: 중복 있음)
            for book in books:  # for 루프 사용: books 리스트의 각 도서를 순회
                if book["ISBN"] == book_number:  # if 조건문 사용: 입력한 ISBN이 이미 존재하면
                    check = 1  # 중복 확인 변수 변경
                    print("❌ 중복된 번호입니다. 새로운 번호로 다시 입력하세요.")  # 중복 메시지 출력
                    break  # break 사용: 중복 발견 시 루프 종료
            if check == 0:  # 중복이 없으면 루프 종료
                break

        book_title = input("제목을 입력하세요 >>> ")  # 사용자 입력 받기 (도서 제목)
        book_author = input("저자를 입력하세요 >>> ")  # 사용자 입력 받기 (도서 저자)

        # 입력받은 정보를 books 리스트에 추가 (append 함수 사용)
        books.append({"ISBN": book_number, "제목": book_title, "저자": book_author, "대여 여부": False})

        print("✅ 도서가 추가되었습니다.")  # print 함수 사용: 완료 메시지 출력

    elif menu == '2':  # 도서 수정 기능
        print('\n✏️ 도서 수정')  # print 함수 사용: 사용자에게 도서 수정 기능을 알림
        if not books:  # if 조건문 사용: books 리스트가 비어 있는 경우
            print("❌ 수정할 도서가 없습니다.")  # 메시지 출력
            continue  # continue 사용: 다음 루프로 넘어감
        
        # 도서 목록 출력 (enumerate 함수 사용: 리스트 순회하며 인덱스와 요소 가져옴)
        for i, book in enumerate(books, start=1):
            print(f"{i}. 제목: {book['제목']} (ISBN: {book['ISBN']}, 저자: {book['저자']}, 대여 여부: {'대여 중' if book['대여 여부'] else '대여 가능'})")

        while True:
            try:
                book_num = int(input("수정할 도서 번호 입력 > ").strip()) - 1  # 사용자 입력을 숫자로 변환 (int 함수 사용)
                if 0 <= book_num < len(books):  # if 조건문 사용: 올바른 범위인지 확인
                    break
                else:
                    print("❌ 존재하지 않는 번호입니다. 다시 입력하세요.")  # 오류 메시지 출력
            except ValueError:  # 예외 처리 (ValueError 발생 시)
                print("❌ 숫자로 입력하세요.")

        while True:
            print("\n수정할 항목을 선택하세요:")  # print 함수 사용: 사용자에게 선택지 제공
            print("1. ISBN")
            print("2. 제목")
            print("3. 저자")

            try:
                number = int(input("수정할 부분 > ").strip())  # 사용자 입력을 숫자로 변환 (int 함수 사용)
                if number in [1, 2, 3]:  # if 조건문 사용: 입력값이 1, 2, 3 중 하나인지 확인
                    break
                else:
                    print("❌ 올바른 번호를 입력하세요.")  # 오류 메시지 출력
            except ValueError:  # 예외 처리 (ValueError 발생 시)
                print("❌ 숫자로 입력하세요.")

        # 선택한 항목을 수정
        if number == 1:
            while True:
                new_isbn = input(f'새 ISBN을 입력하세요 (기존 ISBN: {books[book_num]["ISBN"]}): ').strip()
                if any(book["ISBN"] == new_isbn for book in books):  # any 함수 사용: 리스트 내 중복 확인
                    print("❌ 이미 존재하는 ISBN입니다. 다시 입력하세요.")
                else:
                    books[book_num]["ISBN"] = new_isbn  # 새로운 ISBN 할당
                    print("✅ ISBN이 수정되었습니다.")
                    break
        elif number == 2:
            new_title = input(f'새 제목을 입력하세요 (기존 제목: {books[book_num]["제목"]}): ').strip()
            books[book_num]["제목"] = new_title  # 새로운 제목 할당
            print("✅ 제목이 수정되었습니다.")
        elif number == 3:
            new_author = input(f'새 저자를 입력하세요 (기존 저자: {books[book_num]["저자"]}): ').strip()
            books[book_num]["저자"] = new_author  # 새로운 저자 할당
            print("✅ 저자가 수정되었습니다.")

    elif menu == '6':  # 프로그램 종료 기능
        print('\n프로그램 종료')  # print 함수 사용: 사용자에게 종료 메시지 출력
        sys.exit()  # 프로그램 종료 (sys.exit 함수 사용)

    else:
        print("❌ 잘못된 입력입니다. 다시 선택하세요.")  # print 함수 사용: 잘못된 입력 메시지 출력
