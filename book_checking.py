import sys  # 프로그램 종료를 위해 sys 모듈 사용

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
        print('\n도서 수정')


    elif menu == '3':  # 도서 삭제 기능
        print('\n도서 삭제')


    elif menu == '4':  # 도서 검색 기능
        print('\n도서 검색')


    elif menu == '5':  # 도서 대여 반납 기능
        print('\n도서 검색')

    elif menu == '6':  # 프로그램 종료
        print('\n프로그램 종료')
        sys.exit()

    else:
        print("메뉴 선택을 잘못하셨습니다.")