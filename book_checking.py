import sys  # 프로그램 종료를 위해 sys 모듈 사용

# 사용자에게 보여줄 메뉴 화면
display = '''
-------------------------------------------------------------
1. 도서 추가, 2. 도서 수정, 3. 도서 삭제, 4. 도서 목록 보기, 5. 도서 대여 반납 6. 프로그램종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

# 도서를 저장할 리스트 (초기값: 예제 도서 한 개 포함)
books = [
    {"ISBN": "0000", "제목": "파이썬 프로그래밍", "저자": "홍길동", "대여 여부": False}
]

while True:
    menu = input(display)  # 사용자 입력 받기

    if menu == '1':  # 도서 추가 기능
        print('\n도서 추가')

        while True:
            codename = input("ISBN : ")
        
            check = 0  # 중복 체크 변수
            for existing_book in books:  # 기존 도서중에서
                if existing_book["ISBN"] == codename:  # ISBN이 중복되는지 확인
                    check = 1  # 중복이면
                    print("이미 등록된 ISBN입니다. 다른 ISBN을 입력하세요.")
                    break  # 중복되면 루프 종료하고 다시 입력 받기
        
            if check == 0:  # 중복된 ISBN이 없으면 정상적으로 입력 받음
                break  # ISBN이 중복되지 않으면 반복문 종료

        bookname = input("제목 : ")
        writer = input("저자 : ")
        possibility = input("대여 여부 : ")
       
        book = {  # 딕셔너리 사용
            "ISBN": codename,
            "제목": bookname,
            "저자": writer,
            "대여 여부": possibility
        }
        books.append(book)
        print("\n도서가 추가 되었습니다\n")

    elif menu == '2':  # 도서 수정 기능
        print("\n도서 수정")

    isbn = input("수정할 도서의 ISBN을 입력하세요. >>> ").strip()
    found = None  # 수정할 도서 저장 변수

    for book in books:
        if book["ISBN"] == isbn:
            found = book
            break

    if not found:
        print("해당 ISBN의 도서를 찾을 수 없습니다.")
    else:
        print(f"\n수정할 도서: ISBN: {found['ISBN']} | 제목: {found['제목']} | 저자: {found['저자']} | 대여 여부: {found['대여 여부']}")

        print("\n1. ISBN\n2. 제목\n3. 저자\n4. 대여 여부")
        part = input("수정할 항목 번호를 입력하세요 >>> ").strip()

        if part == '1':  # ISBN 수정
            while True:
                new_isbn = input("새 ISBN을 입력하세요 >>> ").strip()
                check = any(book["ISBN"] == new_isbn for book in books)
                if check:
                    print("이미 존재하는 ISBN입니다. 다시 입력하세요.")
                else:
                    found["ISBN"] = new_isbn
                    print("ISBN이 수정되었습니다.")
                    break

        elif part == '2':  # 제목 수정
            found["제목"] = input("새 제목을 입력하세요 >>> ").strip()
            print("제목이 수정되었습니다.")

        elif part == '3':  # 저자 수정
            found["저자"] = input("새 저자를 입력하세요 >>> ").strip()
            print("저자가 수정되었습니다.")

        elif part == '4':  # 대여 여부 수정
            found["대여 여부"] = input("새 대여 여부 (True/False) >>> ").strip().lower() == "true"
            print("대여 여부가 수정되었습니다.")

        print(f"\n수정된 도서 정보: ISBN: {found['ISBN']} | 제목: {found['제목']} | 저자: {found['저자']} | 대여 여부: {found['대여 여부']}")


    

    elif menu == '3':  # 도서 삭제 기능
        print('\n도서 삭제')

        if not books: 
            print("경고: 삭제할 도서가 없습니다.")

        else:
            remove_isbn = input("삭제할 도서의 ISBN을 입력하세요. >>> ")
            found = False

            for i in range(len(books)):
                if books[i]["ISBN"] == remove_isbn:
                    found = True
                    print(f"'{books[i]['제목']}' 도서를 삭제하시겠습니까? 예 / 아니요 >>> ")
                    answer = input("예 / 아니요: ").strip()

                    if answer == '예':
                        del books[i]
                        print(f"'{remove_isbn}' 도서가 삭제되었습니다.")
                    else:
                        print("삭제를 취소합니다.")

                    break 

            if not found:
                print("해당 ISBN의 도서를 찾을 수 없습니다.")


    elif menu == '4':  # 도서 목록 보기 기능
        print('\n도서 목록 보기')

        if len(books) == 0:
            print("저장된 도서가 없습니다.")
        else:
            for i, book in enumerate(books, start=1):
                print(f"{i} | ISBN: {book['ISBN']} | 제목: {book['제목']} | 저자: {book['저자']} | 대여 여부: {book['대여 여부']}")


    elif menu == '5':  # 도서 대여 반납 기능
        print('\n도서 검색')


    elif menu == '6':  # 프로그램 종료
        print('\n프로그램 종료')
        sys.exit()

    else:
        print("메뉴 선택을 잘못하셨습니다.")