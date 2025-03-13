from operator import index
import Book_Checking_func as bcf  # 프로그램 종료를 위해 sys 모듈 사용

# 사용자에게 보여줄 메뉴 화면
display = '''
-------------------------------------------------------------
1. 도서 추가, 2. 도서 수정, 3. 도서 삭제, 4. 도서 검색, 5. 도서 대여 반납 6. 프로그램종료
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
          book_number = input(" 번호를 입력하세요(4자리로 설정하시오) >>> ")
          check = 0 # 중복확인
          for book in books :
            if book["ISBN"] == book_number: #번호가 존재하면
                check = 1 # 중복 확인 변수 변경
                print("중복된 번호입니다. 새로운 번호로 다시 입력하세요.")
                break # 중복 발견 시 루프 종료

          if check == 0:
              break # 중복되지 않으면 입력 허용

        book_title = input(" 제목을 입력하세요 >>> ")
        book_author = input(" 저자를 입력하세요 >>> ")

        books.append({"ISBN" : book_number, "제목" : book_title, "저자" : book_author, "대여 여부" : False})

        print("도서가 추가되었습니다.")

    elif menu == '2':  # 도서 수정 기능
        print('책 정보 수정')
        books = bcf.book_update(books)

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


    elif menu == '4':  # 도서 목록 보기 (검색 기능 추가)
        print("\n📚 도서 목록 검색")

        search_type = input("검색할 기준을 선택하세요 (1: ISBN, 2: 제목, 3: 저자, Enter: 전체 목록) >>> ").strip()

        if search_type == "1":
            search_value = input("검색할 ISBN을 입력하세요 >>> ").strip()
            found_books = [book for book in books if book["ISBN"] == search_value]
        elif search_type == "2":
            search_value = input("검색할 제목을 입력하세요 >>> ").strip()
            found_books = [book for book in books if search_value.lower() in book["제목"].lower()]
        elif search_type == "3":
            search_value = input("검색할 저자를 입력하세요 >>> ").strip()
            found_books = [book for book in books if search_value.lower() in book["저자"].lower()]
        else:
            found_books = books  # Enter 키 입력 시 전체 도서 목록 출력

        if not found_books:
            print("❌ 검색된 도서가 없습니다.")
        else:
            print("\n📖 도서 목록")
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. ISBN: {book['ISBN']} | 제목: {book['제목']} | 저자: {book['저자']} | 대여 여부: {'대여 중' if book['대여 여부'] else '대여 가능'}")


    elif menu == '5' :  # 도서 검색 및 대여/반납 기능
        print('\n📚 도서 검색 및 대여/반납')

        search = input("검색할 도서의 ISBN 또는 제목을 입력하세요 >>> ").strip()
        found_books = [book for book in books if book["ISBN"] == search or book["제목"] == search]
  
        if not found_books:
            print("❌ 해당 도서를 찾을 수 없습니다.")
        else:
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. ISBN: {book['ISBN']} | 제목: {book['제목']} | 저자: {book['저자']} | 대여 여부: {'대여 중' if book['대여 여부'] else '대여 가능'}")

                select = input("대여/반납할 도서의 번호를 선택하세요 (취소: 0) >>> ").strip()

            if select.isdigit():
                select = int(select)
                if select == 0:
                    print("❌ 도서 대여/반납을 취소했습니다.")
                elif 1 <= select <= len(found_books):
                    selected_book = found_books[select - 1]

                    if selected_book["대여 여부"]:  # 이미 대여 중인 경우
                        confirm = input(f"🔄 '{selected_book['제목']}'을(를) 반납하시겠습니까? (예/아니요) >>> ").strip()
                        if confirm.lower() == "예":
                            selected_book["대여 여부"] = False
                            print(f"✅ '{selected_book['제목']}'이(가) 반납되었습니다.")
                        else:
                            print("❌ 반납이 취소되었습니다.")
                    else:  # 대여 가능한 경우
                        confirm = input(f"📖 '{selected_book['제목']}'을(를) 대여하시겠습니까? (예/아니요) >>> ").strip()
                        if confirm.lower() == "예":
                            selected_book["대여 여부"] = True
                            print(f"✅ '{selected_book['제목']}'이(가) 대여되었습니다.")
                        else:
                            print("❌ 대여가 취소되었습니다.")
                else:
                    print("❌ 잘못된 번호입니다.")
            else:
                print("❌ 숫자로 입력해주세요.")

    elif menu == '6':  # 프로그램 종료
        print('\n프로그램 종료')
        sys.exit()

    else:
        print("메뉴 선택을 잘못하셨습니다.")